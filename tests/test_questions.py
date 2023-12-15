from selenium import webdriver
import locators.main_page_locators
import data
import pages.main_page
import pytest


class TestQuestionsBlock:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @pytest.mark.parametrize('question_locator, answer_locator, answer_text', [
                             [locators.main_page_locators.question_1, locators.main_page_locators.answer_1, data.answer_1_text],
                             [locators.main_page_locators.question_2, locators.main_page_locators.answer_2, data.answer_2_text],
                             [locators.main_page_locators.question_3, locators.main_page_locators.answer_3, data.answer_3_text],
                             [locators.main_page_locators.question_4, locators.main_page_locators.answer_4, data.answer_4_text],
                             [locators.main_page_locators.question_5, locators.main_page_locators.answer_5, data.answer_5_text],
                             [locators.main_page_locators.question_6, locators.main_page_locators.answer_6, data.answer_6_text],
                             [locators.main_page_locators.question_7, locators.main_page_locators.answer_7, data.answer_7_text],
                             [locators.main_page_locators.question_8, locators.main_page_locators.answer_8, data.answer_8_text],
                             ])
    def test_answer(self, question_locator, answer_locator, answer_text):
        self.driver.get(data.main_page_url)
        question_block = pages.main_page.MainPage(self.driver)
        question_block.wait_loading_homepage()
        question_block.load_and_click_question(question_locator)
        actual_answer = question_block.get_answer(answer_locator)
        assert actual_answer == answer_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
