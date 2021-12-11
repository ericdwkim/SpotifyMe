from flask import Blueprint, json, jsonify, abort, request
from ..models import Group, db

bp_groups = Blueprint('groups', __name__, url_prefix='/groups')

# test
@bp_groups.route('', methods=['GET'])
def test():
    return jsonify({"msg": "hello rld"})

