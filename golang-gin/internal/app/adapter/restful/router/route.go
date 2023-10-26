package router

import "github.com/gin-gonic/gin"

func Setup(gin *gin.Engine) {

	publicRouter := gin.Group("")
	NewHealthRouter(publicRouter)

}
