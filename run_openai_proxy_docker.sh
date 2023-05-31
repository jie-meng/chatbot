#!/bin/bash

# 获取标签参数 
tag=$1

# 检查入参
if [ -z $tag ]; then
    echo "Error: tag is empty. Please provide a tag name."
    exit 1 
fi

# 获取主机 IP
hostip=$(ip addr show docker0 | grep "inet " | awk '{print $2}' | cut -d/ -f1)

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
docker run -e IS_DOCKER=Yes -e HOST_IP=$hostip -d --name openai-proxy -p 8000:8000 $repo:$tag
