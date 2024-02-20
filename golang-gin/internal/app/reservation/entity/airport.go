package entity

type Airport struct {
	Id   int64  `redis:"id" mapstructure:"id"`
	Code string `redis:"code" mapstructure:"code"`
	Name string `redis:"name" mapstructure:"name"`
}
