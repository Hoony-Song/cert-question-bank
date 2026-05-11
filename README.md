# cert-question-bank

CKA/CKAD/CKS 모의시험 플랫폼의 문제은행 저장소이다.

## 포함 범위

- exam type metadata
- exam set
- question YAML
- problem Markdown
- setup manifest
- grading DSL
- environment template
- answer explanation
- question-bank validator

## 제외 범위

- Frontend
- Backend API
- Runtime script
- token/session DB
- 실제 사용자 session data
- secret, private key, qcow2 image

## 하네스

작업 전 루트 작업공간의 `../docs/harness`에서 작업 유형에 맞는 하네스를 읽는다.

- Question Bank: `../docs/harness/00-project-brief.md`, `../docs/harness/01-contracts.md`, `../docs/harness/05-question-bank-harness.md`
- Security: `../docs/harness/00-project-brief.md`, `../docs/harness/01-contracts.md`, `../docs/harness/06-security-harness.md`

## Task 기준

Task 문서는 루트 작업공간의 `../docs/tasks`를 단일 기준으로 사용한다.

작업 시작 전 확인 순서:

1. `../docs/project-state.md`
2. `../docs/tasks/<TASK-ID>.md`
3. 루트 `../docs/harness/*.md` 중 작업 유형에 필요한 하네스

이 저장소에서 다른 저장소 변경이 필요해지면 직접 넘겨서 수정하지 않고 루트 `../docs/project-state.md`의 cross-project TODO에 기록한다.

## 핵심 정책

- CKA는 active, CKAD/CKS는 preparing으로 시작한다.
- active 문제는 직접 수정하지 않고 새 version을 만든다.
- exam set은 question version을 고정한다.
- grading은 선언형 DSL로 관리한다.
- `answer/`와 `grade/`는 Bastion에 복사하지 않는다.
