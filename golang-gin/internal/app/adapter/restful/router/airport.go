package router

import (
	"myservice/m/internal/app/adapter/restful/controller"
	"myservice/m/internal/app/usecase"

	"github.com/gin-gonic/gin"
)

func NewAirportRouterV1(routerGroup *gin.RouterGroup, listAirportUc *usecase.AirportListUc) {

	airportController := &controller.AirportV1Controller{
		ListUc: listAirportUc,
	}

	routerGroup.GET("/airports", airportController.GetList)
}
