from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Locators import TestLocators
from selenium.webdriver.support import expected_conditions

class TestNavigationByConstructor:
    def test_go_to_the_buns_section(selfs,driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*TestLocators.LOGIN_TO_ACCOUNT_IN_MAIN_PAGE).click()
        header = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.HEADER_INPUT))
        assert header.is_displayed(), "Заголовок 'Вход' не виден и переход на страницу входа не произведен"
        driver.find_element(*TestLocators.INPUT_FIELD_EMAIL_IN_LOGIN_PAGE).send_keys("ArtemBochkov14999@yandex.ru")
        driver.find_element(*TestLocators.INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE).send_keys("123456")
        driver.find_element(*TestLocators.LOGIN_BUTTON_IN_LOGIN_PAGE).click()
        main_page_element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert main_page_element.is_displayed(), "переход на главную страницу не осуществлен"
        driver.find_element(*TestLocators.SAUCES_SECTION).click()
        sause_name = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.SPICY_X_SAUCE))
        assert sause_name.is_displayed(), "Название соуса не отображается, переход на раздел соусы не выполнен"
        driver.find_element(*TestLocators.FILLING_SECTION ).click()
        filling_name = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.FILLING_NAME))
        assert filling_name.is_displayed(), "Название начинки не отображается, переход на раздел начинки не выполнен"
        driver.find_element(*TestLocators.BUN_SECTION).click()
        bun_name = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(TestLocators.BUN_NAME))
        assert bun_name.is_displayed(), "Название булки не отображается, переход на раздел начинки не выполнен"



