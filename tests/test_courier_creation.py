import allure
from api_client import CourierApi

@allure.feature("Курьеры")
@allure.story("Создание курьера")
class TestCourierCreation:
    @allure.title("Создание курьера возвращает статус 201")
    def test_create_courier_status_201(self, random_courier_data):
        response = CourierApi.create_courier(random_courier_data)
        assert response.status_code == 201

    @allure.title("Создание курьера возвращает 'ok: true'")
    def test_create_courier_returns_ok_true(self, random_courier_data):
        response = CourierApi.create_courier(random_courier_data)
        assert response.json() == {"ok": True}

    @allure.title("Попытка создания дубликата курьера")
    def test_create_duplicate_courier(self, courier):
        payload = {
            "login": courier["login"],
            "password": "any_password",
            "firstName": "Duplicate Name"
        }
        response = CourierApi.create_courier(payload)
        assert response.status_code == 409
        assert response.json() == {
            "code": 409,
            "message": "Этот логин уже используется. Попробуйте другой."
        }

    @allure.title("Создание курьера без логина должно вернуть ошибку 400")
    def test_create_courier_missing_login(self, courier_payload_missing_login):
        response = CourierApi.create_courier(courier_payload_missing_login)
        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }

    @allure.title("Создание курьера без пароля должно вернуть ошибку 400")
    def test_create_courier_missing_password(self, courier_payload_missing_password):
        response = CourierApi.create_courier(courier_payload_missing_password)
        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }

    @allure.title("Успешное создание курьера без firstName")
    def test_create_courier_without_first_name_success(self, courier_payload_without_first_name):
        response = CourierApi.create_courier(courier_payload_without_first_name)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Успешная авторизация курьера без firstName")
    def test_login_courier_without_first_name(self, courier):
        login_response = CourierApi.login_courier(
            courier["login"],
            courier["password"]
        )
        assert login_response.status_code == 200
        assert "id" in login_response.json()

    @allure.title("Успешное создание курьера со всеми полями")
    def test_create_courier_with_all_fields_success(self, random_courier_data):
        response = CourierApi.create_courier(random_courier_data)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Успешная авторизация курьера со всеми полями")
    def test_login_courier_with_all_fields(self, courier):
        login_response = CourierApi.login_courier(
            courier["login"],
            courier["password"]
        )
        assert login_response.status_code == 200
        assert "id" in login_response.json()
