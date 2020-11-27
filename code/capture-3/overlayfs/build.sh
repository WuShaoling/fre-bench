#!/bin/bash

docker run -it -v "$PWD":/go/src golang:1.14 bash -c "cd /go/src && go build -o overlay overlay.go"

scp overlay root@server:/root/bench

rm -f overlay
