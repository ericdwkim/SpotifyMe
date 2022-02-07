from flask import Blueprint, json, jsonify, abort, request
from models import Account, db
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
    if ('username' or 'user_email' or 'user_password') not in request.json:
        return abort(400)
    # ensure username > 4 chars & password > 8 char
    # TODO: (feature): password should contain special chars
    if len(request.json['username']) < 4 or len(request.json['user_password']) < 8:
        return jsonify({"msg": "username must be longer than 4 characters and/or password must be longer than 8 characters!"})
    try:
        a_username = request.json['username']
        a_useremail = request.json['user_email']
        a_userpassword = scramble(request.json['user_password'])
        a = Account(
            username=a_username, user_email=a_useremail, user_password=a_userpassword
        )
        a.insert()
        return jsonify(a.serialize())
    except:
        return abort(422)

# # UPDATE localhost:5000/accounts/<int:id>/update
@bp_accounts.route('/<int:id>/update', methods=['PATCH'])
def update(id: int):
    if ('username' or 'user_email' or 'user_password') not in request.json:
        return abort(400)
    if type(request.json['username'] or request.json['user_email'] or request.json['user_password']) is not str:
        return abort (400)
    try:
        a_id = Account.query.get_or_404(id)
        a_id.username = request.json['username']
        a_id.user_email = request.json['user_email']
        a_id.user_password = request.json['user_password']
        a_username = a_id.username
        a_email = a_id.user_email
        a_password = a_id.user_password
        a = Account(
            username=a_username, user_email=a_email, user_password=a_password
        )
        a.update()
        return jsonify(a.serialize())
    except:
        return abort(422)

# # DELETE localhost:5000/accounts/<int:id>
@bp_accounts.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    a_id = Account.query.get_or_404(id)
    try:
        db.session.delete(a_id)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

