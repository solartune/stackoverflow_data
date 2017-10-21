#!/bin/sh
./manage.py migrate
./manage.py collectstatic --noinput
# ./manage.py compress

gunicorn config.wsgi:application -c config/gunicorn.py
