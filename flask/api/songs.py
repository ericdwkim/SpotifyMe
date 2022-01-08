from flask import Blueprint, json, jsonify, abort, request
from models import Song, db

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

# CREATE localhost:5000/songs/create
@bp_songs.route('/create', methods=['POST'])
def create():
    if ('song_title' or 'song_writer' or 'song_producer' or 'song_length' or 'release_date') not in request.json:
        return abort(400)
    try:
        s_title = request.json['song_title']
        s_writer = request.json['song_writer']
        s_producer = request.json['song_producer']
        s_length = request.json['song_length']
        s_releaseDate = request.json['release_date']
        s = Song(
            song_title=s_title, song_writer=s_writer, song_producer=s_producer, song_length=s_length, release_date=s_releaseDate
        )
        s.insert()
        return jsonify(s.serialize())
    except:
        return abort(422)

# UPDATE localhost:5000/songs/<int:id>/update
@bp_songs.route('/<int:id>/update', methods=['PATCH'])
def update(id: int):
    if ('song_title' or 'song_writer' or 'song_producer' or 'song_length' or 'release_date') not in request.json:
        return abort(400)
    if type(request.json['song_title'] or request.json['song_writer'] or request.json['song_producer']) is not str:
        return abort (400)
    try:
        s_id = Song.query.get_or_404(id)
        s_id.song_title = request.json['song_title']
        s_id.song_writer = request.json['song_writer']
        s_id.song_producer = request.json['song_producer']
        s_id.song_length = request.json['song_length']
        s_id.releaseDate = request.json['release_date']
        s_title = s_id.song_title
        s_writer = s_id.song_writer
        s_producer = s_id.song_producer
        s_length = s_id.song_length
        s_releaseDate = s_id.releaseDate
        s = Song(
            song_title=s_title, song_writer=s_writer, song_producer=s_producer, song_length=s_length, release_date=s_releaseDate
        )
        s.update()
        return jsonify(s.serialize())
    except:
        return abort(422)

# # DELETE localhost:5000/songs/<int:id>
@bp_songs.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    s_id = Song.query.get_or_404(id)
    try:
        db.session.delete(s_id)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
