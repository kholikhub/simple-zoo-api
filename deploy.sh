#!/bin/bash

docker build -t "zoo-app" -f "Dockerfile"
TAG=$(date +%s) # timestamp
docker tag zoo-app kh0lik/zoo-app-poc:$TAG
docker push kh0lik/zoo-app-poc:$TAG