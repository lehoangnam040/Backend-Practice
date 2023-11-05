package router

import (
	"github.com/gin-gonic/gin"
)

func Setup(gin *gin.Engine) {

	public := gin.Group("")
	NewHealthRouter(public)
	NewDocsRouter(public)

	v1 := gin.Group("/v1")
	NewAirportRouterV1(v1)
}
