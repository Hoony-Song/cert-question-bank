# Task

`ssh cka0001`로 접속한 뒤 `cka-vm` 컨텍스트를 사용하세요.

`repair-lab` 네임스페이스의 `metrics-api` Deployment가 잘못된 이미지와 잘못된 Service selector 때문에 정상 제공되지 않습니다.

아래 조건으로 문제를 복구하세요.

- Deployment 이미지: `nginx:1.27`
- Deployment 레플리카 수: `2`
- Pod label: `app: metrics-api`
- Service 이름은 `metrics-api-svc`를 유지하세요
- Service selector: `app: metrics-api`
- Service 포트: `9090`
- Service 타겟 포트: `80`
