# flask_script

```bash
# 打包项目(mac m1打包 linux平台)
# docker build -t flask_demo:1.0 -f ./Dockerfile . --platform linux/amd64
# 打包项目(默认平台打包)
docker build -t flask_demo:1.0 -f ./Dockerfile .
# 运行
docker run -d -p 9090:8080 --name flask_demo_01 -t flask_demo:1.0
# * -d: 后台运行容器，并返回容器ID；
# * -p: 指定端口映射，格式为：主机(宿主)端口:容器端口；
# * --name="flask_demo_01": 为容器指定一个名称；
# * -t: 为容器重新分配一个伪输入终端，通常与 -i 同时使用；

# 测试请求
# http://0.0.0.0:9090



登录腾讯云容器镜像服务 Docker Registry

docker login ccr.ccs.tencentyun.com --username=100018328451复制
从 Registry 拉取镜像

docker pull ccr.ccs.tencentyun.com/flask_script/flask_script:[tag]复制
其中 [tag] 请根据您需要拉取镜像的具体版本镜像替换，如 latest。更多命令说明，请参看官方文档：docker pull

向 Registry 中推送镜像
docker tag [imageId] ccr.ccs.tencentyun.com/flask_script/flask_script:[tag]复制
docker push ccr.ccs.tencentyun.com/flask_script/flask_script:[tag]复制


```
 
