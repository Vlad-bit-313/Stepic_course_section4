import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage


# здесь у нас только тест-кейсы
# pytest -v --tb=line --language=en test_product_page.py
#

@pytest.mark.xfail
@pytest.mark.parametrize('num', ["0", "1", "2", "3", "4", "5", "6",
                                 pytest.param(7, marks=pytest.mark.xfail),
                                 "8", "9"])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'

    button = ProductPage(browser, link)
    button.open()
    button.add_product_in_cart()  # Добавили товар в корзину
    button.solve_quiz_and_get_code()  # вычислили результ
    button.name_book_in_cart()  # проверяем с тем что добавили
    button.price_book_in_cart()  # проверяем цену в корзине и на сайте


# урок 4.3 шаг 6
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link_step_6 = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product = ProductPage(browser, link_step_6)
    product.open()  # открыть страницу товара
    product.add_product_in_cart()  # добавить товар в корзину
    product.sucsess_message_not_in_window()  # Проверяем, что нет сообщения об успехе


def test_guest_cant_see_success_message(browser):
    link_step_6 = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product = ProductPage(browser, link_step_6)
    product.open()  # открыть страницу товара
    product.sucsess_message_not_in_window()  # Проверяем, что нет сообщения об успехе

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link_step_6 = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    product = ProductPage(browser, link_step_6)
    product.open()  # открыть страницу товара
    product.add_product_in_cart()  # добавить товар в корзину
    product.sucsess_message_disappeared()  # Проверяем, что нет сообщения об успехе с помощью

