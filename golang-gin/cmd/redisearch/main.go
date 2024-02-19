package main

import (
	"context"
	"fmt"
	"myservice/m/internal/pkg/redis"

	"github.com/mitchellh/mapstructure"
)

/*
https://developer.redis.com/howtos/moviesdatabase/import
FT.CREATE idx:movie ON hash PREFIX 1 "movie:" SCHEMA title TEXT SORTABLE release_year NUMERIC SORTABLE rating NUMERIC SORTABLE genre TAG SORTABLE
FT.ALTER idx:movie SCHEMA ADD plot TEXT WEIGHT 0.5

HSET movie:11002 title "Star Wars: Episode V - The Empire Strikes Back" plot "After the Rebels are brutally overpowered by the Empire on the ice planet Hoth, Luke Skywalker begins Jedi training with Yoda, while his friends are pursued by Darth Vader and a bounty hunter named Boba Fett all over the galaxy." release_year 1980 genre "Action" rating 8.7 votes 1127635 imdb_id tt0080684
HSET movie:11003 title "The Godfather" plot "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son." release_year 1972 genre "Drama" rating 9.2 votes 1563839 imdb_id tt0068646
HSET movie:11004 title "Heat" plot "A group of professional bank robbers start to feel the heat from police when they unknowingly leave a clue at their latest heist." release_year 1995 genre "Thriller" rating 8.2 votes 559490 imdb_id tt0113277
HSET "movie:11005" title "Star Wars: Episode VI - Return of the Jedi" genre "Action" votes 906260 rating 8.3 release_year 1983  plot "The Rebels dispatch to Endor to destroy the second Empire's Death Star." ibmdb_id "tt0086190"
*/
func main() {
	r, err := redis.New("0.0.0.0:16379", "", 0)
	if err != nil {
		panic(fmt.Errorf("app - Run - redis.New: %w", err))
	}

	ctx := context.Background()
	rawResult, err := r.Client.Do(ctx, "FT.SEARCH", "idx:movie", "%empie%", "RETURN", "2", "title", "plot").Result()
	if err != nil {
		panic(fmt.Errorf("app - Run - FT.SEARCH: %w", err))
	}

	var z redis.FTSearchOutput[struct {
		Title       string `mapstructure:"title"`
		ReleaseYear int    `mapstructure:"release_year"`
	}]
	mapstructure.WeakDecode(rawResult, &z)
	fmt.Println(z.Results)
}
