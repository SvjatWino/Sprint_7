import pytest
import requests
from api.courier_api import CourierApi
from data import DataForOrder, valid_courier_payload
from urls import Url
from generators import login_generator, password_generator, name_generator


@pytest.fixture
def new_courier():
    """Создаёт нового курьера и возвращает данные + ID. После теста удаляет курьера."""
    courier_data = {
        'login': login_generator(),
        'password': str(password_generator()),
        'firstName': name_generator()
    }

    # Создание курьера
    create_url = Url.BASE_URL + Url.CREATE_COURIER
    response = requests.post(create_url, json=courier_data)
    assert response.status_code == 201

    # Логин курьера, чтобы получить ID
    login_url = Url.BASE_URL + Url.COURIER_LOGIN
    login_payload = {
        'login': courier_data['login'],
        'password': courier_data['password']
    }
    login_response = requests.post(login_url, json=login_payload)
    courier_id = login_response.json().get('id')
    assert courier_id is not None

    yield {
        'id': courier_id,
        'login': courier_data['login'],
        'password': courier_data['password'],
        'firstName': courier_data['firstName']
    }

    # Удаление курьера после теста
    delete_url = Url.BASE_URL + Url.COURIER_DELETE.format(courier_id=courier_id)
    requests.delete(delete_url)


@pytest.fixture
def created_courier():
    """Создаёт курьера через CourierApi, возвращает api и payload. После теста удаляет курьера."""
    api = CourierApi()
    payload = valid_courier_payload()
    response = api.create_courier(payload)
    assert response.status_code == 201
    assert response.json().get("ok") is True

    yield api, payload

    # Удаление курьера после теста
    login_resp = api.login_courier({
        "login": payload["login"],
        "password": payload["password"]
    })
    courier_id = login_resp.json().get("id")
    if courier_id:
        api.delete_courier(courier_id)


@pytest.fixture
def order_data():
    """Возвращает данные для создания заказа (без track)"""
    return DataForOrder.order_data


@pytest.fixture(params=DataForOrder.scooter_colors)
def order_with_color(request):
    """Параметризованная фикстура с цветами самоката"""
    order = DataForOrder.order_data.copy()
    order['color'] = request.param
    return order


@pytest.fixture
def created_order(order_with_color):
    """Создаёт заказ, возвращает его track"""
    url = Url.BASE_URL + Url.CREATE_ORDER
    response = requests.post(url, json=order_with_color)
    assert response.status_code == 201
    track = response.json().get('track')
    assert track is not None
    return track
