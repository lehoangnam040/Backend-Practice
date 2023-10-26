package main

import (
	"fmt"
	"myservice/m/internal/app/adapter/restful/router"
	"myservice/m/internal/app/config"

	"github.com/gin-gonic/gin"
)

func main() {

	config, err := config.Setup()
	if err != nil {
		panic(fmt.Sprintf("Read config error %s", err))
	}

	gin := gin.Default()
	router.Setup(gin)

	gin.Run(config.App.Address)
}
