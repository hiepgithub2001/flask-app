from marshmallow import fields, Schema


class UserSchema(Schema):
    id = fields.String(dump_only=True)
    email = fields.String(required=True)
    password = fields.String(required=True)


class ArticleSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True)
    body = fields.String(required=True)
    date = fields.Date()
