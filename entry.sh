#!/bin/bash
set -e

./manage.py migrate --noinput
./manage.py collectstatic --noinput
exec uwsgi uwsgi.ini
