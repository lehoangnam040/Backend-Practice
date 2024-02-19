package redis

type FTSearchItem[T any] struct {
	ExtraAttributes T      `mapstructure:"extra_attributes"`
	Id              string `mapstructure:"id"`
}

type FTSearchOutput[T any] struct {
	Results []FTSearchItem[T] `mapstructure:"results"`
}
