#!bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput


gunicorn config.wsgi:application -b :8001 --timeout 120 --workers=3 --threads=3 --worker-connections=1000
