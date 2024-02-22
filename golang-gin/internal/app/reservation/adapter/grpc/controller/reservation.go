package controller

import (
	"context"
	"myservice/m/internal/app/reservation/adapter/grpc/pb"
	"myservice/m/internal/app/reservation/usecase"

	"github.com/jinzhu/copier"
	"google.golang.org/grpc"
)

type ReservationController struct {
	ListUc *usecase.AirportListUc
	pb.ReservationServer
}

func Setup(grpcServer *grpc.Server, listAirportUc *usecase.AirportListUc) {
	pb.RegisterReservationServer(grpcServer, &ReservationController{ListUc: listAirportUc})
}

func (ctrl *ReservationController) GetListAirport(ctx context.Context, req *pb.GetListAirportRequest) (*pb.GetListAirportResponse, error) {
	airports, err := ctrl.ListUc.Logic(ctx, req.Search, req.CursorNext)
	if err != nil {
		return nil, err
	}

	dto := []*pb.Airport{}
	if err = copier.CopyWithOption(&dto, &airports, copier.Option{
		CaseSensitive: true,
		IgnoreEmpty:   true,
		DeepCopy:      false,
	}); err != nil {
		return nil, err
	}
	return &pb.GetListAirportResponse{
		Aiports: dto,
	}, nil
}
