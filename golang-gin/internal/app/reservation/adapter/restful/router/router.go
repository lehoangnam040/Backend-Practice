package router

import (
	"myservice/m/internal/app/reservation/usecase"

	"github.com/gin-gonic/gin"
)

func Setup(gin *gin.Engine, listAirportUc *usecase.AirportListUc, bookTicketUc *usecase.BookTicketUc) {

	public := gin.Group("")
	NewHealthRouter(public)
	NewDocsRouter(public)

	v1 := gin.Group("/v1")
	NewAirportRouterV1(v1, listAirportUc)
	NewTicketRouterV1(v1, bookTicketUc)
}
