# Task

`ssh cka0001`로 접속한 뒤 `cka-kind` 컨텍스트를 사용하세요.

`payments-frontend` 네임스페이스의 Pod만 `payments-backend` 네임스페이스의 `ledger-api` Pod에 접근할 수 있어야 합니다.

`payments-backend` 네임스페이스에 NetworkPolicy를 생성하세요.

- NetworkPolicy 이름: `allow-payments-frontend`
- 대상 Pod selector: `app: ledger-api`
- 허용할 namespace selector: `team: payments-frontend`
- 허용 포트: `8443`
- policyTypes에 `Ingress`를 포함하세요
