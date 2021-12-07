from flask import Blueprint, json, jsonify, abort, request
from ..models import Artist, db

bp_artists = Blueprint('artists', __name__, url_prefix='/artists')

# test endpoint


# @bp_artists.route('', methods=['GET'])
# def index():
#     return jsonify({"msg": "hello world"})

# localhost:5000/artists


@bp_artists.route('', methods=['GET'])
def index():
    artists = Artist.query.all()
    result = []
    for a in artists:
        result.append(a.serialize())
    return jsonify(result)


# @bp_artists.route('', methods=['POST'])
# def create():
#     # request payload _MUST_ contain artist_name
#     if 'artist_name' not in request.json:
#         return abort(400)
#     Artist.query.get_or_404(request.json['artist_name'])
#     # construct artist
#     a = Artist(
#         artist_name=request.json['artist_name']
#     )
#     db.session.add(a)  # prepare CREATE statement
#     db.session.commit()  # execute CREATE statement
#     return jsonify(a.serialize())
