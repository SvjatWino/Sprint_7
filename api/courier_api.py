import requests
from urls import Url

class CourierApi:
    def create_courier(self, payload):
        """Создаёт курьера"""
        return requests.post(Url.CREATE_COURIER, json=payload)

    def login_courier(self, payload):
        """Логин курьера"""
        return requests.post(Url.COURIER_LOGIN, json=payload)

    def delete_courier(self, courier_id):
        """Удаляет курьера по ID"""
        return requests.delete(f"{Url.COURIER_DELETE}{courier_id}")
