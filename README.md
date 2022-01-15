# SpotifyMe (EC2)

Welcome to the SpotifyMe repository; this is a clone of the popular music streaming app, Spotify!

SpotifyMe is built using the [Flask](https://flask.palletsprojects.com/en/2.0.x/) API framework with the [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) extension for database migrations. This is an ongoing WIP project with new improvements to come! 

## Clone the repository & switch to EC2 branch

```
$ git clone https://github.com/ericdwkim/SpotifyMe
$ git checkout ec2
```

## Install dependencies to build Python
```
$ sudo apt update
$ sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev
$ gcc --version 
```

Install pyenv to control multiple Python versions

```
$ pyenv install -v 3.9.4
$ pyenv versions
$ pyenv global 3.9.4
```

Download Python 3.9.4 from the official [Python download page](https://www.python.org/downloads/source/) with wget:

`$ wget https://www.python.org/ftp/python/3.9.4/Python-3.9.4.tgz`

Once download is complete, extract the zipped archive

`$ tar -xf Python-3.9.4.tgz`

Navigate to source directory and execute the `configure` script

```
$ cd Python-3.9.4
$ ./configure --enable-optimizations
```
The `--enable-optimizations` option optimizes the Python binary by running multiple tests. This makes the build process slower. The script runs a number of checks to ensure that all of the dependencies on your system are present.

Start the Python 3.9.4 build process

`$ make -j 2`

When the build process is complete, install the Python binaries

`$ sudo make altinstall`

We use `altinstall` instead of `install` as the latter will overwrite default system level python3 binary

## Confirm Python version

Ensure that the installed `python3.9` is version `3.9.4` on the venv

`$ python3.9 -V`

## Initialize a virtual environment

Learn more about venv [here](https://docs.python.org/3/library/venv.html#creating-virtual-environments) 

Debian/Ubuntu systems:

```
$ sudo apt install python3.9-venv python3.9-dev
$ python3.9 -m venv --without-pip venv
$ . venv/bin/activate
$ curl https://bootstrap.pypa.io/get-pip.py | python
reactivate venv
check pip
pip instaall --upgrade pip=21.1.2
```
The virtual environment is created with the `--without-pip` option as a workaround to pyenv returning a non-zero exit status 1 error and without having to resort to `setuptool` shenanigans.

# Install and upgrade pip  

Ensure that the installed `pip` is version `21.1.2` on the venv
```
$ python3.9 -m pip install --upgrade pip==21.1.2
$ pip -V
```

## Install dependencies to virtual environment

```
$ cd flask
$ python3.9 -m pip install -r requirements.txt
```
TODO:

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