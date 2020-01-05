

Instalar kubectl y minukube en ubunto 18.04
-

curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/


Para acceder a un servicio NodePort en minikube
-
IP=$(minikube ip)
PORT=$(kubectl get svc mongo-db-service -o jsonpath="{.spec.ports[0].nodePort}")


