import pytest

from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from datetime import datetime, timedelta


class CRM009updateAddAppointmentWithoutVideo(BrowserSetup):

    @pytest.mark.crm
    @pytest.mark.pascal
    @pytest.mark.appointments
    # @pytest.mark.skip
    def test_crm_009_update_appointment_without_video(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        tomorrow = datetime.now() + timedelta(1)
        dd = tomorrow.strftime('%d')
        mm = tomorrow.strftime('%m')
        yyyy = tomorrow.strftime('%Y')
        first_name = "Client"
        scheduled_time = "09:30 AM"
        scheduled_duration = "15 Minutes"
        location_name = "Toronto"
        add_location = " ,paris"
        updated_location = "Toronto ,paris"
        social_insurance_number = "560 141 111"
        updated_duration = "30 Minutes"
        updated_time = "10:30 AM"

        self.dashboard = DashboardPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.clientAccounts = ClientsAccountsPage(self.driver)
        self.addAccount = AddAccountPage(self.driver)
        self.loginPage.login_to_application(TestData.ADVISOR, TestData.PASSWORD)
        self.dashboard.verify_login()
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
        # Turn off the Video conference switch
        self.clientAccounts.toggle_video_conference("off")
        # Select a future date in the calender widget
        self.clientAccounts.select_date(yyyy, mm, dd)
        # Set any time in the Time text field
        self.clientAccounts.set_time(scheduled_time)
        # Select the duration from Duration dropdown
        self.clientAccounts.select_duration(scheduled_duration)
        # Write a Note in the Notes textfield
        self.clientAccounts.enter_notes("notes")
        # Write location in the 'location' text field
        self.clientAccounts.set_location(location_name)
        # Click on save appointment button
        self.clientAccounts.click_save_appointment()
        # Verify Changes saved successfully message is displayed in the appointments tab
        self.clientAccounts.verify_changes_saved_successful_message()
        # Verify the selected date is saved in the upcoming appointment tab
        self.clientAccounts.verify_upcoming_date(mm, dd, yyyy)
        # Verify the given time is saved in the upcoming appointment tab
        self.clientAccounts.verify_upcoming_time(scheduled_time)
        # Verify the duration appears same in the upcoming appointment tab as selected
        self.clientAccounts.verify_time_duration(scheduled_duration)
        # Verify the location in upcoming appointment tab
        self.clientAccounts.verify_location(location_name)
        # Verify the notes in upcoming appointment tab
        self.clientAccounts.verify_notes("notes")
        # Advisor navigates to edit screen
        self.clientAccounts.click_edit_appointment()
        # verify edit appointment screen
        self.clientAccounts.verify_edit_appointment_screen()
        # enter location
        self.clientAccounts.update_location(add_location)
        self.clientAccounts.clear_time()
        # enter the  time
        self.clientAccounts.update_time(updated_time)
        # enter the time duration
        self.clientAccounts.select_duration(updated_duration)
        # save the changes
        self.clientAccounts.click_save_appointment()
        # Verify Changes saved successfully message is displayed in the appointments tab
        self.clientAccounts.verify_changes_saved_successful_message()
        # verify the updated duration
        self.clientAccounts.verify_updated_duration(updated_duration)
        # verify the updated time
        self.clientAccounts.verify_updated_time(updated_time)
        # verify the updated location
        self.clientAccounts.verify_updated_location(updated_location)
        # Click on Dashboard button
        self.clientAccounts.click_dashboard()
        # Advisor navigates to edit screen
        self.dashboard.click_edit_appointment()
        # verify edit appointment screen
        self.dashboard.verify_edit_appointment_screen()
        self.dashboard.clear_time()
        # enter the  time
        self.dashboard.update_time(updated_time)
        # enter the time duration
        self.dashboard.update_time_duration(updated_duration)
        # save the changes
        self.dashboard.click_save_appointment()
        # Verify Changes saved successfully message is displayed in the appointments tab
        self.dashboard.verify_successfully_message()
        # verify the updated duration
        self.dashboard.verify_updated_duration(updated_duration)
        # verify the updated time
        self.dashboard.verify_updated_time(updated_time)
        # cancel all the created appointments
        self.dashboard.cancel_all_appointments()
