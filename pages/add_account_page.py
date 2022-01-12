from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Config import Config
from src.base.BrowserSetup import logger
from src.utils.safe_actions import SafeActions


class AddAccountPage(SafeActions):
    PAGE_TITLE = (By.CSS_SELECTOR, "h1[data-testid='PageContentHeader.title']")
    INVESTOR_NAME = (By.CSS_SELECTOR, ".investor-table-body-investor-name-container a")
    ADD_ACCOUNT = (By.CSS_SELECTOR, "[href='/my-accounts/add-account']")
    ACCOUNT_TYPE = (By.CSS_SELECTOR,
                    "[data-testid='AccountTypeDropdown.account-type-dropdown'] .dropdown-list-item-title")
    CLIENTS_ACCOUNTS_LINK = (By.CSS_SELECTOR, "[data-testid='SideNavMenu.clients-link']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-testid*= 'submit-button']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[class*='account-details-continue-button']")
    ACCOUNT_TYPE_DROPDOWN = (By.CSS_SELECTOR, "button[data-testid*='AccountTypeDropdown'] span")
    CURRENCY_TYPE_DROPDOWN = (By.CSS_SELECTOR, "[data-testid*='currency-dropdown.header-button']")
    ACCOUNT_NAME = (By.NAME, "accountName")
    GO_TO_ACCOUNT_DETAILS = (By.CSS_SELECTOR, ".green-button")
    ACCOUNT_CREATED = (By.CSS_SELECTOR, ".success-modal-body h1")
    FORM_ERROR = (By.ID, "form-error")
    SURVIVOR_TYPE = (By.CSS_SELECTOR, "button[data-testid='AddAccountPage.Form.signature-type-select.header-button']")
    SURVIVOR_DROP_DOWN = (By.CSS_SELECTOR, "li[data-testid*='AddAccountPage.Form.signature-type-select.item']")

    def __init__(self, driver):
        super().__init__(driver)

    def open_investor_account(self, name):
        logger.info("open investor account" + name)
        self.wait_until_visible(self.INVESTOR_NAME, Config.LONG_WAIT)
        element_names = self.driver.find_elements_by_css_selector(".investor-table-body-investor-name-container a")
        flag = False
        for element_name in element_names:
            if element_name.text.upper().__contains__(name.upper()):
                element_name.click()
                flag = True
                break
        assert flag, "Investor Account Not found " + name

    def click_element_text(self, element_name):
        logger.info("click element text" + element_name)
        self.wait_until_visible(self.ACCOUNT_TYPE, Config.MEDIUM_WAIT)
        names = self.driver.find_elements_by_css_selector(
            "[data-testid='AccountTypeDropdown.account-type-dropdown'] .dropdown-list-item-title")
        for name in names:  # Second Example
            print(name.text)
            if name.text.upper() == element_name.upper():
                self.driver.execute_script("arguments[0].click();", name)
                break

    def add_account(self):
        self.safe_click(self.ADD_ACCOUNT, Config.MEDIUM_WAIT)
        logger.info("clicked on add account")

    def goto_clients_accounts(self):
        self.safe_click(self.CLIENTS_ACCOUNTS_LINK, Config.MEDIUM_WAIT)
        logger.info(" clicked on client accounts link")

    def select_account_details(self, account_type, account_name, currency):
        logger.info("select Account Name :" + account_name)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.safe_click(self.ACCOUNT_TYPE_DROPDOWN, Config.MEDIUM_WAIT)
        self.click_element_text(account_type)
        self.safe_enter_text(self.ACCOUNT_NAME, account_name, Config.MEDIUM_WAIT)
        self.safe_click(self.CURRENCY_TYPE_DROPDOWN, Config.MEDIUM_WAIT)
        self.driver.find_element_by_id(currency).click()

    def click_add_account_submit_button(self):
        logger.info("click add account submit button")
        self.safe_click(self.SUBMIT_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        try:
            if self.driver.find_element_by_id("form-error").is_displayed():
                message = self.driver.find_element_by_id("form-error").text
                assert False, message
        except NoSuchElementException:
            logger.info("No error found")

    def click_account_details(self):
        logger.info("Click on account details")
        self.safe_click(self.GO_TO_ACCOUNT_DETAILS, Config.MEDIUM_WAIT)

    def verify_account_created(self):
        self.wait_until_visible(self.ACCOUNT_CREATED, Config.MEDIUM_WAIT)
        text = str(self.get_text(self.ACCOUNT_CREATED))
        self.assert_equal(text, "Account created!")
        logger.info("Account Created " + text)

    def select_province_survivor_type(self, survivor_type):
        logger.info("select the province survivor type" + survivor_type)
        self.safe_click(self.SURVIVOR_TYPE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SURVIVOR_DROP_DOWN, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SURVIVOR_DROP_DOWN, survivor_type, Config.MEDIUM_WAIT)
