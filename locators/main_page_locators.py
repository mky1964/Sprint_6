from selenium.webdriver.common.by import By

class MainPageLocators:
    IMPORTANT_QUESTIONS = (By.XPATH, "//div[text()='Вопросы о важном']")

    QUESTION_ARROW_LOCATOR = (By.XPATH, "//div[@id='accordion__heading-{}']")

    QUESTION_ARROW_1 = (By.XPATH, "//div[@id='accordion__heading-0']")
    QUESTION_ARROW_2 = (By.XPATH, "//div[@id='accordion__heading-1']")
    QUESTION_ARROW_3 = (By.XPATH, "//div[@id='accordion__heading-2']")
    QUESTION_ARROW_4 = (By.XPATH, "//div[@id='accordion__heading-3']")
    QUESTION_ARROW_5 = (By.XPATH, "//div[@id='accordion__heading-4']")
    QUESTION_ARROW_6 = (By.XPATH, "//div[@id='accordion__heading-5']")
    QUESTION_ARROW_7 = (By.XPATH, "//div[@id='accordion__heading-6']")
    QUESTION_ARROW_8 = (By.XPATH, "//div[@id='accordion__heading-7']")

    ANSWER_LOCATOR = (By.XPATH, "//div[@id='accordion__panel-{}']/p")


    ANSWER_1 = (By.XPATH, "//div[@id='accordion__panel-0']/p")
    ANSWER_2 = (By.XPATH, "//div[@id='accordion__panel-1']/p")
    ANSWER_3 = (By.XPATH, "//div[@id='accordion__panel-2']/p")
    ANSWER_4 = (By.XPATH, "//div[@id='accordion__panel-3']/p")
    ANSWER_5 = (By.XPATH, "//div[@id='accordion__panel-4']/p")
    ANSWER_6 = (By.XPATH, "//div[@id='accordion__panel-5']/p")
    ANSWER_7 = (By.XPATH, "//div[@id='accordion__panel-6']/p")
    ANSWER_8 = (By.XPATH, "//div[@id='accordion__panel-7']/p")
    COOKIES_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
    ORDER_UPPER_BUTTON =(By.XPATH, '//button[@class = "Button_Button__ra12g"]')
    ORDER_BOTTOM_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')
    HOME_HEADER = (By.XPATH, "//div[@class='Home_Header__iJKdX']")
    COURIER_GRAPS_SCOOTER = By.XPATH, '//div[@class="Home_Status__YkfmH" and text()="Курьер забирает самокат"]'
