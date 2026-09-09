import requests
import allure
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from helpers import generate_random_string, login_courier
from urls import Urls

@allure.feature("Курьеры")
@allure.story("Создание курьера")
class TestCourierCreation:
    @allure.title("Создание курьера возвращает статус 201")
    def test_create_courier_status_201(self, random_courier_data):
        with allure.step("Отправка POST-запроса на создание курьера"):
            response = requests.post(Urls.CREATE_COURIER, data=random_courier_data)
        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 201

    @allure.title("Создание курьера возвращает 'ok: true'")
    def test_create_courier_returns_ok_true(self, random_courier_data):
        with allure.step("Отправка POST-запроса на создание курьера"):
            response = requests.post(Urls.CREATE_COURIER, data=random_courier_data)
        with allure.step("Проверка тела ответа"):
            assert response.json() == {"ok": True}

    @allure.title("Попытка создания дубликата курьера")
    def test_create_duplicate_courier(self, courier):
        payload = {
            "login": courier["login"],
            "password": "any_password",
            "firstName": "Duplicate Name"
        }
        with allure.step("Отправка запроса на создание курьера с существующим логином"):
            response = requests.post(Urls.CREATE_COURIER, data=payload)
        with allure.step("Проверка кода состояния 409"):
            assert response.status_code == 409
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json() == {
                "code": 409,
                "message": "Этот логин уже используется. Попробуйте другой."
            }

    @allure.title("Создание курьера без логина должно вернуть ошибку 400")
    def test_create_courier_missing_login(self, courier_payload_missing_login):
        with allure.step("Отправка запроса без поля login"):
            response = requests.post(Urls.CREATE_COURIER, data=courier_payload_missing_login)
        with allure.step("Проверка кода состояния 400"):
            assert response.status_code == 400
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json() == {
                "code": 400,
                "message": "Недостаточно данных для создания учетной записи"
            }

    @allure.title("Создание курьера без пароля должно вернуть ошибку 400")
    def test_create_courier_missing_password(self, courier_payload_missing_password):
        with allure.step("Отправка запроса без поля password"):
            response = requests.post(Urls.CREATE_COURIER, data=courier_payload_missing_password)
        with allure.step("Проверка кода состояния 400"):
            assert response.status_code == 400
        with allure.step("Проверка сообщения об ошибке"):
            assert response.json() == {
                "code": 400,
                "message": "Недостаточно данных для создания учетной записи"
            }

    @allure.title("Успешное создание курьера без firstName")
    def test_create_courier_without_first_name_success(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }
        with allure.step("Отправка запроса на создание курьера без firstName"):
            response = requests.post(Urls.CREATE_COURIER, data=payload)
        with allure.step("Проверка успешного статуса 201"):
            assert response.status_code == 201
        with allure.step("Проверка ответа {'ok': True}"):
            assert response.json() == {"ok": True}

    @allure.title("Успешная авторизация курьера без firstName")
    def test_login_courier_without_first_name(self, courier):
        with allure.step("Выполнение авторизации курьера"):
            login_response = login_courier(courier["login"], courier["password"])
        with allure.step("Проверка статуса 200"):
            assert login_response.status_code == 200
        with allure.step("Проверка наличия поля 'id' в ответе"):
            assert "id" in login_response.json()

    @allure.title("Успешное создание курьера со всеми полями")
    def test_create_courier_with_all_fields_success(self, random_courier_data):
        with allure.step("Отправка запроса с полным набором полей"):
            response = requests.post(Urls.CREATE_COURIER, data=random_courier_data)
        with allure.step("Проверка статуса 201"):
            assert response.status_code == 201
        with allure.step("Проверка ответа {'ok': True}"):
            assert response.json() == {"ok": True}

    @allure.title("Успешная авторизация курьера со всеми полями")
    def test_login_courier_with_all_fields(self, courier):
        with allure.step("Выполнение авторизации курьера"):
            login_response = login_courier(courier["login"], courier["password"])
        with allure.step("Проверка статуса 200"):
            assert login_response.status_code == 200
        with allure.step("Проверка наличия поля 'id' в ответе"):
            assert "id" in login_response.json()
