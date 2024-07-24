import time

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from locators.constants import Constants

from locators.main_page_locators import MainPageLocators
from locators.qa_order_1_locators import Qaorder1pageLocators
from locators.qa_order_2_locators import Qaorder2pageLocators
from locators.qa_order_status_page_locators import QaorderStatusPageLocators


from pages import main_page
from pages.base_page import BasePage
from pages.qa_order_1_page import QaOrder1page
from pages.qa_order_2_page import QaOrder2page
from pages.qa_order_status_page import QaOrderStatusPage
from pages.main_page import MainPage


class TestOrderProcedureShort:
    @allure.feature('test_order_procedure_short')
    @allure.description('Позитивный тест. Вход через верхнюю и нижнюю кнопку. Набор данных №1 и №2 с сообщением об успешном создании заказа.')

    @pytest.mark.parametrize("order_button, input_set",
                             [
                                 ('up_button', 'set_1'),
                                 ('bottom_button',  'set_2'),
                                 ('up_button', 'set_2' ),
                                 ('bottom_button', 'set_1')
                             ]
                             )
    def test_order_procedure_short(self, driver, order_button, input_set):#Проверка процедуры заказа до появления всплывающего окна Заказ Оформлен

        order_main = MainPage(driver)
        order_main.go_to_site(Constants.BASE_URL)
        if order_button == 'up_button':
            order_main.click_on_upper_order_button()
        elif order_button == 'bottom_button':
            order_main.click_on_bottom_order_button(driver)

        set = []
        if input_set == 'set_1':
            set = ['Коля', 'Иванов', 'Вавилова 5', Qaorder1pageLocators.INPUT_KRASNOSELSKAYA, '+7911123456',
                  '23.10.24', Qaorder2pageLocators.ONE_DAY_RENT, Qaorder2pageLocators.GREY_COLOR_CHECK_BOX,
                  'Быстрее!']
        elif input_set == 'set_2':
            set = ['Гена', 'Крокодил', 'Болотная 5', Qaorder1pageLocators.INPUT_CHERKIZOVSKAYA, '+7000000111',
                   '23.10.24', Qaorder2pageLocators.TWO_DAYS_RENT, Qaorder2pageLocators.BLACK_COLOR_CHECK_BOX,
                   'Ещё быстрее!']
        order_1 = QaOrder1page(driver)
        order_1.filling_first_page_for_whom_samokat(set[0], set[1], set[2],  set[3], set[4])
        order_2 = QaOrder2page(driver)
        order_2.filling_second_page_about_rent(set[5], set[6], set[7], set[8])
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(Qaorder2pageLocators.ORDER_IS_ACCEPTED_TEXT))


    @allure.feature('test_order_procedure_click_on_logo')
    @allure.description('Позитивный тест. Вход через верхнюю и нижнюю кнопку. Набор данных №1 и №2. Переход по ЛОГО САМОКАТ и ЯНДЕКС.')

    @pytest.mark.parametrize("order_button, input_set, logo_name",
                             [
                                 ('up_button', 'set_1', 'samokat'),
                                 ('bottom_button',  'set_2', 'yandex'),
                                 ('up_button', 'set_2', 'samokat' ),
                                 ('bottom_button', 'set_1', 'yandex' )
                             ]
                             )
    def test_order_procedure_click_on_logo(self, driver, order_button, input_set, logo_name):#'Позитивный тест.
        # Вход через верхнюю и нижнюю кнопку. Набор данных №1 и №2. Переход по ЛОГО САМОКАТ и ЯНДЕКС.'

        order_main = MainPage(driver)
        order_main.go_to_site(Constants.BASE_URL)
        if order_button == 'up_button':
            order_main.click_on_upper_order_button()
        elif order_button == 'bottom_button':
            order_main.click_on_bottom_order_button(driver)

        set = []
        if input_set == 'set_1':
            set = ['Коля', 'Иванов', 'Вавилова 5', Qaorder1pageLocators.INPUT_KRASNOSELSKAYA, '+7911123456',
                  '23.10.24', Qaorder2pageLocators.ONE_DAY_RENT, Qaorder2pageLocators.GREY_COLOR_CHECK_BOX,
                  'Быстрее!']
        elif input_set == 'set_2':
            set = ['Гена', 'Крокодил', 'Болотная 5', Qaorder1pageLocators.INPUT_CHERKIZOVSKAYA, '+7000000111',
                   '23.10.24', Qaorder2pageLocators.TWO_DAYS_RENT, Qaorder2pageLocators.BLACK_COLOR_CHECK_BOX,
                   'Ещё быстрее!']
        order_1 = QaOrder1page(driver)
        order_1.filling_first_page_for_whom_samokat(set[0], set[1], set[2],  set[3], set[4])
        order_2 = QaOrder2page(driver)
        order_2.filling_second_page_about_rent(set[5], set[6], set[7], set[8])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Qaorder2pageLocators.ORDER_IS_ACCEPTED_TEXT))
        order_2.click_see_status_button()#Переход на страницу Статуса заказа
        order_3 = QaOrderStatusPage(driver)
        order_3.find_order_status_2_button()
        if logo_name == 'samokat':
            order_3.click_logo_scooter_status()
            assert WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    MainPageLocators.HOME_HEADER))  # Подтверждение наличия Хедера главной страницы
        elif logo_name == 'yandex':
            order_3.click_logo_yandex_status()
            # time.sleep(5)
            print(driver.current_window_handle)
            print(driver.window_handles)
            tabs = driver.window_handles
            driver.switch_to.window(tabs[1])
            time.sleep(15)
            assert WebDriverWait(driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[text()="Удобный и быстрый Яндекс Браузер с нейросетями"]')))
            # Проверка наличия текста "Удобный и быстрый Яндекс Браузер с нейросетями" на всплывающем окне Яндекса.
            # Работает не стабильно. Сильно зависит от скорости инета.