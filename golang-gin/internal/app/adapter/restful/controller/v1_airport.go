package controller

import (
	"net/http"

	"myservice/m/internal/app/usecase"

	"github.com/gin-gonic/gin"
	"github.com/jinzhu/copier"
)

type airportDto struct {
	Id   int64  `json:"id"`
	Code string `json:"code"`
	Name string `json:"name"`
}

type AirportV1Controller struct {
	listUc usecase.AirportListUc
}

// GetListAirport godoc
// @Summary list airports
// @Schemes
// @Description list airports desc
// @Tags airport
// @Accept json
// @Produce json
// @Success 200 {object} object{code=string,items=airportDto}
// @Router /v1/airports [get]
func (ctrl *AirportV1Controller) GetList(ctx *gin.Context) {

	airports, err := ctrl.listUc.Logic()

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
