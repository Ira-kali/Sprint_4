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

    question_1 = [By.XPATH, "//div[text()='Сколько это стоит? И как оплатить?']"]
    question_2 = [By.XPATH, "//div[text()='Хочу сразу несколько самокатов! Так можно?']"]
    question_3 = [By.XPATH, "//div[text()='Как рассчитывается время аренды?']"]
    question_4 = [By.XPATH, "//div[text()='Можно ли заказать самокат прямо на сегодня?']"]
    question_5 = [By.XPATH, "//div[text()='Можно ли продлить заказ или вернуть самокат раньше?']"]
    question_6 = [By.XPATH, "//div[text()='Вы привозите зарядку вместе с самокатом?']"]
    question_7 = [By.XPATH, "//div[text()='Можно ли отменить заказ?']"]
    question_8 = [By.XPATH, "//div[text()='Я жизу за МКАДом, привезёте?']"]

    answer_1 = [By.XPATH, "//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"]
    answer_2 = [By.XPATH, "//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']"]
    answer_3 = [By.XPATH, "//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']"]
    answer_4 = [By.XPATH, "//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']"]
    answer_5 = [By.XPATH, "//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']"]
    answer_6 = [By.XPATH, "//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"]
    answer_7 = [By.XPATH, "//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']"]
    answer_8 = [By.XPATH, "//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']"]
