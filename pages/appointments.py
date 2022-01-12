from selenium.webdriver.common.by import By
from Config import Config
from src.utils.safe_actions import SafeActions


class Appointments(SafeActions):
    UPCOMING_DATE = (By.CSS_SELECTOR, "p[data-testid *= '.date']")
    UPCOMING_TIME = (By.CSS_SELECTOR, "p[data-testid*='.duration']")
    TIME_DURATION = (By.CSS_SELECTOR, "p[data-testid*='.duration-text']")
    LOCATION = (By.CSS_SELECTOR, "p[data-testid='AppointmentListRow.item-1.item-0.location-cell.first-line-text']")
    NOTES_APPOINTMENT_TEXT = (By.CLASS_NAME, "appointment-list-item-notes")
    USER_NAME = (By.CLASS_NAME, "auth-user-name")
    LOGOUT = (By.ID, "logout")

    def __init__(self, driver):
        super().__init__(driver)

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

    def logout(self):
        self.safe_click(self.USER_NAME, Config.MEDIUM_WAIT)
        self.safe_click(self.LOGOUT, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
