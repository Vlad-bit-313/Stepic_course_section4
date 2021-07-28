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

    def sucsess_message_not_in_window(self):
        sucsess_messge = self.is_not_element_present(*ProductPageLocators.NAME_SUCSESS_MESSAGE)
        assert sucsess_messge, "Появилсось сообщение о добавлении товара в корзину"

    def sucsess_message_disappeared(self):
        message_disappeared = self.is_disappeared(*ProductPageLocators.NAME_SUCSESS_MESSAGE)
        assert message_disappeared, "Сообщения об успехе добавления в корзину не исчезло"


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

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        input_password.send_keys(password)
        input_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_PASSWORD)
        input_password_confirm.send_keys(password)
        click_button_of_registration = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        click_button_of_registration.click()
