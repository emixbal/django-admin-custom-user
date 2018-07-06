# Django DumbWays Boilerplate

An all in one solution Django Boilerplate, to get You started quickly!

## Requirements

- Python3
- Git
- MySQL

## Whats Included?

- CRUDSS REST API + Relational (Django Rest Framework)

- Swagger Documentation

- Unit Test

- JWT authentication

- Migration

- No Put Router

## Installation (DEV)

- create database named "whatever" on MySQL

- cd to deserved folder

- Clone the project:
```
$ git clone https://github.com/DumbwaysDotId/DjangoBoilerplate.git
```

- Change dir to cloned project:
```
$ cd DjangoBoilerplate
```

- Create Virtualenv (make sure you already install pip3 install python-virtualenv)
then run this command to create virtualenv
```
virtualenv venv
```

- Change source to venv that you created
```
source venv/bin/activate
```

- Make sure you are already install mysqlclient on your engine
```
Mac OSx: brew install mysql
Ubuntu: sudo apt-get install libmysqlclient-dev
Ubuntu alternative if failed: sudo apt-get install python-mysqldb
```

- Install requirements.txt to install all required dependencies
```
pip3 install -r requirements.txt
```

- Migrate all table:
```
$ python3 manage.py migrate
```

- Create Super User (admin):
```
$ python3 manage.py createsuperuser
```

- Generate static files, mainly for admin page
```
python manage.py collectstatic
```

- Run the server:
```
$ python3 manage.py runserver
```

- Multiple settings files
```
Since the majority of the content of each of these files is the same,
we put all of the repeated code in a base.py
we use a settings file for......
- local environment - local.py
- heroku environment - heroku.py, to override Heroku configuration variable you can run this command:
    heroku config:set DJANGO_SETTINGS_MODULE=app.settings.heroku
```

Congratz!! Now check on browser http://localhost:8000, to view the API Lists doc that you can play around!

We make "unit" and "user" modules, for example to get You started.

## If you found error on migrations, do these

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
