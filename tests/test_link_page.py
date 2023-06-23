import allure
import time
from pages.base_page import BasePage


class TestLink:
    @allure.title('Проверка перехода по ссылке на логотипе "Самокат"')
    def test_scooter_link(self, driver):
        base_page = BasePage(driver)
        base_page.click_top_order_button()
        base_page.scooter_link()
        url = driver.current_url
        assert url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода по ссылке на логотипе "Яндекс"')
    def test_yandex_link(self, driver):
        base_page = BasePage(driver)
        base_page.yandex_link()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(3)
        url = driver.current_url
        assert url == 'https://dzen.ru/?yredirect=true'
