package repository

import (
	"context"
	"fmt"
	"myservice/m/internal/app/reservation/entity"
	"myservice/m/internal/pkg/postgres"

	"github.com/gofrs/uuid/v5"
	"github.com/jackc/pgx/v5"
)

type PgFlightRepository struct {
	*postgres.Postgres
}

// New
func NewPgFlightRepository(pg *postgres.Postgres) *PgFlightRepository {
	return &PgFlightRepository{pg}
}

func (r *PgFlightRepository) GetOneById(ctx context.Context, id string) (entity.Flight, error) {
	idUuid, err := uuid.FromString(id)
	if err != nil {
		return entity.Flight{}, fmt.Errorf("PgFlightRepository - GetOneById - uuid.FromString: %w", err)
	}
	sql, args, err := r.Builder.
		Select("id, dept_airport_id, dest_airport_id, total_seat, avail_seat, version").
		From("flight").
		Where("id = ?", idUuid).
		ToSql()
	if err != nil {
		return entity.Flight{}, fmt.Errorf("PgFlightRepository - GetOneById - r.Builder: %w", err)
	}

	rows, err := r.Pool.Query(ctx, sql, args...)
	if err != nil {
		return entity.Flight{}, fmt.Errorf("PgFlightRepository - GetOneById - r.Pool.Query: %w", err)
	}
	defer rows.Close()

	return pgx.CollectOneRow[entity.Flight](rows, pgx.RowToStructByNameLax[entity.Flight])
}
