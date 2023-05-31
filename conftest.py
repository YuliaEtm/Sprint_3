import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.locator import Locators
from tests.data import Credential

url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL).send_keys(
        Credential.login_reg)
    driver.find_element(*Locators.PASSWORD).send_keys(
        Credential.password_reg)
    driver.find_element(*Locators.ENTRY_BUTTON).click()
