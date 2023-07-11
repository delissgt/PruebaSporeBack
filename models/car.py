car_list = []


def get_last_id():
    if car_list:
        last_car = car_list[-1]
    else:
        return 1
    return last_car.id + 1


class Car:

    def __init__(self, license_plate, mark, color, model, location_lat, location_lng, owner):
        self.id = get_last_id()
        self.license_plate = license_plate
        self.mark = mark
        self.color = color
        self.model = model
        self.location_lat = location_lat
        self.location_lng = location_lng
        self.owner = owner

    @property
    def data(self):
        return {
            'id': self.id,
            'license_plate': self.license_plate,
            'mark': self.mark,
            'color': self.color,
            'model': self.model,
            'location_lat': self.location_lat,
            'location_lng': self.location_lng,
            'owner': self.owner
        }

    # @data.setter
    # def data(self, value):
    #     self.id = value.id
    #     self.mark = value.mark

