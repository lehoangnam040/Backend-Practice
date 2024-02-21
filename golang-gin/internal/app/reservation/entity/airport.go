package entity

type Airport struct {
	Id   int64  `redis:"id" mapstructure:"id" db:"id"`
	Code string `redis:"code" mapstructure:"code" db:"code"`
	Name string `redis:"name" mapstructure:"name" db:"name"`
}
