from flask import Blueprint, json, jsonify, abort, request
from ..models import Song, db

bp_songs = Blueprint('songs', __name__, url_prefix='/songs')

# test
# @bp_songs.route('', methods=['GET'])
# def test():
#     return jsonify({"msg": "hello rld"})

