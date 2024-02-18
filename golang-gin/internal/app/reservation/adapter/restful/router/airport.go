package router

import (
	"myservice/m/internal/app/reservation/adapter/restful/controller"
	"myservice/m/internal/app/reservation/usecase"

	"github.com/gin-gonic/gin"
)

func NewAirportRouterV1(routerGroup *gin.RouterGroup, listAirportUc *usecase.AirportListUc) {

	airportController := &controller.AirportV1Controller{
		ListUc: listAirportUc,
	}

	routerGroup.GET("/airports", airportController.GetList)
}
