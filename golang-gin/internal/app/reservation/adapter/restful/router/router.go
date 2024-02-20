package router

import (
	postgresrepository "myservice/m/internal/app/reservation/adapter/postgres/repository"
	redisrepository "myservice/m/internal/app/reservation/adapter/redis/repository"
	"myservice/m/internal/app/reservation/usecase"
	"myservice/m/internal/pkg/postgres"
	"myservice/m/internal/pkg/redis"

	"github.com/gin-gonic/gin"
)

func Setup(gin *gin.Engine, pg *postgres.Postgres, redis *redis.Redis) {

	public := gin.Group("")
	NewHealthRouter(public)
	NewDocsRouter(public)

	pgRepository := postgresrepository.New(pg)
	redisRepository := redisrepository.New(redis)

	listAirportUc := &usecase.AirportListUc{
		DbRepo:     pgRepository,
		SearchRepo: redisRepository,
	}

	v1 := gin.Group("/v1")
	NewAirportRouterV1(v1, listAirportUc)
}
