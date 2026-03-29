COMPOSE_FILE := docker/docker-compose.yml
DC := docker-compose -f $(COMPOSE_FILE)

.PHONY: up down build restart logs

server:
	$(DC) up -d

clean:
	$(DC) down

build:
	$(DC) build

restart: down up

logs:
	$(DC) logs -f
