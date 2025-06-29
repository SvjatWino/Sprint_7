import allure
import pytest
from api.order_api import OrderApi
from data import DataForOrder, Flags

@allure.epic("Заказ")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Можно создать заказ с разными цветами самоката")
    @pytest.mark.parametrize("colors", DataForOrder.scooter_colors)
    def test_create_order_successfully(self, colors):
        order_api = OrderApi()
        payload = DataForOrder.order_data.copy()
        payload["color"] = colors

        with allure.step(f"Создание заказа с цветами: {colors}"):
            response = order_api.create_order(payload)

        with allure.step("Проверка кода ответа и наличия трека заказа"):
            assert response.status_code == 201
            assert Flags.SUCCESSFUL_ORDER_CREATION in response.json()
