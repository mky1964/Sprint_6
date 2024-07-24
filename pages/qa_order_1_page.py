import allure
from selenium.webdriver.common.by import By

from locators.qa_order_1_locators import Qaorder1pageLocators

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class QaOrder1page(BasePage):



    @allure.step('find_for_whom_scooter_text')
    def find_for_whom_scooter_text(self):  #Найти текст Для Кого Самокат
        text1 = self.find_element_located(Qaorder1pageLocators.FOR_WHOM_SCOOTER_TEXT).text
        return text1

    @allure.step('enter_first_name')
    def enter_first_name(self,first_name):#Ввод имени
        first_name_field = self.find_element_located(Qaorder1pageLocators.INPUT_FIRST_NAME)
        first_name_field.click()
        first_name_field.send_keys(first_name)
        return first_name_field

    @allure.step('enter_first_name')
    def enter_second_name(self,second_name):#Ввод фамилиии
        second_name_field = self.find_element_located(Qaorder1pageLocators.INPUT_SECOND_NAME)
        second_name_field.send_keys(second_name)
        return second_name_field

    @allure.step('enter_address')
    def enter_address(self,address):#Ввод адреса
        address_field = self.find_element_located(Qaorder1pageLocators.ADDRESS)
        address_field.send_keys(address)
        return address_field


    @allure.step('enter_metro_station')
    def enter_metro_station(self,locator):#Ввод станции метро
        self.find_element_located(Qaorder1pageLocators.PLACEHOLDER_METRO).click()
        self.find_element_located(locator).click()

    @allure.step('enter_telphone')
    def enter_telephone(self,telephone):#Ввод телефона
        telephone_field1 = self.find_element_located(Qaorder1pageLocators.TELEPHONE_FIELD)
        telephone_field1.send_keys(telephone)
        return telephone_field1

    @allure.step('click_on_cookies_button')
    def click_next1_button(self):#Клик на кнопку ДАЛЕЕ на первой форме ввода данных
        self.find_element_located(Qaorder1pageLocators.BUTTON_NEXT1).click()

    @allure.step('filling_first_page_for_whom_samokat')
    def filling_first_page_for_whom_samokat(self, name, second_name, address, m_station, phone):
        self.find_for_whom_scooter_text()
        self.enter_first_name(name)
        self.enter_second_name(second_name)
        self.enter_address(address)
        self.enter_metro_station(m_station)
        self.enter_telephone(phone)
        self.click_next1_button()










