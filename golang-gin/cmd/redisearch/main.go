package main

import (
	"context"
	"fmt"
	postgresrepository "myservice/m/internal/app/reservation/adapter/postgres/repository"
	"myservice/m/internal/app/reservation/entity"
	"myservice/m/internal/config"
	"myservice/m/internal/pkg/postgres"
	"myservice/m/internal/pkg/redis"

	"github.com/mitchellh/mapstructure"
)

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

	fmt.Println(config.Redis)
	r, err := redis.New(config.Redis.Url(), config.Redis.Pass, config.Redis.Db)
	if err != nil {
		panic(fmt.Errorf("app - Run - redis.New: %w", err))
	}
	ctx := context.Background()

	pgRepository := postgresrepository.New(pg)
	airports, err := pgRepository.GetAll(ctx)
	if err != nil {
		panic(err)
	}

	for _, airport := range airports {
		key := fmt.Sprintf("reservation_airport:%d", airport.Id)
		fmt.Println(key, airport)
		if err := r.Client.HSet(ctx, key, airport).Err(); err != nil {
			fmt.Println(err)
		}
	}

	rawResult, err := r.Client.Do(ctx, "FT.SEARCH", "idx:reservation_airport", "*", "LIMIT", 0, 100).Result()
	if err != nil {
		panic(fmt.Errorf("app - Run - FT.SEARCH: %w", err))
	}

	var z redis.FTSearchOutput[entity.Airport]
	mapstructure.WeakDecode(rawResult, &z)
	fmt.Println(z.Results)
}
