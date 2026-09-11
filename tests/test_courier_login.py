import allure
from api_client import CourierApi

@allure.feature("Курьеры")
@allure.story("Логин курьера")
class TestCourierLogin:
    @allure.title("Успешный логин курьера")
    def test_login_courier_success(self, courier):
        response = CourierApi.login_courier(courier["login"], courier["password"])
        assert response.status_code == 200, "Ожидался успешный логин"
        assert "id" in response.json(), "В ответе должен быть id курьера"
        assert isinstance(response.json()["id"], int), "ID должен быть числом"

    @allure.title("Логин без логина")
    def test_login_missing_login(self):
        response = CourierApi.login_courier("", "anypassword")
        assert response.status_code == 400, f"Ожидалась ошибка 400, получено: {response.status_code}"
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Логин с неверным паролем")
    def test_login_wrong_password(self, courier):
        wrong_password = courier["password"] + "_wrong"
        response = CourierApi.login_courier(courier["login"], wrong_password)
        assert response.status_code == 404, "Ожидалась ошибка 404 при неверном пароле"
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Логин с неверным логином")
    def test_login_wrong_login(self, courier):
        wrong_login = courier["login"] + "_wrong"
        response = CourierApi.login_courier(wrong_login, courier["password"])
        assert response.status_code == 404, "Ожидалась ошибка 404 при неверном логине"
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Логин несуществующего курьера")
    def test_login_nonexistent_courier(self):
        response = CourierApi.login_courier("nonexistent_login", "nonexistent_password")
        assert response.status_code == 404, "Ожидалась ошибка 404 для несуществующего курьера"
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Логин без логина (обязательное поле)")
    def test_login_missing_login_required(self, courier):
        response = CourierApi.login_courier("", courier["password"])
        assert response.status_code == 400, f"Ожидалась ошибка 400 без логина, получено: {response.status_code}"
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Логин без пароля (обязательное поле)")
    def test_login_missing_password_required(self, courier):
        response = CourierApi.login_courier(courier["login"], "")
        assert response.status_code == 400, f"Ожидалась ошибка 400 без пароля, получено: {response.status_code}"
        assert response.json()["message"] == "Недостаточно данных для входа"
