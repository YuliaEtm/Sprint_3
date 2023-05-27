from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.lokator import Locators


class TestPersonalAccount:

# переход в личный кабинет для зарегистрированного пользователя
    def test_personal_account_entry(self, login):
        driver = login
        #   нажать на кнопку личный кабинет
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        reg_name = WebDriverWait(driver,3).until(EC.presence_of_element_located(Locators.NAME_ACCOUNT)).get_attribute('value')

        assert reg_name == 'Etm'
