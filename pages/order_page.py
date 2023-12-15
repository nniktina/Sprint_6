from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import locators.order_locators
import locators.main_page_locators


class ScooterOrderPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_loading_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(data.order_page_url))

    def fill_name(self, name_fixture):
        self.driver.find_element(*locators.order_locators.name_field).send_keys(name_fixture)

    def fill_surname(self, surname_fixture):
        self.driver.find_element(*locators.order_locators.surname_field).send_keys(surname_fixture)

    def fill_address(self, address_fixture):
        self.driver.find_element(*locators.order_locators.address_field).send_keys(address_fixture)

    def fill_phone(self, phone_fixture):
        self.driver.find_element(*locators.order_locators.phone_field).send_keys(phone_fixture)

    def fill_metro_station(self, metro_station_locator):
        self.driver.find_element(*locators.order_locators.metro_field).click()
        self.driver.find_element(*metro_station_locator).click()

    def click_next_button(self):
        self.driver.find_element(*locators.order_locators.next_button).click()

    def fill_first_form_and_click(self, name_fixture, surname_fixture, address_fixture, phone_fixture, metro_station_locator):
        self.fill_name(name_fixture)
        self.fill_surname(surname_fixture)
        self.fill_address(address_fixture)
        self.fill_phone(phone_fixture)
        self.fill_metro_station(metro_station_locator)
        self.click_next_button()

    def fill_date(self):
        self.driver.find_element(*locators.order_locators.date_field).click()
        self.driver.find_element(*locators.order_locators.current_day_at_calendar).click()

    def fill_rental_period(self):
        self.driver.find_element(*locators.order_locators.rental_period_field).click()
        self.driver.find_element(*locators.order_locators.rental_periods).click()

    def choose_colour_field(self, colour_locator):
        self.driver.find_element(*colour_locator).click()

    def click_order_button(self):
        self.driver.find_element(*locators.order_locators.order_button).click()

    def wait_order_modal(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.order_locators.order_modal_window))

    def click_yes_button(self):
        self.driver.find_element(*locators.order_locators.yes_button).click()

    def order_fill_second_form_and_click(self, colour_locator):
        self.fill_date()
        self.fill_rental_period()
        self.choose_colour_field(colour_locator)
        self.click_order_button()
        self.wait_order_modal()
        self.click_yes_button()

    def click_yandex_logo(self):
        self.driver.find_element(*locators.order_locators.yandex_logo).click()
        WebDriverWait(self.driver, 5).until(lambda driver: len(driver.window_handles) > 1)
        dzen_window = self.driver.window_handles[1]
        self.driver.switch_to.window(dzen_window)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locators.order_locators.dzen_page_widget))

    def click_scooter_logo(self):
        self.driver.find_element(*locators.order_locators.scooter_logo).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locators.main_page_locators.main_header))



