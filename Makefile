DB_USER=postgres
DB_NAME=chats
DB_CONTAINER_NAME=devcontainer-db-1

.PHONY: db-connect
db-connect:
	docker exec -it $(DB_CONTAINER_NAME) psql -U $(DB_USER) -d $(DB_NAME)
