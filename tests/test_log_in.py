from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from tests.lokator import Locators

class TestLogIn:
    #вход по кнопке "Войти в аккаунт" на главной
    def test_log_in_account(self, driver):
        email = 'etm878@ya.ru'
        password = '888888'
        name = 'Etm'
        #нажимаем кнопку войти в аккаунт на главной странице
        driver.find_element(*Locators.ENTRY_ACCOUNT).click()
        # заполняем поля
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.implicitly_wait(3)
        #Нажимаем кнопку войти
        driver.find_element(*Locators.ENTRY_BUTTON).click()

        #  Проверка, что вход удачный
        #  нажать на кнопку личный кабинет, проверить имя пользователя
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        reg_name = driver.find_element(*Locators.NAME_ACCOUNT).get_attribute('value')
        assert reg_name == name

    # вход через личный кабинет
    def test_log_in_personal_account(self, driver):
        email = 'etm878@ya.ru'
        password = '888888'
        name = 'Etm'
        #нажимаем кнопку личный кабинет на главной странице
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # заполняем поля
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.implicitly_wait(3)
        #Нажимаем кнопку войти
        driver.find_element(*Locators.ENTRY_BUTTON).click()

        #  Проверка, что вход удачный
        # нажать на кнопку личный кабинет, проверить имя пользователя
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        reg_name = driver.find_element(*Locators.NAME_ACCOUNT).get_attribute('value')
        assert reg_name == name

# Вход через кнопку в форме регистрации
    def test_log_in_registration_form(self, driver):
        email = 'etm878@ya.ru'
        password = '888888'
        name = 'Etm'
        # нажать на кнопку личный кабинет
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # переход на форму "Вы новый пользователь, зарегистрироваться"
        driver.find_element(*Locators.REG_FORM_NEW).click()
        #нажимаем кнопку войти на странице регистрации "Уже заренистрированы - Войти"
        driver.find_element(*Locators.ENTRY_REG_BUTTON).click()
        # заполняем поля
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.implicitly_wait(3)
        #Нажимаем кнопку войти
        driver.find_element(*Locators.ENTRY_BUTTON).click()

        #  Проверка, что вход удачный
        #  нажать на кнопку личный кабинет, проверить имя пользователя
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        reg_name = driver.find_element(*Locators.NAME_ACCOUNT).get_attribute('value')
        assert reg_name == name

# Вход через форму восстановление пароля
    def test_log_in_password_recov(self, driver):
            email = 'etm878@ya.ru'
            password = '888888'
            name= 'Etm'
            # нажать на кнопку  личный кабинет
            driver.find_element(*Locators.ACCOUNT_BUTTON).click()
            #нажимаем кнопку войти на странице регистрации "забыли пароль - востановить пароль
            driver.find_element(*Locators.FORGOT_PASS).click()
            # нажимаем вспомнили пароль войти
            driver.find_element(*Locators.ENTRY_REG_BUTTON).click()
            # заполняем поля
            driver.find_element(*Locators.EMAIL).send_keys(email)
            driver.find_element(*Locators.PASSWORD).send_keys(password)
            driver.implicitly_wait(3)
            #Нажимаем кнопку войти
            driver.find_element(*Locators.ENTRY_BUTTON).click()

            #  Проверка, что вход удачный
            # нажать на кнопку личный кабинет, проверить имя пользователя
            driver.find_element(*Locators.ACCOUNT_BUTTON).click()

            reg_name = driver.find_element(*Locators.NAME_ACCOUNT).get_attribute('value')
            assert reg_name == name