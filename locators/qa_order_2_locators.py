from selenium.webdriver.common.by import By

class Qaorder2pageLocators:
    ABOUT_RENT_BUTTON = (By.XPATH, "//div[@class='Order_Header__BZXOb']")
    DATE_OF_DELIVERY =(By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    LENGTH_OF_RENT_ARROW = (By.XPATH, "//div[@class='Dropdown-root Order_FilledDate__1pb8n']")
    ONE_DAY_RENT = (By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']")
    TWO_DAYS_RENT = (By.XPATH,"//div[@class='Dropdown-option' and text()='двое суток']")
    TO_ORDER_BUTTON =(By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    WANT_TO_BOOK_ORDER = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")#ХЕДЕР Хотите оформить заказ
    YES_BUTTON_APPROVE_ORDER = (By.XPATH, "//button[(@class='Button_Button__ra12g Button_Middle__1CSJM') and (text()='Да')]")
    ORDER_IS_ACCEPTED_TEXT = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")#Текс Заказ принят
    SEE_STATUS_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")#Кнопка Посмотреть статус заказа
    BLACK_COLOR_CHECK_BOX = (By.XPATH, '//input[@id="black"]')
    GREY_COLOR_CHECK_BOX = (By.XPATH, '//input[@id="black"]')
    PLACEHOLDER_FOR_COMMENT =(By.XPATH, '//input[@placeholder="Комментарий для курьера"]')