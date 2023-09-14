
.PHONY: d-homework-i-run
# Make all actions needed for run homework from zero.
d-homework-i-run:
	@bash ./scripts/d-homework-i-run.sh

.PHONY: d-homework-i-purge
# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge


.PHONY: init-configs
# Configuration files initialization
init-configs:
	@cp .env.homework .env &&\
	cp docker-compose.override.dev.yml docker-compose.override.yml


.PHONY: d-run
# Just run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=outside_dev \
		docker compose \
			up --build


.PHONY: d-run-i-local-dev
# Just run
d-run-i-local-dev:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=local_dev \
		docker compose \
			up --build


.PHONY: d-purge
# Purge all data related with services
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0


.PHONY: init-dev
# Attention! First use d-run-i-local-dev. Init environment for development.
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements/local.txt && \
	pre-commit install && \
	python manage.py initialize_currency && \
	python manage.py create_cache_table

.PHONY: homework-i-run
# Run homework.
homework-i-run:
	@make migrate && \
	@python manage.py runserver localhost:8000


.PHONY: homework-i-purge
homework-i-purge:
	@echo Goodbye


.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files


.PHONY: migrations
# Make migrations
migrations:
	@python manage.py makemigrations

.PHONY: migrate
# Migrate
migrate:
	@python manage.py migrate

.PHONY: create-admin
# Create admin
create-admin:
	@python manage.py create_admin

.PHONY: generate-users
# Generate data for apps
generate-users:
	@python manage.py generate_users