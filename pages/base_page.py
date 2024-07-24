from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element_located(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')


    def scroll_to_element_located(self, driver, locator):
        element = self.find_element_located(locator)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')

    def click_on_element_located(self , locator):
        element = self.find_element_located(locator)
        element.click()

    def get_text_from_element_located(self, locator):
        return self.find_element_located(locator).text

    def set_text_to_element_located(self, locator, text):
        element = self.find_element_located(locator)
        return element.send_keys(text)

