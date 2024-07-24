import time

import allure
import pytest
from selenium.webdriver.common.by import By

from conftest import driver
from locators.constants import Constants
from locators.main_page_locators import  MainPageLocators
from pages import main_page
from pages.base_page import BasePage
from pages.main_page import  MainPage


class TestQaSamokat:

    @allure.feature('test_samokat_main_page_questions')
    @allure.description('Проверка "Вопросы о важном": когда нажимаешь на стрелку c вопросом, открывается нужный  текст')
    @pytest.mark.parametrize("question_num, expected_result",
                             [
                                 (0, Constants.ANSWER_1_TEXT),
                                 (1, Constants.ANSWER_2_TEXT),
                                 (2, Constants.ANSWER_3_TEXT),
                                 (3, Constants.ANSWER_4_TEXT),
                                 (4, Constants.ANSWER_5_TEXT),
                                 (5, Constants.ANSWER_6_TEXT),
                                 (6, Constants.ANSWER_7_TEXT),
                                 (7, Constants.ANSWER_8_TEXT)

                             ]
                             )
    def test_samokat_main_page_questions(self, driver, question_num, expected_result):
        main_page1 = MainPage(driver)
        main_page1.go_to_site(Constants.BASE_URL)
        #time.sleep(1)
        actual_result = main_page1.click_question_get_answer(question_num, driver)
        #time.sleep(1)
        assert main_page1.check_answer(actual_result, expected_result)


