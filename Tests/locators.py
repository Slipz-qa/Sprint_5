from selenium.webdriver.common.by import By

class TestLocators:
    INPUT_FIELD_NAME = By.XPATH, "(//input[@class='text input__textfield text_type_main-default' and @name='name'])[1]" # Поле для ввода имени пользователя на странице регистрации
    INPUT_FIELD_EMAIL = By.XPATH, "(//input[@class='text input__textfield text_type_main-default' and @name='name'])[2]" # Поле для ввода email на странице регистрации
    INPUT_FIELD_PASSWORD = By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль']" # Поле для ввода пароля на странице регистрации
    REGISTRATION_BUTTON = By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]" # Кнопка для регистрации пользователя
    PLACE_AN_ORDER_BUTTON = By.XPATH, "//button[contains(text(), 'Оформить заказ')]" # Кнопка для оформления заказа на главной странице
    LOGIN_TO_ACCOUNT_IN_MAIN_PAGE = By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(text(), 'Войти в аккаунт')]" # Кнопка для входа в аккаунт на главной странице
    HEADER_INPUT = By.XPATH, "//h2[contains(text(), 'Вход')]" # Заголовок страницы входа в аккаунт
    INPUT_FIELD_EMAIL_IN_LOGIN_PAGE = By.XPATH, "//input[@name='name']" # Поле для ввода email на странице входа
    INPUT_FIELD_PASSWORD_IN_LOGIN_PAGE = By.XPATH, "//input[@name='Пароль']"  # Поле для ввода пароля на странице входа
    LOGIN_BUTTON_IN_LOGIN_PAGE = By.XPATH, "//button[contains(text(), 'Войти')]" # Кнопка для подтверждения входа на странице входа
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//a[normalize-space()='Личный Кабинет']" # Кнопка для перехода в личный кабинет на главной странице
    LOGIN_BUTTON_IN_REGISTRATION_PAGE = By.XPATH, "//a[contains(text(), 'Войти')]" # Кнопка для перехода на страницу входа из страницы регистрации
    RECOVER_PASSWORD_BUTTON = By.XPATH, "//a[contains(@class, 'Auth_link') and contains(text(), 'Восстановить пароль')]" # Кнопка для восстановления пароля
    HEADER_RECOVER_PASSWORD_PAGE = By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]" # Заголовок страницы восстановления пароля
    LOGIN_BUTTON_IN_RECOVER_PASSWORD_PAGE = By.XPATH, "//a[contains(@class, 'Auth_link')]"  # Кнопка для входа на страницу восстановления пароля
    TEXT_IN_PERSONAL_ACCOUNT_PAGE = By.XPATH, "//p[contains(text(), 'В этом разделе вы можете изменить свои персональные данные')]" # Текст на странице личного кабинета, информирующий пользователя о возможности изменения персональных данных
    HEADER_IN_CONSTRUCTOR_PAGE = By.XPATH, "//h1[contains(text(), 'Соберите бургер')]" # Заголовок страницы конструктора бургеров
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(), 'Конструктор')]" # Кнопка для перехода в конструктор бургеров
    LOGO = By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]" # Логотип приложения
    LOGOUT_BUTTON = By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and normalize-space()='Выход']" # Кнопка выхода из личного кабинета
    SAUCES_SECTION = By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]" # Раздел соусов в конструкторе
    BUN_SECTION = By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]" # Раздел булок в конструкторе
    FILLING_SECTION = By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]" # Раздел начинок в конструкторе
    SPICY_X_SAUCE = By.XPATH, "//p[contains(@class, 'BurgerIngredient_ingredient__text__yp3dH') and text()='Соус Spicy-X']" # Название соуса Spicy-X в разделе соусов
    FILLING_NAME = By.XPATH, "//p[contains(@class, 'BurgerIngredient_ingredient__text__yp3dH') and text()='Говяжий метеорит (отбивная)']"  # Название начинки Говяжий метеорит (отбивная) в разделе начинок
    BUN_NAME = By.XPATH, "//p[contains(@class, 'BurgerIngredient_ingredient__text__yp3dH') and text()='Краторная булка N-200i']" # Название булки Краторная булка N-200i в разделе булок
    ERROR_MASSEGE = By.XPATH, "//p[@class='input__error text_type_main-default' and contains(text(), 'Некорректный пароль')]" # Сообщение о неорректном пароле





