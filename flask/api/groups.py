from flask import Blueprint, json, jsonify, abort, request
from models import Group, db

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
    for g in groups:
        result.append(g.serialize())
    return jsonify(result)

# # SHOW localhost:5000/groups/<int:id>
@bp_groups.route('/<int:id>', methods=['GET'])
def show(id: int):
    g = Group.query.get_or_404(id)
    return jsonify(g.serialize())

# # CREATE localhost:5000/groups/create
@bp_groups.route('/create', methods=['POST'])
def create():
    if ('group_name' or 'group_num_members') not in request.json:
        return abort(400)
    try:
        g_name = request.json['group_name']
        g_num_members = request.json['group_num_members']
        g = Group(
            group_name=g_name, group_num_members=g_num_members
        )
        g.insert()
        return jsonify(g.serialize())
    except:
        return abort(422)

# # UPDATE localhost:5000/groups/<int:id>/update
@bp_groups.route('/<int:id>/update', methods=['PATCH'])
def update(id: int):
    if ('group_name' or 'group_num_members') not in request.json:
        return abort(400)
    # if type(request.json['group_name']) is not str:
    #     return abort (400)
    # if type(request.json['group_num_members']) is not int:
    #     return abort (400)
    try:
        g_id = Group.query.get_or_404(id)
        g_id.group_name = request.json['group_name']
        g_id.group_num_members = request.json['group_num_members']
        g_name = g_id.group_name
        g_num_members = g_id.group_num_members
        g = Group(
            group_name=g_name, group_num_members=g_num_members
        )
        g.update()
        return jsonify(g.serialize())
    except:
        return abort(422)

# # DELETE localhost:5000/groups/<int:id>
@bp_groups.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    g_id = Group.query.get_or_404(id)
    try:
        db.session.delete(g_id)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

