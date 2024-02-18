package router

import (
	"myservice/m/internal/app/reservation/adapter/restful/controller"

	"github.com/gin-gonic/gin"
)

func NewHealthRouter(routerGroup *gin.RouterGroup) {

	healthController := &controller.HealthController{}

	routerGroup.GET("/health/check", healthController.Check)
	routerGroup.GET("/health/ready", healthController.Ready)
}
