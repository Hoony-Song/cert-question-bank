# Task

`ssh cka0001`로 접속한 뒤 `cka-kind` 컨텍스트를 사용하세요.

`tls-demo` 네임스페이스의 `secure-svc` Service를 HTTPS 호스트로 노출하기 위한 Kubernetes 리소스를 준비하세요.

아래 조건을 만족하세요.

- TLS Secret 이름: `portal-tls`
- Secret 타입: `kubernetes.io/tls`
- Ingress 이름: `portal-ingress`
- Ingress class: `nginx`
- 호스트: `portal.demo.local`
- TLS secretName: `portal-tls`
- 백엔드 서비스: `secure-svc`, 포트 `8443`
