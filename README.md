# SpotifyMe Clone 

Welcome to the SpotifyMe repository. This is a work-in-progress portfolio project of the popular music streaming app, Spotify!

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
If you have a working [Docker Environment](https://docs.docker.com/engine/) already, pull the following container images and run the containers.

## Container images

Flask application image

`docker pull ericdwkim/spotifyme-flask:v2`

Postgres database image

`docker pull ericdwkim/spotify-me-pg:v1`

pgAdmin4 image 

`docker push ericdwkim/spotify-me-pgadmin:v1`

## Run containers

`docker compose up -d`

## Tear down containers

`docker compose down --rmi all`