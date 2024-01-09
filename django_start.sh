#!/bin/bash

echo 'Create migrations...'
python manage.py makemigrations client
echo =================================

echo 'Create migrations...'
python manage.py makemigrations rpg
echo =================================

echo 'Start Migrations...'
python manage.py migrate
echo =================================

echo 'start Server...'
python manage.py runserver 0.0.0.0:8000