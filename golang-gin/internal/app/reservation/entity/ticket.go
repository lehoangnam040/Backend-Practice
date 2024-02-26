package entity

type Ticket struct {
	Id       string `db:"id"`
	FlightId string `db:"flight_id"`
}
