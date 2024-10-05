from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators
from selenium.webdriver.support import expected_conditions

class TestLogin:
    def test_login_main_page(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert header.is_displayed(), "Заголовок 'Вход' не виден и переход на страницу входа не произведен"
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys("ArtemBochkov14999@yandex.ru")
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "переход на главную страницу не осуществлен"

    def test_login_in_personal_account(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert header.is_displayed(), "Заголовок 'Вход' не виден и переход на страницу входа не произведен"
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys("ArtemBochkov14999@yandex.ru")
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "Переход на главную страницу не осуществлен"

    def test_via_registration_button(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_REGISTRATION_PAGE).click()
        header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert header.is_displayed(), "Заголовок 'Вход' не виден и переход на страницу входа не произведен"
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys("ArtemBochkov14999@yandex.ru")
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "Переход на главную страницу не осуществлен"

    def test_via_reset_password_button(selfs,driver):
        driver.get("https://stellarburgers.nomoreparties.site/login")
        driver.find_element(*TestLocators.RECOVER_PASSWORD_BUTTON).click()
        header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_RECOVER_PASSWORD_PAGE))
        assert header.is_displayed(), "Заголовок 'Восстановления пароля' не виден и переход на страницу входа не произведен"
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_RECOVER_PASSWORD_PAGE).click()
        header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert header.is_displayed(), "Заголовок 'Вход' не виден и переход на страницу входа не произведен"
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys("ArtemBochkov14999@yandex.ru")
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "Переход на главную страницу не осуществлен"


