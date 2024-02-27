package controller

import (
	"fmt"
	"net/http"

	"myservice/m/internal/app/reservation/usecase"

	"github.com/gin-gonic/gin"
	"github.com/jinzhu/copier"
)

type CreateTicketUri struct {
	FlightId string `uri:"flight_id" binding:"required"`
}

type ticketDto struct {
	Id       string `json:"id"`
	FlightId string `json:"flight_id"`
}

type TicketV1Controller struct {
	BookTicketUc *usecase.BookTicketUc
}

// CreateTicketOptimisticLock godoc
// @Summary create a ticket
// @Schemes
// @Description create a ticket desc
// @Tags ticket
// @Produce json
// @Param flight_id path string true "Flight ID"
// @Success 201 {object} object{code=string,item=ticketDto}
// @Router /v1/flights/{flight_id}/tickets [post]
func (ctrl *TicketV1Controller) CreateTicketOptimisticLock(ctx *gin.Context) {
	var pathVars CreateTicketUri
	if err := ctx.ShouldBindUri(&pathVars); err != nil {
		ctx.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	ticket, err := ctrl.BookTicketUc.LogicOptimisticLock(ctx.Request.Context(), pathVars.FlightId)

	if err != nil {
		ctx.JSON(http.StatusInternalServerError, gin.H{
			"code": "LogicError",
		})
		fmt.Println(err)
		return
	}

	dto := ticketDto{}
	if err = copier.CopyWithOption(&dto, &ticket, copier.Option{
		CaseSensitive: true,
		IgnoreEmpty:   true,
		DeepCopy:      false,
	}); err != nil {
		ctx.JSON(http.StatusInternalServerError, gin.H{
			"code": "CopyError",
		})
		return
	}

	ctx.JSON(http.StatusOK, gin.H{
		"code": "OK",
		"item": dto,
	})

}
