import allure
from locators import Locators
from pages.base_page import BasePage

class QuestionsPage(BasePage):
    @allure.step('Пролистать до раздела "Вопросы о важном" на главной странице')
    def scroll_to_the_most_asked_questions_section(self):
        section = self.find_element_located(Locators.most_asked_questions)
        self.scroll_to_element(section)
        self.wait_element_visible(Locators.question_locator)

    def go_to_site(self):
        url = 'https://qa-scooter.praktikum-services.ru/'
        return self.driver.get(url)

    @allure.step('Нажать на каждый вопрос')
    def click_on_questions(self, index):
        self.wait_element_visible(Locators.question_locator)
        questions = self.find_elements_located(Locators.question_locator)
        questions[index].click()

    @allure.step('Получить текст ответа на вопрос')
    def get_answers(self):
        self.wait_element_visible(Locators.answer_locator)
        return self.find_element_located(Locators.answer_locator).text
