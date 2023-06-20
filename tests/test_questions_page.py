import allure
from pages.questions_page import QuestionsPage


class TestQuestion:

    @allure.description('Проверяем, что при открытии первого вопроса, открывается соответствующий текст ответа')
    def test_question_one(self,driver):
        questions_page = QuestionsPage(driver)
        questions_page.question_one()
        assert questions_page.answer_one() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.description('Проверяем, что при открытии второго вопроса, открывается соответствующий текст ответа')
    def test_question_two(self,driver):
        questions_page = QuestionsPage(driver)
        questions_page.question_two()
        assert questions_page.answer_two() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.description('Проверяем, что при открытии третьего вопроса, открывается соответствующий текст ответа')
    def test_question_three(self,driver):
        questions_page = QuestionsPage(driver)
        questions_page.question_three()
        assert questions_page.answer_three() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.description('Проверяем, что при открытии четвертого вопроса, открывается соответствующий текст ответа')
    def test_question_four(self,driver):
        questions_page = QuestionsPage(driver)
        questions_page.question_four()
        assert questions_page.answer_four() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.description('Проверяем, что при открытии пятого вопроса, открывается соответствующий текст ответа')
    def test_question_five(self,driver):
        questions_page = QuestionsPage(driver)
        questions_page.question_five()
        assert questions_page.answer_five() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.description('Проверяем, что при открытии шестого вопроса, открывается соответствующий текст ответа')
    def test_question_six(self,driver):
        questions_page = QuestionsPage(driver)
        questions_page.question_six()
        assert questions_page.answer_six() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.description('Проверяем, что при открытии седьмого вопроса, открывается соответствующий текст ответа')
    def test_question_seven(self,driver):
        questions_page = QuestionsPage(driver)
        questions_page.question_seven()
        assert questions_page.answer_seven() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'


    @allure.description('Проверяем, что при открытии восьмого вопроса, открывается соответствующий текст ответа')
    def test_question_eight(self,driver):
        questions_page = QuestionsPage(driver)
        questions_page.question_eight()
        assert questions_page.answer_eight() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
