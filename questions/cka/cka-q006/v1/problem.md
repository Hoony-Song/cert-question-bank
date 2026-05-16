# Task

현재 노드가 `cka0002`임을 확인하세요. 아니면 `ssh cka0002`로 이동하세요.

`service-lab` 네임스페이스의 `inventory-api` Deployment를 NodePort Service로 노출하세요.

Deployment 수정 요구사항:

- 컨테이너 포트 `80`포트를 `8080/tcp`로 변경하세요 

Service 요구사항:

- 이름: `inventory-api-nodeport`
- 타입: `NodePort`
- 서비스 포트: `8080`
- 타겟 포트: `8080`
- 셀렉터: `app: inventory-api`
