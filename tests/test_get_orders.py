import pytest
import allure
from api.order_api import OrderApi
from data import Flags

@allure.epic("API Яндекс Самокат")
@allure.feature("Получение списка заказов")
class TestGetOrders:

    @allure.story("Успешное получение заказов")
    @allure.description("Проверяет, что API возвращает список заказов и статус-код 200")
    @allure.tag("positive", "orders")
    def test_get_orders_returns_list(self):
        with allure.step("Отправляем GET-запрос на получение заказов"):
            response = OrderApi().get_orders()

        with allure.step("Проверяем, что статус ответа — 200"):
            assert response.status_code == 200, "Ожидался статус 200"

        with allure.step("Проверяем, что тело ответа содержит ключ 'orders', и он является списком"):
            response_body = response.json()
            assert Flags.SUCCESSFUL_GET_ORDER_LIST in response_body, "Ключ 'orders' отсутствует в ответе"
            assert isinstance(response_body[Flags.SUCCESSFUL_GET_ORDER_LIST], list), "'orders' должен быть списком"
