package main

import (
	"fmt"
	"log"
	"net"

	"myservice/m/internal/app/reservation/adapter/grpc/controller"
	postgresrepository "myservice/m/internal/app/reservation/adapter/postgres/repository"
	redisrepository "myservice/m/internal/app/reservation/adapter/redis/repository"
	"myservice/m/internal/app/reservation/adapter/restful/router"
	"myservice/m/internal/app/reservation/usecase"
	"myservice/m/internal/config"
	"myservice/m/internal/pkg/postgres"
	"myservice/m/internal/pkg/redis"
	"runtime"

	"google.golang.org/grpc/health"
	healthgrpc "google.golang.org/grpc/health/grpc_health_v1"

	"github.com/gin-gonic/gin"
	"google.golang.org/grpc"
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
	pgRepository := postgresrepository.NewPgAirportRepository(pg)

	redis, err := redis.New(config.Redis.Url(), config.Redis.Pass, config.Redis.Db)
	if err != nil {
		panic(fmt.Errorf("app - Run - redis.New: %w", err))
	}
	redisRepository := redisrepository.New(redis)

	listAirportUc := &usecase.AirportListUc{
		DbRepo:     pgRepository,
		SearchRepo: redisRepository,
	}

	// GRPC
	grpcServer := grpc.NewServer()
	controller.Setup(grpcServer, listAirportUc)
	healthcheck := health.NewServer()
	healthgrpc.RegisterHealthServer(grpcServer, healthcheck)

	// Rest
	gin := gin.Default()
	router.Setup(gin, listAirportUc)

	go func(_grpcServer *grpc.Server) {
		lis, err := net.Listen("tcp", ":8001")
		if err != nil {
			panic(err)
		}

		if err := grpcServer.Serve(lis); err != nil {
			log.Fatalln("Could not serve the GRPC Server: ", err)
		}
	}(grpcServer)
	gin.Run(config.App.HttpAddress)
}
