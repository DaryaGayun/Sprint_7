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
    return {
        "login": generate_random_string(8),
        "password": generate_random_string(12),
    }

def generate_courier_data_missing_login():
    return {
        "password": generate_random_string(12),
        "firstName": generate_random_string(6),
    }

def generate_courier_data_missing_password():
    return {
        "login": generate_random_string(8),
        "firstName": generate_random_string(6),
    }
