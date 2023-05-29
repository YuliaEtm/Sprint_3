from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locator import Locators


class TestReg:

    def test_registration(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REG_FORM_NEW).click()
        driver.find_element(*Locators.REG_NAME).send_keys(Locators.NAME)
        driver.find_element(*Locators.REG_EMAIL).send_keys(Locators.LOGIN_REG)
        driver.find_element(*Locators.REG_PASS).send_keys(Locators.PASSWORD_REG)
        driver.find_element(*Locators.ENTRY_BUTTON).click()

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Locators.LOGIN_REG)
        driver.find_element(*Locators.PASSWORD).send_keys(Locators.PASSWORD_REG)
        driver.implicitly_wait(3)
        driver.find_element(*Locators.ENTRY_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        reg_name = driver.find_element(*Locators.NAME_ACCOUNT).get_attribute('value')
        assert reg_name == Locators.NAME

    def test_nonregistration(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(Locators.LOGIN_REG)
        driver.find_element(*Locators.PASSWORD).send_keys(Locators.PASSWORD_INVALID)
        driver.implicitly_wait(3)
        driver.find_element(*Locators.ENTRY_BUTTON).click()

        assert driver.find_element(By.XPATH,
                                   "//p[contains(text(),'Некорректный пароль')]").text == 'Некорректный пароль'
