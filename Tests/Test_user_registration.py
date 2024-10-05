from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators

class TestRegistration:
    def test_registration(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.INPUT_FIELD_NAME).send_keys("Артем")
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL).send_keys("ArtemBochkov14999@yandex.ru")
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD).send_keys("123456")
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()

