class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

    # Курьеры
    CREATE_COURIER = BASE_URL + "api/v1/courier"
    COURIER_LOGIN = BASE_URL + "api/v1/courier/login"
    COURIER_DELETE = BASE_URL + "api/v1/courier/{courier_id}"

    # Заказы
    CREATE_ORDER = BASE_URL + "api/v1/orders"
    GET_ORDER_LIST = BASE_URL + "api/v1/orders"
    CANCEL_ORDER = BASE_URL + "api/v1/orders/cancel?track={track_id}"
    TRACK_ORDER = BASE_URL + "api/v1/orders/track?t={track_id}"
