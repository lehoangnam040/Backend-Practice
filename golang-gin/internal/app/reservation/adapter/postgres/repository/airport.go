package repository

import (
	"context"
	"fmt"
	"myservice/m/internal/app/reservation/entity"
	"myservice/m/internal/pkg/postgres"
)

type PgAirportRepository struct {
	*postgres.Postgres
}

// New
func New(pg *postgres.Postgres) *PgAirportRepository {
	return &PgAirportRepository{pg}
}

func (r *PgAirportRepository) GetAll(ctx context.Context) ([]entity.Airport, error) {
	sql, _, err := r.Builder.
		Select("id, code, name").
		From("airport").
		ToSql()
	if err != nil {
		return nil, fmt.Errorf("PgAirportRepository - GetAll - r.Builder: %w", err)
	}

	rows, err := r.Pool.Query(ctx, sql)
	if err != nil {
		return nil, fmt.Errorf("PgAirportRepository - GetAll - r.Pool.Query: %w", err)
	}
	defer rows.Close()

	entities := make([]entity.Airport, 0, 64)
	for rows.Next() {
		e := entity.Airport{}

		err = rows.Scan(&e.Id, &e.Code, &e.Name)
		if err != nil {
			return nil, fmt.Errorf("PgAirportRepository - GetAll - rows.Scan: %w", err)
		}

		entities = append(entities, e)
	}

	return entities, nil
}
