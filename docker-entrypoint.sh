#!/bin/sh
set -e

# Hanya untuk docker compose lokal: SECRET_KEY acak per start jika diizinkan.
if [ ${ALLOW_EPHEMERAL_SECRET_KEY:-0} = 1 ] && [ -z ${SECRET_KEY:-} ]; then
  export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(50))')
fi

python manage.py migrate --noinput
exec gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2