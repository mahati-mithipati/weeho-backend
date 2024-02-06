# weeho_backend

This project was generated using fastapi_template.

## Poetry

This project uses poetry. It's a modern dependency management
tool.

To run the project use this set of commands:

```bash
poetry install
poetry run python -m weeho_backend
```

This will start the server on the configured host.

You can find swagger documentation at `/api/docs`.

You can read more about poetry here: https://python-poetry.org/


## Project structure

```bash
$ tree "weeho_backend"
weeho_backend
├── conftest.py  # Fixtures for all tests.
├── db  # module contains db configurations
│   ├── dao  # Data Access Objects. Contains different classes to interact with database.
│   └── models  # Package contains different models for ORMs.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.
```

## Configuration

WEEHO_BACKEND_ENVIRONMENT="dev"

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.



## Running tests

1. you need to start a database.
Either install MYSQL locally, or simply use docker

```
docker run -p "3306:3306" -e "MYSQL_PASSWORD=weeho_backend" -e "MYSQL_USER=weeho_backend" -e "MYSQL_DATABASE=weeho_backend" -e ALLOW_EMPTY_PASSWORD=yes bitnami/mysql:8.0.30
```


2. Run the pytest.
```bash
pytest -vv .
```
