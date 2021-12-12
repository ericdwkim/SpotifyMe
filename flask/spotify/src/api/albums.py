from flask import Blueprint, json, jsonify, abort, request
from ..models import Album, db

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
    if 'artist_name' not in request.json or 'artist_bio' not in request.json:
        return abort(400)
    try:
        a_name = request.json['artist_name']
        a_bio = request.json['artist_bio']
        a = Album(
            artist_name=a_name, artist_bio=a_bio
        )
        a.insert()
        return jsonify(a.serialize())
    except:
        return abort(422)

# UPDATE localhost:5000/albums/<int:id>/update
@bp_albums.route('/<int:id>/update', methods=['PATCH'])
def update(id: int):
    # ensure payload params exist
    if 'artist_name' not in request.json or 'artist_bio' not in request.json:
        return abort(400)
    # ensure payload params are strings
    if type(request.json['artist_name'] or request.json['artist_bio']) is not str:
        return abort (400)
    try:
        a_id = Album.query.get_or_404(id)
        a_id.artist_name = request.json['artist_name']
        a_id.artist_bio = request.json['artist_bio']
        a_name = a_id.artist_name
        a_bio = a_id.artist_bio
        a = Album(
            artist_name=a_name, artist_bio=a_bio
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

