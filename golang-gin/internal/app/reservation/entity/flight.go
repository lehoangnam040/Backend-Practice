package entity

type Flight struct {
	Id            string `db:"id"`
	DeptAirportId int64  `db:"dept_airport_id"`
	DestAirportId int64  `db:"dest_airport_id"`
	TotalSeat     int    `db:"total_seat"`
	AvailSeat     int    `db:"avail_seat"`
	Version       int    `db:"version"`
}
