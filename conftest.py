import pytest
from helpers import generate_random_string
from api_client import CourierApi, OrderApi

@pytest.fixture
def courier():
    data = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }
    CourierApi.create_courier(data)
    login_resp = CourierApi.login_courier(data["login"], data["password"])
    courier_id = login_resp.json()["id"]
    yield {
        "login": data["login"],
        "password": data["password"],
        "firstName": data["firstName"],
        "id": courier_id,
    }
    CourierApi.delete_courier(courier_id)

@pytest.fixture
def random_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }

@pytest.fixture
def courier_payload_missing_login():
    return {
        "password": generate_random_string(10),
        "firstName": generate_random_string(10),
    }

@pytest.fixture
def courier_payload_missing_password():
    return {
        "login": generate_random_string(10),
        "firstName": generate_random_string(10),
    }

@pytest.fixture
def courier_payload_without_first_name():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
    }

@pytest.fixture(autouse=True)
def setup_teardown_orders():
    yield

@pytest.fixture
def cleanup_order():
    tracks = []
    yield tracks
    for track in tracks:
        OrderApi.delete_by_track(track)
