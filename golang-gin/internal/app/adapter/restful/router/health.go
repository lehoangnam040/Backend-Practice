package router

import (
	"myservice/m/internal/app/adapter/restful/controller"

	"github.com/gin-gonic/gin"
)

func NewHealthRouter(routerGroup *gin.RouterGroup) {

	healthController := &controller.HealthV1Controller{}

	routerGroup.GET("v1/health/check", healthController.Check)
	routerGroup.GET("v1/health/ready", healthController.Ready)
}
