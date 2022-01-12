# SpotifyMe Clone 

Welcome to the SpotifyMe repository. This is a WIP portfolio project of the popular music streaming app, Spotify!

SpotifyMe is built using the [Flask](https://flask.palletsprojects.com/en/2.0.x/) API microframework with a Postgres database. 


## Create and activate the virtual environment

`python -m venv venv`

MacOS

`. venv/bin/activate`

Windows

`. venv/Scripts/activate`

## Check Python and pip versions 

Ensure that `python` is version 3.9.4

`python -V`

`python -m pip install --upgrade pip==21.1.2`

Ensure that `pip` is version 21.1.2

`pip -V`


## Install dependencies to virtual environment

```
    cd flask
    python -m pip install -r requirements.txt
```

There are two ways to run the app:

1. If you have a working [Docker Environment](https://docs.docker.com/engine/) already, pull the following container images and run the containers.

## Container images

Flask application image

`docker pull ericdwkim/spotifyme-flask:v2`

Postgres database image

`docker pull ericdwkim/spotify-me-pg:v1`

pgAdmin4 image 

`docker pull ericdwkim/spotify-me-pgadmin:v1`

## Run containers

`docker compose up -d`

## Run multiple instances

`docker compose up -d --build --scale app=3` 

This command will result in 3 separate instances of the spotifyme-flask (v2) app. 

## Tear down containers

`docker compose down --rmi all`

## Webpage & Endpoints

Visit `localhost:7777`/api 

<br> </br>
2. Running locally on virtual environment

Toggle `SQLALCHEMY_DATABASE_URI` in `flask/app.py` to `localhost` 

Toggle `host` in `flask/config.py` to `localhost` 

```
cd flask
export FLASK_ENV=development
flask run
```

## Run Migrations

```
flask db init
flask db stamp head
flask db migrate
flask db upgrade
```

## Webpage & Endpoints

Visit `localhost:5000`/api 
