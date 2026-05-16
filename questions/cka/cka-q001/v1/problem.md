# Task

Confirm you are on `cka0001`. If not, connect with `ssh cka0001`.

An nginx Pod is already running in the `app-team` namespace.

Create the resources needed to expose that Pod:

- Service name: `nginx-svc`
- Service port: `80`
- Service target port: `80`
- Ingress name: `nginx-ingress`
- Ingress class: `nginx`
- Ingress backend service: `nginx-svc`
