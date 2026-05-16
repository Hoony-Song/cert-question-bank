# Task

현재 노드가 `cka0001`임을 확인하세요. 아니면 `ssh cka0001`로 이동하세요.

클러스터의 기존 CNI가 보안 심사를 통과하지 못해 제거되었습니다.

NetworkPolicy를 적용할 수 있는 새 CNI를 설치해야 합니다.

아래 manifest를 사용해 Calico Tigera operator를 설치하세요.

- 설치 URL: `https://raw.githubusercontent.com/projectcalico/calico/v3.27.0/manifests/tigera-operator.yaml`
- `tigera-operator` namespace가 생성되어야 합니다
- `tigera-operator` Deployment가 생성되어야 합니다
- Tigera operator CRD가 생성되어야 합니다
