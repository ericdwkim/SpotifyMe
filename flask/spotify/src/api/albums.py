from flask import Blueprint, json, jsonify, abort, request
from ..models import Album, db

bp_albums = Blueprint('albums', __name__, url_prefix='/albums')
# print(bp_albums)

# test
@bp_albums.route('', methods=['GET'])
def test():
    return jsonify({"msg": "hello rld"})

