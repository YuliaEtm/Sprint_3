import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.locator import Locators

url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(By.XPATH, '//header/nav[1]/a[1]/p').click()
    driver.find_element(By.XPATH, '// form[@class ="Auth_form__3qKeq mb-20"] // input[@ name="name"]').send_keys(
        Locators.LOGIN_REG)
    driver.find_element(By.XPATH, '// form[@class ="Auth_form__3qKeq mb-20"] // input[@ name="Пароль"]').send_keys(
        Locators.PASSWORD_REG)
    driver.find_element(By.XPATH, '//form [@class="Auth_form__3qKeq mb-20"]/button').click()

