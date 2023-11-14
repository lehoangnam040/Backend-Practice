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

type AppConfig struct {
	Address string `mapstructure:"address"`
}

type Config struct {
	DbPg DbPgConfig
	App  AppConfig
}

func Setup() (*Config, error) {

	dbViper := viper.New()
	dbViper.SetEnvPrefix("DB_PG")
	dbViper.AutomaticEnv()

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
		App: AppConfig{
			Address: appViper.GetString("address"),
		},
	}, nil
}
