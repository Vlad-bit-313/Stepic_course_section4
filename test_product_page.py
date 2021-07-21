import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage


# здесь у нас только тест-кейсы
# pytest -v --tb=line --language=en test_product_page.py

@pytest.mark.xfail
@pytest.mark.parametrize('num', ["0", "1", "2", "3", "4", "5", "6",
                                 pytest.param(7, marks=pytest.mark.xfail),
                                 "8", "9"])
def test_guest_can_add_product_to_basket(browser, num):
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = MainPage(browser, link)
    page.open()
    button = ProductPage(browser, link)
    button.add_product_in_cart()  # Добавили товар в корзину
    button.solve_quiz_and_get_code()  # вычислили результ
    button.name_book_in_cart()  # проверяем с тем что добавили
    button.price_book_in_cart()  # проверяем цену в корзине и на сайте
