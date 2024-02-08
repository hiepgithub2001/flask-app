from flask import Flask
from flask_cors import CORS
from models import db
from config import ApplicationConfig
from flask_bcrypt import Bcrypt
from flask_session import Session

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
CORS(app, supports_credentials=True)
bcrypt = Bcrypt(app)
Session(app)

db.init_app(app)

with app.app_context():
    db.create_all()

# Import and register routes from user.py and article.py
from API.user import app as user_app
from API.article import app as article_app


app.register_blueprint(user_app)
app.register_blueprint(article_app)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
