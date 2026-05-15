# Task

`ssh cka0001`로 접속한 뒤 `cka-kind` 컨텍스트를 사용하세요.

`cms-prod` 네임스페이스의 `blog` Deployment가 트래픽 증가로 인해 더 많은 Pod와 리소스 요청량이 필요합니다.

아래 조건에 맞게 Deployment를 수정하세요.

- 레플리카 수: `3`
- 컨테이너 CPU request: `150m`
- 컨테이너 memory request: `256Mi`
- 기존 Deployment 이름은 변경하지 마세요
