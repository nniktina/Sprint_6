from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.order_locators
import locators.main_page_locators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_loading_homepage(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locators.main_page_locators.header_logo))

    def scroll_down_to_questions(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_questions_visibility(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locators.main_page_locators.faq_block))

    def click_on_question(self, question_locator):
        self.driver.find_element(*question_locator).click()

    def wait_loading_answer(self):
        WebDriverWait(self.driver, 5)

    def load_and_click_question(self, question_locator):
        self.scroll_down_to_questions()
        self.wait_questions_visibility()
        self.click_on_question(question_locator)
        self.wait_loading_answer()

    def get_answer(self, answer_locator):
        text = self.driver.find_element(*answer_locator).text
        return text

    def click_top_order_button(self):
        self.driver.find_element(*locators.main_page_locators.top_order_button).click()

    def scroll_to_bottom_order_button(self):
        element = self.driver.find_element(*locators.main_page_locators.bottom_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_bottom_order_button(self):
        self.driver.find_element(*locators.main_page_locators.bottom_order_button).click()
