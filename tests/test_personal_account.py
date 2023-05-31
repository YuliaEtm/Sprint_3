from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locator import Locators
from tests.data import Credential


class TestPersonalAccount:

    def test_personal_account_entry(self, login, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        reg_name = WebDriverWait(driver, 3).until(EC.presence_of_element_located(Locators.NAME_ACCOUNT)).get_attribute(
            'value')

        assert reg_name == Credential.name
