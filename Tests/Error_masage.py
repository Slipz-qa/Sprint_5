from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators

class TestRegistration:
    def test_registration(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.INPUT_FIELD_NAME).send_keys("Артем")
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL).send_keys("ArtemBochkov14999@yandex.ru")
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD).send_keys("11")
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        error_message = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[@class='input__error text_type_main-default' and contains(text(), 'Некорректный пароль')]")))
        assert error_message.is_displayed()
        header_login_page = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert header_login_page.is_displayed(), "Переход на страницу входа не осуществлён после выхода"
