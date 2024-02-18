package controller

import (
	"net/http"

	"myservice/m/internal/app/reservation/usecase"

	"github.com/gin-gonic/gin"
	"github.com/jinzhu/copier"
)

type AirportSearchParams struct {
	Search string `json:"search" form:"search"`
}

type airportDto struct {
	Id   int64  `json:"id"`
	Code string `json:"code"`
	Name string `json:"name"`
}

type AirportV1Controller struct {
	ListUc *usecase.AirportListUc
}

// GetListAirport godoc
// @Summary list airports
// @Schemes
// @Description list airports desc
// @Tags airport
// @Produce json
// @Param _ query AirportSearchParams false "query filter"
// @Success 200 {object} object{code=string,items=airportDto}
// @Router /v1/airports [get]
func (ctrl *AirportV1Controller) GetList(ctx *gin.Context) {
	var params AirportSearchParams
	if err := ctx.ShouldBindQuery(&params); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	airports, err := ctrl.ListUc.Logic(ctx.Request.Context(), params.Search)

	if err != nil {
		ctx.JSON(http.StatusInternalServerError, gin.H{
			"code": "Error",
		})
	}

	dto := []airportDto{}
	if err = copier.CopyWithOption(&dto, &airports, copier.Option{
		CaseSensitive: true,
		IgnoreEmpty:   true,
		DeepCopy:      false,
	}); err != nil {
		ctx.JSON(http.StatusInternalServerError, gin.H{
			"code": "Error",
		})
	}

	ctx.JSON(http.StatusOK, gin.H{
		"code":  "OK",
		"items": dto,
	})

}
