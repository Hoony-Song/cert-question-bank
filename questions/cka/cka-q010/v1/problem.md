# Task

현재 노드가 `cka0001`임을 확인하세요. 아니면 `ssh cka0001`로 이동하세요.

`routing-lab` 네임스페이스에는 `catalog-api` Service와 오래된 `legacy-ingress` Ingress가 있습니다.

기존 Ingress를 대체하는 새 HTTPRoute를 생성하고, 기존 Ingress는 삭제하세요.

새 HTTPRoute 요구사항:

- 이름: `catalog-route`
- parent Gateway: `routing-gateway`
- 호스트: `catalog.apps.local`
- 경로: `/catalog`
- path type: `PathPrefix`
- 백엔드 서비스: `catalog-api`
- 백엔드 서비스 포트: `8080`
