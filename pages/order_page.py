from selenium.webdriver.support.wait import WebDriverWait
import data
import locators.order_locators
import locators.main_page_locators
from pages.base_page import BasePage
import allure


class ScooterOrderPage(BasePage):

    @allure.step('Заполняем поле "Станция метро"')
    def fill_metro_station(self, metro_station_locator):
        self.click(locators.order_locators.metro_field)
        self.click(metro_station_locator)

    @allure.step('Заполняем все поля для формы "Для кого самокат" и клик на кнопку "Далее"')
    def fill_first_form_and_click(self, metro_station_locator):
        self.send_keys(locators.order_locators.name_field, data.user_name)
        self.send_keys(locators.order_locators.surname_field, data.user_surname)
        self.send_keys(locators.order_locators.address_field, data.user_address)
        self.send_keys(locators.order_locators.phone_field, data.user_phone)
        self.fill_metro_station(metro_station_locator)
        self.click(locators.order_locators.next_button)

    @allure.step('Ждем загрузки формы "Про аренду"')
    def wait_loading_second_form(self):
        self.waiting(locators.order_locators.about_rent_form_title)

    @allure.step('Выбираем дату аренды из календаря')
    def fill_date(self):
        self.click(locators.order_locators.date_field)
        self.click(locators.order_locators.current_day_at_calendar)

    @allure.step('Выбираем срок аренды из выпадающего списка')
    def fill_rental_period(self):
        self.click(locators.order_locators.rental_period_field)
        self.click(locators.order_locators.rental_periods)

    @allure.step('Заполняем чекбокс выбора цвета самоката')
    def choose_colour_field(self, colour_locator):
        self.click(colour_locator)

    @allure.step('Нажимаем кнопку "Да" в окне подтверждения заказа')
    def click_yes_button(self):
        self.click(locators.order_locators.yes_button)

    @allure.step('Заполнение полей на форме заказа "Про аренду"')
    def fill_second_form_and_click(self, colour_locator):
        self.fill_date()
        self.fill_rental_period()
        self.choose_colour_field(colour_locator)
        self.click(locators.order_locators.order_button)
        self.waiting(locators.order_locators.order_modal_window)
        self.click_yes_button()

    @allure.step('Ждем загрузку отображения кнопки просмотра заказа после оформления заказа')
    def wait_loading_success_popup(self):
        self.waiting(locators.order_locators.order_check_button)

    @allure.step('Нажимаем на лого "Яндекс" в левом верхнем углу и переходим в открывшееся окно')
    def click_yandex_logo(self):
        self.click(locators.order_locators.yandex_logo)
        WebDriverWait(self.driver, 5).until(lambda driver: len(driver.window_handles) > 1)
        dzen_window = self.driver.window_handles[1]
        self.driver.switch_to.window(dzen_window)
        self.waiting(locators.order_locators.dzen_page_widget)

    @allure.step('Нажимаем на лого "Самокат" в левом верхнем углу')
    def click_scooter_logo(self):
        self.click(locators.order_locators.scooter_logo)
        self.waiting(locators.main_page_locators.main_header)

    @allure.step('Ищем попап об успешном заказе самоката')
    def find_success_popup(self):
        return self.driver.find_element(*locators.order_locators.success_order_info)

    @allure.step('Ищем блок "Для кого самокат" на странице заказа')
    def find_order_form(self):
        return self.driver.find_element(*locators.order_locators.order_for_whom_block)

    @allure.step('Получаем текущий url')
    def get_url(self):
        return self.driver.current_url



