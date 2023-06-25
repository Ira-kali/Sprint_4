import allure
from pages.order_page import OrderPage
from locators import Locators
from pages.base_page import BasePage

class TestOrderPage:
    @allure.title('Проверка верхней кнопки "Заказать"')
    def test_top_order_button(self, driver):
        order_page = OrderPage(driver)
        order_page.click_top_order_button() # Заказать
        order_page.filling_page_for_whom_scooter() # заполнение окна Для кого самокат
        order_page.click_next_button() # Далее
        order_page.filling_about_rent() # заполнение окна Про аренду
        order_page.click_lower_order_button() # кнопка заказать
        order_page.click_button_yes() # кнопка подтверждения заказа
        text = driver.find_element(*Locators.order_processed).text
        assert "Заказ оформлен" in text

    @allure.title('Проверка нижней кнопки "Заказать"')
    def test_lower_order_button(self, driver):
        order_page = OrderPage(driver)
        base_page = BasePage(driver)
        base_page.click_cookie() # убрать куки
        order_page.click_lower_order_button() # нажать нижнюю кнопку заказать
        order_page.filling_page_for_whom_scooter()
        order_page.click_next_button()  # Далее
        order_page.filling_about_rent()
        order_page.click_lower_order_button()  # кнопка заказать
        order_page.click_button_yes()  # кнопка подтверждения заказа
        text = driver.find_element(*Locators.order_processed).text
        assert "Заказ оформлен" in text
