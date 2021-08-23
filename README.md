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

minikube delete && minikube start --insecure-registry=47.106.112.61:3000 --base-image="anjone/kicbase" --image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers --registry-mirror=https://registry.docker-cn.com
此时会拉取阿里的镜像仓库.
minikube delete && minikube start --insecure-registry=192.168.50.73:3000 --registry-mirror=https://registry.docker-cn.com
minikube start --image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers --registry-mirror=https://registry.docker-cn.com --vm-driver=<driver_name>
minikube start --driver=none --extra-config=kubeadm.ignore-preflight-errors=NumCPU --force --cpus 1
# https://researchlab.github.io/2019/08/24/minikube-pull-image-from-docker-registry/

kubectl create  -f ./mainfests/backdemo_deployment.yml
# kubectl rollout restart deployment backdemo-deployment
# kubectl delete deployment backdemo-deployment
    更新镜像: 修改deploy文件 kubectl apply -f mainfests/backdemo_deployment.yml 一个个镜像更新


kubectl create  -f ./mainfests/backdemo_service.yml
# 在minikube容器中访问 cluster-ip:6001
# 在minikube容器中访问 endpoint:6000


# https://kubernetes.io/zh/docs/tasks/access-application-cluster/connecting-frontend-backend/
# 创建前端应用
前端使用被赋予后端 Service 的 DNS 名称将请求发送到后端工作 Pods。这一DNS 名称为 hello，也就是 examples/service/access/backend-service.yaml 配置 文件中 name 字段的取值。
可以在 pods中使用service.name访问

# 前端镜像
kubectl create  -f ./mainfests/frontdemo_deployment.yml
kubectl create  -f ./mainfests/frontdemo_service.yml

