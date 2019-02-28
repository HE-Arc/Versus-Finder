@ECHO OFF
cd versusfinder_project
python.exe .\manage.py migrate
python.exe .\manage.py loaddata game.json
python.exe .\manage.py loaddata fighters.json
python.exe .\manage.py runserver

PAUSE