from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Config import Config
from src.base.BrowserSetup import logger
from src.utils.safe_actions import SafeActions


class DashboardPage(SafeActions):
    PAGE_TITLE = (By.CSS_SELECTOR, "h1[data-testid='PagecontentHeader.title']")
    INVESTOR_NAME = (By.CSS_SELECTOR, ".investor-table-body-investor-name-container a")
    ACCOUNT_NAME = (By.CLASS_NAME, "investor-dashboard-account-name")
    ADD_ACCOUNT = (By.CSS_SELECTOR, "[href='/my-accounts/add-account']")
    STATUS = (By.CSS_SELECTOR, "h1>p")
    ACCOUNT_TYPE = (By.CSS_SELECTOR,
                    "[data-testid='AccountTypeDropdown.account-type-dropdown'] .dropdown-list-item-title")
    CLIENTS_ACCOUNTS_LINK = (By.CSS_SELECTOR, "[data-testid='SideNavMenu.clients-link']")

    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-testid*= 'submit-button']")
    USER_NAME = (By.CLASS_NAME, "auth-user-name")
    LOGOUT = (By.ID, "logout")
    HEADER = (By.TAG_NAME, "h1")
    DETAILS_TAB = (By.CSS_SELECTOR, ".tab-view-item [href*='kyc']")
    EDIT_BUTTON = (By.CSS_SELECTOR, ".edit-button")
    UPCOMING_DATE = (By.CSS_SELECTOR, "p[data-testid *= '.date']")
    UPCOMING_TIME = (By.CSS_SELECTOR, "p[data-testid*='.duration']")
    TIME_DURATION = (By.CSS_SELECTOR, "p[data-testid*='.duration-text']")
    LOCATION = (By.CSS_SELECTOR, "p[data-testid='AppointmentListRow.item-1.item-0.location-cell.first-line-text']")
    NOTES_APPOINTMENT_TEXT = (By.CLASS_NAME, "appointment-list-item-notes")
    APPOINTMENT_LIST = (By.CSS_SELECTOR, ".upcoming-appointments-list .list-item.appointment-list-item")
    APPOINTMENT_NOTES = (By.CSS_SELECTOR, "p[data-testid*='.appointment-notes']")
    EDIT_APPOINTMENT = (By.CSS_SELECTOR, "button[data-testid*='.edit-button']")
    EDIT_APPOINTMENT_SCREEN = (By.CSS_SELECTOR, "h1[data-testid='PageContentHeader.title']")
    LOCATION_INPUT = (By.CSS_SELECTOR, "[data-testid='AppointmentForm.location-name-input']")
    UPDATE_TIME = (By.CSS_SELECTOR, "input[id='AppointmentForm.time-input.input']")
    DURATION_DROPDOWN = (By.CSS_SELECTOR, "[data-testid='AppointmentForm.duration-dropdown.header-button']")
    DURATION_DROPDOWN_LIST = (By.CSS_SELECTOR, "[data-testid='AppointmentForm.duration-dropdown'] li")
    SAVE_APPOINTMENT = (By.CSS_SELECTOR, "[data-testid='AppointmentForm.submit-button']")
    CHANGES_SAVED_SUCCESSFULLY = (By.CLASS_NAME, "floating-message-text")
    UPDATED_TIME = (By.CSS_SELECTOR, "p[data-testid*='.duration-cell']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "[class*='appointment-list-item-cancel-button']")
    VERIFY_ACCOUNT_TYPE = (By.CSS_SELECTOR, "p[data-testid*='.AccountTypeNameRow.name']")

    NAME_ACCOUNT = (By.CSS_SELECTOR, "p[data-testid*='.account-name']")
    ACCOUNT_OPENING_STATUS = (By.CSS_SELECTOR, "p[data-testid*='descriptive-text']")
    CLIENT_PROFILE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='AuthUserDropdown.header-button']")
    ACCOUNT_NAME_LIST = (By.CSS_SELECTOR, "p[data-testid*='account-name']")
    APPOINTMENTS_BUTTON = (By.CSS_SELECTOR, "span[data-testid*='appointments']")
    SELECTED_ACCOUNT_TYPE = (By.CSS_SELECTOR, "p[data-testid*='AccountTypeNameRow']")

    def __init__(self, driver):
        super().__init__(driver)
        # self.assertion = Assertions(self.driver)

    def get_homepage_title(self):
        """ Method to get home page title"""
        return self.get_title()

    def verify_login(self):
        self.wait_until_visible(self.USER_NAME, Config.MEDIUM_WAIT)
        self.wait_until_visible(self.HEADER, Config.MEDIUM_WAIT)

    def goto_clients_accounts(self):
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        clients_accounts_link = self.driver.find_element_by_css_selector("[data-testid='SideNavMenu.clients-link']")
        self.driver.execute_script("arguments[0].click();", clients_accounts_link)
        self.wait_for_time(Config.MEDIUM_WAIT)

    def open_investor_account(self, name):
        self.safe_click_from_list_of_elements(self.INVESTOR_NAME, name, Config.LONG_WAIT)

    def logout(self):
        self.safe_click(self.USER_NAME, Config.MEDIUM_WAIT)
        self.safe_click(self.LOGOUT, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)

    def select_disclosures_no(self):
        no_buttons = self.driver.find_elements_by_css_selector("[value='no']")
        for button in no_buttons:
            self.driver.execute_script("arguments[0].click();", button)

    def click_submit_button(self):
        self.safe_click(self.SUBMIT_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)

    def click_details_tab(self):
        self.safe_click(self.DETAILS_TAB, Config.MEDIUM_WAIT)

    def click_edit_button(self):
        self.safe_click(self.EDIT_BUTTON, Config.MEDIUM_WAIT)

    def verify_account_status(self, status):
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.wait_until_visible(self.STATUS, Config.MEDIUM_WAIT)
        text = str(self.get_text(self.STATUS))
        self.assert_contains(text, status)
        logger.info(f"Account status as {status} is verified")

    def select_risk_exposure(self, time_horizon, criticality, use_of_account):
        self.wait_for_time(Config.SHORT_WAIT)
        wait = WebDriverWait(self.driver, Config.MEDIUM_WAIT)
        from selenium.webdriver.support import expected_conditions as ec
        wait.until(ec.presence_of_element_located(self.HEADER))
        q1 = self.driver.find_elements_by_css_selector(".time_horizon li label")
        for option1 in q1:
            if option1.text.__contains__(time_horizon):
                option1.click()
                break

        q2 = self.driver.find_elements_by_css_selector(".criticality label .radio-input-icon+p")
        self.driver.execute_script("arguments[0].scrollIntoView();", q2[0])
        # print(str(len(q2)))
        for option2 in q2:
            # print(option2.text)
            if option2.text.__contains__(criticality):
                # option2.click()
                self.driver.execute_script("arguments[0].click();", option2)
                break

        q3 = self.driver.find_elements_by_css_selector(".intended_use_of_account label")
        # print(str(len(q3)))
        for option3 in q3:
            print(option3.text)
            if option3.text.__contains__(use_of_account):
                self.driver.execute_script("arguments[0].click();", option3)
                break

    def open_account(self, account_name):
        self.driver.refresh()
        self.wait_for_time(Config.SHORT_WAIT)
        wait = WebDriverWait(self.driver, Config.LONG_WAIT)
        from selenium.webdriver.support import expected_conditions as ec
        wait.until(ec.visibility_of_element_located(self.ACCOUNT_NAME))
        element_names = self.driver.find_elements_by_class_name("investor-dashboard-account-name")
        flag = False
        # print(str(len(element_names)))
        for element_name in element_names:  # Second Example
            logger.info("Account Names found")
            logger.info(element_name.text)
            if element_name.text.upper().__contains__(account_name.upper()):
                element_name.click()
                flag = True
                break
        assert flag, "Account Not found " + account_name

    def verify_upcoming_date(self, mm, dd, yyyy):
        from datetime import datetime
        month_num = mm
        datetime_object = datetime.strptime(month_num, "%m")
        month_name = datetime_object.strftime("%b")
        if str(dd).startswith("0"):
            dd = dd[1:]
        actual_date = f"{month_name} {dd}, {yyyy}"
        expected_date = self.get_text(self.UPCOMING_DATE)
        self.assert_equal(actual_date, expected_date)

    def verify_upcoming_time(self, scheduled_time):
        expected_time = scheduled_time
        actual_time = self.get_text(self.UPCOMING_TIME)
        self.assert_equal(actual_time, expected_time)

    def verify_time_duration(self, duration):
        actual_time_duration = duration
        expected_time_duration = self.get_text(self.TIME_DURATION)
        self.assert_equal(actual_time_duration, expected_time_duration)

    def verify_location(self, location):
        actual_location = location
        expected_location = self.get_text(self.LOCATION)
        self.assert_equal(actual_location, expected_location)

    def verify_notes(self, notes):
        expected_notes_duration = notes
        actual_notes_duration = self.get_text(self.NOTES_APPOINTMENT_TEXT)
        self.assert_equal(actual_notes_duration, expected_notes_duration)

    def click_edit_appointment(self):
        # action = ActionChains(driver)
        # element = self.driver.find_element(*self.EDIT_APPOINTMENT)
        # action.move_to_element(element).click().perform()
        self.safe_click(self.APPOINTMENT_NOTES, Config.VERY_SHORT_WAIT)
        self.safe_click(self.EDIT_APPOINTMENT, Config.MEDIUM_WAIT)

    def verify_edit_appointment_screen(self):
        self.wait_until_visible(self.EDIT_APPOINTMENT_SCREEN, Config.MEDIUM_WAIT)

    def update_location(self, add_location):
        self.safe_enter_text(self.LOCATION_INPUT, add_location, Config.MEDIUM_WAIT)

    def clear_time(self):
        self.safe_enter_text(self.UPDATE_TIME, "10:30 AM", Config.VERY_SHORT_WAIT)
        self.safe_click(self.DURATION_DROPDOWN, Config.MEDIUM_WAIT)

    def update_time(self, update_time, ):
        self.safe_enter_text(self.UPDATE_TIME, update_time, Config.VERY_SHORT_WAIT)

    def update_time_duration(self, update_time_duration):
        self.safe_click(self.DURATION_DROPDOWN, Config.MEDIUM_WAIT)
        wait = WebDriverWait(self.driver, Config.LONG_WAIT)
        from selenium.webdriver.support import expected_conditions as ec
        wait.until(ec.presence_of_all_elements_located(self.DURATION_DROPDOWN_LIST))
        element_names = self.driver.find_elements_by_css_selector(
            "[data-testid='AppointmentForm.duration-dropdown'] li")
        for element_name in element_names:
            if element_name.text.upper().__contains__(update_time_duration.upper()):
                element_name.click()
                break

    def click_save_appointment(self):
        self.safe_click(self.SAVE_APPOINTMENT, Config.MEDIUM_WAIT)

    def verify_successfully_message(self):
        expected_message = "Changes saved successfully!"
        actual_message = self.get_text(self.CHANGES_SAVED_SUCCESSFULLY)
        self.assert_equal(expected_message, actual_message)

    def verify_updated_duration(self, updated_duration):
        actual_time_duration = updated_duration
        expected_time_duration = self.get_text(self.TIME_DURATION)
        self.assert_equal(actual_time_duration, expected_time_duration)

    def verify_updated_time(self, updated_time):
        actual_time_duration = updated_time
        expected_time_duration = self.get_text(self.UPDATED_TIME)
        self.assert_equal(actual_time_duration, expected_time_duration)

    def verify_updated_location(self, updated_location):
        expected_updated_location = updated_location
        actual_updated_location = self.get_text(self.LOCATION)
        self.assert_equal(expected_updated_location, actual_updated_location)

    def cancel_all_appointments(self):
        if self.is_element_displayed((By.CSS_SELECTOR, ".button.panel-footer-button")):
            self.driver.find_element(*(By.CSS_SELECTOR, ".button.panel-footer-button")).click()
        value = self.safe_wait_for_presence_of_all_elements_located(self.APPOINTMENT_LIST, Config.SHORT_WAIT)
        if value:
            elements = self.driver.find_elements(*self.APPOINTMENT_LIST)
            if self.is_element_displayed(self.APPOINTMENT_LIST):
                if len(elements) == 1:
                    self.safe_click(self.APPOINTMENT_LIST, Config.VERY_SHORT_WAIT)
                    self.safe_js_click(self.CANCEL_BUTTON, Config.MEDIUM_WAIT)
                else:
                    for element in elements:
                        self.safe_click(self.APPOINTMENT_LIST, Config.VERY_SHORT_WAIT)
                        self.safe_js_click(self.CANCEL_BUTTON, Config.MEDIUM_WAIT)
                        self.wait_for_time(2)

    def verify_client_name(self, account_name):
        self.wait_until_visible(self.HEADER, Config.MEDIUM_WAIT)
        expected_name = account_name
        actual_name = self.get_text(self.NAME_ACCOUNT)
        self.assert_equal(expected_name, actual_name)

    def verify_account_opening_status(self, account_opening_status):
        self.wait_until_visible(self.ACCOUNT_OPENING_STATUS, Config.MEDIUM_WAIT)
        expected_status_name = account_opening_status
        actual_status_name = self.get_text(self.ACCOUNT_OPENING_STATUS)
        self.assert_equal(expected_status_name, actual_status_name)

    def logout_from_client_account(self):
        self.wait_for_time(Config.MEDIUM_WAIT)
        self.safe_click(self.CLIENT_PROFILE_BUTTON, Config.VERY_SHORT_WAIT)
        self.safe_click(self.LOGOUT, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)

    def verify_onboarding_account_type(self, account_type):
        expected_name = account_type
        actual_name = self.get_text(self.VERIFY_ACCOUNT_TYPE)
        self.assert_equal(expected_name, actual_name)

    def click_account_created(self, account_name):
        self.driver.refresh()
        self.wait_for_time(Config.SHORT_WAIT)
        wait = WebDriverWait(self.driver, Config.LONG_WAIT)
        from selenium.webdriver.support import expected_conditions as ec
        wait.until(ec.visibility_of_element_located(self.ACCOUNT_NAME_LIST))
        element_names = self.driver.find_elements_by_class_name("p[data-testid*='account-name']")
        flag = False
        # print(str(len(element_names)))
        for element_name in element_names:  # Second Example
            logger.info("Account Names found")
            logger.info(element_name.text)
            if element_name.text.upper().__contains__(account_name.upper()):
                element_name.click()
                flag = True
                break
        assert flag, "Account Not found " + account_name

    def click_appointments(self):
        self.safe_click(self.APPOINTMENTS_BUTTON, Config.SHORT_WAIT)