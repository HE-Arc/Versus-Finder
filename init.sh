@ECHO OFF

cd versusfinder_project
python ./manage.py makemigrations versusfinder_app
python ./manage.py migrate
python ./manage.py loaddata users.json
python ./manage.py loaddata game.json
python ./manage.py loaddata fighters.json
python ./manage.py loaddata timetable.json
python ./manage.py loaddata usergameprofile.json
python ./manage.py loaddata match.json
python ./manage.py loaddata usermatch.json
python ./manage.py runserver

PAUSE