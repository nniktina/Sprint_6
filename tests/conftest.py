import pytest
import random

@pytest.fixture
def name_fixture():
    return "Имя"

@pytest.fixture
def surname_fixture():
    return "Фамилия"

@pytest.fixture
def address_fixture():
    return "Москва, ул. Ленина, д.50"

@pytest.fixture
def phone_fixture():
    random_number = random.randint(11111111111, 99999999999)
    return random_number

