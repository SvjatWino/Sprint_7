import requests
from urls import Url

class OrderApi:
    def create_order(self, payload):
        """Создаёт заказ"""
        return requests.post(Url.CREATE_ORDER, json=payload)

    def get_orders(self):
        """Получает список заказов"""
        return requests.get(Url.GET_ORDER_LIST)
