# Task

`ssh cka0001`로 접속한 뒤 `cka-vm` 컨텍스트를 사용하세요.

`reporting-data` 네임스페이스에서 사용할 기본 StorageClass와 PVC를 생성하세요.

StorageClass 요구사항:

- 이름: `fast-local`
- 프로비저너: `rancher.io/local-path`
- volumeBindingMode: `WaitForFirstConsumer`
- 클러스터 기본 StorageClass로 설정

PersistentVolumeClaim 요구사항:

- 이름: `reports-pvc`
- 네임스페이스: `reporting-data`
- StorageClass: `fast-local`
- 접근 모드: `ReadWriteOnce`
- 요청 용량: `2Gi`
