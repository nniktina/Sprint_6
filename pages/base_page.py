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

    def waiting_new_browser_tab(self):
        return WebDriverWait(self.driver, 10).until(lambda driver: len(driver.window_handles) > 1)

    def send_keys(self, locator, key):
        return self.driver.find_element(*locator).send_keys(key)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        return self.driver.find_element(*locator).click()

    def go_main_page(self):
        self.driver.get(data.main_page_url)
        self.waiting(locators.main_page_locators.header_logo)

    def go_order_page(self):
        self.driver.get(data.order_page_url)
        self.waiting(locators.order_locators.order_for_whom_block)

    def switch_to_new_tab(self):
        dzen_window = self.driver.window_handles[1]
        self.driver.switch_to.window(dzen_window)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):
        return self.driver.current_url

