#!/bin/bash

docker run -it --rm -v "$PWD":/go/src golang:1.14 bash -c "cd /go/src && go build -o free main.go"

scp free root@server:/free/

rm -f free
