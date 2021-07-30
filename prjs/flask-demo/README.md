# 打包镜像
docker build -t backdemo  -f ./BackDockerfile .

# 上传registry
# 需要本地registry
# docker 配置 --insecure-registry=192.168.50.73:3000
docker tag backdemo 192.168.50.73:3000/backdemo:latest
docker push 192.168.50.73:3000/backdemo:latest
 docker search 192.168.50.73:3000
 http://192.168.50.73:3000/v2/_catalog
# docker增加insecure-registries配置
# minikube 增加--insecure-registry
minikube start --insecure-registry=192.168.50.73:3000
# https://researchlab.github.io/2019/08/24/minikube-pull-image-from-docker-registry/

# docker run -d -p 7000:6000 backdemo 测试

# docker run -p 6379:6379 -d redis:latest redis-server