import pytest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from helpers import *

@pytest.fixture
def courier():
    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {"login": login, "password": password, "firstName": first_name}
    response = requests.post(Urls.CREATE_COURIER, data=payload)
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)
    login_resp = login_courier(login_pass[0], login_pass[1])
    courier_id = login_resp.json()["id"]
    yield {"login": login_pass[0], "password": login_pass[1], "id": courier_id}
    delete_courier(courier_id)

@pytest.fixture
def random_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }

@pytest.fixture
def courier_payload_missing_login():
    return {
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }

@pytest.fixture
def courier_payload_missing_password():
    return {
        "login": generate_random_string(10),
        "firstName": generate_random_string(10)
    }
@pytest.fixture(autouse=True)
def setup_teardown_orders():
    yield

@pytest.fixture
def cleanup_order():
    tracks = []
    yield tracks
    for track in tracks:
        delete_test_order(track)
