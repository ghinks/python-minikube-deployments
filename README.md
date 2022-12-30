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