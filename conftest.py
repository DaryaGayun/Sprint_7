import pytest
from helpers import generate_courier_data
from api_client import CourierApi, OrderApi

@pytest.fixture
def random_courier_data():
    return generate_courier_data()

@pytest.fixture
def courier_payload_without_first_name():
    from helpers import generate_courier_data_without_first_name
    return generate_courier_data_without_first_name()

@pytest.fixture
def courier_payload_missing_login():
    from helpers import generate_courier_data_missing_login
    return generate_courier_data_missing_login()

@pytest.fixture
def courier_payload_missing_password():
    from helpers import generate_courier_data_missing_password
    return generate_courier_data_missing_password()

@pytest.fixture
def courier():
    data = generate_courier_data()
    response = CourierApi.create_courier(data)
    if response.status_code not in (200, 201):
        yield data
        return
    login_resp = CourierApi.login_courier(data["login"], data["password"])
    courier_id = login_resp.json().get("id")
    yield {
        "login": data["login"],
        "password": data["password"],
        "firstName": data["firstName"],
        "id": courier_id,
    }
    if courier_id:
        CourierApi.delete_courier(courier_id)

@pytest.fixture
def cleanup_order():
    tracks = []
    yield tracks
    for track in tracks:
        OrderApi.delete_by_track(track)
