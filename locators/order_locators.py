from selenium.webdriver.common.by import By

order_for_whom_block = '.App_App__15LM-'

name_field = [By.XPATH, './/input[@placeholder="* Имя"]']
surname_field = [By.XPATH, './/input[@placeholder="* Фамилия"]']
address_field = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
phone_field = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
metro_field = [By.CSS_SELECTOR, '.select-search__input']
metro_first_station = [By.XPATH, './/li[@data-value="1"]/child::button']
metro_third_station = [By.XPATH, './/li[@data-value="3"]/child::button']
next_button = [By.CSS_SELECTOR, '.Button_Middle__1CSJM']

about_rent_form_title = [By.XPATH, './/div[text()="Про аренду"]']
date_field = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
rental_period_field = [By.CSS_SELECTOR, '.Dropdown-placeholder']
rental_periods = [By.XPATH, './/div[@class="Dropdown-menu"]/child::*']
scooter_black_checkbox = [By.XPATH, './/input[@id="black"]']
scooter_grey_checkbox = [By.XPATH, './/input[@id="grey"]']
order_button = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/child::button[text()="Заказать"]']

order_modal_window = [By.CSS_SELECTOR, '.Order_Modal__YZ-d3']
current_day_at_calendar = [By.CSS_SELECTOR, '.react-datepicker__day--today']
yes_button = [By.XPATH, './/button[text()="Да"]']
success_order_info = [By.CSS_SELECTOR, '.Order_Modal__YZ-d3']
order_check_button = [By.XPATH, './/button[text()="Посмотреть статус"]']

yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
dzen_page_widget = [By.CLASS_NAME, 'dzen-desktop__widget-r2']
