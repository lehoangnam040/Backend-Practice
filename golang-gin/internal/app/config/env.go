package config

import (
	"github.com/spf13/viper"
)

type DbPgConfig struct {
	Host string `mapstructure:"host"`
	Port string `mapstructure:"port"`
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
		},
		App: AppConfig{
			Address: appViper.GetString("address"),
		},
	}, nil
}
