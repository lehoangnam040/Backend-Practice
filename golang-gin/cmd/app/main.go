package main

import (
	"fmt"
	"myservice/m/internal/app/adapter/restful/router"
	"myservice/m/internal/app/config"
	"myservice/m/pkg/postgres"
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

	// Repository
	(config.DbPg.Url())
	pg, err := postgres.New(config.DbPg.Url(), postgres.MaxPoolSize(20))
	if err != nil {
		panic(fmt.Errorf("app - Run - postgres.New: %w", err))
	}
	defer pg.Close()

	gin := gin.Default()
	router.Setup(gin, pg)

	gin.Run(config.App.Address)
}
