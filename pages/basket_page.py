from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def no_product_in_the_basket(self):
        product_in_basket = self.is_not_element_present(*BasePageLocators.BASKET_PRODUCTS)
        assert product_in_basket, "В корзине есть товары"

    def message_about_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_MESSAGE), "Нет сообщения 'Ваша корзина пуста'"
