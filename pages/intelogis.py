#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'http://u920152e.beget.tech/#'

        super().__init__(web_driver, url)

    # поле ввода "email"
    email = WebElement(xpath='//input[@name="auth_email"]')
    # поле ввода "пароль"
    password = WebElement(xpath='//input[@name="auth_pass"]')
    # кнопка "Войти"
    login_button = WebElement(class_name='form_auth_button')
    # форма "Сколько вам лет"
    form = WebElement(xpath='//form[@class="form_auth_style"]/p')







