from flask import Flask, request
from flask_cors import CORS, cross_origin
from models import db
from config import ApplicationConfig
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_socketio import SocketIO, emit


# Create a Flask application
app = Flask(__name__,)
app.config.from_object(ApplicationConfig)
CORS(app, supports_credentials=True)
bcrypt = Bcrypt(app)
Session(app)
socketio = SocketIO(app, cors_allowed_origins="*")

db.init_app(app)
socketio.init_app(app)

with app.app_context():
    db.create_all()

# Import and register routes from user.py and article.py
from API.user import app as user_app
from API.article import app as article_app


@socketio.on('connect')
def connected():
    print('request.sid =', request.sid)
    print('Client is connected !!!')
    emit('connect', {
        'data': f'id: {request.sid} is connected'
    })


@socketio.on('disconnect')
def disconnected():
    print('User disconnected !!!')
    emit(
        'disconnect',
        f'id: {request.sid} has been disconnected',
        broadcast=True
    )


@socketio.on('data')
def handle_message(data):
    print('Data from Frontend:', str(data))
    emit('data', {
        'data': data,
        'id': request.sid
    }, broadcast=True)


app.register_blueprint(user_app)
app.register_blueprint(article_app)

if __name__ == "__main__":
    # app.run(debug=True, port=5000)
    socketio.run(app, debug=True, port=5000)
