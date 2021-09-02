#!/bin/bash

#python3 manage.py makemigrations --dry-run --verbosity 3
python3 manage.py collectstatic --no-input
python3 manage.py makemigrations
python3 manage.py migrate --no-input

#python3 manage.py create_default_user
while true; do
    python3 manage.py runserver 0.0.0.0:8000
    sleep 5s
done
