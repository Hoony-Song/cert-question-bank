# Task

`ssh cka0001`로 접속한 뒤 `cka-vm` 컨텍스트를 사용하세요.

`secure-web` 네임스페이스의 `edge-nginx` Deployment는 immutable ConfigMap인 `edge-tls-config`를 사용합니다.

ConfigMap을 교체하여 TLS 설정을 강화하세요.

- `ssl_protocols` 값을 `TLSv1.3`으로 변경하세요
- ConfigMap은 계속 `immutable: true` 상태여야 합니다
- ConfigMap 교체 후 `edge-nginx` Deployment의 Pod template에 `config-revision: v2` label을 추가하세요
