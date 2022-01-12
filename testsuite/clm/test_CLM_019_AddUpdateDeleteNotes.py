import pytest

from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage


class CLM019AddUpdateDeleteNotes(BrowserSetup):

    @pytest.mark.clm
    @pytest.mark.pascal
    # @pytest.mark.skip
    def test_clm_019_add_Update_delete_notes(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        first_name = "Client"
        full_name = "Client " + str(milliseconds)
        notes = "test"
        update_notes = "zenq"
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
        self.clientAccounts.add_single_client(first_name, milliseconds, social_insurance_number,
                                              "zenq" + str(milliseconds) + "@mailinator.com")
        self.clientAccounts.click_edit_client_details_button()
        self.dashboard.goto_clients_accounts()
        # Search for the client on the 'search bar' and click on client
        self.clientAccounts.search_client_accounts(full_name)
        self.clientAccounts.open_investor_account(full_name)
        # Add notes
        self.clientAccounts.add_note()
        self.clientAccounts.enter_note(notes)
        # Submit the notes
        self.clientAccounts.submit_notes()
        # Verify successful message
        self.clientAccounts.verify_successfully_message()
        # Verify notes
        self.clientAccounts.verify_client_notes(notes)
        # Update the notes
        self.clientAccounts.edit_notes()
        self.clientAccounts.update_notes(update_notes)
        # Verify updated notes
        self.clientAccounts.submit_notes()
        self.clientAccounts.verify_updated_client_notes(notes)
        self.clientAccounts.delete_notes()
