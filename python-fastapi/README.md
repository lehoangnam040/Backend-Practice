# Service


## Requirements
- python 3.11
- PostgreSQL 14

## Setup development environment

- Install
```
$ pip install -r requirements/dev.txt
```

- Run app with reload to dev
```
$ set -a;source devops/docker/.env.local;set +a
$ uvicorn src.app.first.main:app --reload
...
```


## Test

- UT by pytest (min 90% coverage)
```
$ pytest --cov-report html --cov service --cov-fail-under=90 tests/
```

- Linting
```
$ ./tests/linting/linting.sh
```

## Setup docker

- Build
```
$ docker build -f devops/docker/Dockerfile -t {image_tag} .
```

- Quick run and test at http://localhost:8000
```
$ cd devops/docker
$ docker compose up -d
```
