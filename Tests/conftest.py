import pytest
from selenium import webdriver
import pytest
import random
import string

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def generate_random_email():
    letters = ''.join(random.choices(string.ascii_letters, k=5))
    digits = random.randint(1000, 9999)
    email = f"{letters}{digits}@yandex.ru"
    password = "123456"
    return email, password
