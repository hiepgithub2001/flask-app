from flask import Blueprint, jsonify, request, abort, session
from models import db, User
from schema import UserSchema
from flask_bcrypt import Bcrypt


app = Blueprint('user_api', __name__)
bcrypt = Bcrypt()

user_schema = UserSchema()


@app.route('/register', methods=['POST'])
def register_user():
    email = request.json['email']
    password = request.json['password']

    user_exist = User.query.filter(User.email == email).first() is not None

    if user_exist:
        abort(409, "The email has been already registered!")

    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.dump(new_user)


@app.route('/login', methods=['POST'])
def login_user():
    email = request.json['email']
    password = request.json['password']

    user = User.query.filter(User.email == email).first()

    if not user:
        return jsonify({"error": "The user does not exist!"}), 401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Password is not correct!"}), 401

    session['user_id'] = user.id
    print(f'set session: {session.get("user_id")}')

    return jsonify({
        "status": "login successfully!"
    })


@app.route('/@me', methods=['GET'])
def get_current_user():
    user_id = session.get('user_id')
    print(f'user_id={user_id}')

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    user = User.query.filter(User.id == user_id).first()

    return user_schema.dump(user)


@app.route('/logout', methods=['POST'])
def logout_user():
    session.pop('user_id', None)

    return jsonify({
        "status": "logout successfully!"
    })
