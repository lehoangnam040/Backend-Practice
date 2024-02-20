# Backend in Golang Gin follow Clean Architecture


## Generate docs
```
$ ~/go/bin/swag init -g internal/app/reservation/adapter/restful/router/router.go -o api/reservation
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