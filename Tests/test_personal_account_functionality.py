from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from urls import MAIN_PAGE_URL, REGISTER_PAGE_URL, LOGIN_PAGE_URL
from test_data import USER_NAME, VALID_EMAIL, INVALID_PASSWORD, CORRECT_PASSWORD

class TestLoginAndAccountManagement:

    def test_login_page_visible(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert header.is_displayed(), "Заголовок 'Вход' не виден и переход на страницу входа не произведён"

    def test_login_with_valid_credentials(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys(VALID_EMAIL)
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys(CORRECT_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_visible = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_visible.is_displayed(), "Переход на главную страницу не осуществлён"

    def test_switch_to_personal_account(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys(VALID_EMAIL)
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys(CORRECT_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        personal_account_visible = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_IN_PERSONAL_ACCOUNT_PAGE))
        assert personal_account_visible.is_displayed(), "Текст на странице личного кабинета не найден"

    def test_switch_to_constructor(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys(VALID_EMAIL)
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys(CORRECT_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        constructor_visible = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_IN_CONSTRUCTOR_PAGE))
        assert constructor_visible.is_displayed(), "Переход в конструктор не выполнен"

    def test_switch_by_logo(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys(VALID_EMAIL)
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys(CORRECT_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*TestLocators.LOGO).click()
        constructor_visible = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_IN_CONSTRUCTOR_PAGE))
        assert constructor_visible.is_displayed(), "Переход в конструктор не выполнен"

    def test_logout(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys(VALID_EMAIL)
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys(CORRECT_PASSWORD)
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        logout_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.LOGOUT_BUTTON))
        logout_button.click()
        login_visible = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert login_visible.is_displayed(), "Заголовок 'Вход' не виден и переход на страницу входа не произведён"
