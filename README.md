# Versus-Finder
Project to help Smash Bros (or other games maybe) players to find some opponents according to their game schedules

# User guide to install the project

## First clone the project


```bash
git clone https://github.com/HE-Arc/Versus-Finder.git
```
Go into the folder project.

## Installation of dependencies

Create and activate a python virtual environement. 
```bash
python -m virtualenv venv

source venv/bin/activate
```
Now we can install the dependencies 

```bash
pip install -r requirements.txt
```
## Launch the project

First, we must initiate the project.


```bash
sh init.sh
```

Then you can launch the project with the following command.

```bash
python manage.py runserver
```

Open a brower and go to localhost:8000
