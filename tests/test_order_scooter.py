import locators.order_locators
import pytest
from pages.main_page import MainPage
from pages.order_page import ScooterOrderPage
import allure


class TestOrderScenario:

    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проходим все этапы заполнения данных для заказа самоката и проверяем, что появляется попап об успешном оформлении заказа')
    @pytest.mark.parametrize('colour_locator, metro_station_locator', [
                    [locators.order_locators.scooter_black_checkbox, locators.order_locators.metro_first_station],
                    [locators.order_locators.scooter_grey_checkbox, locators.order_locators.metro_third_station]
                    ])
    def test_scooter_order_success_popup(self, colour_locator, metro_station_locator, driver):
        order_page = ScooterOrderPage(driver)
        main_page = MainPage(driver)
        main_page.go_main_page()
        main_page.click_top_order_button()
        order_page.fill_first_form_and_click(metro_station_locator)
        order_page.wait_loading_second_form()
        order_page.fill_second_form_and_click(colour_locator)
        order_page.wait_loading_success_popup()
        assert order_page.find_success_popup().is_displayed()


