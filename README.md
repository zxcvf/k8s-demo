# https://researchlab.github.io/2019/08/24/minikube-pull-image-from-docker-registry/

[解决 ErrorImgPull]
#搭建docker registry
docker pull registry

#docker run -d -v /opt/registry:/var/lib/registry -p 5000:5000 --restart=always --name registry registry:latest
docker run -d -p 3000:5000 -e REGISTRY_STORAGE_DELETE_ENABLED=true  --restart=always --name registry registry:latest

上传 后端、前端容器
# 打包镜像
docker build -t backdemo  -f ./BackDockerfile .
# 上传registry
docker tag backdemo 192.168.50.73:3000/backdemo:latest
docker push 192.168.50.73:3000/backdemo:latest

 docker search 192.168.50.73:3000

http://192.168.50.73:3000/v2/_catalog

# docker增加insecure-registries配置
# minikube 增加--insecure-registry
minikube delete && minikube start --insecure-registry=192.168.50.73:3000
# https://researchlab.github.io/2019/08/24/minikube-pull-image-from-docker-registry/

kubectl create  -f ./mainfests/backdemo_deployment.yml
# kubectl rollout restart deployment backdemo-deployment
# kubectl delete deployment backdemo-deployment

kubectl create  -f ./mainfests/backdemo_service.yml
# 在minikube容器中访问 cluster-ip:6001
# 在minikube容器中访问 endpoint:6000