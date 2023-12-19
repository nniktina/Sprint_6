# Sprint_6
Тестирование сервиса https://qa-scooter.praktikum-services.ru/

pages:
pages/base_page.py - базовые методы, используемые в методах на страницах 
pages/main_page.py - методы для работы с объектами на главной странице 
pages/order_page.py - методы для работы с объектами на странице заказа самоката


locators:
locators/main_page_locators.py - локаторы главной страницы
locators/order_locators.py - локаторы на странице заказа самоката (включая все формы и попапы)


test:
tests/conftest.py - файл с фикстурами
tests/test_questions.py - тест блока с ответами на главной странице сервиса
tests/test_order_scooter.py - тест позитивного сценария заказа самоката
tests/test_buttons_redirect.py - тесты для првоерки корректного редиректа кнопок "Заказать", а также лого кнопок