#!/bin/sh
REPOSITORY_NAME=tyronextian
IMAGE_NAME=api_infra_base

cd ..

# 检查是否在Git仓库中
if [ -d .git ] || git rev-parse --is-inside-work-tree &> /dev/null; then
  # 获取当前分支名
  branch_name=$(git symbolic-ref --short HEAD 2>/dev/null)
  if [ -n "$branch_name" ]; then
    # 使用cut命令提取分支名中的 / 后面的内容
    branch_suffix=$(echo "$branch_name" | cut -d'/' -f2)
    echo "当前分支的后缀: $branch_suffix"
  else
    echo "无法获取分支名"
  fi
else
  echo "不在Git仓库中"
fi

DATE=$(date +"%Y%m%d")

# 获取当前的 git commit ID
commit_id=$(git rev-parse --short HEAD)

TAG=${branch_suffix}_${DATE}_${commit_id}

docker build -t ${IMAGE_NAME}:${TAG} -f ./docker/Dockerfile .
docker tag ${IMAGE_NAME}:${TAG} ${REPOSITORY_NAME}${IMAGE_NAME}:${TAG}
docker push ${REPOSITORY_NAME}/${IMAGE_NAME}:${TAG}

echo "docker pull ${REPOSITORY_NAME}/${IMAGE_NAME}:${TAG}"