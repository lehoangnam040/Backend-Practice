# Backend in Golang Gin follow Clean Architecture


## Generate docs
```
$ ~/go/bin/swag init -g internal/app/reservation/adapter/restful/router/router.go -o api
```

## Build 
```
$ docker build -t {tag} -f build/package/Dockerfile.reservation .
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