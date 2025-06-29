import pytest
import allure
from api.courier_api import CourierApi
from data import ResponseBody


@allure.epic("Курьер")
@allure.feature("Логин курьера")
class TestCourierLogin:

    @allure.title("Курьер может залогиниться с валидными данными")
    def test_login_courier_successfully(self, created_courier):
        courier_api, payload = created_courier

        with allure.step("Отправка запроса на логин"):
            response = courier_api.login_courier({
                "login": payload["login"],
                "password": payload["password"]
            })

        with allure.step("Проверка успешного логина"):
            assert response.status_code == ResponseBody.COURIER_LOGIN_SUCCESS["status_code"]
            assert "id" in response.json()

    @allure.title("Нельзя войти с неверными логином или паролем")
    def test_login_invalid_credentials(self, created_courier):
        courier_api, payload = created_courier

        with allure.step("Попытка логина с неправильным паролем"):
            wrong_payload = {
                "login": payload["login"],
                "password": "wrong_password"
            }
            response = courier_api.login_courier(wrong_payload)

        with allure.step("Проверка кода ошибки и сообщения"):
            assert response.status_code == ResponseBody.COURIER_ACCOUNT_NOT_FOUND["status_code"]
            assert response.json()["message"] == ResponseBody.COURIER_ACCOUNT_NOT_FOUND["message"]

    @allure.title("Нельзя войти без логина или пароля")
    @pytest.mark.parametrize("payload", [
        {"password": "somepassword"},     # отсутствует login
        {"login": "somelogin"},           # отсутствует password
        {}                                # оба поля отсутствуют
    ])
    @pytest.mark.xfail(reason="API не обрабатывает отсутствие обязательных полей корректно (возвращает 504)")
    def test_login_missing_required_fields(self, payload):
        courier_api = CourierApi()

        with allure.step("Отправка запроса логина без обязательных полей"):
            response = courier_api.login_courier(payload)

        with allure.step("Проверка кода и сообщения об ошибке"):
            assert response.status_code == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA["status_code"]
            assert response.json()["message"] == ResponseBody.COURIER_LOGIN_NOT_ENOUGH_DATA["message"]
