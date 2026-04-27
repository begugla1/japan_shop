#!/usr/bin/env bash
set -euo pipefail

echo "Waiting for PostgreSQL on localhost:5432..."
until pg_isready -h localhost -p 5432 -U "${POSTGRES_USER:-japanshop_user}" >/dev/null 2>&1; do
  sleep 1
done

echo "Applying migrations..."
python manage.py migrate --noinput

if [[ "${CREATE_SUPERUSER:-0}" == "1" ]]; then
  echo "Ensuring Django superuser exists..."
  python manage.py createsuperuser --noinput || true
fi

if [[ "${RUN_HTTPS:-1}" == "1" ]]; then
  echo "Starting Django HTTPS server (runserver_plus)..."
  exec python manage.py runserver_plus 0.0.0.0:8000 --cert-file cert.crt
else
  echo "Starting Django HTTP development server..."
  exec python manage.py runserver 0.0.0.0:8000
fi
