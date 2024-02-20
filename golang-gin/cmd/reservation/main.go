package main

import (
	"fmt"
	"myservice/m/internal/app/reservation/adapter/restful/router"
	"myservice/m/internal/config"
	"myservice/m/internal/pkg/postgres"
	"myservice/m/internal/pkg/redis"
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
	pg, err := postgres.New(config.DbPg.Url(), postgres.MaxPoolSize(20))
	if err != nil {
		panic(fmt.Errorf("app - Run - postgres.New: %w", err))
	}
	defer pg.Close()

	redis, err := redis.New(config.Redis.Url(), config.Redis.Pass, config.Redis.Db)
	if err != nil {
		panic(fmt.Errorf("app - Run - redis.New: %w", err))
	}

	gin := gin.Default()
	router.Setup(gin, pg, redis)

	gin.Run(config.App.Address)
}
