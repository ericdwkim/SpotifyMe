from flask import Blueprint, json, jsonify, abort, request
from ..models import Group, db

bp_groups = Blueprint('groups', __name__, url_prefix='/groups')

# test
# @bp_groups.route('', methods=['GET'])
# def test():
#     return jsonify({"msg": "hello rld"})

# READ localhost:5000/groups
@bp_groups.route('', methods=['GET'])
def index():
    groups = Group.query.all()
    result = []
    for a in groups:
        result.append(a.serialize())
    return jsonify(result)

# SHOW localhost:5000/groups/<int:id>
@bp_groups.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Group.query.get_or_404(id)
    return jsonify(a.serialize())

# CREATE localhost:5000/groups/create
@bp_groups.route('/create', methods=['POST'])
def create():
    if ('artist_name' or 'artist_bio') not in request.json:
        return abort(400)
    try:
        a_name = request.json['artist_name']
        a_bio = request.json['artist_bio']
        a = Group(
            artist_name=a_name, artist_bio=a_bio
        )
        a.insert()
        return jsonify(a.serialize())
    except:
        return abort(422)

# UPDATE localhost:5000/groups/<int:id>/update
@bp_groups.route('/<int:id>/update', methods=['PATCH'])
def update(id: int):
    if ('artist_name' or 'artist_bio') not in request.json:
        return abort(400)
    if type(request.json['artist_name'] or request.json['artist_bio']) is not str:
        return abort (400)
    try:
        a_id = Group.query.get_or_404(id)
        a_id.artist_name = request.json['artist_name']
        a_id.artist_bio = request.json['artist_bio']
        a_name = a_id.artist_name
        a_bio = a_id.artist_bio
        a = Group(
            artist_name=a_name, artist_bio=a_bio
        )
        a.update()
        return jsonify(a.serialize())
    except:
        return abort(422)

# DELETE localhost:5000/groups/<int:id>
@bp_groups.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    a_id = Group.query.get_or_404(id)
    try:
        db.session.delete(a_id)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

