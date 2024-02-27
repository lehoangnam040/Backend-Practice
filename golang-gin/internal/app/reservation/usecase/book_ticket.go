package usecase

import (
	"context"
	"myservice/m/internal/app/reservation/entity"
)

type flightDbRepo interface {
	GetOneById(context.Context, string) (entity.Flight, error)
}

type ticketDbRepo interface {
	CreateATicketOfFlightOptimisticLock(context.Context, string, int) (entity.Ticket, error)
}

type BookTicketUc struct {
	FlightDbRepo flightDbRepo
	TicketDbRepo ticketDbRepo
}

func (uc *BookTicketUc) LogicOptimisticLock(ctx context.Context, id string) (entity.Ticket, error) {
	flight, err := uc.FlightDbRepo.GetOneById(ctx, id)
	if err != nil {
		return entity.Ticket{}, err
	}

	ticket, err := uc.TicketDbRepo.CreateATicketOfFlightOptimisticLock(ctx, flight.Id, flight.Version)
	if err != nil {
		return entity.Ticket{}, err
	}

	return ticket, nil
}
