from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
import data


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def waiting(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def send_keys(self, locator, key):
        return self.driver.find_element(*locator).send_keys(key)

    def click(self, locator):
        return self.driver.find_element(*locator).click()

    def go_main_page(self):
        self.driver.get(data.main_page_url)
        self.waiting(locators.main_page_locators.header_logo)

    def go_order_page(self):
        self.driver.get(data.order_page_url)
        self.waiting(locators.order_locators.order_for_whom_block)

