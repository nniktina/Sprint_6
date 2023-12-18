import locators.order_locators
import locators.main_page_locators
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    @allure.step('Скролл до блока "Вопросы о важном"')
    def scroll_down_to_questions(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    @allure.step('Клик на вопрос')
    def click_on_question(self, question_locator):
        self.click(question_locator)

    @allure.step('Скролл до блока вопросов и клик на вопрос')
    def load_and_click_question(self, question_locator):
        self.scroll_down_to_questions()
        self.waiting(locators.main_page_locators.faq_block)
        self.click_on_question(question_locator)

    @allure.step('Получаем ответ')
    def get_answer(self, answer_locator):
        self.waiting(answer_locator)
        text = self.driver.find_element(*answer_locator).text
        return text

    @allure.step('Клик на верхнюю кнопку "Заказать"')
    def click_top_order_button(self):
        self.click(locators.main_page_locators.top_order_button)

    @allure.step('Скролл до нижней кнопки "Заказать"')
    def scroll_to_bottom_order_button(self):
        element = self.driver.find_element(*locators.main_page_locators.bottom_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.waiting(locators.main_page_locators.bottom_order_button)

    @allure.step('Клик на нижнюю кнопку "Заказать"')
    def click_bottom_order_button(self):
        self.click(locators.main_page_locators.bottom_order_button)
