from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.lokator import Locators





class TestConstratrutor:


    def test_constructor_sause(self, login):

        driver = login
        driver.find_element(*Locators.CONSTRUCTOR).click()
        #   переход в соусы
        WebDriverWait(driver,3).until(EC.element_to_be_clickable(Locators.SAUSE)).click()
        # проерка, что вкладка активна
        assert 'current' in driver.find_element(*Locators.SAUSE_ACT).get_attribute('class')

    def test_constructor_filling(self, login):
        driver = login
        #   переход в начинки
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.FILLING)).click()
        # проверка, что вкладка активна
        assert WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute(Locators.FILLING_ACT, 'class', "current"))

    def test_constructor_bun(self, login):
        driver = login
        #  Сначала перейдем в начинки
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.FILLING)).click()
        #  и вернемся переход в булочки
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(Locators.BUN)).click()

        # проверка, что вкладка активна
        assert WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element_attribute(Locators.BUN_ACT, 'class', "current"))