package controller

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type HealthV1Controller struct{}

func (ctrl *HealthV1Controller) Check(ctx *gin.Context) {
	ctx.JSON(http.StatusOK, gin.H{
		"code": "OK",
	})
}

func (ctrl *HealthV1Controller) Ready(ctx *gin.Context) {
	ctx.JSON(http.StatusOK, gin.H{
		"code": "OK",
	})
}
