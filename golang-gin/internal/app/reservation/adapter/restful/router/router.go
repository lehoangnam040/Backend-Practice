package router

import (
	postgresrepository "myservice/m/internal/app/reservation/adapter/postgres/repository"
	"myservice/m/internal/app/reservation/usecase"
	"myservice/m/internal/pkg/postgres"

	"github.com/gin-gonic/gin"
)

func Setup(gin *gin.Engine, pg *postgres.Postgres) {

	public := gin.Group("")
	NewHealthRouter(public)
	NewDocsRouter(public)

	pgRepository := postgresrepository.New(pg)

	listAirportUc := &usecase.AirportListUc{
		Repo: pgRepository,
	}

	v1 := gin.Group("/v1")
	NewAirportRouterV1(v1, listAirportUc)
}
