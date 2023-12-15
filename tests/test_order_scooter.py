from selenium import webdriver
import locators.order_locators
import data
import pytest
import pages.main_page
import pages.order_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestOrderScenario:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    def test_top_order_button(self):
        self.driver.get(data.main_page_url)
        question_block = pages.main_page.MainPage(self.driver)
        order_page = pages.order_page.ScooterOrderPage(self.driver)
        question_block.wait_loading_homepage()
        question_block.click_top_order_button()
        order_page.wait_loading_order_page()
        assert self.driver.find_element(By.CSS_SELECTOR, locators.order_locators.order_for_whom_block).is_displayed()

    def test_bottom_order_button(self):
        self.driver.get(data.main_page_url)
        question_block = pages.main_page.MainPage(self.driver)
        order_page = pages.order_page.ScooterOrderPage(self.driver)
        question_block.wait_loading_homepage()
        question_block.scroll_to_bottom_order_button()
        question_block.click_bottom_order_button()
        order_page.wait_loading_order_page()
        assert self.driver.find_element(By.CSS_SELECTOR, locators.order_locators.order_for_whom_block).is_displayed()

    @pytest.mark.parametrize('colour_locator, metro_station_locator', [
        [locators.order_locators.scooter_black_checkbox, locators.order_locators.metro_first_station],
        [locators.order_locators.scooter_grey_checkbox, locators.order_locators.metro_third_station]
        ])
    def test_scooter_order_success_popup(self, colour_locator, metro_station_locator, name_fixture, surname_fixture, address_fixture, phone_fixture):
        self.driver.get(data.main_page_url)
        question_block = pages.main_page.MainPage(self.driver)
        order_page = pages.order_page.ScooterOrderPage(self.driver)
        question_block.wait_loading_homepage()
        question_block.click_top_order_button()
        order_page.wait_loading_order_page()
        order_page.fill_first_form_and_click(name_fixture, surname_fixture, address_fixture, phone_fixture, metro_station_locator)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.order_locators.about_rent_form_title))
        order_page.order_fill_second_form_and_click(colour_locator)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.order_locators.order_check_button))
        assert self.driver.find_element(*locators.order_locators.success_order_info).is_displayed()

    def test_yandex_logo_redirect(self):
        self.driver.get(data.order_page_url)
        order_page = pages.order_page.ScooterOrderPage(self.driver)
        order_page.click_yandex_logo()
        assert self.driver.current_url == data.dzen_url

    def test_scooter_logo_redirect(self):
        self.driver.get(data.order_page_url)
        order_page = pages.order_page.ScooterOrderPage(self.driver)
        order_page.click_scooter_logo()
        assert self.driver.current_url == data.main_page_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
