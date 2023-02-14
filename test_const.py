class Const:
    ROOT_URL = 'https://stellarburgers.nomoreparties.site/'
    PATH_LOGIN = '/login'
    PATH_REG = '/register'
    PATH_FORGOT_PASS = '/forgot-password'
    PATH_ACCOUNT = '/account'
    CLS_BURGER_CONSTRUCTOR_ING_TAB_SELECTED = 'tab_tab_type_current'


class Strings:
    MAIN_PAGE_HEADER = 'Соберите бургер'
    LOGOUT = 'Выход'
    LOGIN = 'Вход'
    MAKE_ORDER = 'Оформить заказ'


class Locators:
    # Главный заголовок
    MAIN_PAGE_MAIN_HEADER = '//h1'

    # Кнопка "Войти в аккаунт" в баскете
    BASKET_LOGIN_BTN = '//section[starts-with(@class, "BurgerConstructor_basket")]//button'

    # Кнопка "Оформить заказ" в баскете
    BASKET_MAKE_ORDER_BTN = '//section[starts-with(@class, "BurgerConstructor_basket")]//button'

    # Контейнер основного компонента в ЛК
    ACCOUNT_PAGE_BODY = '//div[starts-with(@class, "Account_account")]'

    # Страница регистрации
    REG_PAGE_ANCHOR = '//a[@href="/register"]'

    # Форма регистрации
    REG_FORM = '//form'

    #  Поле "Имя" в форме регистрации
    REG_FORM_INPUT_NAME = './/fieldset[1]//input'

    # Поле "Email" в форме регистрации
    REG_FORM_INPUT_EMAIL = './/fieldset[2]//input'

    # Поле "Пароль" в форме регистрации
    REG_FORM_INPUT_PASS = './/fieldset[3]//input'

    # Кнопка "Войти" на странице регистрации
    REG_FORM_SUBMIT_BTN = './button'

    # Страница авторизации через кнопку "Личный кабинет"
    PERSONAL_ACCOUNT_BTN = f'//header//a[@href="{Const.PATH_ACCOUNT}"]'

    # Форма логина
    LOGIN_FORM = '//form'

    # Форма логина
    LOGIN_FORM_HEADER = '//div[starts-with(@class, "Auth_login")]/h2'

    # Поле Email на странице авторизации
    LOGIN_FORM_EMAIL = './/fieldset[1]//input'

    # Поле Пароль на странице авторизации
    LOGIN_FORM_PASS = './/fieldset[2]//input'

    # Кнопка "Войти" на странице авторизации
    LOGIN_FORM_SUBMIT_BTN = './button'

    # Ссылка на восстановление пароля на странице логина
    LOGIN_PAGE_FORGOT_PASS = f'//a[@href="{Const.PATH_FORGOT_PASS}"]'

    # Кнопка "Войти" в форме регистрации
    REG_PAGE_ALREADY_SIGNED_UP = f'//a[@href="{Const.PATH_LOGIN}"]'

    # Кнопка "Войти" в форме восстановления пароля
    FORGOT_PASS_PAGE_LOGIN = f'//a[@href="{Const.PATH_LOGIN}"]'

    # Ссылка "Конструктор" в хидере
    HEADER_CONSTRUCTOR_LINK = '//header//ul/li[1]'

    # Лого
    HEADER_LOGO = '//div[starts-with(@class, "AppHeader_header__logo")]'

    # Тело основного компонента с ингредиентами
    BURGER_CONSTRUCTOR_ING_BODY = '//section[starts-with(@class, "BurgerIngredients_ingredients")]'

    # Таб с названием категории ингредиента
    BURGER_CONSTRUCTOR_ING_TAB = './/div[starts-with(@class, "tab_tab")]'

    # Текущий таб категории ингредиента
    BURGER_CONSTRUCTOR_ING_TAB_SELECTED = f'.//div[starts-with(@class, "{Const.CLS_BURGER_CONSTRUCTOR_ING_TAB_SELECTED}")]'

    # Хидер категории в списке ингредиентов
    BURGER_CONSTRUCTOR_ING_HEADER_BY_TEXT = lambda txt: f'.//h2[contains(text(), "{txt}")]'

    # Кнопка "Выход" в ЛК
    LOGOUT_BTN = '//div[starts-with(@class, "Account_account")]//nav//button'
