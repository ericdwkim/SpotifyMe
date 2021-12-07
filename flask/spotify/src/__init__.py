import os
from flask import Flask
from flask_migrate import Migrate
from .models import db
from .api import accounts, artists, albums, groups, songs

# https://flask.palletsprojects.com/en/2.0.x/patterns/appfactories/


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='postgresql://postgres@localhost:5432/spotify',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    migrate = Migrate(app, db)

    # app.register_blueprint(accounts.bp_accounts)
    # app.register_blueprint(albums.bp_albums)
    app.register_blueprint(artists.bp_artists)
    # app.register_blueprint(groups.bp_groups)
    # app.register_blueprint(songs.bp_songs)

    return app
