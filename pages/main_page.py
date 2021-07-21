from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    # Тест-кейс. Проверить, что есть ссылка, которая ведет на логин
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # если добавиться allert, то мы можем добавиь эту строчку и всё, остальные тесты менять не нужно
        # alert = self.browser.switch_to.alert
        # alert.accept()
