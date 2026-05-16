# Task

현재 노드가 `cka0002`임을 확인하세요. 아니면 `ssh cka0002`로 이동하세요.

`cms-prod` 네임스페이스의 `blog` Deployment가 트래픽 증가로 인해 더 많은 Pod와 리소스 요청량이 필요합니다.

아래 조건에 맞게 Deployment를 수정하세요.

- 레플리카 수는 `3`이어야 합니다.
- 컨테이너 1개당 CPU/메모리 요청량을 조정해서 전체 Deployment의
  총 CPU request가 `100m` 초과이고 총 memory request가 `256Mi`를 초과하도록 하세요.
- 기존 Deployment 이름은 변경하지 마세요
