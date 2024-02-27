package main

import (
	"context"
	"fmt"

	postgresrepository "myservice/m/internal/app/reservation/adapter/postgres/repository"
	"myservice/m/internal/config"
	"myservice/m/internal/pkg/postgres"
	"runtime"
)

func init() {
	runtime.GOMAXPROCS(runtime.NumCPU())
}

func main() {

	config, err := config.Setup()
	if err != nil {
		panic(fmt.Sprintf("Read config error %s", err))
	}

	// Repository
	pg, err := postgres.New(config.DbPg.Url(), postgres.MaxPoolSize(20))
	if err != nil {
		panic(fmt.Errorf("app - Run - postgres.New: %w", err))
	}
	defer pg.Close()

	pgTicketRepository := postgresrepository.NewPgTicketRepository(pg)

	ticket, err := pgTicketRepository.CreateATicketOfFlightOptimisticLock(context.Background(), "any-id-string", 0)
	if err != nil {
		panic(err)
	}

	fmt.Println(ticket)
}
