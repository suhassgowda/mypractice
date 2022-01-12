import pytest
from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage


class CRM025AddMultipleNotes(BrowserSetup):

    @pytest.mark.crm
    @pytest.mark.pascal
    # @pytest.mark.skip
    def test_crm_025_add_multiple_notes(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        first_name = "Client"
        # full_name = "Client " + str(milliseconds)
        sample_notes = "test"
        social_insurance_number = "560 141 111"

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
        # Click on Notes Tab
        self.clientAccounts.click_on_notes_button()
        self.clientAccounts.delete_all_crm_notes()
        # Click on AddNote and add 'Notes' button
        self.clientAccounts.click_add_note()
        self.clientAccounts.type_notes(sample_notes)
        # Click on save notes button
        self.clientAccounts.save_notes()
        # Verify changes saved successfully message is displayed
        self.clientAccounts.verify_successfully_message()
        # Click on view notes button
        self.clientAccounts.view_crm_notes()
        # Verify changes has been reflected in the upcoming added notes
        self.clientAccounts.verify_crm_note(sample_notes)
        self.clientAccounts.delete_crm_notes()

        # Click on AddNote and add 'Notes' button
        self.clientAccounts.click_add_note()
        self.clientAccounts.type_notes(sample_notes)
        # Click on save notes button
        self.clientAccounts.save_notes()
        # Verify changes saved successfully message is displayed
        self.clientAccounts.verify_successfully_message()
        # Click on view notes button
        self.clientAccounts.view_crm_notes()
        # Verify changes has been reflected in the upcoming added notes
        self.clientAccounts.verify_crm_note(sample_notes)
        # Delete crm notes
        self.clientAccounts.delete_crm_notes()
