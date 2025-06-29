import pytest
import allure
from api.courier_api import CourierApi
from data import ResponseBody
from data import valid_courier_payload


@allure.epic("Курьер")
@allure.feature("Создание курьера")
class TestCourierCreation:

    @allure.title("Курьера можно создать")
    def test_create_courier_successfully(self, created_courier):
        courier_api, payload = created_courier

        with allure.step("Логин созданного курьера"):
            login_resp = courier_api.login_courier({
                "login": payload["login"],
                "password": payload["password"]
            })

        with allure.step("Проверка успешного логина и наличия ID"):
            assert login_resp.status_code == 200
            assert "id" in login_resp.json()

    @allure.title("Нельзя создать курьера с уже существующим логином")
    def test_create_existing_courier(self, created_courier):
        courier_api, payload = created_courier

        with allure.step("Повторная попытка создать того же курьера"):
            second_response = courier_api.create_courier(payload)

        with allure.step("Проверка кода ответа и сообщения"):
            assert second_response.status_code == ResponseBody.COURIER_NAME_ALREADY_EXIST["status_code"]
            assert second_response.json()["message"] == ResponseBody.COURIER_NAME_ALREADY_EXIST["message"]

    @allure.title("Нельзя создать курьера без обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @pytest.mark.xfail(reason="API зависает или неправильно обрабатывает запрос без обязательного поля")
    def test_create_courier_missing_required_field(self, missing_field):
        courier_api = CourierApi()
        payload = valid_courier_payload()

        # Удаляем поле
        payload.pop(missing_field)

        with allure.step(f"Запрос без обязательного поля: {missing_field}"):
            response = courier_api.create_courier(payload)

        with allure.step("Проверка кода ответа и текста ошибки"):
            assert response.status_code == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA["status_code"]
            assert response.json()["message"] == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA["message"]

    @allure.title("Нельзя создать курьера без одного из обязательных полей (параметризация)")
    @pytest.mark.parametrize("payload", [
        {"login": "user_only_login"},
        {"password": "user_only_password"},
        {"firstName": "only_name"}
    ])
    def test_create_courier_with_missing_required_fields(self, payload):
        courier_api = CourierApi()

        with allure.step("Запрос с неполными данными"):
            response = courier_api.create_courier(payload)

        with allure.step("Проверка кода ответа и текста ошибки"):
            assert response.status_code == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA["status_code"]
            assert response.json()["message"] == ResponseBody.COURIER_REGISTRATION_NOT_ENOUGH_DATA["message"]
