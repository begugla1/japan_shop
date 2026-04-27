SHELL := /usr/bin/env bash

PYTHON ?= python3
VENV ?= .venv
BIN := $(VENV)/bin
PIP := $(BIN)/pip
PY := $(BIN)/python
MANAGE := $(PY) manage.py

DB_NAME ?= japanshop
DB_USER ?= japanshop_user
DB_PASSWORD ?=

.PHONY: help bootstrap venv install env check-system check-python check-postgres db-role db-create migrate run run-https shell superuser clean

help:
	@echo "Targets:"
	@echo "  make bootstrap     - full local setup: venv, deps, env file, postgres role/db, migrate"
	@echo "  make venv          - create Python virtual environment"
	@echo "  make install       - install pip requirements into venv"
	@echo "  make env           - create .env from .env.example if missing"
	@echo "  make check-system  - check required system tools"
	@echo "  make db-role       - create/update postgres role ($(DB_USER))"
	@echo "  make db-create     - create postgres database ($(DB_NAME))"
	@echo "  make migrate       - apply Django migrations"
	@echo "  make run           - run Django dev server"
	@echo "  make run-https     - run HTTPS server via runserver_plus"
	@echo "  make shell         - open Django shell"
	@echo "  make superuser     - create Django superuser"
	@echo "  make clean         - remove local virtual environment"

bootstrap: check-system venv install env db-role db-create migrate
	@echo "Bootstrap complete."
	@echo "Start with: make run"

venv:
	@test -d "$(VENV)" || $(PYTHON) -m venv "$(VENV)"

install: venv
	@$(PIP) install --upgrade pip setuptools wheel
	@$(PIP) install -r requirements.txt

env:
	@test -f .env || cp .env.example .env
	@echo ".env ready (edit secrets if needed)."

check-system: check-python check-postgres

check-python:
	@command -v $(PYTHON) >/dev/null || (echo "Missing $(PYTHON). Install Python 3.10+." && exit 1)

check-postgres:
	@command -v psql >/dev/null || (echo "Missing psql (PostgreSQL client/server). Install PostgreSQL first." && exit 1)

db-role: check-postgres
	@psql postgres -v ON_ERROR_STOP=1 -c "DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '$(DB_USER)') THEN CREATE ROLE $(DB_USER) LOGIN PASSWORD '$(DB_PASSWORD)'; ELSE ALTER ROLE $(DB_USER) WITH LOGIN PASSWORD '$(DB_PASSWORD)'; END IF; END $$;"

db-create: check-postgres
	@psql -tc "SELECT 1 FROM pg_database WHERE datname = '$(DB_NAME)'" postgres | rg -q 1 || createdb -O "$(DB_USER)" "$(DB_NAME)"

migrate:
	@$(MANAGE) migrate

run:
	@$(MANAGE) runserver

run-https:
	@$(MANAGE) runserver_plus --cert-file cert.crt

shell:
	@$(MANAGE) shell

superuser:
	@$(MANAGE) createsuperuser

clean:
	@rm -rf "$(VENV)"
