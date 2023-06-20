import allure
from pages.order_page import OrderPage
from locators import Locators


class TestOrderPage:
    @allure.title('Проверка верхней кнопки "Заказать"')
    def test_top_order_button(self, driver):
        driver.find_element(*Locators.top_order_button).click() # нажать верхнюю кнопку Заказать
        order_page = OrderPage(driver)
        order_page.name()
        order_page.address()
        order_page.phone()
        driver.find_element(*Locators.next_button).click() # Далее
        order_page.delivery_day()
        order_page.rental_period()
        order_page.scooter_color()
        order_page.comment()
        driver.find_element(*Locators.lower_order_button).click()
        driver.find_element(*Locators.button_yes).click()
        text = driver.find_element(*Locators.order_processed).text
        assert "Заказ оформлен" in text

    @allure.title('Проверка нижней кнопки "Заказать"')
    def test_lower_order_button(self, driver):
        driver.find_element(*Locators.cookie).click()
        driver.find_element(*Locators.lower_order_button).click()
        order_page = OrderPage(driver)
        order_page.name()
        order_page.address()
        order_page.phone()
        driver.find_element(*Locators.next_button).click()  # Далее
        order_page.delivery_day()
        order_page.rental_period()
        order_page.scooter_color()
        order_page.comment()
        driver.find_element(*Locators.lower_order_button).click()
        driver.find_element(*Locators.button_yes).click()
        text = driver.find_element(*Locators.order_processed).text
        assert "Заказ оформлен" in text
