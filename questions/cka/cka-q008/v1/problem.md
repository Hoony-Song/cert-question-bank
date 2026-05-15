# Task

`ssh cka0001`로 접속한 뒤 `cka-kind` 컨텍스트를 사용하세요.

`gitops-system` 네임스페이스에 GitOps 컨트롤러 역할의 workload를 배포하세요.

아래 조건을 만족해야 합니다.

- Deployment 이름: `gitops-controller`
- 이미지: `nginx:1.27`
- 레플리카 수: `2`
- 컨테이너 이름: `controller`
- 컨테이너 포트: `8080`
- Service 이름: `gitops-controller-svc`
- Service 포트: `80`
- Service 타겟 포트: `8080`
- Service 셀렉터: `app: gitops-controller`
