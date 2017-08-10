#!/bin/bash
project=$(basename "$PWD")
mkdir ../venv
mkdir -p ~/opt/docker/"$project"
virtualenv -p python3 ../venv/"$project"
source ../venv/"$project"/bin/activate
pip install -r requirements.txt
docker-compose up -d
db_name="$project"
docker exec $project-db psql -U postgres -c "CREATE DATABASE $db_name;"
cd "$project"
python manage.py migrate
python manage.py createsuperuser
