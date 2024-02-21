package usecase

import (
	"context"
	"myservice/m/internal/app/reservation/entity"
)

type airportDbRepo interface {
	GetAll(context.Context) ([]entity.Airport, error)
}

type airportSearchRepo interface {
	Search(context.Context, string, int64) ([]entity.Airport, error)
	UpdateCache(context.Context, []entity.Airport) error
}

type AirportListUc struct {
	DbRepo     airportDbRepo
	SearchRepo airportSearchRepo
}

func (uc *AirportListUc) Logic(ctx context.Context, search string, cursorNext int64) ([]entity.Airport, error) {
	airports, err := uc.SearchRepo.Search(ctx, search, cursorNext)
	if err != nil {
		return nil, err
	} else if len(airports) == 0 && search == "" {
		// read aside
		if allAirports, err := uc.DbRepo.GetAll(ctx); err != nil {
			return nil, err
		} else {
			if err := uc.SearchRepo.UpdateCache(ctx, allAirports); err != nil {
				return nil, err
			}
			return allAirports, nil
		}
	}
	return airports, nil

	// ONLY DB
	// if airports, err := uc.DbRepo.GetAll(ctx); err != nil {
	// 	return nil, err
	// } else {
	// 	return airports, nil
	// }
}
