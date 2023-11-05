package main

import (
	"fmt"
	"myservice/m/internal/app/adapter/restful/router"
	"myservice/m/internal/app/config"
	"runtime"

	"github.com/gin-gonic/gin"
)

func init() {
	runtime.GOMAXPROCS(runtime.NumCPU())
}

func main() {

	config, err := config.Setup()
	if err != nil {
		panic(fmt.Sprintf("Read config error %s", err))
	}

	gin := gin.Default()
	router.Setup(gin)

	gin.Run(config.App.Address)
}
