import allure
from locators import Locators
from pages.order_page import OrderPage

class Link(OrderPage):

    @allure.step('Нажать на надпись-логотип "Самокат"')
    def scooter_link(self):
        self.driver.find_element(*Locators.logo_scooter_locator).click()

    @allure.step('Нажать на надпись-логотип "Яндекс"')
    def yandex_link(self):
        self.driver.find_element(*Locators.logo_ya_locator).click()
