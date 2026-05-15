# Task

`ssh cka0001`로 접속한 뒤 `cka-kind` 컨텍스트를 사용하세요.

`service-lab` 네임스페이스의 `inventory-api` Deployment를 NodePort Service로 노출하세요.

Deployment 수정 요구사항:

- 컨테이너 포트 `8080/tcp`를 명시적으로 추가하세요

Service 요구사항:

- 이름: `inventory-api-nodeport`
- 타입: `NodePort`
- 서비스 포트: `8080`
- 타겟 포트: `8080`
- 셀렉터: `app: inventory-api`
