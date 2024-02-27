package usecase

import (
	"context"
	"fmt"
	"myservice/m/internal/app/reservation/entity"
	"time"
)

type flightDbRepo interface {
	GetOneById(context.Context, string) (entity.Flight, error)
}

type ticketDbRepo interface {
	CreateATicketOfFlightOptimisticLock(context.Context, string, int, int) (entity.Ticket, error)
	CreateATicketOfFlightPessimisticLock(context.Context, string, int) (entity.Ticket, error)
}

type ticketFlightLocker interface {
	AcquireLockOfAFlight(context.Context, string, time.Duration) (bool, error)
	ReleaseLockOfAFlight(context.Context, string) (bool, error)
}

type BookTicketUc struct {
	FlightDbRepo       flightDbRepo
	TicketDbRepo       ticketDbRepo
	TicketFlightLocker ticketFlightLocker
}

func (uc *BookTicketUc) LogicOptimisticLock(ctx context.Context, id string) (entity.Ticket, error) {
	flight, err := uc.FlightDbRepo.GetOneById(ctx, id)
	if err != nil {
		return entity.Ticket{}, err
	}
	if flight.AvailSeat <= 0 {
		return entity.Ticket{}, fmt.Errorf("no avail seat")
	}

	ticket, err := uc.TicketDbRepo.CreateATicketOfFlightOptimisticLock(ctx, flight.Id, flight.AvailSeat-1, flight.Version)
	if err != nil {
		return entity.Ticket{}, err
	}

	return ticket, nil
}

func (uc *BookTicketUc) LogicPessimisticLock(ctx context.Context, id string) (entity.Ticket, error) {
	lockSuccess, err := uc.TicketFlightLocker.AcquireLockOfAFlight(ctx, id, time.Second*10)
	if err != nil {
		return entity.Ticket{}, err
	} else if !lockSuccess {
		return entity.Ticket{}, fmt.Errorf("locked by another transaction")
	}
	defer func() {
		unlockSuccess, err := uc.TicketFlightLocker.ReleaseLockOfAFlight(ctx, id)
		if err == nil && unlockSuccess {
			fmt.Println("unlock success!")
		} else {
			fmt.Println("unlock failed", err)
		}
	}()

	flight, err := uc.FlightDbRepo.GetOneById(ctx, id)
	if err != nil {
		return entity.Ticket{}, err
	}
	if flight.AvailSeat <= 0 {
		return entity.Ticket{}, fmt.Errorf("no avail seat")
	}

	ticket, err := uc.TicketDbRepo.CreateATicketOfFlightPessimisticLock(ctx, flight.Id, flight.AvailSeat-1)
	if err != nil {
		return entity.Ticket{}, err
	}
	return ticket, nil
}
