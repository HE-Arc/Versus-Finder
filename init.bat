@ECHO OFF

# Use this inside your venv

if exist .\versusfinder_project\db.sqlite3 del .\versusfinder_project\db.sqlite3
if exist .\versusfinder_project\versusfinder_app\migrations\0001_initial.py del .\versusfinder_project\versusfinder_app\migrations\0001_initial.py

cd versusfinder_project
python.exe .\manage.py makemigrations versusfinder_app
python.exe .\manage.py migrate
python.exe .\manage.py loaddata users.json
python.exe .\manage.py loaddata game.json
python.exe .\manage.py loaddata fighters.json
python.exe .\manage.py loaddata timetable.json
python.exe .\manage.py loaddata usergameprofile.json
python.exe .\manage.py loaddata match.json
python.exe .\manage.py loaddata usermatch.json
python.exe .\manage.py runserver

PAUSE