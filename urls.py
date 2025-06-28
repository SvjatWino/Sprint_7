class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

    # Курьеры
    CREATE_COURIER = 'api/v1/courier'
    COURIER_LOGIN = 'api/v1/courier/login'
    COURIER_DELETE = 'api/v1/courier/{courier_id}'

    # Заказы
    CREATE_ORDER = 'api/v1/orders'
    GET_ORDER_LIST = 'api/v1/orders'
    CANCEL_ORDER = 'api/v1/orders/cancel?track={track_id}'
    TRACK_ORDER = 'api/v1/orders/track?t={track_id}'
