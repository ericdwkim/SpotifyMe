from datetime import datetime
from flask import Blueprint, json, jsonify, abort, request
from sqlalchemy.sql.sqltypes import Date
from models import Album, db

bp_albums = Blueprint('albums', __name__, url_prefix='/albums')
# print(bp_albums)

# test
# @bp_albums.route('', methods=['GET'])
# def test():
#     return jsonify({"msg": "hello rld"})

# READ localhost:5000/albums
@bp_albums.route('', methods=['GET'])
def index():
    albums = Album.query.all()
    result = []
    for a in albums:
        result.append(a.serialize())
    return jsonify(result)

# SHOW localhost:5000/albums/<int:id>
@bp_albums.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Album.query.get_or_404(id)
    return jsonify(a.serialize())

# CREATE localhost:5000/albums/create
@bp_albums.route('/create', methods=['POST'])
def create():
    if ('album_title' or 'album_length' or 'artwork_url' or 'num_of_songs' or ' release_date') not in request.json:
        return abort(400)
    try:
        a_title = request.json['album_title']
        a_length = request.json['album_length']
        a_url = request.json['artwork_url']
        a_numSongs = request.json['num_of_songs']
        a_releaseDate = request.json['release_date']

        a = Album(
            album_title=a_title, album_length=a_length, artwork_url=a_url, num_of_songs=a_numSongs, release_date=a_releaseDate
        )
        a.insert()
        return jsonify(a.serialize())
    except:
        return abort(422)

# UPDATE localhost:5000/albums/<int:id>/update
@bp_albums.route('/<int:id>/update', methods=['PATCH'])
def update(id: int):
    if ('album_title' or 'album_length' or 'artwork_url' or 'num_of_songs' or ' release_date') not in request.json:
        return abort(400)
    if type(request.json['album_title'] or request.json['artwork_url']) is not str:
        return abort (400)
    try:
        a_id = Album.query.get_or_404(id)
        a_id.album_title = request.json['album_title']
        a_id.album_length = request.json['album_length']
        a_id.artwork_url = request.json['artwork_url']
        a_id.num_of_songs = request.json['num_of_songs']
        a_id.release_date = request.json['release_date']
        a_title= a_id.album_title
        a_length = a_id.album_length
        a_artworkURL = a_id.artwork_url
        a_numOfSongs = a_id.num_of_songs
        a_releaseDate = a_id.release_date
        a = Album(
            album_title=a_title, album_length=a_length, artwork_url=a_artworkURL, num_of_songs=a_numOfSongs, release_date=a_releaseDate
        )
        a.update()
        return jsonify(a.serialize())
    except:
        return abort(422)

# DELETE localhost:5000/albums/<int:id>
@bp_albums.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    a_id = Album.query.get_or_404(id)
    try:
        db.session.delete(a_id)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

