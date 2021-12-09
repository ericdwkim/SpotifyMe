from flask import Blueprint, json, jsonify, abort, request
from ..models import Artist, db

bp_artists = Blueprint('artists', __name__, url_prefix='/artists')

# read from artsts tale


@bp_artists.route('', methods=['GET'])
def index():
    artists = Artist.query.all()
    result = []
    for a in artists:
        result.append(a.serialize())
    return jsonify(result)

# create record to artists table


@bp_artists.route('/create', methods=['POST'])
def create():
    if 'artist_name' not in request.json:
        return abort(400)
    # try:
    #     Artist.query.get_or_404(request.json['artist_name'])
    #     a = Artist(
    #         artist_name=request.json['artist_name']
    #     )
    #     a.insert()
    #     return jsonify(a.serialize())
    # except:
    #     return abort(422)
    Artist.query.get_or_404(request.json['artist_name'])
    a = Artist(
        artist_name=request.json['artist_name']
    )
    a.insert()
    return jsonify(a.serialize())
