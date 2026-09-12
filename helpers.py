import random
import string

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_courier_data():
    return {
        "login": generate_random_string(8),
        "password": generate_random_string(12),
        "firstName": generate_random_string(6),
    }

def generate_courier_data_without_first_name():
    data = generate_courier_data()
    del data["firstName"]
    return data

def generate_courier_data_missing_login():
    data = generate_courier_data()
    del data["login"]
    return data

def generate_courier_data_missing_password():
    data = generate_courier_data()
    del data["password"]
    return data
