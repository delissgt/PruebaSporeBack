user_list = []


def get_last_id():
    if user_list:
        last_user = user_list[-1]
    else:
        return 1
    return last_user.id + 1


class User:

    def __init__(self, email, password, rol):
        self.id = get_last_id()
        self.email = email
        self.password = password
        self.rol = rol

    @property
    def data(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'rol': self.rol
        }
