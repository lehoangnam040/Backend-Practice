package router

import (
	"github.com/gin-gonic/gin"

	swaggerfiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"

	// Swagger docs
	_ "myservice/m/docs"
)

func NewDocsRouter(routerGroup *gin.RouterGroup) {
	routerGroup.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerfiles.Handler))
}
