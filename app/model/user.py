from app.basemodel import db, CURD_MixIn
from marshmallow import validate
from marshmallow_jsonapi import Schema, fields


class User(db.Model, CURD_MixIn):
    id = db.Column(db.Integer, primary_key=True)

    mobile = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    account = db.Column(db.String(250), nullable=False, unique=True)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, mobile, password, account):
        self.mobile = mobile
        self.password = password
        self.account = account

    def __repr__(self):
        return '<User %r>' % self.account


class UserSchema(Schema):
    not_blank = validate.Length(min=1, error='Field cannot be blank')

    id = fields.Integer(dump_only=True)

    mobile = fields.String(validate=not_blank)
    password = fields.String(validate=not_blank)
    account = fields.String(validate=not_blank)

    def get_top_level_links(self, data, many):
        if many:
            self_link = "/user/"
        else:
            self_link = "/user/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'user'
