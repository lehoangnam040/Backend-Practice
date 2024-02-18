package main

import (
	"context"
	"fmt"
	"myservice/m/internal/pkg/redis"

	"github.com/mitchellh/mapstructure"
)

type Movie struct {
	Title       string `mapstructure:"title"`
	ReleaseYear int32  `mapstructure:"release_year"`
}

type Document struct {
	ExtraAttributes Movie  `mapstructure:"extra_attributes"`
	Id              string `mapstructure:"id"`
}

type Search struct {
	Results []Document `mapstructure:"results"`
}

func main() {
	r, err := redis.New("0.0.0.0:16379", "", 0)
	if err != nil {
		panic(fmt.Errorf("app - Run - redis.New: %w", err))
	}

	ctx := context.Background()
	rawResult, err := r.Client.Do(ctx, "FT.SEARCH", "idx:movie", "war", "RETURN", "2", "title", "release_year").Result()
	if err != nil {
		panic(fmt.Errorf("app - Run - FT.SEARCH: %w", err))
	}

	var z Search
	mapstructure.WeakDecode(rawResult, &z)
	fmt.Println(z.Results)
}
