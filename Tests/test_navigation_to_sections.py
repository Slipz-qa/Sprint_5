from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from urls import MAIN_PAGE_URL

class TestNavigationToSections:

    def test_switch_to_sauces(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.SAUCES_SECTION).click()
        sauces_tab = driver.find_element(*TestLocators.SAUCES_SECTION)
        assert 'tab_tab_type_current__2BEPc' in sauces_tab.get_attribute('class'), "Класс для раздела 'Соусы' не добавлен"

    def test_switch_to_buns(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.SAUCES_SECTION).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(TestLocators.BUN_SECTION))
        driver.find_element(*TestLocators.BUN_SECTION).click()
        buns_tab = driver.find_element(*TestLocators.BUN_SECTION)
        assert 'tab_tab_type_current__2BEPc' in buns_tab.get_attribute('class'), "Класс для раздела 'Булки' не добавлен"

    def test_switch_to_fillings(self, driver):
        driver.get(MAIN_PAGE_URL)
        driver.find_element(*TestLocators.FILLING_SECTION).click()
        fillings_tab = driver.find_element(*TestLocators.FILLING_SECTION)
        assert 'tab_tab_type_current__2BEPc' in fillings_tab.get_attribute('class'), "Класс для раздела 'Начинки' не добавлен"


