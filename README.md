# Simple deployments for demonstration of issue with python kubernetes client 

## List of commands applied 
### image build commands
- docker build --tag ghinks/python-for-cloud:0.0.1 .
- docker push ghinks/python-for-cloud:0.0.1

### kubernetes cmds
- kubectl apply -f deployment.yml --dry-run=server
- kubectl apply -f deployment.yml
- kubectl apply -f service.yml --dry-run=server
- kubectl apply -f service.yml
- kubectl get svc
- k get pod &lt;pod-name&gt; -o json | jq ".spec.containers" | jq ".[].name"

- k get ns
- k describe ns default
- [istio setup from istio docs](https://istio.io/latest/docs/setup/getting-started/)
- k label namespace default istio-injection=enabled
- k label namespace default &lt;label_name&gt;- to delete
- k describe ns default

### local python commands (new linux box)
- apt install python3.10-venv
- python3.10 -m venv env
