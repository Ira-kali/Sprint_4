from selenium.webdriver.common.by import By

class Locators:
    logo_ya_locator = [By.XPATH, "// a[ @ href = '//yandex.ru']"] # логотип кнопки Яндекс
    logo_scooter_locator = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"] # логотип кнопки Самокат
    top_order_button = [By.XPATH, '(//button[text()="Заказать"])[1]'] # верхняя кнопка Заказать
    lower_order_button = [By.XPATH, "(//button[text()='Заказать'])[2]"] # нижняя кнопка Заказать
    name_field = [By.XPATH, "//input[@placeholder='* Имя']"] # поле Имя
    last_name_field = [By.XPATH, "//input[@placeholder='* Фамилия']"] # поле Фапилия
    address_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"] # поле Адрес: куда привезти заказ
    metro_station_field = (By.CLASS_NAME, "select-search__input")  # поле Метро
    metro_station = (By.XPATH, "//div[contains(text(),'Сокольники')]")  # Выбор станции метро
    phone_box = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"] # поле Телефон
    next_button = [By.XPATH, "//button[text()='Далее']"] # кнопка Далее
    field_date = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"] # поле Когда привезти самокат
    date_confirmation = [By.XPATH, "//div[contains(@class,'react-datepicker__day--selected')]"] # подтверждение даты
    rental_period_field = [By.CLASS_NAME, "Dropdown-control"] # поле Срок аренды
    rental_period_choice = [By.XPATH, "//div[text()='трое суток']"] # период времени
    scooter_color_field = [By.XPATH, "//input[@id='black' and @type='checkbox']"] # выбор черного самоката
    comment = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"] # поле Комментарий для курьера
    button_yes = [By.XPATH, "//button[text()='Да']"] # кнопка Да при подтверждении заказа
    order_processed = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"] # сообщение о новом заказе
    cookie = [By.XPATH, "//button[text()='да все привыкли']"] # куки

    most_asked_questions = [By.XPATH, "//div[contains(@class, 'Home_FAQ')]"]
    question_locator = (By.XPATH, "//div[contains(@class, 'accordion__item')]")
    answer_locator = (By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]")