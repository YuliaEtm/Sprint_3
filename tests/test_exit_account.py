from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locator import Locators


class TestExitAccout:

    def test_entry_personal_account(self, login, driver):

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.EXIT_ACCOUNT)).click()

        driver.find_element(*Locators.LOGO).click()

        assert WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')))
