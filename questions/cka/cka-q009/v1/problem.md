# Task

`ssh cka0001`로 접속한 뒤 `cka-vm` 컨텍스트를 사용하세요.

`db-restore` 네임스페이스의 데이터베이스 Deployment가 삭제된 상태입니다. PVC와 Deployment를 다시 생성하세요.

PVC 요구사항:

- 이름: `orders-db-data`
- 접근 모드: `ReadWriteOnce`
- 요청 용량: `1Gi`
- StorageClass: `local-path`

Deployment 요구사항:

- 이름: `orders-db`
- 이미지: `mysql:8.0`
- 환경변수: `MYSQL_ROOT_PASSWORD=change-me`
- PVC를 `/var/lib/mysql`에 마운트하세요
