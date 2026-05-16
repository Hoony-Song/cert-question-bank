# Task

현재 노드가 `cka0002`임을 확인하세요. 아니면 `ssh cka0002`로 이동하세요.

`edge-web` 네임스페이스에 `orders-svc` Service가 이미 생성되어 있습니다.

아래 조건에 맞는 Ingress를 생성하세요.

- Ingress 이름: `orders-ingress`
- Ingress class: `nginx`
- 호스트: `orders.internal.local`
- 경로: `/orders`
- pathType: `Prefix`
- 백엔드 서비스: `orders-svc`
- 백엔드 서비스 포트: `8080`
