import time
import pytest
from .pages.product_page import ProductPage
from .pages.product_page import LoginPage
from .pages.basket_page import BasketPage

# здесь у нас только тест-кейсы
# pytest -v --tb=line --language=en test_product_page.py
#
link_step_6 = "http://selenium1py.pythonanywhere.com/"


class TestUserAddToBasketFromProductPage:
    """Здесь реализованны подготовительные действия перед тестированием авторизованного пользователя"""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        start_page = LoginPage(browser, link_step_6)
        start_page.open()
        start_page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        start_page.register_new_user(email, password)
        start_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product = ProductPage(browser, link_step_6)
        product.open()  # Открыть страницу товара
        product.sucsess_message_not_in_window()  # Проверяем, что нет сообщения об успехе

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        button = ProductPage(browser, link)
        button.open()
        button.add_product_in_cart()  # Добавили товар в корзину
        button.name_book_in_cart()  # Проверяем с тем что добавили
        button.price_book_in_cart()  # Проверяем цену в корзине и на сайте


@pytest.mark.skip
@pytest.mark.parametrize('num', ["0", "1", "2", "3", "4", "5", "6",
                                 pytest.param(7, marks=pytest.mark.xfail),
                                 "8", "9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    button = ProductPage(browser, link)
    button.open()
    button.add_product_in_cart()  # Добавили товар в корзину
    button.solve_quiz_and_get_code()  # Вычислить результ
    button.name_book_in_cart()  # Проверяем с тем что добавили
    button.price_book_in_cart()  # Проверяем цену в корзине и на сайте


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product = ProductPage(browser, link_step_6)
    product.open()  # Открыть страницу товара
    product.add_product_in_cart()  # Добавить товар в корзину
    product.sucsess_message_not_in_window()  # Проверяем, что нет сообщения об успехе


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    product = ProductPage(browser, link_step_6)
    product.open()  # Открыть страницу товара
    product.sucsess_message_not_in_window()  # Проверяем, что нет сообщения об успехе


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    product = ProductPage(browser, link_step_6)
    product.open()  # Открыть страницу товара
    product.add_product_in_cart()  # Добавить товар в корзину
    product.sucsess_message_disappeared()  # Проверяем, что нет сообщения об успехе с помощью


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()  # Открыть страницу товара
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)  # для перехода на новую страницу
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()  # открываем страницу
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.no_product_in_the_basket()  # Ожидаем, что в корзине нет товаров
    basket_page.message_about_empty_basket()  # Ожидаем, что есть текст о том что корзина пуста
