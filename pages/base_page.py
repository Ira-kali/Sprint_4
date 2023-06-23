import allure
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на верхнюю кнопку Заказать')
    def click_top_order_button(self):
        self.driver.find_element(*Locators.top_order_button).click()

    @allure.step('Нажать нижнюю кнопку Заказать')
    def click_lower_order_button(self):
        self.driver.find_element(*Locators.lower_order_button).click()

    @allure.step('Убрать куки')
    def click_cookie(self):
        self.driver.find_element(*Locators.cookie).click()

    @allure.step('Нажать на надпись-логотип "Самокат"')
    def scooter_link(self):
        self.driver.find_element(*Locators.logo_scooter_locator).click()

    @allure.step('Нажать на надпись-логотип "Яндекс"')
    def yandex_link(self):
        self.driver.find_element(*Locators.logo_ya_locator).click()

    def go_to_site(self):
        url = 'https://qa-scooter.praktikum-services.ru/'
        return self.driver.get(url)

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f"Элемент {locator} не найден")

    def find_elements_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), message=f"Элементы {locator} не найдены")

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_element_visible(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
