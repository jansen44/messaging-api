# Description
Very simple implementation of Messaging System API (thread-oriented).

## Features:
- [x] Basic auth (register/login) using email+password;
- [x] Create threads between 1 or more users (unlimited for now);
- [x] Send and read messages from threads;
- [x] Search any message in a thread;


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

