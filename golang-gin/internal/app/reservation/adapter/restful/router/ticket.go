package router

import (
	"myservice/m/internal/app/reservation/adapter/restful/controller"
	"myservice/m/internal/app/reservation/usecase"

	"github.com/gin-gonic/gin"
)

func NewTicketRouterV1(routerGroup *gin.RouterGroup, bookTicketUc *usecase.BookTicketUc) {

	ticketController := &controller.TicketV1Controller{
		BookTicketUc: bookTicketUc,
	}

	routerGroup.POST("/flights/:flight_id/tickets", ticketController.CreateTicketOptimisticLock)
}
