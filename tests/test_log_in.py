from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locator import Locators

login_reg = 'Etm878@ya.ru'
password_reg = '888888'
name = 'Etm'


class TestLogIn:

    def test_log_in_account(self, driver):
        driver.find_element(*Locators.ENTRY_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL).send_keys(login_reg)
        driver.find_element(*Locators.PASSWORD).send_keys(password_reg)
        driver.implicitly_wait(3)
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        reg_name = driver.find_element(*Locators.NAME_ACCOUNT).get_attribute('value')
        assert reg_name == name

    def test_log_in_personal_account(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(login_reg)
        driver.find_element(*Locators.PASSWORD).send_keys(password_reg)
        driver.implicitly_wait(3)
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        reg_name = driver.find_element(*Locators.NAME_ACCOUNT).get_attribute('value')
        assert reg_name == name

    def test_log_in_registration_form(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_FORM_NEW).click()
        driver.find_element(*Locators.ENTRY_REG_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(login_reg)
        driver.find_element(*Locators.PASSWORD).send_keys(password_reg)
        driver.implicitly_wait(3)
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        reg_name = driver.find_element(*Locators.NAME_ACCOUNT).get_attribute('value')
        assert reg_name == name

    def test_log_in_password_recov(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.FORGOT_PASS).click()
        driver.find_element(*Locators.ENTRY_REG_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(login_reg)
        driver.find_element(*Locators.PASSWORD).send_keys(password_reg)
        driver.implicitly_wait(3)
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        reg_name = driver.find_element(*Locators.NAME_ACCOUNT).get_attribute('value')
        assert reg_name == name
