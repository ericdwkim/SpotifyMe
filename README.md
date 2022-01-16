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
$ make
$ sudo make install
```
The `--enable-optimizations` option optimizes the Python binary by running multiple tests. This makes the build process slower. The script runs a number of checks to ensure that all of the dependencies on your system are present.

Start the Python 3.9.4 build process

`$ make -j 2`

When the build process is complete, install the Python binaries

`$ sudo make altinstall`

We use `altinstall` instead of `install` as the latter will overwrite default system level python3 binary

## Confirm Python version

Ensure that the installed `python3.9` is version `3.9.4` at the system level

`$ python3.9 -V`

## Initialize a virtual environment

Learn more about venv [here](https://docs.python.org/3/library/venv.html#creating-virtual-environments) 

Debian/Ubuntu systems:

```
$ sudo apt install python3.9-venv python3.9-dev
$ python3.9 -m venv --without-pip venv
$ . venv/bin/activate
```
The virtual environment is created with the `--without-pip` option as a workaround to pyenv returning a non-zero exit status 1 error and without having to resort to `setuptool` shenanigans.

## Install pip to venv
```
$ curl https://bootstrap.pypa.io/get-pip.py | python
$ deactivate
$ rm -rf venv
$ python3.9 -m venv venv
$ . venv/bin/activate
$ ls venv/bin
$ which pip
```
Pip is installed with `curl` to the virtual environment. A new `venv` is created to reflect the correct `pip` installation which can be confirmed in `venv/bin` directory. 

# Upgrade pip  

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

Set up a [Docker Environment](https://docs.docker.com/engine/), pull the images, and run the containers.

## Container images

Flask web app image

`$ docker pull ericdwkim/ec2-spotifyme-flask-web:v3`

Postgres database (linux/amd64) image

`$ docker pull ericdwkim/spotifyme-pg:v1`

Nginx reverse-proxy image

`$ docker pull ericdwkim/ec2-spotifyme-flask-nginx:v4`

## Run containers

```
$ docker compose up -d
$ docker ps 
```
This command will run the `ec2_web`, `ec2_nginx` , `ec2_pg` containers. 

## Tear down containers

`$ docker compose down --rmi all`

This command will stop and remove the `ec2_web`, `ec2_nginx` , `ec2_pg` containers. 

## Webpage & Endpoints

Ping `ec2-3-135-127-249.us-east-2.compute.amazonaws.com:5000`/api 

## Run Migrations


```
$ cd flask
$ flask db init
$ flask db stamp head
$ flask db migrate
$ flask db upgrade
```

