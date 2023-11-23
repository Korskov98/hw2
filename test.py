from Pages import SearchHelper

"""Успешная авторизация"""

def test_auth(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.login("test@protei.ru", "test")
    main_title = main_page.check_main_title()
    assert main_title.is_displayed()
    assert main_title.text == "Добро пожаловать!"


"""Авторизация с пустым паролем"""


def test_auth_empty_pass(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.login("test@protei.ru", "")
    main_title = main_page.check_email_error_title()
    assert main_title.is_displayed()
    assert main_title.text == "Неверный E-Mail или пароль"


"""Авторизация с пустым адресом и паролем"""


def test_auth_empty_email_pass(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.login("", "")
    main_title = main_page.check_empty_email_error_title()
    assert main_title.is_displayed()
    assert main_title.text == "Неверный формат E-Mail"


"""Авторизация с пустым адресом"""


def test_auth_empty_email(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.login("", "test")
    main_title = main_page.check_empty_email_error_title()
    assert main_title.is_displayed()
    assert main_title.text == "Неверный формат E-Mail"