import allure
from selenium.webdriver.common.by import By

from locators.qa_order_1_locators import Qaorder1pageLocators
from locators.qa_order_2_locators import Qaorder2pageLocators

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class QaOrder2page(BasePage):#Object page -вторая страница ввода данных




    @allure.step('find_for_about_rent_text')
    def find_for_about_rent_text(self):  #Найти текст Про Аренду
        text1 = self.find_element_located(Qaorder1pageLocators.FOR_WHOM_SCOOTER_TEXT)
        return text1


    @allure.step('enter_date')
    def enter_date(self,date):#Дата, Когда привезти самокат
        date_field = self.find_element_located(Qaorder2pageLocators.DATE_OF_DELIVERY).send_keys(date)

        return date_field



    @allure.step('enter_term_of_rent')
    def enter_term_of_rent(self,locator):#Ввод длительности аренды

        date_field = self.find_element_located((By.XPATH, "//span[@class='Dropdown-arrow']")).click()
        self.find_element_located(locator).click()



    @allure.step('click_on_cookies_button')
    def click_to_order_button(self):#Клик на кнопку ДАЛЕЕ на первой форме ввода данных
        self.find_element_located(Qaorder2pageLocators.TO_ORDER_BUTTON).click()

    @allure.step('find_for_whant_to_book_order_text')
    def find_want_to_book_order_text(self):  #Найти текст Хотите оформить заказ
        text1 = self.find_element_located(Qaorder2pageLocators.WANT_TO_BOOK_ORDER).text

    @allure.step('click_yes_button_approve_order')
    def click_yes_button_approve_order(self):#Клик на кнопку ДА в окне подтверждения заказа
        self.find_element_located(Qaorder2pageLocators.YES_BUTTON_APPROVE_ORDER).click()

    @allure.step('find_order_is_accepted_text')
    def find_order_is_accepted_text(self):  #Найти текст Заказ Принят на выпадающем окне
        text1 = self.find_element_located(Qaorder2pageLocators.ORDER_IS_ACCEPTED_TEXT).text

    @allure.step('click_see_status_button')
    def click_see_status_button(self):#Клик на кнопку ДА в окне подтверждения заказа
        self.find_element_located(Qaorder2pageLocators.SEE_STATUS_BUTTON).click()

    @allure.step('filling_second_page_about_rent')
    def filling_second_page_about_rent(self, date, rent_term_locator, color_locator, text):
        self.find_for_about_rent_text()
        self.enter_date(date)
        self.enter_term_of_rent(rent_term_locator)
        self.click_on_element_located(color_locator)
        self.set_text_to_element_located(Qaorder2pageLocators.PLACEHOLDER_FOR_COMMENT, text)
        self.click_to_order_button()
        self.find_want_to_book_order_text()
        self.click_yes_button_approve_order()
        self.find_order_is_accepted_text()















