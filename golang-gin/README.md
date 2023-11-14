# Backend in Golang Gin follow Clean Architecture


## Generate docs
```
$ ~/go/bin/swag init -g internal/app/adapter/restful/router/router.go -o api
```

## Build 
```
$ docker build -t ginapp -f build/package/Dockerfile.app .
```
