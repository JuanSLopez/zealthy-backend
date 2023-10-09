#!/bin/bash

#Build Project
echo "Bulilding... "
pip install -r requirements.txt

#Migration
echo "Migrating... "
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collecting Static... "
python3.9 manage.py collectstatic --noinput --clear