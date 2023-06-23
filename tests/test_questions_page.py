import allure
from pages.questions_page import QuestionsPage
from pages.base_page import BasePage
from conftest import Answers
import pytest



class TestQuestion:
    @allure.title('Проверка часто задаваемых вопросов и ответов')
    @pytest.mark.parametrize("index", range(8))
    def test_most_asked_questions_on_main_page(self, driver, index):
        base_page = BasePage(driver)
        base_page.go_to_site()
        base_page.click_cookie()
        questions_page = QuestionsPage(driver)
        questions_page.scroll_to_the_most_asked_questions_section()
        questions_page.click_on_questions(index)
        answer = questions_page.get_answers()
        assert answer == Answers.answers[index]
