from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators
from urls import REGISTER_PAGE_URL
from test_data import USER_NAME, VALID_EMAIL, INVALID_PASSWORD, CORRECT_PASSWORD

class TestRegistration:
    def test_registration(self,driver,generate_random_email):
        driver.get(REGISTER_PAGE_URL)
        email,password = generate_random_email
        driver.find_element(*TestLocators.INPUT_FIELD_NAME).send_keys(USER_NAME)
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL).send_keys(email)
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

