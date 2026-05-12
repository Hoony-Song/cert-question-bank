#!/usr/bin/env python3
"""문제은행 구조와 선언형 YAML 계약을 검증한다."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - 실행 환경 오류 안내용
    print("오류: PyYAML 패키지가 필요합니다. python3 환경에 PyYAML을 설치하세요.", file=sys.stderr)
    raise SystemExit(2) from exc


ROOT = Path(__file__).resolve().parents[1]

EXAM_TYPES = {
    "CKA": {"file": "cka.yaml", "directory": "cka", "status": "active"},
    "CKAD": {"file": "ckad.yaml", "directory": "ckad", "status": "preparing"},
    "CKS": {"file": "cks.yaml", "directory": "cks", "status": "preparing"},
}

EXAM_TYPE_REQUIRED_FIELDS = (
    "id",
    "displayName",
    "status",
    "defaultDurationMinutes",
    "description",
)

QUESTION_REQUIRED_FIELDS = (
    "id",
    "version",
    "examType",
    "title",
    "status",
    "category",
    "score",
    "difficulty",
    "environment.template",
    "environment.context",
    "environment.namespace",
    "ui.order",
    "ui.displayContext",
    "ui.displayNamespace",
    "ui.estimatedMinutes",
    "question.file",
    "setup",
    "grading",
)

EXAM_SET_REQUIRED_FIELDS = (
    "id",
    "examType",
    "title",
    "status",
    "durationMinutes",
    "questions",
)

QUESTION_STATUSES = {"draft", "review", "active", "deprecated", "archived"}
EXAM_SET_STATUSES = {"draft", "review", "active", "deprecated", "archived"}
ACTIVE_ALLOWED_QUESTION_STATUSES = {"active"}


class ValidationContext:
    """검증 오류와 경고를 한곳에 모은다."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: Path | str, message: str) -> None:
        self.errors.append(f"{display_path(path)}: {message}")

    def warn(self, path: Path | str, message: str) -> None:
        self.warnings.append(f"{display_path(path)}: {message}")


