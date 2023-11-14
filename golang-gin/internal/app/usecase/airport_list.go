package usecase

import (
	"context"
	"myservice/m/internal/app/entity"
)

type airportListRepo interface {
	SearchAirports(context.Context, string, int64) ([]entity.Airport, error)
}

type AirportListUc struct {
	Repo airportListRepo
}

func (uc *AirportListUc) Logic(ctx context.Context, search string, cursorNext int64) ([]entity.Airport, error) {
	return uc.Repo.SearchAirports(ctx, search, cursorNext)
}
