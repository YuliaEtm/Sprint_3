from selenium.webdriver.common.by import By


class Locators:
    # личный кабинет кнопка войти
    ACCOUNT_BUTTON = (By.XPATH, '//a [@href="/account"]')
    # Вызов формы рагистрация для нового
    REG_FORM_NEW = (By.XPATH, "//p[@class='undefined text text_type_main-default text_color_inactive mb-4']/a")
    # Поле регистрации имя
    REG_NAME = (By.XPATH, "//label[contains(text(),'Имя')]/parent::div/input")
    # Поле регистрации E-mail
    REG_EMAIL = (By.XPATH, "//label[contains(text(),'Email')]/parent::div/input")
    # Поле регистрации пароль
    REG_PASS = (By.XPATH, "//label[contains(text(),'Пароль')]/parent::div/input")
    # Кнопка зарегистрироваться для нового, войти для существующего
    ENTRY_BUTTON = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']/button")
    # Поле EMAIL для входа зарегистрированного пользователя
    EMAIL = (By.XPATH, '//form[@class="Auth_form__3qKeq mb-20"]//input[@name="name"]')
    # Поле пароль для входа зарегистрированного пользователя
    PASSWORD = (By.XPATH, '//form[@class ="Auth_form__3qKeq mb-20"] // input[@ name="Пароль"]')
    # Поле Имя в личном кабинете
    NAME_ACCOUNT = (
    By.XPATH, '//input [@class="text input__textfield text_type_main-default input__textfield-disabled"]')
    # Кнопка войти ваккаунт на главной
    ENTRY_ACCOUNT = (By.XPATH, '//div[@class="BurgerConstructor_basket__container__2fUl3 mt-10"]/button')
    # кнопка войти из формы регистрации уже зарегистрированы войти и вспомнили пароль войти
    ENTRY_REG_BUTTON = (By.XPATH, '//a[@class="Auth_link__1fOlj" ]')
    # забыли пароль из формы регистации
    FORGOT_PASS = (By.XPATH, '//a[@ href="/forgot-password"]')
    # переход в конструктор
    CONSTRUCTOR = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX"]/p')
    # Заголовок Соберите бургер
    BUILD = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')
    # ЛОГОТИП
    LOGO = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]/a')
    # Кнопка выйти из личного кабинета
    EXIT_ACCOUNT = (By.XPATH, '//button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]')
    # конструктор вкладка соусы(не активная)
    SAUSE = (By.XPATH, '// div[ @ style = "display: flex;"] // span[text() = "Соусы"]')
    # конструктор вкладка соусы(активная)
    SAUSE_ACT = (By.XPATH, '// div[ @ style = "display: flex;"] // span[text() = "Соусы"]/parent::div')
    # конструктор вкладка Начинки (не активная)
    FILLING = (By.XPATH, '//div[@style="display: flex;"]//span[text()="Начинки"]')
    # конструктор вкладка Начинки (активная)
    FILLING_ACT = (By.XPATH, '//div[@style="display: flex;"]//span[text()="Начинки"]/parent::div')
    # конструктор вкладка Булочки (не активная)
    BUN = (By.XPATH, '//div[@style="display: flex;"]//span[text()="Булки"]')
    # конструктор вкладка Булочки (активная)
    BUN_ACT = (By.XPATH, '//div[@style="display: flex;"]//span[text()="Булки"]/parent::div')
    # Всплывающее окно, ошибка регистрации, Некорректный пароль
    WINDOW_INVALID_PASSWORD = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
