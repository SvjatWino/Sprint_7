import generators
from generators import login_generator, password_generator, name_generator

class DataForOrder:
    order_data = {
        'firstName': 'Василий',
        'lastName': 'Теркин',
        'address': 'Москва',
        'metroStation': 1,
        'phone': '+79991234567',
        'rentTime': 5,
        'deliveryDate': '2025-08-01',
        'comment': 'Test comment',
    }

    scooter_colors = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []  # без цвета
    ]


class DataForRegistration:
    @staticmethod
    def generate_reg_data():
        return {
            'login': generators.login_generator(),
            'password': generators.password_generator(),
            'firstName': generators.name_generator()
        }


class ResponseBody:
    COURIER_CREATION_SUCCESS = {'status_code': 201, 'ok': True}
    COURIER_NAME_ALREADY_EXIST = {'status_code': 409, "message": "Этот логин уже используется. Попробуйте другой."}
    COURIER_REGISTRATION_NOT_ENOUGH_DATA = {'status_code': 400, "message": "Недостаточно данных для создания учетной записи"}
    COURIER_ACCOUNT_NOT_FOUND = {'status_code': 404, "message": "Учетная запись не найдена"}
    COURIER_LOGIN_NOT_ENOUGH_DATA = {'status_code': 400, "message": "Недостаточно данных для входа"}
    COURIER_LOGIN_SUCCESS = {"status_code": 200}


class Flags:
    SUCCESSFUL_ORDER_CREATION = 'track'
    SUCCESSFUL_GET_ORDER_LIST = 'orders'


def valid_courier_payload():
    return {
        "login": login_generator(),
        "password": password_generator(),
        "firstName": name_generator()
    }
