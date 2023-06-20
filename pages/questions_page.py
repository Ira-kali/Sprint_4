import allure
from pages.order_page import OrderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import Locators


class QuestionsPage(OrderPage):
    @allure.step('Клик по "Сколько это стоит? И как оплатить?" в блоке Вопросы о важном')
    def question_one(self):
        question = self.driver.find_element(*Locators.question_1)
        self.driver.execute_script('arguments[0].scrollIntoView();', question)
        element = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(Locators.question_1))
        element.click()
    def answer_one(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(Locators.answer_1)).text


    @allure.step('Клик по "Хочу сразу несколько самокатов! Так можно?" в блоке Вопросы о важном')
    def question_two(self):
        question = self.driver.find_element(*Locators.question_2)
        self.driver.execute_script('arguments[0].scrollIntoView();', question)
        element = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(Locators.question_2))
        element.click()
    def answer_two(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(Locators.answer_2)).text


    @allure.step('Клик по "Как рассчитывается время аренды?" в блоке Вопросы о важном')
    def question_three(self):
        question = self.driver.find_element(*Locators.question_3)
        self.driver.execute_script('arguments[0].scrollIntoView();', question)
        element = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(Locators.question_3))
        element.click()
    def answer_three(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(Locators.answer_3)).text


    @allure.step('Клик по "Можно ли заказать самокат прямо на сегодня?" в блоке Вопросы о важном')
    def question_four(self):
        question = self.driver.find_element(*Locators.question_4)
        self.driver.execute_script('arguments[0].scrollIntoView();', question)
        element = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(Locators.question_4))
        element.click()
    def answer_four(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(Locators.answer_4)).text


    @allure.step('Клик по "Можно ли продлить заказ или вернуть самокат раньше?" в блоке Вопросы о важном')
    def question_five(self):
        question = self.driver.find_element(*Locators.question_5)
        self.driver.execute_script('arguments[0].scrollIntoView();', question)
        element = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(Locators.question_5))
        element.click()
    def answer_five(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(Locators.answer_5)).text


    @allure.step('Клик по "Вы привозите зарядку вместе с самокатом?" в блоке Вопросы о важном')
    def question_six(self):
        question = self.driver.find_element(*Locators.question_6)
        self.driver.execute_script('arguments[0].scrollIntoView();', question)
        element = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(Locators.question_6))
        element.click()
    def answer_six(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(Locators.answer_6)).text


    @allure.step('Клик по "Можно ли отменить заказ?" в блоке Вопросы о важном')
    def question_seven(self):
        question = self.driver.find_element(*Locators.question_7)
        self.driver.execute_script('arguments[0].scrollIntoView();', question)
        element = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(Locators.question_7))
        element.click()
    def answer_seven(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(Locators.answer_7)).text


    @allure.step('Клик по "Я жизу за МКАДом, привезёте?" в блоке Вопросы о важном')
    def question_eight(self):
        question = self.driver.find_element(*Locators.question_8)
        self.driver.execute_script('arguments[0].scrollIntoView();', question)
        element = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(Locators.question_8))
        element.click()
    def answer_eight(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(Locators.answer_8)).text
