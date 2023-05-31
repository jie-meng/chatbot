#!/bin/bash

# 获取标签参数 
tag=$1

# 设置镜像名和 repo 
image="openai-proxy"
repo="jmengxy/openai-proxy"

# 拉取镜像
echo "Pulling $repo:$tag..." 
docker pull $repo:$tag

# 列出本地镜像,确认拉取成功
docker images

# 运行镜像
echo "Running $repo:$tag..."
docker run -p 8000:8000 $repo:$tag