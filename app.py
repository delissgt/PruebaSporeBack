# from flask import Flask, jsonify, request
# from http import HTTPStatus
#
# app = Flask(__name__)
#
# recipes = [
#     {
#         'id': 1,
#         'name': 'Egg Salad',
#         'description': 'This is a lovely egg salad recipe.'
#     },
#     {
#         'id': 2, 'name': 'Tomato Pasta',
#         'description': 'This is a lovely tomato pasta recipe.'
#     }
# ]
#
#
# @app.route('/recipes', methods=['GET'])
# def get_recipes():
#     return jsonify({'data': recipes})
#
#
# @app.route('/recipes/<int:recipe_id>', methods=['GET'])
# def get_recipe(recipe_id):
#     recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
#
#     if recipe:
#         return jsonify(recipe)
#
#     return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
#
#
# @app.route('/recipes', methods=['POST'])
# def create_recipe():
#     data = request.get_json()
#
#     name = data.get('name')
#     description = data.get('description')
#
#     recipe = {
#         'id': len(recipes) + 1,
#         'name': name,
#         'description': description
#     }
#
#     recipes.append(recipe)
#
#     return jsonify(recipe), HTTPStatus.CREATED
#
#
# @app.route('/recipes/<int:recipe_id>', methods=['PUT'])
# def update_recipe(recipe_id):
#     recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
#
#     if not recipe:
#         return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
#
#     data = request.get_json()
#
#     recipe.update(
#         {
#             'name': data.get('name'),
#             'description': data.get('description')
#         }
#     )
#
#     return jsonify(recipe)
#
#
# if __name__ == '__main__':
#     app.run()

from flask import Flask
from flask_restful import Api

from resources.car import CarListResource, CarResource, CarDeleteResource
from resources.user import UserListResource, UserResource, UserResourceLogin, UserDeleteResource

app = Flask(__name__)
api = Api(app)

api.add_resource(CarListResource, '/cars')
api.add_resource(CarResource, '/cars/<int:car_id>')
api.add_resource(CarDeleteResource, '/cars/<int:car_id>/delete')

api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserResourceLogin, '/user/<user_email>')
api.add_resource(UserDeleteResource, '/users/<int:user_id>/delete')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
