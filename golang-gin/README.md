# Backend in Golang Gin follow Clean Architecture

## Config go path
```
$ vim ~/.bashrc
export GOPATH=$HOME/go
export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin:$HOME/.local/bin
```

## Install tools

```
$ [protoc-25.3-linux-x86_64.zip](https://github.com/protocolbuffers/protobuf/releases/download/v25.3/protoc-25.3-linux-x86_64.zip)
$ unzip protoc-25.3-linux-x86_64.zip -d $HOME/.local
$ go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
$ go install github.com/swaggo/swag/cmd/swag@latest
```

## Generate docs
```
$ ~/go/bin/swag init -g internal/app/reservation/adapter/restful/router/router.go -o api/reservation
```
   

## Generate protobuf
```
$ protoc \      # --plugin=/home/ubuntu/go/bin/protoc-gen-go ...
    --proto_path=./pkg \
    --go_out=. \
    --go_opt=Mproto/reservation.proto=./internal/app/reservation/adapter/grpc/pb \
    --go-grpc_out=. \
    --go-grpc_opt=Mproto/reservation.proto=./internal/app/reservation/adapter/grpc/pb \
    ./pkg/proto/reservation.proto
```

## Build 
```
$ docker build -t {tag} -f build/package/Dockerfile.reservation .
```

## Data storage

- redis
```
$ docker run -tid --rm --name redis-stack-server -p 16379:6379 redis/redis-stack-server:7.2.0-v8
$ cat internal/app/reservation/adapter/redis/migrations/airport.redis | docker exec -i redis-stack-server redis-cli --pipe
```

## Migrations
- template: internal/app/{app_name}/adapter/{db_name}/migrations/*.sql
```
Ex: internal/app/reservation/adapter/postgres/migrations/1.sql
```

## Run dev
```
$ source configs/.env.reservation
$ go run cmd/reservation/main.go
```