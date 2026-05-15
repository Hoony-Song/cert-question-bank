# Task

`ssh cka0001`로 접속한 뒤 `cka-kind` 컨텍스트를 사용하세요.

`routing-lab` 네임스페이스에는 `catalog-api` Service와 오래된 `legacy-ingress` Ingress가 있습니다.

기존 Ingress를 대체하는 새 Ingress를 생성하고, 기존 Ingress는 삭제하세요.

새 Ingress 요구사항:

- 이름: `catalog-ingress`
- Ingress class: `nginx`
- 호스트: `catalog.apps.local`
- 경로: `/catalog`
- pathType: `Prefix`
- 백엔드 서비스: `catalog-api`
- 백엔드 서비스 포트: `8080`
