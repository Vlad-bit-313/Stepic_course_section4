base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

basket.py - Здесь хранятся методы для тест-кейсов из test_product_page.py связанные с корзиной

conftest.py -  Для хранения часто употребимых фикстур и хранения глобальных настроек. Тут лежит фикстура browser, которая создает нам экземпляр браузера для тестов

locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

login_page.py = Здесь хранятся методы для тест-кейсов из test_product_page.py и test_main_page.py связанные со страницей регистрации

main_page.py - тут мы храним методы по конкретной странице (главной странице), завернутые в класс этой странице.
Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

test_main_page.py - Здесь хранятся тест-кейсы для главной страницы

test_product_page.py - Здесь хранятся тест-кейсы, связанных со страницей товара.

product_page.py - Здесь хранятся методы для тест-кейсов из test_product_page.py связанные со страницей продукта

pytest.ini - Здесь хранятся зарегестрированная метка need_review для запуска оперделенных (промаркированных) тестов

