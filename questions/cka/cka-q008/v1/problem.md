# Task

현재 노드가 `cka0002`임을 확인하세요. 아니면 `ssh cka0002`로 이동하세요.

metrics-server Helm repository를 추가하고 `metrics-server` 네임스페이스에 metrics-server를 Helm으로 설치하세요.

아래 조건을 만족해야 합니다.

- repo 이름: `metrics-server`
- repo 주소: `https://kubernetes-sigs.github.io/metrics-server/`
- release 이름: `metrics-server`
- chart: `metrics-server/metrics-server`
- 레플리카 수: `2`
- Service 포트: `80`
