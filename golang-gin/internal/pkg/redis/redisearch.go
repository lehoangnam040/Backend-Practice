package redis

type FTSearchItem[T any] struct {
	ExtraAttributes T      `mapstructure:"extra_attributes"`
	Id              string `mapstructure:"id"`
}

type FTSearchOutput[T any] struct {
	Results []FTSearchItem[T] `mapstructure:"results"`
}

func (o *FTSearchOutput[T]) SearchItems() []T {
	output := make([]T, len(o.Results))
	for i, searchItem := range o.Results {
		output[i] = searchItem.ExtraAttributes
	}
	return output
}
