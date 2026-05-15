# Task

`ssh cka0001`로 접속한 뒤 `cka-vm` 컨텍스트를 사용하세요.

운영팀이 kubeadm 클러스터의 worker 노드를 네트워크 플러그인 검증 대상으로 분리하려고 합니다.

`worker` 노드에 아래 설정을 적용하세요.

- label: `networking.cert-platform.io/plugin=calico`
- taint: `networking.cert-platform.io/validation=required:NoSchedule`
- 기존 노드 이름과 다른 노드는 수정하지 마세요
