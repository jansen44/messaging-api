# Running locally
> [!NOTE]
> This doc assumes you're running postgres through the provided .devcontainer setup, hence you need docker or similar container engine compatible with docker compose.

## Setup
```bash
$ export PGSERVICEFILE=$(pwd)/.devcontainer/.pg_service.conf
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## Running
```bash
$ python manage.py runserver
```

