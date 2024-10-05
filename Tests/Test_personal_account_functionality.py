from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators
from selenium.webdriver.support import expected_conditions

class TestPersonalAccount:
    def test_switch_to_personal_account(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert header.is_displayed(), "Заголовок 'Вход' не виден и переход на страницу входа не произведен"
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys("ArtemBochkov14999@yandex.ru")
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "переход на главную страницу не осуществлен"
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        text_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_IN_PERSONAL_ACCOUNT_PAGE))
        assert text_element is not None, "Текст на странице личного кабинета не найден"

    def test_switch_to_constructor(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert header.is_displayed(), "Заголовок 'Вход' не виден и переход на страницу входа не произведен"
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys("ArtemBochkov14999@yandex.ru")
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "переход на главную страницу не осуществлен"
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        text_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_IN_PERSONAL_ACCOUNT_PAGE))
        assert text_element is not None, "Текст на странице личного кабинета не найден"
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        constructor_header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_IN_CONSTRUCTOR_PAGE))
        assert constructor_header.is_displayed(), "Переход в конструктор не выполнен"

    def test_switch_by_logo(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert header.is_displayed(), "Заголовок 'Вход' не виден и переход на страницу входа не произведен"
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys("ArtemBochkov14999@yandex.ru")
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "переход на главную страницу не осуществлен"
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        text_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_IN_PERSONAL_ACCOUNT_PAGE))
        assert text_element is not None, "Текст на странице личного кабинета не найден"
        driver.find_element(*TestLocators.LOGO).click()
        constructor_header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_IN_CONSTRUCTOR_PAGE))
        assert constructor_header.is_displayed(), "Переход в конструктор не выполнен"

    def test_logout(self,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert header.is_displayed(), "Заголовок 'Вход' не виден и переход на страницу входа не произведен"
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys("ArtemBochkov14999@yandex.ru")
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "переход на главную страницу не осуществлен"
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        text_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.TEXT_IN_PERSONAL_ACCOUNT_PAGE))
        assert text_element is not None, "Текст на странице личного кабинета не найден"
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()






