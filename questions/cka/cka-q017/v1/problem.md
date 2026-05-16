# Task

현재 노드가 `cka0001`임을 확인하세요. 아니면 `ssh cka0001`로 이동하세요.

`kubelet`이 기본 런타임을 containerd에서 Docker로 사용하도록 전환해야 합니다.
`/home/ubuntu/docker` 경로에 Docker 런타임 설치 파일이 준비되어 있습니다.

사용할 설치 파일은 아래 경로입니다.

- `/home/ubuntu/docker/cri-dockerd_0.3.6.3-0.ubuntu-jammy_amd64.deb`

`worker` 노드(`cka0003`)에 아래 설정을 적용하세요.

- 제공된 deb 파일로 `cri-dockerd`를 설치하고 실행되도록 하세요.
- 시스템 커널 파라미터를 아래 값으로 설정하세요.
  - `net.bridge.bridge-nf-call-iptables = 1`
  - `net.ipv6.conf.all.forwarding = 1`
  - `net.ipv4.ip_forward = 1`
  - `net.netfilter.nf_conntrack_max = 131072`
- `kubelet` 런타임 엔드포인트를 Docker 소켓으로 변경하세요.
- `kubelet` 설정이 반영되도록 갱신하거나 재시작하세요.
