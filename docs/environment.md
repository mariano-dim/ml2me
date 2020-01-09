
Instalar kubectl y minukube en ubunto 18.04
-

curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/


Para acceder a un servicio NodePort en minikube
-
IP=$(minikube ip)
PORT=$(kubectl get svc mongo-db-service -o jsonpath="{.spec.ports[0].nodePort}")

Para trabajar con python
-

To install a package from pip use instead (in windows 10) python -m pip install pymongo --user


Para buildear la imagen de docker
-

Para montar volume con el code base
-
Tener en cuenta de darle permisos a docker sobre el drive C

docker run -it --rm -v c:\\Users\\mdima\\Documents\\workspace\\ml2me:/usr/src/app ffx11-app
