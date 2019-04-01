@ECHO OFF

cd versusfinder_project
python ./manage.py makemigrations versusfinder_app
python ./manage.py migrate

PAUSE