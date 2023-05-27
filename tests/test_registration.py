from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

from tests.lokator import Locators


class TestReg:
    # Проверка успешной регистрации
    def test_registration(self,driver):
        email = 'Etm8786@ya.ru'
        password = '888688'
        name = 'Etm6'
        # нажать на кнопку  личный кабинет
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # переход на форму "Вы новый пользователь - зарегистрироваться"
        driver.find_element(*Locators.REG_FORM_NEW).click()
        # заполняем поля
        driver.find_element(*Locators.REG_NAME).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).send_keys(email)
        driver.find_element(*Locators.REG_PASS).send_keys(password)
        # нажать "зарегистриваться"
        driver.find_element(*Locators.ENTRY_BUTTON).click()

        #Проверка
        #Войдем как зарегистр пользователь
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(
             email)
        driver.find_element(*Locators.PASSWORD).send_keys(
             password)
        driver.implicitly_wait(3)
        driver.find_element(*Locators.ENTRY_BUTTON).click()

        #Перейдем в личный кабинет, проверяем имя.
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        reg_name = driver.find_element(*Locators.NAME_ACCOUNT).get_attribute('value')
        assert reg_name == name

    def test_nonregistration(self, driver):
        email = 'Etm8785@ya.ru'
        password_invalid = '88858'
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password_invalid)
        driver.implicitly_wait(3)
        driver.find_element(*Locators.ENTRY_BUTTON).click()

        assert driver.find_element(By.XPATH,"//p[contains(text(),'Некорректный пароль')]").text == 'Некорректный пароль'

