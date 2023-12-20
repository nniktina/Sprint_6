import data
import allure
from pages.main_page import MainPage
from pages.order_page import ScooterOrderPage


class TestOrderButtons:

    @allure.title('Проверка кнопки "Заказать" вверху страницы')
    @allure.description('На главной странице находим кнопку "Заказать" вверху и проверяем что она ведет на страницу заказа самоката')
    def test_top_order_button(self, driver):
        main_page = MainPage(driver)
        order_page = ScooterOrderPage(driver)
        main_page.go_main_page()
        main_page.click_top_order_button()
        assert order_page.find_order_form().is_displayed()

    @allure.title('Проверка кнопки "Заказать" в нижней части страницы')
    @allure.description('На главной странице находим кнопку "Заказать" в нижней части и проверяем что она ведет на страницу заказа самоката')
    def test_bottom_order_button(self, driver):
        main_page = MainPage(driver)
        order_page = ScooterOrderPage(driver)
        main_page.go_main_page()
        main_page.scroll_to_bottom_order_button()
        main_page.click_bottom_order_button()
        assert order_page.find_order_form().is_displayed()


class TestLogoButtons:

    @allure.title('Проверка редиректа на страницу Дзена через лого Яндекса')
    @allure.description('Со страницы заказа нажимаем на лого Я и проверяем что открылось новое окно в браузере с Дзеном')
    def test_yandex_logo_redirect(self, driver):
        order_page = ScooterOrderPage(driver)
        order_page.go_order_page()
        order_page.click_yandex_logo()
        assert order_page.get_url() == data.dzen_url

    @allure.title('Проверка редиректа на главную страницу через лого Самоката')
    @allure.description('Со страницы заказа нажимаем на лого Самоката и проверяем, что открылась главная страница приложения')
    def test_scooter_logo_redirect(self, driver):
        order_page = ScooterOrderPage(driver)
        order_page.go_order_page()
        order_page.click_scooter_logo()
        assert order_page.get_url() == data.main_page_url
