import requests
import allure
from urls import Urls

class CourierApi:
    @staticmethod
    @allure.step("Создание курьера: {courier_data}")
    def create_courier(courier_data):
        return requests.post(Urls.CREATE_COURIER, json=courier_data)

    @staticmethod
    @allure.step("Логин курьера: login={login}")
    def login_courier(login, password):
        payload = {"login": login, "password": password}
        return requests.post(Urls.LOGIN_COURIER, json=payload)

    @staticmethod
    @allure.step("Получение ID курьера по логину {login}")
    def get_courier_id(login, password):
        response = CourierApi.login_courier(login, password)
        if response.status_code == 200:
            return response.json().get("id")
        return None

    @staticmethod
    @allure.step("Удаление курьера с ID {courier_id}")
    def delete_courier(courier_id):
        return requests.delete(f"{Urls.DELETE_COURIER}{courier_id}")

class OrderApi:
    @staticmethod
    @allure.step("Создание заказа: {order_data}")
    def create_order(order_data):
        return requests.post(Urls.CREATE_ORDER, json=order_data)

    @staticmethod
    @allure.step("Получение заказа по треку {track_number}")
    def get_order_by_track(track_number):
        return requests.get(f"{Urls.GET_ORDER_BY_TRACK}?t={track_number}")

    @staticmethod
    @allure.step("Получение списка заказов (limit={limit}, page={page})")
    def get_orders_list(limit=None, page=None):
        params = {}
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        return requests.get(Urls.GET_ORDERS_LIST, params=params)

    @staticmethod
    @allure.step("Удаление заказа с треком {track_number}")
    def delete_by_track(track_number):
        try:
            return requests.delete(f"{Urls.DELETE_ORDER}{track_number}")
        except Exception:
            return None
