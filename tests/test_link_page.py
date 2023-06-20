import allure
import time
from pages.link_page import Link
from locators import Locators


class TestLink:
    @allure.title('Проверка перехода по ссылке на логотипе "Самокат"')
    def test_scooter_link(self, driver):
        driver.find_element(*Locators.top_order_button).click()
        link_page = Link(driver)
        link_page.scooter_link()
        url = driver.current_url
        assert url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода по ссылке на логотипе "Яндекс"')
    def test_yandex_link(self, driver):
        link_page = Link(driver)
        link_page.yandex_link()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(3)
        url = driver.current_url
        assert url == 'https://dzen.ru/?yredirect=true'
