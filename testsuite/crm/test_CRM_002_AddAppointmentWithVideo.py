import pytest


from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from datetime import datetime, timedelta


class CRM002AddAppointmentWithVideo(BrowserSetup):

    @pytest.mark.crm
    @pytest.mark.pascal
    @pytest.mark.appointments
    # @pytest.mark.skip
    def test_crm_002_add_appointment_with_video(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        tomorrow = datetime.now() + timedelta(1)
        dd = tomorrow.strftime('%d')
        mm = tomorrow.strftime('%m')
        yyyy = tomorrow.strftime('%Y')
        first_name = "Client"
        scheduled_time = "09:30 AM"
        scheduled_duration = "15 Minutes"
        social_insurance_number = "560 141 111"
        self.dashboard = DashboardPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.clientAccounts = ClientsAccountsPage(self.driver)
        self.addAccount = AddAccountPage(self.driver)
        self.loginPage.login_to_application(TestData.ADVISOR, TestData.PASSWORD)
        self.dashboard.verify_login()
        self.dashboard.cancel_all_appointments()
        # Click on clients and accounts button
        self.dashboard.goto_clients_accounts()
        # Create a single client
        self.clientAccounts.search_client_accounts(first_name)
        full_name = self.clientAccounts.open_investor_account(first_name)
        if full_name.__contains__("null"):
            self.clientAccounts.add_single_client(first_name, milliseconds, social_insurance_number,
                                                  "zenq" + str(milliseconds) + "@mailinator.com")
            self.clientAccounts.click_edit_client_details_button()
            self.dashboard.goto_clients_accounts()
            # Search for the client on the 'search bar' and click on client
            self.clientAccounts.search_client_accounts(full_name)
            self.clientAccounts.open_investor_account(full_name)
        # Click On 'CRM' button
        self.clientAccounts.click_crm_tab()
        self.clientAccounts.cancel_all_appointments()
        # Click On 'Add Appointment' button
        self.clientAccounts.click_add_appointment_button()
        self.clientAccounts.verify_video_conference_switch("on")
        # Turn on the Video conference switch
        self.clientAccounts.toggle_video_conference("on")
        # Select a future date in the calender widget
        self.clientAccounts.select_date(yyyy, mm, dd)
        # Set any time in the Time text field
        self.clientAccounts.set_time(scheduled_time)
        # Select the duration from Duration dropdown
        self.clientAccounts.select_duration(scheduled_duration)
        # Write a Note in the Notes textfield
        self.clientAccounts.enter_notes("notes")
        # Click on add client and add multiple clients
        self.clientAccounts.add_client_appointment("client1 Zenq")
        # Click on save appointment button
        self.clientAccounts.click_save_appointment()
        # Verify Changes saved successfully message is displayed in the appointments tab
        self.clientAccounts.verify_changes_saved_successful_message()
        # Verify the selected date is saved in the upcoming appointment tab
        self.clientAccounts.verify_upcoming_date(mm, dd, yyyy)
        # Verify the given time is saved in the upcoming appointment tab
        self.clientAccounts.verify_upcoming_time(scheduled_time)
        # Verify the Note is displayed in upcoming appointment tab
        self.clientAccounts.verify_notes("notes")
        # Verify the duration appears same in the upcoming appointment tab as selected
        self.clientAccounts.verify_time_duration(scheduled_duration)
        # Click on Dashboard button
        self.clientAccounts.click_dashboard()
        # Verify the selected date is saved in  dashboard tab under appointments
        self.dashboard.verify_upcoming_date(mm, dd, yyyy)
        # Verify the given time is saved in the dashboard tab under appointments
        self.dashboard.verify_upcoming_time(scheduled_time)
        # Verify the duration appears same in the dashboard page under appointments
        self.dashboard.verify_time_duration(scheduled_duration)
        # Verify the Note is displayed in the dashboard page under appointments
        self.dashboard.verify_notes("notes")
        # Cancel all the created appointments
        self.dashboard.cancel_all_appointments()
        # self.driver.find_element().is_displayed()
