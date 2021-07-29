from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_login_url()
        self.should_be_register_form()

    def should_be_login_url(self):
        # роверка на корректный url адрес
        login_url = self.browser.current_url
        assert "login" in login_url, "URL incorrect"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
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
