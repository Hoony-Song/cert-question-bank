# Task

현재 노드가 `cka0001`임을 확인하세요. 아니면 `ssh cka0001`로 이동하세요.

`secure-web` 네임스페이스의 `edge-nginx` Deployment는 immutable ConfigMap인 `edge-tls-config`를 사용합니다.

ConfigMap을 교체하여 nginx 설정을 강화하세요.

- `ssl_protocols` 값을 `TLSv1.3`으로 변경하세요
- `client_max_body_size` 값을 `20m`으로 변경하세요
- `keepalive_timeout` 값을 `65`로 변경하세요
- ConfigMap은 계속 `immutable: true` 상태여야 합니다
- ConfigMap 교체 후 `edge-nginx` Deployment의 Pod template에 `config-revision: v2` label을 추가하세요
