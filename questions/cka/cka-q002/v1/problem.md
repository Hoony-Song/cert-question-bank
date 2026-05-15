# Task

`ssh cka0001`로 접속한 뒤 `cka-kind` 컨텍스트를 사용하세요.

`autoscale-lab` 네임스페이스에 `web-frontend` Deployment가 이미 실행 중입니다.

해당 Deployment를 대상으로 HorizontalPodAutoscaler를 생성하세요.

- HPA 이름: `web-frontend-hpa`
- 대상 Deployment: `web-frontend`
- Pod당 CPU 평균 사용률 목표: `55`%
- 최소 레플리카 수: `2`
- 최대 레플리카 수: `5`
- 축소 안정화 윈도우: `45`초
