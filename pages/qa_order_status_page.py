import allure
from selenium.webdriver.common.by import By

from locators.qa_order_1_locators import Qaorder1pageLocators
from locators.qa_order_2_locators import Qaorder2pageLocators
from locators.qa_order_status_page_locators import QaorderStatusPageLocators

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class QaOrderStatusPage(BasePage):#Object page -страница Статуса заказа


    @allure.step('find_order_status_2_button')
    def find_order_status_2_button(self):  #Найти кнопку Статус Заказа на странице Статус заказа
        self.find_element_located(QaorderStatusPageLocators.ORDER_STATUS_2_BUTTON)





    @allure.step('click_logo_scooter_status')
    def click_logo_scooter_status(self):#Клик на ЛОГО Самокат на странице Статус заказа
        self.find_element_located(QaorderStatusPageLocators.TRANSFERE_LOGO_SCOOTER).click()

    @allure.step('click_logo_yandex_status')
    def click_logo_yandex_status(self):#Клик на ЛОГО ЯНДЕКС на странице Статус заказа
        self.find_element_located(QaorderStatusPageLocators.TRANSFERE_LOGO_YANDEX).click()

    def shut_pop_up_window_zen_status(self):#Клик на ЛОГО Самокат на странице Статус заказа
        self.find_element_located(QaorderStatusPageLocators.SHUT_POP_UP_WINDOW_BUTTON).click()