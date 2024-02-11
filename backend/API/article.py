from flask import jsonify, request, Blueprint, session
from models import db, Articles
from schema import ArticleSchema


app = Blueprint('article_api', __name__)

article_schema = ArticleSchema()


@app.route('/get', methods=['GET'])
def get_articles():
    records = Articles.query.filter(
        Articles.user_id == session.get('user_id')
    ).all()
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
