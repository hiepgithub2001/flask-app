from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, User, Articles
from config import ApplicationConfig
from schema import ArticleSchema


app = Flask(__name__)
app.config.from_object(ApplicationConfig)
CORS(app)

db.init_app(app)

with app.app_context():
    db.create_all()


article_schema = ArticleSchema()

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
