import time

import allure
from selenium.webdriver.common.by import By

from conftest import driver
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Click_on_arrow')
    def click_on_arrow_question(self, locator):  #Кликнуть стрелку с вопросом
        self.find_element_located(locator).click()

    @allure.step('Find_answer_on_question')
    def find_answer_on_question(self, locator):  #Найти ответ на Важный вопрос
        answer = self.find_element_located(locator).text
        return answer

    @allure.step('click_on_cookies_button')
    def click_on_cookies_button(self):#Клик на кнопку с куками
        self.find_element_located(MainPageLocators.COOKIES_BUTTON).click()

    @allure.step('click_on_upper_order_button')
    def click_on_upper_order_button(self):#Клик на верхнюю кнопку Заказать
        self.find_element_located(MainPageLocators.ORDER_UPPER_BUTTON).click()

    @allure.step('click_on_bottom_order_button')
    def click_on_bottom_order_button(self, driver):#Клик на верхнюю кнопку Заказать
        element = self.find_element_located(MainPageLocators.COURIER_GRAPS_SCOOTER)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        self.find_element_located(MainPageLocators.ORDER_BOTTOM_BUTTON).click()
    @allure.step('click_question_get_answer')
    def click_question_get_answer(self,  num, driver):
        method, locator = MainPageLocators.QUESTION_ARROW_LOCATOR
        locator = locator.format(num)
        self.click_on_cookies_button()
        self.click_on_element_located((method, locator))
        method, locator = MainPageLocators.ANSWER_LOCATOR
        locator = locator.format(num)
        return self.get_text_from_element_located((method, locator))
    @allure.step('check_answer')
    def check_answer(self, actual_result, expected_result):
        return actual_result == expected_result







