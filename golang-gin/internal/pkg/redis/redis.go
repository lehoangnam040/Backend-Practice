package redis

import (
	"context"

	goRedis "github.com/redis/go-redis/v9"
)

type Redis struct {
	Client *goRedis.Client
}

func New(url string, pass string, db int) (*Redis, error) {
	redis := &Redis{}

	redis.Client = goRedis.NewClient(&goRedis.Options{
		Addr:     url,
		Password: pass,
		DB:       db,
	})

	if err := redis.Client.Ping(context.Background()).Err(); err != nil {
		return nil, err
	}

	return redis, nil
}
