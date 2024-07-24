from selenium.webdriver.common.by import By

class Qaorder1pageLocators:
    FOR_WHOM_SCOOTER_TEXT = (By.XPATH, "//div[@class='Order_Header__BZXOb']")
    INPUT_FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя' ]")
    INPUT_SECOND_NAME =(By.XPATH, "//input[@placeholder='* Фамилия' ]")
    ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    PLACEHOLDER_METRO = (By.XPATH, "//input[@class='select-search__input']")
    INPUT_KRASNOSELSKAYA = (By.XPATH, "//div[text()='Красносельская']")
    INPUT_CHERKIZOVSKAYA = (By.XPATH, "//div[text()='Черкизовская']")
    TELEPHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT1 =(By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")



