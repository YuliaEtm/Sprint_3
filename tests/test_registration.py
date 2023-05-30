from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locator import Locators

login_reg = 'Etm878@ya.ru'
password_reg = '888888'
name = 'Etm'
password_invalid = '88858'


class TestReg:

    def test_registration(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_FORM_NEW).click()
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(login_reg)
        driver.find_element(*Locators.REG_PASS).send_keys(password_reg)
        driver.find_element(*Locators.ENTRY_BUTTON).click()

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(login_reg)
        driver.find_element(*Locators.PASSWORD).send_keys(password_reg)
        driver.implicitly_wait(3)
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        reg_name = driver.find_element(*Locators.NAME_ACCOUNT).get_attribute('value')
        assert reg_name == name

    def test_nonregistration(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(login_reg)
        driver.find_element(*Locators.PASSWORD).send_keys(password_invalid)
        driver.implicitly_wait(3)
        driver.find_element(*Locators.ENTRY_BUTTON).click()

        assert driver.find_element(*Locators.WINDOW_INVALID_PASSWORD).text == 'Некорректный пароль'
