import pytest
from pages.magazin_turist import MainPage, RegPage, CatalogPage

# тест авторизации с корректными данными
def test_authorisation(web_browser):
    page = MainPage(web_browser)
    page.vhod.click()
    page.email.send_keys('grapes-vn@ngs.ru')
    page.password.send_keys('VinTur')
    page.login_button.click()
    assert page.cabinet.find()

# тест авторизации с пустым паролем
def test_authorisation_with_empty_pass(web_browser):
    page = MainPage(web_browser)
    page.vhod.click()
    page.email.send_keys('grapes-vn@ngs.ru')
    page.login_button.click()
    assert page.password_error.get_text() == 'Заполните это поле!'

# тест авторизации с невалидным email
def test_authorisation_with_not_valid_email(web_browser):
    page = MainPage(web_browser)
    page.vhod.click()
    page.email.send_keys('grapes')
    page.login_button.click()
    assert page.login_error.get_text() == 'Неверный формат!'

# тест авторизации с некорректным паролем
def test_authorisation_with_not_correct_password(web_browser):
    page = MainPage(web_browser)
    page.vhod.click()
    page.email.send_keys('grapes-vn@ngs.ru')
    page.password.send_keys('12345678')
    page.login_button.click()
    assert page.login_alert.find()

# тест ссылки "Забыл пароль"
def test_authorisation_forgot_password(web_browser):
    page = MainPage(web_browser)
    page.vhod.click()
    page.forgot_password.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/auth/forgot-password/'

# тест ссылки на главную страницу
def test_main_page_link(web_browser):
    page = MainPage(web_browser)
    page.main_page_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/'

