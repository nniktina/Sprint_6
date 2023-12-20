import locators.main_page_locators
import data
import pytest
import allure
from pages.main_page import MainPage


class TestQuestionsBlock:

    @allure.title('Проверка ответов на вопросы в блоке "Вопросы о важном"')  # декораторы
    @allure.description('На главной странице проверяем ответ на каждый вопрос блока "Вопросы о важном" через параметризацию тестов')
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
    def test_answer(self, question_locator, answer_locator, answer_text, driver):
        question_block = MainPage(driver)
        question_block.go_main_page()
        question_block.load_and_click_question(question_locator)
        actual_answer = question_block.get_answer(answer_locator)
        assert actual_answer == answer_text
