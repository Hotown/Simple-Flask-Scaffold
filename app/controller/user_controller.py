from app.controller import user
from flask import jsonify
import json

from app.model.user import UserSchema, User

user_data = [
    {
        'name': 'Hotown',
        'id': 1
    },
    {
        'name': 'Mark',
        'id': 2
    }
]

schema = UserSchema(strict=True)


@user.route('/<int:user_id>', methods=['GET', ])
def get(user_id):
    # for user in user_data:
    #     if int(user['id'] == id):
    #         return jsonify(status='success', user=user)
    users_query = User.query.filter_by(id=user_id)
    results = schema.dump(users_query, many=True).data
    return jsonify(results)
