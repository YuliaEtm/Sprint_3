from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

from tests.lokator import Locators


class TestTransitPers:

    #Переход из личного кабинета в конструктор
    def test_transit_personal_account_constructor(self, login):
        driver = login
        #   вход в личный кабинет
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # переход в конструктор
        driver.find_element(*Locators.CONSTRUCTOR).click()
        #Проверка видимости заголовка
        assert WebDriverWait(driver,3).until(EC.text_to_be_present_in_element((Locators.BUILD),'Соберите бургер'))

    #Переход из личного кабинета на логотип
    def test_transit_personal_account_logo(self, login):
         driver = login
         #  вход в  личный кабинет
         driver.find_element(*Locators.ACCOUNT_BUTTON).click()
         # переход по логотипу
         driver.find_element(*Locators.LOGO).click()
         # Проверка видимости заголовка
         assert WebDriverWait(driver,3).until(EC.text_to_be_present_in_element(Locators.BUILD,'Соберите бургер'))

