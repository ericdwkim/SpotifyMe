from flask import Blueprint, json, jsonify, abort, request
from ..models import Account, db
import hashlib
import secrets

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp_accounts = Blueprint('accounts', __name__, url_prefix='/accounts')

# test localhost:5000/accounts
# @bp_accounts.route('', methods=['GET'])
# def test():
#     return jsonify({"msg": "hello rld"})

# READ localhost:5000/accounts
@bp_accounts.route('', methods=['GET'])
def index():
    accounts = Account.query.all()
    result = []
    for a in accounts:
        result.append(a.serialize()) 
    return jsonify(result)

# SHOW localhost:5000/accounts/<int:id>
@bp_accounts.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Account.query.get_or_404(id)
    return jsonify(a.serialize())

# CREATE localhost:5000/accounts/create
@bp_accounts.route('/create', methods=['POST'])
def create():
    if 'username' not in request.json or 'user_email' not in request.json:
        return abort(400)
    try:
        a_username = request.json['username']
        a_useremail = request.json['user_email']
        a_userpassword = scramble(request.json['user_password'])

        # construct Account
        a = Account(
            username=a_username, user_email=a_useremail, user_password=a_userpassword
        )
        a.insert()
        return jsonify(a.serialize())
    except:
        return abort(422)

# # UPDATE localhost:5000/artists/<int:id>/update
# @bp_accounts.route('/<int:id>/update', methods=['PATCH'])
# def update(id: int):
#     # ensure payload params exist
#     if 'artist_name' not in request.json or 'artist_bio' not in request.json:
#         return abort(400)
#     # ensure payload params are strings
#     if type(request.json['artist_name'] or request.json['artist_bio']) is not str:
#         return abort (400)
#     try:
#         a_id = Artist.query.get_or_404(id)
#         a_id.artist_name = request.json['artist_name']
#         a_id.artist_bio = request.json['artist_bio']
#         a_name = a_id.artist_name
#         a_bio = a_id.artist_bio
#         a = Artist(
#             artist_name=a_name, artist_bio=a_bio
#         )
#         a.update()
#         return jsonify(a.serialize())
#     except:
#         return abort(422)

# # DELETE localhost:5000/artists/<int:id>
# @bp_accounts.route('/<int:id>', methods=['DELETE'])
# def delete(id: int):
#     a_id = Artist.query.get_or_404(id)
#     try:
#         db.session.delete(a_id)
#         db.session.commit()
#         return jsonify(True)
#     except:
#         return jsonify(False)

