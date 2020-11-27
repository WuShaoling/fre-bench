#!/bin/bash

docker run --rm -it -v "$PWD":/go/src golang:1.14 bash \
  -c "cd /go/src && go build -o docker_bench main.go" &&
  scp ./docker_bench root@192.168.2.6:/root &&
  rm -rf docker_bench
