import allure
from locators import Locators

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполнить поля "Имя", "Фамилия"')
    def name(self):
        self.driver.find_element(*Locators.name_field).send_keys('Ирина')
        self.driver.find_element(*Locators.last_name_field).send_keys('Калинина')

    @allure.step('Заполнить поля "Адрес: куда привезти заказ", "Станция метро"')
    def address(self):
        self.driver.find_element(*Locators.address_field).send_keys('Москва, Русаковская, 24')
        self.driver.find_element(*Locators.metro_station_field).click()
        self.driver.find_element(*Locators.metro_station).click()

    @allure.step('Заполнить поле "Телефон: на него позвонит курьер"')
    def phone(self):
        self.driver.find_element(*Locators.phone_box).send_keys('89279069875')

    @allure.step('Заполнить поле "Когда привезти самокат"')
    def delivery_day(self):
        self.driver.find_element(*Locators.field_date).send_keys('20.06.2023')
        self.driver.find_element(*Locators.date_confirmation).click()

    @allure.step('Заполнить поле "Срок аренды"')
    def rental_period(self):
        self.driver.find_element(*Locators.rental_period_field).click()
        self.driver.find_element(*Locators.rental_period_choice).click()

    @allure.step('Заполнить поле "Цвет самоката"')
    def scooter_color(self):
        self.driver.find_element(*Locators.scooter_color_field).click()

    @allure.step('Заполнить поле "Комментарий для курьера"')
    def comment(self):
        self.driver.find_element(*Locators.comment).send_keys('Хорошего дня')
