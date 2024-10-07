from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators
from urls import MAIN_PAGE_URL, REGISTER_PAGE_URL, LOGIN_PAGE_URL
from test_data import VALID_EMAIL, CORRECT_PASSWORD

class TestLogin:

    def test_check_login_page_header(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        header = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert header.is_displayed(), "Заголовок 'Вход' не виден и переход на страницу входа не произведён"

    def test_login_via_main_page(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys(VALID_EMAIL)
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys(CORRECT_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "Переход на главную страницу не осуществлён"

    def test_login_via_personal_account(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys(VALID_EMAIL)
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys(CORRECT_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "Переход на главную страницу не осуществлён"

    def test_login_via_registration_page(self, driver):
        driver.get(REGISTER_PAGE_URL)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_REGISTRATION_PAGE).click()
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys(VALID_EMAIL)
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys(CORRECT_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "Переход на главную страницу не осуществлён"


    def test_login_via_reset_password(self, driver):
        driver.get(LOGIN_PAGE_URL)
        driver.find_element(*TestLocators.RECOVER_PASSWORD_BUTTON).click()
        header = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.HEADER_RECOVER_PASSWORD_PAGE))
        assert header.is_displayed(), "Заголовок 'Восстановления пароля' не виден и переход на страницу восстановления пароля не произведён"

    def test_login_from_recovery_page(self, driver):
        driver.get(LOGIN_PAGE_URL)
        driver.find_element(*TestLocators.RECOVER_PASSWORD_BUTTON).click()
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_RECOVER_PASSWORD_PAGE).click()
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys(VALID_EMAIL)
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys(CORRECT_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "Переход на главную страницу не осуществлён"



