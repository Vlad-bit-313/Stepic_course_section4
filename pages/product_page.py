from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_CART), "Button добавить_в_корзину is not presented"
        button_add_product_to_cart = self.browser.find_element(*ProductPageLocators.ADD_CART)
        button_add_product_to_cart.click()

    def name_book_in_cart(self):
        name_book = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_book_to_cart = self.browser.find_elements(*ProductPageLocators.PRODUCT_NAME_IN_CART)
        name_book_to_cart = name_book_to_cart[0].text
        assert name_book == name_book_to_cart, "Названия не совпадают"

    def price_book_in_cart(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_book_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_CART).text
        assert price_book == price_book_in_cart, "Цены не совпадают"
        print(f'Цена в корзине {price_book_in_cart}')

    def sucsess_message_not_in_window(self):
        sucsess_messge = self.is_not_element_present(*ProductPageLocators.NAME_SUCSESS_MESSAGE)
        assert sucsess_messge, "Появилсось сообщение о добавлении товара в корзину"

    def sucsess_message_disappeared(self):
        message_disappeared = self.is_disappeared(*ProductPageLocators.NAME_SUCSESS_MESSAGE)
        assert message_disappeared, "Сообщения об успехе добавления в корзину не исчезло"
