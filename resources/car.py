from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.car import Car, car_list


class CarListResource(Resource):

    def get(self):
        # GET ALL CARS

        data = [car.data for car in car_list]

        # for car in car_list:
        #     # if car.is_publish is True:
        #     #     data.append(car.data)
        #     data.append(car.data)
        return {'data': data}, HTTPStatus.OK

    def post(self):
        # CREATES A CAR
        data = request.get_json()

        car = Car(license_plate=data['license_plate'],
                  mark=data['mark'],
                  color=data['color'],
                  model=data['model'],
                  location_lat=data['location_lat'],
                  location_lng=data['location_lng'],
                  owner=data['owner'],
                  )

        car_list.append(car)

        return car.data, HTTPStatus.CREATED


class CarResource(Resource):

    def get(self, car_id):
        car = next((car for car in car_list if car.id == car_id), None)

        if car is None:
            return {'message': 'car not found'}, HTTPStatus.NOT_FOUND

        return car.data, HTTPStatus.OK

    def put(self, car_id):
        data = request.get_json()

        car = next((car for car in car_list if car.id == car_id), None)

        if car is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        car.license_plate = data['license_plate']
        car.mark = data['mark']
        car.color = data['color']
        car.model = data['model']
        car.location_lat = data['location_lat']
        car.location_lng = data['location_lng']

        return car.data, HTTPStatus.OK


class CarDeleteResource(Resource):

    def delete(self, car_id):
        car = next((car for car in car_list if car.id == car_id), None)

        if car is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        car_list.remove(car)

        return {}, HTTPStatus.NO_CONTENT
