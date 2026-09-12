import pytest
import allure
from api_client import OrderApi

@allure.feature("Заказы")
@allure.story("Списки заказов")
class TestOrdersList:
    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        response = OrderApi.get_orders_list()
        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        content_type = response.headers.get('Content-Type', '')
        assert 'application/json' in content_type, f"Ответ должен быть в формате JSON, получен: {content_type}"
        response_json = response.json()
        assert "orders" in response_json, "В ответе должно быть поле 'orders'"
        assert isinstance(response_json["orders"], list), "Поле 'orders' должно быть списком"
        assert len(response_json["orders"]) > 0, "Список заказов не должен быть пустым для проверки структуры"
        first_order = response_json["orders"][0]
        required_fields = [
            "id", "track", "firstName", "lastName", "address",
            "metroStation", "phone", "rentTime", "deliveryDate", "status"
        ]
        for field in required_fields:
            assert field in first_order, f"Заказ должен содержать поле '{field}'"
        assert isinstance(first_order["id"], int), "ID заказа должен быть числом"
        assert isinstance(first_order["track"], int), "Track номер должен быть числом"
        assert (
            first_order.get("firstName") is None
            or isinstance(first_order["firstName"], str)
        ), "firstName должно быть строкой или отсутствовать (None)"
        assert (
            first_order.get("lastName") is None
            or isinstance(first_order["lastName"], str)
        ), "lastName должно быть строкой или отсутствовать (None)"
        allure.dynamic.description(f"Получено заказов: {len(response_json['orders'])}")

    @allure.title("Пагинация списка заказов с лимитом {limit}")
    @pytest.mark.parametrize("limit", [1, 5, 10, 30])
    def test_orders_list_pagination(self, limit):
        response = OrderApi.get_orders_list(limit=limit)
        assert response.status_code == 200, f"Ожидался код 200 для лимита {limit}"
        response_json = response.json()
        assert "orders" in response_json, "В ответе должно быть поле 'orders'"
        assert isinstance(response_json["orders"], list), "Поле 'orders' должно быть списком"
        assert len(response_json["orders"]) <= limit, f"Количество заказов превышает лимит {limit}"

    @allure.title("Получение списка заказов с лимитом")
    def test_orders_list_with_limit(self):
        response = OrderApi.get_orders_list(limit=5)
        assert response.status_code == 200
        response_json = response.json()
        assert "orders" in response_json
        assert isinstance(response_json["orders"], list)
        assert len(response_json["orders"]) <= 5

    @allure.title("Получение списка заказов с номером страницы")
    def test_orders_list_with_page(self):
        response = OrderApi.get_orders_list(page=1)
        assert response.status_code == 200
        response_json = response.json()
        assert "orders" in response_json
        assert isinstance(response_json["orders"], list)

    @allure.title("Получение списка заказов с комбинированными параметрами")
    def test_orders_list_with_combined_params(self):
        response = OrderApi.get_orders_list(limit=3, page=2)
        assert response.status_code == 200
        response_json = response.json()
        assert "orders" in response_json
        assert isinstance(response_json["orders"], list)
        assert len(response_json["orders"]) <= 3
