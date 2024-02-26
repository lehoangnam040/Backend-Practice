package repository

import (
	"context"
	"fmt"
	"myservice/m/internal/app/reservation/entity"
	"myservice/m/internal/pkg/postgres"

	"github.com/jackc/pgx/v5"
)

type PgAirportRepository struct {
	*postgres.Postgres
}

// New
func NewPgAirportRepository(pg *postgres.Postgres) *PgAirportRepository {
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

	return pgx.CollectRows[entity.Airport](rows, pgx.RowToStructByNameLax[entity.Airport])
}
