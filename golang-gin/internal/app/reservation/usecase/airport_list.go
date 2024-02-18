package usecase

import (
	"context"
	"myservice/m/internal/app/reservation/entity"
)

type airportListRepo interface {
	SearchAirports(context.Context, string) ([]entity.Airport, error)
}

type airportListCache interface {
}

type AirportListUc struct {
	Repo airportListRepo
}

func (uc *AirportListUc) Logic(ctx context.Context, search string) ([]entity.Airport, error) {
	return uc.Repo.SearchAirports(ctx, search)
}
