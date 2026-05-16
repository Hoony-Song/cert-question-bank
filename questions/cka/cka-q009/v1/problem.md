# Task

현재 노드가 `cka0001`임을 확인하세요. 아니면 `ssh cka0001`로 이동하세요.

`web-restore` 네임스페이스의 nginx Deployment가 삭제되어 PV만 남은 상태입니다. PVC와 Deployment를 다시 생성한 뒤 기존 PV와 연결하세요.

기존 PV 이름:

- `web-restore-content-pv`

PVC 요구사항:

- 이름: `nginx-content`
- 접근 모드: `ReadWriteOnce`
- 요청 용량: `1Gi`
- StorageClass: `local-path`
- 기존 PV `web-restore-content-pv`와 `Bound` 상태여야 합니다

Deployment 요구사항:

- 이름: `web-nginx`
- 이미지: `nginx:1.27`
- 컨테이너 포트: `80`
- PVC를 `/usr/share/nginx/html`에 마운트하세요
