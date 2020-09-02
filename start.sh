#!/bin/bash
app="img.repo"
docker build -t ${app} .
docker run -d -p 5050:80 \
  --name=${app} \
  -v $PWD:/app ${app}
