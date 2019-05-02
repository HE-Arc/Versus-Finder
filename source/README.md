# Versus-Finder
Project to help Smash Bros (or other games maybe) players to find some opponents according to their game schedules

#  User guide to install the project


## Requirements
* Python 3.7.3
* Pip 19.0.3


## 1. Clone the project


```bash
git clone https://github.com/HE-Arc/Versus-Finder.git
```
Go into the folder project.

## 2. Installation of dependencies

Create and activate a python virtual environement. 
```bash
python -m virtualenv venv

source venv/bin/activate
```
Now we can install the dependencies.

```bash
pip install -r requirements.txt
```
## 3. Launch the project

First, we must initiate the project.


```bash
sh init.sh
```

Then you can launch the project with the following command.

```bash
python manage.py runserver
```

Open a browser and go to [http://localhost:8000](http://localhost:8000).
