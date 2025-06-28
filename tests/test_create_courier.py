import pytest
import allure
from api.courier_api import CourierApi
from data import ResponseBody
from data import valid_courier_payload


@allure.epic("Курьер")
@allure.feature("Создание курьера")
@allure.title("Курьера можно создать")
def test_create_courier_successfully():
    courier_api = CourierApi()
    payload = valid_courier_payload()

    with allure.step("Отправка запроса на создание курьера"):
        response = courier_api.create_courier(payload)

    with allure.step("Проверка кода ответа и тела"):
        assert response.status_code == ResponseBody.COURIER_CREATION_SUCCESS["status_code"]
        assert response.json().get("ok") is ResponseBody.COURIER_CREATION_SUCCESS["ok"]

    with allure.step("Удаление тестового курьера"):
        login_resp = courier_api.login_courier({
            "login": payload["login"],
            "password": payload["password"]
        })
        courier_id = login_resp.json()["id"]
        courier_api.delete_courier(courier_id)


@allure.epic("Курьер")
@allure.feature("Создание курьера")
@allure.title("Нельзя создать курьера с уже существующим логином")
def test_create_existing_courier():
    courier_api = CourierApi()
    payload = valid_courier_payload()

    with allure.step("Создание курьера с уникальным логином"):
        response_first = courier_api.create_courier(payload)
        assert response_first.status_code == ResponseBody.COURIER_CREATION_SUCCESS["status_code"]

    with allure.step("Попытка создать курьера с тем же логином"):
        response_second = courier_api.create_courier(payload)
        assert response_second.status_code == ResponseBody.COURIER_NAME_ALREADY_EXIST["status_code"]
        assert response_second.json()["message"] == ResponseBody.COURIER_NAME_ALREADY_EXIST["message"]

    with allure.step("Удаление тестового курьера"):
        login_resp = courier_api.login_courier({
            "login": payload["login"],
            "password": payload["password"]
        })
        courier_id = login_resp.json()["id"]
        courier_api.delete_courier(courier_id)


@allure.epic("Курьер")
@allure.feature("Создание курьера")
@allure.title("Нельзя создать курьера без обязательного поля")
@pytest.mark.parametrize("missing_field", ["login", "password"])
@pytest.mark.xfail(reason="API зависает или неправильно обрабатывает запрос без обязательного поля")
def test_create_courier_missing_required_field(missing_field):
    courier_api = CourierApi()
    payload = valid_courier_payload()

    # Удаляем одно обязательное поле
    payload.pop(missing_field)

    with allure.step(f"Отправка запроса без поля: {missing_field}"):
        response = courier_api.create_courier(payload)

    with allure.step("Проверка, что вернулась ошибка 400 и ожидаемое сообщение"):
        assert response.status_code == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA["status_code"]
        assert response.json()["message"] == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA["message"]


@allure.epic("Курьер")
@allure.feature("Создание курьера")
@allure.title("Нельзя создать курьера без одного из обязательных полей")
@pytest.mark.parametrize("payload", [
    {"login": "user_only_login"},
    {"password": "user_only_password"},
    {"firstName": "only_name"}
])
def test_create_courier_with_missing_required_fields(payload):
    courier_api = CourierApi()

    with allure.step("Попытка создать курьера без обязательных полей"):
        response = courier_api.create_courier(payload)

    with allure.step("Проверка кода ответа и сообщения об ошибке"):
        assert response.status_code == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA["status_code"]
        assert response.json()["message"] == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA["message"]
