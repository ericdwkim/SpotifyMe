from flask import Blueprint, json, jsonify, abort, request
from ..models import Artist, db

bp_artists = Blueprint('artists', __name__, url_prefix='/artists')


# GET artist objects; test passes
@bp_artists.route('', methods=['GET'])
def index():
    artists = Artist.query.all()
    result = []
    for a in artists:
        result.append(a.serialize())
    return jsonify(result)


@bp_artists.route('', methods=['POST'])
def create():
    # request payload _MUST_ contain artist_name; recall artist_bio is NULLABLE
    if 'artist_name' not in request.json:
        return abort(400)
    Artist.query.get_or_404(request.json['artist_name'])
    a = Artist(
        artist_name=request.json['artist_name']
    )
    a.insert()
    return jsonify(a.serialize())
