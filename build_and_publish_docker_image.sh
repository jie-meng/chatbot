#!/bin/bash

# 获取标签参数
tag=$1

# 设置镜像名和 repo 
image="openai-proxy"
repo="jmengxy/openai-proxy"

# 构建镜像
docker build -t $repo:$tag .

# 登录 Docker Hub
echo "Login to Docker Hub..."
docker login

# 推送镜像
echo "Pushing $repo:$tag..."
docker push $repo:$tag

# 列出本地和远程镜像,确认推送成功
docker images

echo "Done!"