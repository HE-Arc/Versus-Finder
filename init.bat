@ECHO OFF

# Use this inside your venv

cd versusfinder_project
python.exe .\manage.py makemigrations versusfinder_app
python.exe .\manage.py migrate
python.exe .\manage.py loaddata users.json
python.exe .\manage.py loaddata game.json
python.exe .\manage.py loaddata fighters.json
python.exe .\manage.py loaddata timetable.json
python.exe .\manage.py loaddata usertimetable.json
python.exe .\manage.py loaddata usergameprofile.json
python.exe .\manage.py loaddata match.json
python.exe .\manage.py runserver

PAUSE