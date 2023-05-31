from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locator import Locators


class TestConstratrutor:

    def test_constructor_sause(self, login,driver):

        driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.SAUSE)).click()
        assert 'current' in driver.find_element(*Locators.SAUSE_ACT).get_attribute('class'), 'Вкладка не активна'

    def test_constructor_filling(self, login,driver):

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.FILLING)).click()
        assert WebDriverWait(driver, 3).until(
            EC.text_to_be_present_in_element_attribute(Locators.FILLING_ACT, 'class', "current"))

    def test_constructor_bun(self, login,driver):

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.FILLING)).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUN)).click()
        assert WebDriverWait(driver, 3).until(
            EC.text_to_be_present_in_element_attribute(Locators.BUN_ACT, 'class', "current"))
