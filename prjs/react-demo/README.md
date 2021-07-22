docker build -t frontdemo  -f ./FrontDockerfile .

docker run -d -p 7001:3000 frontdemo