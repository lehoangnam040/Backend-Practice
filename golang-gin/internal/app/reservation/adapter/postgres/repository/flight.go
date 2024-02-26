package repository

import (
	"context"
	"fmt"
	"myservice/m/internal/app/reservation/entity"
	"myservice/m/internal/pkg/postgres"

	"github.com/Masterminds/squirrel"
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
	sql, args, err := r.Builder.
		Select("id, dept_airport_id, dest_airport_id, total_seat, avail_seat, version").
		From("flight").
		Where("id = ?", id).
		ToSql()
	if err != nil {
		return entity.Flight{}, fmt.Errorf("PgFlightRepository - GetOneById - r.Builder: %w", err)
	}

	rows, err := r.Pool.Query(ctx, sql, args)
	if err != nil {
		return entity.Flight{}, fmt.Errorf("PgFlightRepository - GetOneById - r.Pool.Query: %w", err)
	}
	defer rows.Close()

	return pgx.CollectOneRow[entity.Flight](rows, pgx.RowToStructByNameLax[entity.Flight])
}

func (r *PgFlightRepository) CreateATicketOfFlightOptimisticLock(ctx context.Context, id string, version int) (entity.Ticket, error) {
	updateSql, updateArgs, err := r.Builder.
		Update("flight").
		Set("avail_seat", squirrel.Expr("avail_seat - 1")).
		Set("version", version+1).
		Where("id = ? AND version = ?", id, version).ToSql()
	if err != nil {
		return entity.Ticket{}, fmt.Errorf("PgFlightRepository - CreateATicketOfFlightOptimisticLock - r.Builder: %w", err)
	}
	createTickSql, createArgs, err := r.Builder.Insert("ticket").Columns("flight_id").Values(id).Suffix("RETURNING *").ToSql()
	if err != nil {
		return entity.Ticket{}, fmt.Errorf("PgFlightRepository - CreateATicketOfFlightOptimisticLock - r.Builder: %w", err)
	}
	// start lock
	tx, err := r.Pool.BeginTx(ctx, pgx.TxOptions{})
	if err != nil {
		return entity.Ticket{}, fmt.Errorf("PgFlightRepository - CreateATicketOfFlightOptimisticLock - r.Builder: %w", err)
	}
	defer func() {
		if err != nil {
			tx.Rollback(ctx)
		} else {
			// Uncomment to test 2 concurrent transaction
			// fmt.Print("Press 'Enter' to continue...")
			// bufio.NewReader(os.Stdin).ReadBytes('\n')
			tx.Commit(ctx)
		}
	}()
	res, err := tx.Exec(ctx, updateSql, updateArgs...)
	if err != nil {
		return entity.Ticket{}, fmt.Errorf("PgFlightRepository - CreateATicketOfFlightOptimisticLock - r.Pool.Exec: %w", err)
	}
	if res.RowsAffected() == 0 {
		return entity.Ticket{}, fmt.Errorf("PgFlightRepository - CreateATicketOfFlightOptimisticLock - res.RowsAffected() == 0: %w", err)
	}
	ticket := entity.Ticket{}
	err = tx.QueryRow(ctx, createTickSql, createArgs...).Scan(&ticket.Id, &ticket.FlightId)
	if err != nil {
		return entity.Ticket{}, fmt.Errorf("PgFlightRepository - CreateATicketOfFlightOptimisticLock - CreateTicket: %w", err)
	}
	// end lock
	return ticket, nil
}
