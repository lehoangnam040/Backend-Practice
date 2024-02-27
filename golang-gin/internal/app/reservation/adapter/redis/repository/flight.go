package repository

import (
	"context"
	"fmt"
	"myservice/m/internal/pkg/redis"
	"time"
)

type RedisFlightRepository struct {
	redis *redis.Redis
}

// New
func NewRedisFlightRepository(redis *redis.Redis) *RedisFlightRepository {
	return &RedisFlightRepository{redis}
}

func (r *RedisFlightRepository) AcquireLockOfAFlight(ctx context.Context, id string, expire time.Duration) (bool, error) {
	return r.redis.Client.SetNX(ctx, fmt.Sprintf("dislock-flight-%s", id), 1, expire).Result()
}

func (r *RedisFlightRepository) ReleaseLockOfAFlight(ctx context.Context, id string) (bool, error) {
	res, err := r.redis.Client.Del(ctx, fmt.Sprintf("dislock-flight-%s", id)).Result()
	return res > 0, err
}
