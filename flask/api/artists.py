from flask import Blueprint, json, jsonify, abort, request
from models import Artist, db

bp_artists = Blueprint('artists', __name__, url_prefix='/artists')

# test
# @bp_artists.route('', methods=['GET'])
# def test():
#     return jsonify({"msg": "hello rld"})

# READ localhost:5000/artists
@bp_artists.route('', methods=['GET'])
def index():
    artists = Artist.query.all()
    result = []
    for a in artists:
        result.append(a.serialize())
    return jsonify(result)

# SHOW localhost:5000/artists/<int:id>
@bp_artists.route('/<int:id>', methods=['GET'])
def show(id: int):
    a_id = Artist.query.get_or_404(id)
    return jsonify(a_id.serialize())

# CREATE localhost:5000/artists/create
@bp_artists.route('/create', methods=['POST'])
def create():
    if ('artist_name' or 'artist_bio') not in request.json:
        return abort(400)
    try:
        a_name = request.json['artist_name']
        a_bio = request.json['artist_bio']
        a = Artist(
            artist_name=a_name, artist_bio=a_bio
        )
        a.insert()
        return jsonify(a.serialize())
    except:
        return abort(422)

# UPDATE localhost:5000/artists/<int:id>/update
@bp_artists.route('/<int:id>/update', methods=['PATCH'])
def update(id: int):
    if ('artist_name' or 'artist_bio') not in request.json:
        return abort(400)
    if type(request.json['artist_name'] or request.json['artist_bio']) is not str:
        return abort (400)
    try:
        a_id = Artist.query.get_or_404(id)
        a_id.artist_name = request.json['artist_name']
        a_id.artist_bio = request.json['artist_bio']
        a_name = a_id.artist_name
        a_bio = a_id.artist_bio
        a = Artist(
            artist_name=a_name, artist_bio=a_bio
        )
        a.update()
        return jsonify(a.serialize())
    except:
        return abort(422)

# DELETE localhost:5000/artists/<int:id>
@bp_artists.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    a_id = Artist.query.get_or_404(id)
    try:
        db.session.delete(a_id)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

