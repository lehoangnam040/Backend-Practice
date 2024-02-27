package repository

import (
	"context"
	"fmt"
	"myservice/m/internal/app/reservation/entity"
	"myservice/m/internal/pkg/postgres"

	// "github.com/Masterminds/squirrel"
	"github.com/jackc/pgx/v5"
)

type PgTicketRepository struct {
	*postgres.Postgres
}

// New
func NewPgTicketRepository(pg *postgres.Postgres) *PgTicketRepository {
	return &PgTicketRepository{pg}
}

func (r *PgTicketRepository) CreateATicketOfFlightOptimisticLock(ctx context.Context, id string, availSeat int, version int) (entity.Ticket, error) {
	updateSql, updateArgs, err := r.Builder.
		Update("flight").
		// Set("avail_seat", squirrel.Expr("avail_seat - 1")).
		Set("avail_seat", availSeat).
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

func (r *PgTicketRepository) CreateATicketOfFlightPessimisticLock(ctx context.Context, id string, availSeat int) (entity.Ticket, error) {
	updateSql, updateArgs, err := r.Builder.
		Update("flight").
		Set("avail_seat", availSeat).
		Where("id = ?", id).ToSql()
	if err != nil {
		return entity.Ticket{}, fmt.Errorf("PgFlightRepository - CreateATicketOfFlightPessimisticLock - r.Builder: %w", err)
	}
	createTickSql, createArgs, err := r.Builder.Insert("ticket").Columns("flight_id").Values(id).Suffix("RETURNING *").ToSql()
	if err != nil {
		return entity.Ticket{}, fmt.Errorf("PgFlightRepository - CreateATicketOfFlightPessimisticLock - r.Builder: %w", err)
	}
	// start lock
	tx, err := r.Pool.BeginTx(ctx, pgx.TxOptions{})
	if err != nil {
		return entity.Ticket{}, fmt.Errorf("PgFlightRepository - CreateATicketOfFlightPessimisticLock - r.Builder: %w", err)
	}
	defer func() {
		if err != nil {
			tx.Rollback(ctx)
		} else {
			tx.Commit(ctx)
		}
	}()
	res, err := tx.Exec(ctx, updateSql, updateArgs...)
	if err != nil {
		return entity.Ticket{}, fmt.Errorf("PgFlightRepository - CreateATicketOfFlightPessimisticLock - r.Pool.Exec: %w", err)
	}
	if res.RowsAffected() == 0 {
		return entity.Ticket{}, fmt.Errorf("PgFlightRepository - CreateATicketOfFlightPessimisticLock - res.RowsAffected() == 0: %w", err)
	}
	ticket := entity.Ticket{}
	err = tx.QueryRow(ctx, createTickSql, createArgs...).Scan(&ticket.Id, &ticket.FlightId)
	if err != nil {
		return entity.Ticket{}, fmt.Errorf("PgFlightRepository - CreateATicketOfFlightPessimisticLock - CreateTicket: %w", err)
	}
	// end lock
	return ticket, nil
}
