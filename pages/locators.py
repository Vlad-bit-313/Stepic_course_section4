from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "[name=registration-email]")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "[name=registration-password1]")
    REGISTER_FORM_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "[name=registration-password2]")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators:
    ADD_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, ".alertinner>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_PRICE_IN_CART = (By.CSS_SELECTOR, ".alertinner>p>strong")
    NAME_SUCSESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group>.btn.btn-default:nth-child(1)')
    BASKET_PRODUCTS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
