#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://magazin-turist.ru/'

        super().__init__(web_driver, url)
    # кнопка "Вход"
    vhod = WebElement(xpath='//span[contains(text(), "Вход")]')
    # поле ввода "email"
    email = WebElement(id='USER_LOGIN_POPUP')
    # поле ввода "пароль"
    password = WebElement(id='USER_PASSWORD_POPUP')
    # кнопка "Войти"
    login_button = WebElement(xpath='//button[@name="Login"]')
    # "Личный кабинет"
    cabinet = WebElement(xpath='//span[contains(text(), "Личный кабинет")]')
    # PASSWORD_POPUP-error
    password_error = WebElement(id='USER_PASSWORD_POPUP-error')
    # LOGIN_POPUP-error
    login_error = WebElement(id='USER_LOGIN_POPUP-error')
    # LOGIN_alert
    login_alert = WebElement(xpath='//div[@class="alert alert-danger"]')
    # ссылка "Забыли пароль?"
    forgot_password = WebElement(class_name='forgot')
    # ссылка на главную страницу
    main_page_link = WebElement(xpath='//img[@title="Магазин Турист"]')
    # ссылка "Заказать звонок"
    callback_link = WebElement(class_name='callback_btn')
    # форма "Заказать звонок"
    callback_form = WebElement(xpath='//div[@class="form CALLBACK"]')
    # ссылка "Договор-оферта"
    dogovor_oferta_link = WebElement(xpath='//a[contains(text(), "Договор-оферта")]')
    # ссылка "Вопрос-ответ"
    faq_link = WebElement(xpath='//a[contains(text(), "Вопрос-ответ")]')
    # ссылка "Наша команда"
    staff_link = WebElement(xpath='//a[contains(text(), "Наша команда")]')
    # ссылка "Наличный и безналичный расчет"
    payment_link = WebElement(xpath='//img[@title="Наличный и безналичный расчет"]')
    # ссылка "Доставка по всей России"
    delivery_link = WebElement(xpath='//img[@title="Доставка по всей России"]')
    # ссылка "Гарантия качества всех товаров"
    warranty_link = WebElement(xpath='//img[@title="Гарантия качества всех товаров"]')
    # ссылка меню "Каталог"
    menu_catalog_link = WebElement(xpath='//span[contains(text(), "Каталог")]')
    # ссылка меню "Оплата"
    menu_payment_link = WebElement(xpath='//span[contains(text(), "Оплата")]')
    # ссылка меню "Доставка"
    menu_delivery_link = WebElement(xpath='//span[contains(text(), "Доставка")]')
    # ссылка меню "Контакты"
    menu_contacts_link = WebElement(xpath='//span[contains(text(), "Контакты")]')
    # ссылка меню "Статьи"
    menu_articles_link = WebElement(xpath='//span[contains(text(), "Статьи")]')
    # ссылка меню "Акции"
    menu_sale_link = WebElement(xpath='//span[contains(text(), "Акции")]')
    # ссылка меню "Услуги"
    menu_services_link = WebElement(xpath='//span[contains(text(), "Услуги")]')
    # ссылка меню "Прокат"
    menu_prokat_link = WebElement(xpath='//span[contains(text(), "Прокат")]')
    # ссылка меню "Товары со скидкой"
    menu_aktsii_link = WebElement(xpath='//span[contains(text(), "Товары со скидкой")]')
    # ссылка "Дисконт"
    diskont_link = WebElement(xpath='//span[contains(text(), "Дисконт")]')
    # ссылка "Бренды"
    brands_link = WebElement(xpath='//span[contains(text(), "Бренды")]')
    # вкладка "Акция"
    tab_stock = WebElement(xpath='//span[contains(text(), "Акция")]')
    # вкладка "Новинка"
    tab_new = WebElement(xpath='//span[contains(text(), "Новинка")]')
    # вкладка "Хит"
    tab_hit = WebElement(xpath='//span[contains(text(), "Хит")]')
    # вкладка "Советуем"
    tab_recommend = WebElement(xpath='//span[contains(text(), "Советуем")]')
    # список товаров "Акция"
    catalog_item_stock = ManyWebElements(xpath='//li[@data-code="STOCK"]//li[@class="catalog_item"]')
    # стикер "Акция"
    sticker_stock = ManyWebElements(xpath='//li[@data-code="STOCK"]//div[@class="sticker_stock"]')
    # список товаров "Новинка"
    catalog_item_new = ManyWebElements(xpath='//li[@data-code="NEW"]//li[@class="catalog_item"]')
    # стикер "Новинка"
    sticker_new = ManyWebElements(xpath='//li[@data-code="NEW"]//div[@class="sticker_new"]')
    # список товаров "Хит"
    catalog_item_hit = ManyWebElements(xpath='//li[@data-code="HIT"]//li[@class="catalog_item"]')
    # стикер "Хит"
    sticker_hit = ManyWebElements(xpath='//li[@data-code="HIT"]//div[@class="sticker_hit"]')
    # список товаров "Советуем"
    catalog_item_recommend = ManyWebElements(xpath='//li[@data-code="RECOMMEND"]//li[@class="catalog_item"]')
    # стикер "Советуем"
    sticker_recommend = ManyWebElements(xpath='//li[@data-code="RECOMMEND"]//div[@class="sticker_recommend"]')
    # Поле ввода поиска
    search = WebElement(id='title-search-input2')
    # название товаров в поле ввода поиска
    item_text = ManyWebElements(xpath='//div[@class="title-search-result title-search-input2 undefined_type"]//b')
    # кнопка "scrollToTop"
    scroll_to_top = WebElement(id='scrollToTop')

class RegPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://magazin-turist.ru/auth/registration/'

        super().__init__(web_driver, url)
    # поле ввода "ФИО"
    name = WebElement(id='input_NAME')
    name_error = WebElement(id='input_NAME-error')
    # поле ввода "email"
    email = WebElement(id='input_EMAIL')
    email_error = WebElement(id='input_EMAIL-error')
    # поле ввода "Пароль"
    password = WebElement(id='input_PASSWORD')
    password_error = WebElement(id='input_PASSWORD-error')
    # поле ввода "Подтверждение пароля"
    confirm_password = WebElement(id='input_CONFIRM_PASSWORD')
    confirm_password_error = WebElement(id='input_CONFIRM_PASSWORD-error')
    # поле ввода "Телефон"
    phone = WebElement(id='input_PERSONAL_PHONE')
    phone_error = WebElement(id='input_PERSONAL_PHONE-error')
    # popup-error "Я согласен на обработку персональных данных"
    licenses_register_error = WebElement(id='licenses_register-error')
    # кнопка "Зарегистрироваться"
    register_button = WebElement(xpath='//button[@name="register_submit_button1"]')

class CatalogPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://magazin-turist.ru/catalog/'

        super().__init__(web_driver, url)
    # ссылка раздела "Компасы"
    sect_kompas = WebElement(xpath='//li[@class="sect"]/a[@href="/catalog/prochee/kompasy/"]')
    # ссылка раздела "Костровое оборудование"
    sect_koster = WebElement(xpath='//li[@class="sect"]/a[@href="/catalog/bivachnoe-snaryazhenie/kostrovoe-oborudovanie/"]')
    # предметы каталога
    catalog_item = ManyWebElements(class_name='catalog_item_wrapp')
    # цены предметов
    catalog_item_price = ManyWebElements(xpath='//div[@class="price"]')
    # кнопка "Отложить"
    wish_item = WebElement(xpath='//span[@title="Отложить"]')
    wish_count = WebElement(xpath='//div[@class="wish_count"]//div[@class="items"]/div')
    # кнопка Сравнить
    compare_item = WebElement(xpath='//span[@title="Сравнить"]')
    compare_count = WebElement(xpath='//div[@id="compare_line"]//span[@class="items"]/span')
    # кнопка Поделиться
    share = WebElement(xpath='//div[@class="text button transparent"]')
    share_block = WebElement(xpath='//div[@class="ya-share2 shares ya-share2_inited"]')
    # кнопка В Корзину
    basket_item = WebElement(xpath='//span[@class="big_btn to-cart button"]')
    # счётчик Корзина
    basket_count = WebElement(xpath='//div[@class="basket_count"]//div[@class="items"]/div')
    # блок ОТЗЫВА
    review_tab = WebElement(id='product_reviews_tab')
    # кнопка ОСТАВИТЬ ОТЗЫВ
    review = WebElement(id='swREPLIERZZtH')
    # форма ОТЗЫВА
    review_form = WebElement(class_name='reviews-reply-form')
    # фильтр "В наличии"
    in_stock = WebElement(xpath='//div[@data-prop_code="in_stock"]')
    in_stock_count = WebElement(xpath='//div[@data-prop_code="in_stock"]//span[@title="В наличии"]/span')
    # кнопка сортировки "По цене"
    sort_price = WebElement(xpath='//span[contains(text(), "По цене")]')
    # кнопка сортировки "По алфавиту"
    sort_abc = WebElement(xpath='//span[contains(text(), "По цене")]')
    # фильтр "Цена"
    filter_price = WebElement(xpath='//div[@class="bx_filter_parameters_box prices"]')
    filter_price_min = WebElement(class_name='min-price')
    filter_price_max = WebElement(class_name='max-price')
    # кнопка "Показать"
    filter_price_result = WebElement(xpath='//span[contains(text(), "Показать")]')
    # фильтр "Бренд"
    filter_brand = WebElement(xpath='//div[@data-prop_code="brand"]')
    # пункты фильтра "Бренд"
    filter_brand_points = ManyWebElements(xpath='//div[@data-prop_code="brand"]//div[@class="filter label_block"]')
    # количество выбранных брендов
    filter_brand_count = WebElement(xpath='//div[@data-prop_code="brand"]//span[contains(text(), ": ")]')
    # количество выбранных предметов
    filter_brand_count_items = WebElement(xpath='//div[@data-prop_code="brand"]//span[contains(text(), "Выбрано: ")]')
    # кнопка "Показать"
    filter_brand_result = WebElement(xpath='//div[@data-prop_code="brand"]//span[contains(text(), "Показать")]')
    # кнопка "Очистить фильтр"
    del_filter = WebElement(id='del_filter')
    # блок представления предметов
    vid = WebElement(class_name='ajax_load')
    # кнопка представления предметов в виде списка
    vid_list = WebElement(xpath='//div[@class="sort_display"]//i[@title="списком"]')
    # кнопка представления предметов в виде таблицы
    vid_table = WebElement(xpath='//div[@class="sort_display"]//i[@title="таблицей"]')






