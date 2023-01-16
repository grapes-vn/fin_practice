import pytest
from pages.intelogis import MainPage

# тест авторизации с корректными данными
def test_authorisation(web_browser):
    page = MainPage(web_browser)
    page.email.send_keys('grapes-vn@mail.ru')
    page.password.send_keys('123')
    page.login_button.click()
    assert page.form.get_text() == 'Сколько Вам лет?'