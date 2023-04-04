#!/bin/sh

python ../company/manage.py makemigrations
python ../company/manage.py migrate
python ../company/manage.py loaddata initial_data.json