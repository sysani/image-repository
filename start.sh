#!/bin/bash
app="img.repo"
portnum=${1:-5050}
docker build -t ${app} .
docker run -d -p $portnum:80 \
  --name=${app} \
  -v $PWD:/app ${app}
