import pytest
from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from datetime import datetime, timedelta


class CRM012AddAppointmentWithVideoForProspect(BrowserSetup):

    @pytest.mark.crm
    @pytest.mark.pascal
    @pytest.mark.appointments
    # @pytest.mark.skip
    def test_crm_012_add_appointment_with_video_for_prospect(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        tomorrow = datetime.now() + timedelta(1)
        dd = tomorrow.strftime('%d')
        mm = tomorrow.strftime('%m')
        YYYY = tomorrow.strftime('%Y')
        date = datetime.utcnow()
        yyyy = date.strftime('2000')
        first_name = "Prospect"
        # full_name = "client 1627
        full_name = "Prospect " + str(milliseconds)
        scheduled_time = "09:30 AM"
        scheduled_duration = "15 Minutes"
        self.dashboard = DashboardPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.clientAccounts = ClientsAccountsPage(self.driver)
        self.addAccount = AddAccountPage(self.driver)
        self.loginPage.login_to_application(TestData.ADVISOR, TestData.PASSWORD)
        self.dashboard.verify_login()
        self.dashboard.cancel_all_appointments()
        # Click on clients and accounts button
        self.dashboard.goto_clients_accounts()
        self.clientAccounts.add_single_prospect(first_name, milliseconds, "zenq" + str(milliseconds) + "@mailinator.com", yyyy, mm, dd)
        self.clientAccounts.click_edit_prospect_details()
        self.dashboard.goto_clients_accounts()
        self.clientAccounts.search_client_accounts(full_name)
        self.clientAccounts.open_investor_account(full_name)
        # Click on 'CRM' button
        self.clientAccounts.click_crm_tab()
        self.clientAccounts.cancel_all_appointments()
        # Click On 'Add Appointment' button
        self.clientAccounts.click_add_appointment_button()
        self.clientAccounts.verify_video_conference_switch("on")
        # Turn on the Video conference switch
        self.clientAccounts.toggle_video_conference("on")
        # Select a future date in the calender widget
        self.clientAccounts.select_date(YYYY, mm, dd)
        # Set any time in the Time text field
        self.clientAccounts.set_time(scheduled_time)
        # Select the duration from Duration dropdown
        self.clientAccounts.select_duration(scheduled_duration)
        # Write a Note in the Notes textfield
        self.clientAccounts.enter_notes("notes")
        # Click on add client and add multiple clients
        self.clientAccounts.add_client_appointment("Prospect")
        # Click on save appointment button
        self.clientAccounts.click_save_appointment()
        # Verify Changes saved successfully message is displayed in the appointments tab
        self.clientAccounts.verify_changes_saved_successful_message()
        # Verify the selected date is saved in the upcoming appointment tab
        self.clientAccounts.verify_upcoming_date(mm, dd, YYYY)
        # Verify the given time is saved in the upcoming appointment tab
        self.clientAccounts.verify_upcoming_time(scheduled_time)
        # Verify the duration appears same in the upcoming appointment tab as selected
        self.clientAccounts.cancel_all_appointments()
        # self.driver.find_element().is_displayed()
