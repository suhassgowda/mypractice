from selenium.webdriver.common.by import By

from Config import Config
from src.utils.safe_actions import SafeActions


class LoginPage(SafeActions):
    USERNAME = (By.ID, "LoginPage.email-input")
    PASSWORD = (By.ID, "LoginPage.password-input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit']")

    def __init__(self, driver):
        super().__init__(driver)

    def login_to_application(self, username, password):
        """ Method to input username, password and clicks login button"""
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.safe_enter_text(self.USERNAME, username, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.PASSWORD, password, Config.MEDIUM_WAIT)
        self.safe_click(self.LOGIN_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
