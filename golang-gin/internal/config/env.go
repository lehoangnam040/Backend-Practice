package config

import (
	"fmt"

	"github.com/spf13/viper"
)

type DbPgConfig struct {
	Host string `mapstructure:"host"`
	Port string `mapstructure:"port"`
	Name string `mapstructure:"name"`
	User string `mapstructure:"user"`
	Pass string `mapstructure:"pass"`
}

func (c DbPgConfig) Url() string {
	return fmt.Sprintf("postgres://%s:%s@%s:%s/%s", c.User, c.Pass, c.Host, c.Port, c.Name)
}

type RedisConfig struct {
	Host string `mapstructure:"host"`
	Port string `mapstructure:"port"`
	Pass string `mapstructure:"pass"`
	Db   int    `mapstructure:"db"`
}

func (c RedisConfig) Url() string {
	return fmt.Sprintf("%s:%s", c.Host, c.Port)
}

type AppConfig struct {
	Address string `mapstructure:"address"`
}

type Config struct {
	DbPg  DbPgConfig
	Redis RedisConfig
	App   AppConfig
}

func Setup() (*Config, error) {

	dbViper := viper.New()
	dbViper.SetEnvPrefix("DB_PG")
	dbViper.AutomaticEnv()

	redisViper := viper.New()
	redisViper.SetEnvPrefix("REDIS")
	redisViper.AutomaticEnv()

	appViper := viper.New()
	appViper.SetEnvPrefix("APP")
	appViper.AutomaticEnv()

	return &Config{
		DbPg: DbPgConfig{
			Host: dbViper.GetString("host"),
			Port: dbViper.GetString("port"),
			User: dbViper.GetString("user"),
			Pass: dbViper.GetString("pass"),
			Name: dbViper.GetString("name"),
		},
		Redis: RedisConfig{
			Host: redisViper.GetString("host"),
			Port: redisViper.GetString("port"),
			Pass: redisViper.GetString("pass"),
			Db:   redisViper.GetInt("db"),
		},
		App: AppConfig{
			Address: appViper.GetString("address"),
		},
	}, nil
}
