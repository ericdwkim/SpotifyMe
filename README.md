# SpotifyMe

Welcome to the SpotifyMe repository; this is a clone of the popular music streaming app, Spotify!

SpotifyMe is built using the [Flask](https://flask.palletsprojects.com/en/2.0.x/) API framework with the [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) extension for database migrations. This is an ongoing WIP project with new improvements to come! 

## Clone the repository 

`$ git clone https://github.com/ericdwkim/SpotifyMe`

## Initialize a virtual environment

Learn more about venv [here](https://docs.python.org/3/library/venv.html#creating-virtual-environments) 

Unix/MacOS:

```
$ python3 -m venv venv
$ . venv/bin/activate
```

Windows:

```
$ python3 -m venv venv
$ . venv/Scripts/activate
```
## Check Python and pip versions 

This project has only been tested with the following `python` and `pip` versions.

Ensure that the installed `python` is version `3.9.4` on the venv

`$ python -V`

Ensure that the installed `pip` is version `21.1.2` on the venv

```
$ python -m pip install --upgrade pip==21.1.2
$ pip -V
```

## Install dependencies to virtual environment

```
$ cd flask
$ python -m pip install -r requirements.txt
```

There are two ways to run the app:

1. If you have a working [Docker Environment](https://docs.docker.com/engine/) already, pull the following images and run the containers.

## Container images

Flask application image

`$ docker pull ericdwkim/spotifyme-flask:v2`

Postgres database image

`$ docker pull ericdwkim/spotify-me-pg:v1`

pgAdmin image (optional)

`$ docker pull ericdwkim/spotify-me-pgadmin:v1`

## Run containers

`$ docker compose up -d`

## Run multiple instances

`$ docker compose up -d --build --scale app=3` 

This command will result in 3 separate instances of the spotifyme-flask (v2) app. 

## Tear down containers

`$ docker compose down --rmi all`

## Webpage & Endpoints

Visit `localhost:7777`/api 

<br> </br>
2. Running locally on virtual environment

Toggle `SQLALCHEMY_DATABASE_URI` in `flask/app.py` to `localhost` 

Toggle `host` in `flask/config.py` to `localhost` 

```
$ cd flask
$ export FLASK_ENV=development
$ flask run
```

## Run Migrations

`$ flask db init` (if `migrations` directory does not yet exist)

```
$ flask db stamp head
$ flask db migrate
$ flask db upgrade
```

## Webpage & Endpoints

Visit `localhost:5000`/api 
