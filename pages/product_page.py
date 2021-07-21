from .base_page import BasePage
from .locators import LoginPageLocators
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


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_login_url()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.current_url
        assert "login" in login_url, "URL incorrect"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
