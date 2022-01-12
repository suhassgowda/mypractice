from selenium.webdriver.common.by import By
from Config import Config
from src.base.BrowserSetup import logger
from src.utils.safe_actions import SafeActions


class MailinatorPage(SafeActions):

    ENTER_MAILINATOR_INBOX = (By.ID, "addOverlay")
    GO = (By.ID, "go-to-public")
    OPEN_INVESTOR_MAIL = (By.CSS_SELECTOR, "tr[id*='row']")
    REGISTRATION = (By.XPATH, "//*[text()='Register']")
    REGISTER_FRAME = "html_msg_body"
    INVESTOR_EMAIL = (By.CSS_SELECTOR, "dd[data-testid*='.email.description']")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_mailinator_email(self, url):
        email = self.get_text(self.INVESTOR_EMAIL)
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(url)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.safe_enter_text(self.ENTER_MAILINATOR_INBOX, email, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.safe_click(self.GO, Config.MEDIUM_WAIT)

    def click_public_message(self):
        logger.info("Enter into mailinator ")
        self.wait_until_visible(self.OPEN_INVESTOR_MAIL, Config.VERY_SHORT_WAIT)
        self.safe_click(self.OPEN_INVESTOR_MAIL, Config.MEDIUM_WAIT)

    def click_registration(self):
        logger.info("click registration")
        self.driver.switch_to.frame(self.REGISTER_FRAME)
        self.safe_click(self.REGISTRATION, Config.MEDIUM_WAIT)
