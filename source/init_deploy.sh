@ECHO OFF

cd versusfinder_project
python ./manage.py makemigrations versusfinder_app
python ./manage.py migrate
python ./manage.py loaddata game.json
python ./manage.py loaddata fighters.json

PAUSE