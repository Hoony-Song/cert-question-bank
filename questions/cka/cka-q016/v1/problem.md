# Task

현재 노드가 `cka0001`임을 확인하세요. 아니면 `ssh cka0001`로 이동하세요.

클러스터의 `kube-scheduler` Pod CPU request가 너무 낮아 불안정할 수 있습니다.
또한 `kube-apiserver`에 감사 로그 디테일을 높이기 위한 아규먼트를 추가해야 합니다.

아래 조건으로 문제를 복구하세요.

- `kube-system` 네임스페이스의 `kube-scheduler` Pod CPU request를 `200m`으로 수정하세요.
- `kube-system` 네임스페이스의 `kube-apiserver` Pod에서 아래 아규먼트를 추가하세요.
  - `--profiling=false`
  - `--v=4`
  - `--request-timeout=300s`