# тест формы обратной связи
def test_callback_form_link(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.callback_link.click()
    assert page.callback_form.find()

# тест ссылки "Договор-оферта"
def test_dogovor_oferta_link(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.dogovor_oferta_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/help/warranty/'

# тест ссылки "Вопрос-ответ"
def test_faq_link(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.faq_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/info/faq/'

# тест ссылки "Наша команда"
def test_staff_link(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    page.staff_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/company/staff/'

# тест ссылки "Наличный и безналичный расчет"
def test_payment_link(web_browser):
    page = MainPage(web_browser)
    page.payment_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/help/payment/'

# тест ссылки "Доставка по всей России"
def test_delivery_link(web_browser):
    page = MainPage(web_browser)
    page.delivery_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/help/delivery/'

# тест ссылки "Гарантия качества всех товаров"
def test_warranty_link(web_browser):
    page = MainPage(web_browser)
    page.warranty_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/help/warranty/'

# тест пункта меню "Каталог"
def test_menu_catalog_link(web_browser):
    page = MainPage(web_browser)
    page.menu_catalog_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/catalog/'

# тест пункта меню "Оплата"
def test_menu_payment_link(web_browser):
    page = MainPage(web_browser)
    page.menu_payment_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/help/payment/'

# тест пункта меню "Доставка"
def test_menu_delivery_link(web_browser):
    page = MainPage(web_browser)
    page.menu_delivery_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/help/delivery/'

# тест пункта меню "Контакты"
def test_menu_contacts_link(web_browser):
    page = MainPage(web_browser)
    page.menu_contacts_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/contacts/'

# тест пункта меню "Статьи"
def test_menu_articles_link(web_browser):
    page = MainPage(web_browser)
    page.menu_articles_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/articles/'

# тест пункта меню "Акции"
def test_menu_sale_link(web_browser):
    page = MainPage(web_browser)
    page.menu_sale_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/sale/'

# тест пункта меню "Услуги"
def test_menu_services_link(web_browser):
    page = MainPage(web_browser)
    page.menu_services_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/services/'

# тест пункта меню "Прокат"
def test_menu_prokat_link(web_browser):
    page = MainPage(web_browser)
    page.menu_prokat_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/prokat/'

# тест пункта меню "Товары со скидкой"
def test_menu_aktsii_link(web_browser):
    page = MainPage(web_browser)
    page.menu_aktsii_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/news/aktsii/'

# тест ссылки "Дисконт"
def test_diskont_link(web_browser):
    page = MainPage(web_browser)
    page.diskont_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/sale/diskontnaya-programma/'

# тест ссылки "Бренды"
def test_brands_link(web_browser):
    page = MainPage(web_browser)
    page.brands_link.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://magazin-turist.ru/info/brands/'

# тест вкладки "Акция"
def test_items_po_aktsii(web_browser):
    page = MainPage(web_browser)
    page.scroll_down(offset=1000)
    page.tab_stock.click()
    assert page.catalog_item_stock.count() == page.sticker_stock.count()

# тест вкладки "Новинка"
def test_items_new(web_browser):
    page = MainPage(web_browser)
    page.scroll_down(offset=1000)
    page.tab_new.click()
    assert page.catalog_item_new.count() == page.sticker_new.count()

# тест вкладки "Хит"
def test_items_hit(web_browser):
    page = MainPage(web_browser)
    page.scroll_down(offset=1000)
    page.tab_new.click()
    assert page.catalog_item_hit.count() == page.sticker_hit.count()

# тест вкладки "Советуем"
def test_items_recommend(web_browser):
    page = MainPage(web_browser)
    page.scroll_down(offset=1000)
    page.tab_recommend.click()
    assert page.catalog_item_recommend.count() == page.sticker_recommend.count()

# тест поиска
@pytest.mark.parametrize("key", ['рюкзак', 'h.rpfr'], ids=["correct_input", "wrong_input"])
def test_search(web_browser, key):
    page = MainPage(web_browser)
    page.search.send_keys(key)
    text = page.item_text.get_text()
    for i in range(len(text)):
        assert text[i] == 'Рюкзак'

# тест кнопки "scroll-to-top"
def test_scroll_to_top(web_browser):
    page = MainPage(web_browser)
    page.scroll_down()
    assert page.scroll_to_top.get_attribute('class') == 'scroll-to-top RECT_COLOR TOUCH visible'

# тест регистрации с пустыми полями
def test_registration_with_empty_fields(web_browser):
    page = RegPage(web_browser)
    page.scroll_down(200)
    page.register_button.click()
    assert page.name_error.get_text() == 'Заполните это поле!'
    assert page.email_error.get_text() == 'Заполните это поле!'
    assert page.password_error.get_text() == 'Заполните это поле!'
    assert page.confirm_password_error.get_text() == 'Заполните это поле!'
    assert page.phone_error.get_text() == 'Заполните это поле!'
    assert page.licenses_register_error.get_text() == 'Согласитесь с условиями!'

# тест регистрации с невалидным email
def test_registration_with_not_valid_email(web_browser):
    page = RegPage(web_browser)
    page.scroll_down(200)
    page.email.send_keys('grapes')
    page.register_button.click()
    assert page.email_error.get_text() == 'Неверный формат!'

# тест регистрации с невалидным номером телефона
def test_registration_with_not_valid_phone(web_browser):
    page = RegPage(web_browser)
    page.scroll_down(200)
    page.phone.send_keys('777')
    page.register_button.click()
    assert page.phone_error.get_text() == 'Неверный формат!'

# тест регистрации с невалидным паролем
def test_registration_with_not_valid_password(web_browser):
    page = RegPage(web_browser)
    page.scroll_down(200)
    page.password.send_keys('777')
    page.register_button.click()
    assert page.password_error.get_text() == 'Минимум 6 символов!'

# тест регистрации с ошибочным поддтверждением пароля
def test_registration_with_error_confirm_password(web_browser):
    page = RegPage(web_browser)
    page.scroll_down(200)
    page.password.send_keys('1234567')
    page.confirm_password.send_keys('12345678')
    page.register_button.click()
    assert page.confirm_password_error.get_text() == 'Пароли не совпадают! Попробуйте еще раз'

# тест регистрации с введенными пробелами
def test_registration_with_space_name(web_browser):
    page = RegPage(web_browser)
    page.scroll_down(200)
    page.name.send_keys('       ')
    page.register_button.click()
    assert page.name_error.get_text() == 'Заполните это поле!'

# тест кнопки "Отложить"
def test_wish_count(web_browser):
    page = CatalogPage(web_browser)
    page.sect_kompas.click()
    page.catalog_item[0].click()
    page.wait_page_loaded()
    page.wish_item.click()
    assert page.wish_count.get_text() == '1'

# тест кнопки "Сравнить"
def test_compare_count(web_browser):
    page = CatalogPage(web_browser)
    page.sect_kompas.click()
    page.catalog_item[0].click()
    page.wait_page_loaded()
    page.compare_item.click()
    page.refresh()
    assert page.compare_count.get_text() == '1'

# тест кнопки "Поделиться"
def test_share_block(web_browser):
    page = CatalogPage(web_browser)
    page.sect_kompas.click()
    page.catalog_item[0].click()
    page.wait_page_loaded()
    page.share.click()
    assert page.share_block.is_visible()

# тест кнопки "В корзину"
def test_basket_count(web_browser):
    page = CatalogPage(web_browser)
    page.sect_kompas.click()
    page.catalog_item[0].click()
    page.wait_page_loaded()
    page.basket_item.click()
    assert page.basket_count.get_text() == '1'

# тест формы "Оставить отзыв"
def test_review_form(web_browser):
    page = CatalogPage(web_browser)
    page.sect_kompas.click()
    page.catalog_item[0].click()
    page.wait_page_loaded()
    page.review_tab.click()
    page.review.click()
    assert page.review_form.is_visible()

# тест фильтра "В наличии"
def test_in_stock(web_browser):
    page = CatalogPage(web_browser)
    page.sect_kompas.click()
    page.in_stock.click()
    page.wait_page_loaded()
    assert int(page.in_stock_count.get_text()) == page.catalog_item.count()

# тест сортировки "По цене"
def test_sort_by_price(web_browser):
    page = CatalogPage(web_browser)
    page.sect_koster.click()
    page.in_stock.click()
    page.wait_page_loaded()
    page.sort_price.click()
    page.wait_page_loaded()
    list_price = [int(price) for price in page.catalog_item_price.get_attribute('data-value')]
    list_price_sort = sorted(list_price, reverse=True)
    assert list_price == list_price_sort

# тест фильтра "Цена"
def test_filter_price(web_browser, min='100', max='500'):
    page = CatalogPage(web_browser)
    page.sect_koster.click()
    page.wait_page_loaded()
    page.filter_price.click()
    page.filter_price_min.wait_to_be_clickable()
    page.filter_price_min.send_keys(min)
    page.filter_price_max.send_keys(max)
    page.filter_price_result.click()
    page.wait_page_loaded()
    list_price = [int(price) for price in page.catalog_item_price.get_attribute('data-value')]
    for price in list_price:
        assert int(min) <= price <= int(max)


# тест счетчика позиций в фильтре "Бренд"
def test_filter_brand_count(web_browser):
    page = CatalogPage(web_browser)
    page.sect_koster.click()
    page.wait_page_loaded()
    page.filter_brand.click()
    page.filter_brand_points.wait_to_be_clickable()
    list_of_points = page.filter_brand_points.find()
    for i in range(len(list_of_points)):
        page.filter_brand_points[i].click()
    count= page.filter_brand_count.get_text().split(' ')
    assert int(count[1]) == page.filter_brand_points.count()

# тест фильтра "Бренд"
def test_filter_brand_count_items(web_browser):
    page = CatalogPage(web_browser)
    page.sect_koster.click()
    page.wait_page_loaded()
    page.filter_brand.click()
    page.filter_brand_points.wait_to_be_clickable()
    page.filter_brand_points[0].click()
    count_items = page.filter_brand_count_items.get_text().split(' ')
    count_items = int(count_items[1])
    page.filter_brand_result.click()
    page.wait_page_loaded()
    assert count_items == page.catalog_item.count()

# тест кнопки "Очистить фильтр"
def test_del_filter(web_browser):
    page = CatalogPage(web_browser)
    page.sect_koster.click()
    page.wait_page_loaded()
    count = page.catalog_item.count()
    page.filter_brand.click()
    page.filter_brand_points.wait_to_be_clickable()
    page.filter_brand_points[0].click()
    page.filter_brand_result.click()
    page.wait_page_loaded()
    assert count != page.catalog_item.count()
    page.del_filter.click()
    page.wait_page_loaded()
    assert count == page.catalog_item.count()

# тест представления предметов в виде списка
@pytest.mark.xfail
def test_vid_list(web_browser):
    page = CatalogPage(web_browser)
    page.sect_kompas.click()
    page.wait_page_loaded()
    page.vid_list.click()
    page.wait_page_loaded()
    assert page.vid.get_attribute('data-code') == 'list'

# тест представления предметов в виде таблицы
@pytest.mark.xfail
def test_vid_table(web_browser):
    page = CatalogPage(web_browser)
    page.sect_kompas.click()
    page.wait_page_loaded()
    page.vid_table.click()
    page.wait_page_loaded()
    assert page.vid.get_attribute('data-code') == 'table'
