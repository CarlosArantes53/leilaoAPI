from flask_restful import Resource, reqparse
from models import User, db
from schemas.user_schema import UserSchema
from flask import request

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.query.get_or_404(user_id)
            return user_schema.dump(user)
        else:
            users = User.query.all()
            return users_schema.dump(users)

    def post(self):
        data = request.get_json()
        user = user_schema.load(data)
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)
