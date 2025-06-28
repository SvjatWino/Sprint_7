import requests
from urls import Url

class OrderApi:
    def __init__(self):
        self.base_url = Url.BASE_URL

    def create_order(self, payload, headers=None):
        """Создаёт заказ"""
        return requests.post(self.base_url + Url.CREATE_ORDER, json=payload, headers=headers)

    def get_orders(self, headers=None):
        """Получает список заказов"""
        return requests.get(self.base_url + Url.GET_ORDER_LIST, headers=headers)
