from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.user import User, user_list


class UserListResource(Resource):

    def get(self):
        #GET ALL USERS
        data = [user.data for user in user_list]

        return {'data': data}, HTTPStatus.OK

    def post(self):
        # CREATES A USER
        data = request.get_json()

        user = User(email=data['email'],
                    password=data['password'],
                    rol=data['rol'])

        user_list.append(user)

        return user.data, HTTPStatus.CREATED


class UserResource(Resource):

    def get(self, user_id):
        print("USER ID LOGIN", user_id)
        user = next((user for user in user_list if user.id == user_id), None)

        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND

        return user.data, HTTPStatus.OK

    def put(self, user_id):
        data = request.get_json()

        user = next((user for user in user_list if user.id == user_id), None)

        if user is None:
            return {'message': 'user not fount'}, HTTPStatus.NOT_FOUND

        user.email = data['email']
        user.password = data['password']
        user.rol = data['rol']

        return user.data, HTTPStatus.OK


class UserResourceLogin(Resource):

    def get(self, user_email):
        user = next((user for user in user_list if user.email == user_email), None)

        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND

        return user.data, HTTPStatus.OK


class UserDeleteResource(Resource):

    def delete(self, user_id):
        user = next((user for user in user_list if user.id == user_id), None)
        # how is returned user
        if user is None:
            return {'message': 'user not fount'}, HTTPStatus.NOT_FOUND

        user_list.remove(user)

        return {}, HTTPStatus.NO_CONTENT
