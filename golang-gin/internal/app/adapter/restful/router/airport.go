package router

import (
	"myservice/m/internal/app/adapter/restful/controller"

	"github.com/gin-gonic/gin"
)

func NewAirportRouterV1(routerGroup *gin.RouterGroup) {

	airportController := &controller.AirportV1Controller{}

	routerGroup.GET("/airports", airportController.GetList)
}
