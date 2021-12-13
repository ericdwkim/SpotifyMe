from flask import Blueprint, json, jsonify, abort, request
from ..models import Song, db

bp_songs = Blueprint('songs', __name__, url_prefix='/songs')

# test
# @bp_songs.route('', methods=['GET'])
# def test():
#     return jsonify({"msg": "hello rld"})

# # READ localhost:5000/songs
@bp_songs.route('', methods=['GET'])
def index():
    songs = Song.query.all()
    result = []
    for s in songs:
        result.append(s.serialize())
    return jsonify(result)

# # SHOW localhost:5000/songs/<int:id>
@bp_songs.route('/<int:id>', methods=['GET'])
def show(id: int):
    s_id = Song.query.get_or_404(id)
    return jsonify(s_id.serialize())

# # CREATE localhost:5000/songs/create
@bp_songs.route('/create', methods=['POST'])
def create():
    if ('song_title' or 'song_writer' or 'song_producer' or 'song_length' or 'release_date') not in request.json:
        return abort(400)
    try:
        a_name = request.json['artist_name']
        a_bio = request.json['artist_bio']
        a_bio = request.json['artist_bio']
        a_bio = request.json['artist_bio']
        a_bio = request.json['artist_bio']
        a = Song(
            artist_name=a_name, artist_bio=a_bio
        )
        a.insert()
        return jsonify(a.serialize())
    except:
        return abort(422)

# # UPDATE localhost:5000/songs/<int:id>/update
# @bp_songs.route('/<int:id>/update', methods=['PATCH'])
# def update(id: int):
#     if ('artist_name' or 'artist_bio') not in request.json:
#         return abort(400)
#     if type(request.json['artist_name'] or request.json['artist_bio']) is not str:
#         return abort (400)
#     try:
#         a_id = Song.query.get_or_404(id)
#         a_id.artist_name = request.json['artist_name']
#         a_id.artist_bio = request.json['artist_bio']
#         a_name = a_id.artist_name
#         a_bio = a_id.artist_bio
#         a = Song(
#             artist_name=a_name, artist_bio=a_bio
#         )
#         a.update()
#         return jsonify(a.serialize())
#     except:
#         return abort(422)

# # DELETE localhost:5000/songs/<int:id>
# @bp_songs.route('/<int:id>', methods=['DELETE'])
# def delete(id: int):
#     a_id = Song.query.get_or_404(id)
#     try:
#         db.session.delete(a_id)
#         db.session.commit()
#         return jsonify(True)
#     except:
#         return jsonify(False)
