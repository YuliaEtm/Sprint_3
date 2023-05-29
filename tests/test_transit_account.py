from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locator import Locators


class TestTransitPers:

    def test_transit_personal_account_constructor(self, login,driver):

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR).click()

        assert WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((Locators.BUILD), 'Соберите бургер'))

    def test_transit_personal_account_logo(self, login,driver):

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGO).click()

        assert WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element(Locators.BUILD, 'Соберите бургер'))
