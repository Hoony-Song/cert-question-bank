# Task

`ssh cka0001`로 접속한 뒤 `cka-kind` 컨텍스트를 사용하세요.

`logging-lab` 네임스페이스의 `audit-worker` Deployment는 로그 파일을 생성하지만, 현재 `kubectl logs`로 해당 파일 내용을 확인하기 어렵습니다.

Deployment를 수정해 로그 파일을 출력하는 사이드카 컨테이너를 추가하세요.

- 사이드카 컨테이너 이름: `log-tail`
- 사이드카 이미지: `busybox:1.36`
- 사이드카 명령: `/bin/sh -c "tail -n+1 -f /var/log/audit/audit.log"`
- `audit-logs` 이름의 `emptyDir` 볼륨을 사용하세요
- 기존 컨테이너와 사이드카 모두 `/var/log/audit` 경로에 같은 볼륨을 마운트하세요
