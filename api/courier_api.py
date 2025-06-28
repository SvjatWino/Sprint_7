import requests
from urls import Url

class CourierApi:
    def __init__(self):
        self.base_url = Url.BASE_URL

    def create_courier(self, payload, headers=None):
        """Создаёт курьера"""
        return requests.post(self.base_url + Url.CREATE_COURIER, json=payload, headers=headers)

    def login_courier(self, payload, headers=None):
        """Логин курьера"""
        return requests.post(self.base_url + Url.COURIER_LOGIN, json=payload, headers=headers)

    def delete_courier(self, courier_id, headers=None):
        """Удаляет курьера по ID"""
        return requests.delete(self.base_url + Url.COURIER_DELETE + str(courier_id), headers=headers)