def display_path(path: Path | str) -> str:
    path_obj = Path(path)
    try:
        return str(path_obj.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def load_yaml(path: Path, ctx: ValidationContext) -> dict[str, Any] | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        ctx.error(path, f"YAML 파싱 실패: {exc}")
        return None
    except OSError as exc:
        ctx.error(path, f"파일 읽기 실패: {exc}")
        return None

    if data is None:
        return {}

    if not isinstance(data, dict):
        ctx.error(path, "YAML 최상위 값은 object 형태여야 합니다.")
        return None

    return data


def get_nested(data: dict[str, Any], dotted_key: str) -> Any:
    current: Any = data
    for key in dotted_key.split("."):
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def has_field(data: dict[str, Any], dotted_key: str) -> bool:
    return get_nested(data, dotted_key) is not None


def require_fields(path: Path, data: dict[str, Any], fields: tuple[str, ...], ctx: ValidationContext) -> None:
    for field in fields:
        if not has_field(data, field):
            ctx.error(path, f"필수 필드 누락: {field}")


def validate_exam_types(ctx: ValidationContext) -> dict[str, dict[str, Any]]:
    exam_types: dict[str, dict[str, Any]] = {}

    for exam_type, spec in EXAM_TYPES.items():
        path = ROOT / "exam-types" / spec["file"]
        if not path.exists():
            ctx.error(path, "시험 유형 파일이 없습니다.")
            continue

        data = load_yaml(path, ctx)
        if data is None:
            continue

        require_fields(path, data, EXAM_TYPE_REQUIRED_FIELDS, ctx)

        if data.get("id") != exam_type:
            ctx.error(path, f"id는 {exam_type}이어야 합니다.")

        if data.get("status") != spec["status"]:
            ctx.error(path, f"status는 {spec['status']}이어야 합니다.")

        duration = data.get("defaultDurationMinutes")
        if not isinstance(duration, int) or duration <= 0:
            ctx.error(path, "defaultDurationMinutes는 양의 정수여야 합니다.")

        exam_types[exam_type] = data

    return exam_types


def find_yaml_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    files = list(directory.rglob("*.yaml"))
    files.extend(directory.rglob("*.yml"))
    return sorted(files)


def find_question_files() -> list[Path]:
    question_root = ROOT / "questions"
    if not question_root.exists():
        return []
    return sorted(question_root.glob("*/*/*/question.yaml"))


def validate_directory_layout(ctx: ValidationContext) -> None:
    required_directories = [
        ROOT / "exam-types",
        ROOT / "exam-sets",
        ROOT / "questions",
        ROOT / "environment-templates",
        ROOT / "tools",
    ]

    for directory in required_directories:
        if not directory.is_dir():
            ctx.error(directory, "필수 디렉토리가 없습니다.")

    for spec in EXAM_TYPES.values():
        for base in ("exam-sets", "questions", "environment-templates"):
            directory = ROOT / base / spec["directory"]
            if not directory.is_dir():
                ctx.error(directory, "시험 유형별 필수 디렉토리가 없습니다.")

    common_template_dir = ROOT / "environment-templates" / "common"
    if not common_template_dir.is_dir():
        ctx.error(common_template_dir, "공통 환경 템플릿 디렉토리가 없습니다.")


def resolve_environment_template(template: str) -> Path | None:
    raw_path = ROOT / "environment-templates" / template
    candidates = [raw_path]

    if raw_path.suffix not in {".yaml", ".yml"}:
        candidates.append(raw_path.with_suffix(".yaml"))
        candidates.append(raw_path.with_suffix(".yml"))

    for candidate in candidates:
        if candidate.is_file():
            return candidate

    return None


def validate_question_file(path: Path, data: dict[str, Any], ctx: ValidationContext) -> None:
    require_fields(path, data, QUESTION_REQUIRED_FIELDS, ctx)

    version_dir = path.parent
    question_dir = version_dir.parent
    exam_dir = question_dir.parent
    expected_exam_type = exam_dir.name.upper()

    if expected_exam_type not in EXAM_TYPES:
        ctx.error(path, f"알 수 없는 시험 유형 디렉토리입니다: {exam_dir.name}")
        return

    question_id = data.get("id")
    if question_id != question_dir.name:
        ctx.error(path, f"id는 문제 디렉토리명 {question_dir.name}과 일치해야 합니다.")

    version = data.get("version")
    if version != version_dir.name:
        ctx.error(path, f"version은 버전 디렉토리명 {version_dir.name}과 일치해야 합니다.")

    if not isinstance(version, str) or not version.startswith("v") or len(version) == 1:
        ctx.error(path, "version은 v1 같은 고정 버전 형식이어야 합니다.")

    exam_type = data.get("examType")
    if exam_type != expected_exam_type:
        ctx.error(path, f"examType은 상위 디렉토리 기준 {expected_exam_type}이어야 합니다.")

    status = data.get("status")
    if status not in QUESTION_STATUSES:
        ctx.error(path, f"status는 {sorted(QUESTION_STATUSES)} 중 하나여야 합니다.")

    score = data.get("score")
    if not isinstance(score, (int, float)) or score <= 0:
        ctx.error(path, "score는 양수여야 합니다.")

    order = get_nested(data, "ui.order")
    if not isinstance(order, int) or order <= 0:
        ctx.error(path, "ui.order는 양의 정수여야 합니다.")

    estimated_minutes = get_nested(data, "ui.estimatedMinutes")
    if not isinstance(estimated_minutes, int) or estimated_minutes <= 0:
        ctx.error(path, "ui.estimatedMinutes는 양의 정수여야 합니다.")

    problem_file = get_nested(data, "question.file")
    if isinstance(problem_file, str) and problem_file:
        problem_path = (path.parent / problem_file).resolve()
        if not problem_path.is_file():
            ctx.error(path, f"question.file 대상 파일이 없습니다: {problem_file}")
    elif problem_file is not None:
        ctx.error(path, "question.file은 비어 있지 않은 문자열이어야 합니다.")

    template = get_nested(data, "environment.template")
    if isinstance(template, str) and template:
        if resolve_environment_template(template) is None:
            ctx.error(path, f"environment.template 대상 파일이 없습니다: {template}")
    elif template is not None:
        ctx.error(path, "environment.template은 비어 있지 않은 문자열이어야 합니다.")


def index_questions(ctx: ValidationContext) -> dict[tuple[str, str], dict[str, Any]]:
    question_index: dict[tuple[str, str], dict[str, Any]] = {}
    question_files = find_question_files()

    for path in question_files:
        data = load_yaml(path, ctx)
        if data is None:
            continue

        validate_question_file(path, data, ctx)

        question_id = data.get("id")
        version = data.get("version")
        if isinstance(question_id, str) and isinstance(version, str):
            key = (question_id, version)
            if key in question_index:
                ctx.error(path, f"중복 문제 버전입니다: {question_id}/{version}")
            question_index[key] = data

    return question_index


def validate_exam_set_file(
    path: Path,
    data: dict[str, Any],
    question_index: dict[tuple[str, str], dict[str, Any]],
    exam_type_statuses: dict[str, str],
    ctx: ValidationContext,
) -> None:
    require_fields(path, data, EXAM_SET_REQUIRED_FIELDS, ctx)

    exam_dir = path.parent.name
    expected_exam_type = exam_dir.upper()

    if expected_exam_type not in EXAM_TYPES:
        ctx.error(path, f"알 수 없는 시험 유형 디렉토리입니다: {exam_dir}")
        return

    exam_type = data.get("examType")
    if exam_type != expected_exam_type:
        ctx.error(path, f"examType은 상위 디렉토리 기준 {expected_exam_type}이어야 합니다.")

    status = data.get("status")
    if status not in EXAM_SET_STATUSES:
        ctx.error(path, f"status는 {sorted(EXAM_SET_STATUSES)} 중 하나여야 합니다.")

    if status == "active" and exam_type_statuses.get(expected_exam_type) != "active":
        ctx.error(path, "preparing 시험 유형은 active exam set을 가질 수 없습니다.")

    duration = data.get("durationMinutes")
    if not isinstance(duration, int) or duration <= 0:
        ctx.error(path, "durationMinutes는 양의 정수여야 합니다.")

    questions = data.get("questions")
    if questions is None:
        return
    if not isinstance(questions, list):
        ctx.error(path, "questions는 list 형태여야 합니다.")
        return

    seen_questions: set[tuple[str, str]] = set()
    for index, entry in enumerate(questions, start=1):
        if not isinstance(entry, dict):
            ctx.error(path, f"questions[{index}]는 object 형태여야 합니다.")
            continue

        question_id = entry.get("id")
        version = entry.get("version")

        if not isinstance(question_id, str) or not question_id:
            ctx.error(path, f"questions[{index}].id는 비어 있지 않은 문자열이어야 합니다.")
            continue

        if not isinstance(version, str) or not version:
            ctx.error(path, f"questions[{index}].version은 비어 있지 않은 문자열이어야 합니다.")
            continue

        if not version.startswith("v"):
            ctx.error(path, f"questions[{index}].version은 v1 같은 고정 버전이어야 합니다.")

        key = (question_id, version)
        if key in seen_questions:
            ctx.error(path, f"중복 문제 참조입니다: {question_id}/{version}")
        seen_questions.add(key)

        question = question_index.get(key)
        if question is None:
            ctx.error(path, f"참조한 문제 버전이 없습니다: {question_id}/{version}")
            continue

        if question.get("examType") != expected_exam_type:
            ctx.error(path, f"{question_id}/{version} examType이 exam set과 일치하지 않습니다.")

        if status == "active" and question.get("status") not in ACTIVE_ALLOWED_QUESTION_STATUSES:
            ctx.error(path, f"active exam set에는 active 문제만 포함할 수 있습니다: {question_id}/{version}")


def validate_exam_sets(
    question_index: dict[tuple[str, str], dict[str, Any]],
    exam_types: dict[str, dict[str, Any]],
    ctx: ValidationContext,
) -> None:
    exam_type_statuses = {
        exam_type: str(data.get("status", ""))
        for exam_type, data in exam_types.items()
    }

    for path in find_yaml_files(ROOT / "exam-sets"):
        data = load_yaml(path, ctx)
        if data is None:
            continue
        validate_exam_set_file(path, data, question_index, exam_type_statuses, ctx)


def main() -> int:
    ctx = ValidationContext()

    validate_directory_layout(ctx)
    exam_types = validate_exam_types(ctx)
    question_index = index_questions(ctx)
    validate_exam_sets(question_index, exam_types, ctx)

    for warning in ctx.warnings:
        print(f"경고: {warning}")

    if ctx.errors:
        print("문제은행 검증 실패")
        for error in ctx.errors:
            print(f"- {error}")
        return 1

    print("문제은행 검증 성공")
    print(f"- 시험 유형: {len(exam_types)}개")
    print(f"- 문제 버전: {len(question_index)}개")
    print(f"- exam set: {len(find_yaml_files(ROOT / 'exam-sets'))}개")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
