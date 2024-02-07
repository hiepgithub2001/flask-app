from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow
from sqlalchemy import and_
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://hiep6:123456@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.app_context().push()

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.Date, default=datetime.datetime.now)

    def __init__(self, title, body):
        self.title = title
        self.body = body


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date')


article_schema = ArticleSchema()
# article_schema = ArticleSchema(many=True)


@app.route('/get', methods=['GET'])
def get_articles():
    records = Articles.query.all()
    articles = [dict(
        id=item.id,
        title=item.title,
        body=item.body,
        date=item.date
    ) for item in records]
    return jsonify(articles)

@app.route('/add', methods=['POST'])
def add_articles():
    title = request.json['title']
    body = request.json['body']

    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()

    return article_schema.dump(articles)


@app.route('/update/<id>', methods=['PUT'])
def update_article(id):
    article = Articles.query.get(id)

    title = request.json['title']
    body = request.json['body']

    article.title = title
    article.body = body

    db.session.commit()
    return article_schema.dump(article)


@app.route('/delete/<id>', methods=['DELETE'])
def delete_article(id):
    article = Articles.query.get(id)

    if not article:
        return jsonify({
            "Status": "The article is not exist!"
        })

    db.session.delete(article)
    db.session.commit()
    return article_schema.dump(article)    


if __name__ == "__main__":
    app.run(debug=True)
