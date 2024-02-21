package repository

import (
	"context"
	"fmt"
	"myservice/m/internal/app/reservation/entity"
	"myservice/m/internal/pkg/redis"

	"github.com/mitchellh/mapstructure"
)

type RedisAirportRepository struct {
	redis *redis.Redis
}

// New
func New(redis *redis.Redis) *RedisAirportRepository {
	return &RedisAirportRepository{redis}
}

func (r *RedisAirportRepository) Search(ctx context.Context, search string, cursorNext int64, limit int) ([]entity.Airport, error) {
	if search != "" {
		search = fmt.Sprintf("%%%s%%", search)
	}

	// cursor rely on id ASC
	query := fmt.Sprintf("%s @id:[(%d +inf]", search, cursorNext)
	redisResult, err := r.redis.Client.Do(ctx, "FT.SEARCH", IDX_AIRPORT, query, "LIMIT", 0, limit, "SORTBY", "id", "ASC").Result()
	if err != nil {
		panic(fmt.Errorf("RedisAirportRepository - Search - FT.SEARCH: %w", err))
	}

	var parsedResult redis.FTSearchOutput[entity.Airport]
	if err := mapstructure.WeakDecode(redisResult, &parsedResult); err != nil {
		return nil, err
	}
	return parsedResult.SearchItems(), nil
}

func (r *RedisAirportRepository) UpdateCache(ctx context.Context, airports []entity.Airport) error {
	for _, airport := range airports {
		if err := r.redis.Client.HSet(ctx, fmt.Sprintf("%s:%d", HASH_AIRPORT, airport.Id), airport).Err(); err != nil {
			return err
		}
	}
	return nil
}
