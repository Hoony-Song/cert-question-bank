# Task

`ssh cka0001`로 접속한 뒤 `cka-vm` 컨텍스트를 사용하세요.

`priority-lab` 네임스페이스의 `queue-consumer` Deployment가 다른 일반 workload보다 우선 스케줄링되어야 합니다.

아래 조건에 맞게 PriorityClass를 생성하고 Deployment에 적용하세요.

- PriorityClass 이름: `platform-critical`
- value: `900000`
- globalDefault: `false`
- description: `platform critical workload`
- `queue-consumer` Deployment의 Pod template에 위 PriorityClass를 지정하세요
