from selenium.webdriver.common.by import By

class QaorderStatusPageLocators:
    ORDER_STATUS_2_BUTTON = (By.XPATH, "//button[@class='Header_Link__1TAG7' and text()='Статус заказа']")# Кнопка Статус заказа на странице Статус заказа
    TRANSFERE_LOGO_SCOOTER = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")#Переход по ссылке ЛОГО Самокат
    TRANSFERE_LOGO_YANDEX = (By.XPATH, "//a[@href='//yandex.ru']")#Переход по ссылке ЛОГО ЯНДЕКС
    LOGO_ZEN_SYMBOL = (By.ID, "logo_2486--react-icons-branding-logo-svg-react-tsx")
    SHUT_POP_UP_WINDOW_BUTTON = (By.XPATH, 'span[@class=j4ce81622 t8cf1ed06 ad2527f7e i770eea60"]')
    POP_UP_WINDOW_LOGO = (By.XPATH, 'div[@class="of6c95d9f"]')