# NAICA PROJECT
#### Technologies

  * [Django](https://www.djangoproject.com/)
  * [Docker](https://www.docker.com/)
  * [Python 3.6 / 3.7](https://www.python.org/)

# Prepare project
For run the project, complete the next steps to make up, all the commands and compact in a makefile with a list.
 
You need to have installed `git`, `docker`, `ssh` and and a use a `terminal`.

# Run project

After that, run in the next order to generate a correct environment:

#### Basic commands
  * `make up` Create a docker image, run migrations to create database and make runserver of project.
  
Now, can access since next URLs:

* `http://localhost:8000/`
* `http://127.0.0.1:8000/`
* `http://0.0.0.0:8000/`


## Run project without Docker (not recommended)

If you don't want to use Docker, you need to have installed `virtualenv`, `python 3.7 or 3.6`.

For install virtualenv: https://virtualenv.pypa.io/en/latest/installation.html

* ` virtualenv env --python=python3.7* ` Create and environment with python version assigned.

After that, active environmet with the next command (check env location):

* `source env/bin/activate` this will active environment, and if have a custom terminal you can check in the promp,  see the env name.

Install requirements with  next command, inside the naica project.

* `pip install -r requirements.txt`

Run migration, to create database

* `python manage.py migrate`

Run project with next command:

* `python manage.py runserver`

