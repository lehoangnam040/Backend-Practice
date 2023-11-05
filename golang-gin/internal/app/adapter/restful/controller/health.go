package controller

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

type HealthController struct{}

// HealthCheck godoc
// @Summary health check
// @Schemes
// @Description do health check
// @Tags health
// @Accept json
// @Produce json
// @Success 200 {object} object{code=string}
// @Router /health/check [get]
func (ctrl *HealthController) Check(ctx *gin.Context) {
	ctx.JSON(http.StatusOK, gin.H{
		"code": "OK",
	})
}

// HealthReady godoc
// @Summary health ready
// @Schemes
// @Description do health ready
// @Tags health
// @Accept json
// @Produce json
// @Success 200 {object} object{code=string}
// @Router /health/ready [get]
func (ctrl *HealthController) Ready(ctx *gin.Context) {
	ctx.JSON(http.StatusOK, gin.H{
		"code": "OK",
	})
}
