# Task

`ssh cka0001`로 접속한 뒤 `cka-vm` 컨텍스트를 사용하세요.

`worker` 노드를 컨테이너 런타임 검증용 workload가 스케줄링될 수 있는 상태로 표시해야 합니다.

`worker` 노드에 아래 설정을 적용하세요.

- label: `runtime.cert-platform.io/ready=true`
- label: `runtime.cert-platform.io/handler=containerd`
- taint: `runtime.cert-platform.io/bootstrap=complete:NoExecute`
