package usecase

import "myservice/m/internal/app/entity"

type AirportListUc struct{}

func (uc *AirportListUc) Logic() ([]entity.Airport, error) {
	return []entity.Airport{
		{
			Id:   1,
			Code: "HAN",
			Name: "Noi Bai",
		},
		{
			Id:   2,
			Code: "SGN",
			Name: "Tan Son Nhat",
		},
		{
			Id:   3,
			Code: "PQC",
			Name: "Phu Quoc",
		},
		{
			Id:   4,
			Code: "DAD",
			Name: "Da Nang",
		},
		{
			Id:   5,
			Code: "CXR",
			Name: "Cam Ranh",
		},
		{
			Id:   6,
			Code: "VDO",
			Name: "Van Don",
		},
		{
			Id:   7,
			Code: "VCA",
			Name: "Can Tho",
		},
	}, nil
}
