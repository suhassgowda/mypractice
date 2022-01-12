import pytest

from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage


class CRM014UpdateTheExistingNoteAndDelete(BrowserSetup):

    @pytest.mark.crm
    @pytest.mark.pascal
    # @pytest.mark.skip
    def test_crm_014_update_the_existing_note_and_delete(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        first_name = "Client"
        # full_name = "Client " + str(milliseconds)
        social_insurance_number = "560 141 111"
        sample_note = "Testing"
        tab_name = "Update Note"
        updated_note = "ZenQ Testing C1"
        popup = "Are you sure?"
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
        # Click on AddNote and add 'Notes'
        self.clientAccounts.click_add_note()
        self.clientAccounts.type_notes(sample_note)
        # Click on save button
        self.clientAccounts.save_notes()
        # Verify changes saved successfully message is displayed
        self.clientAccounts.verify_changes_saved_successful_message()
        # Click on 'View Note' button , click on edit button
        self.clientAccounts.view_crm_notes()
        self.clientAccounts.click_edit_button()
        # Verify advisor navigates to Update Note tab
        self.clientAccounts.verify_update_note_tab(tab_name)
        # Enter 'Notes' in the notes field and click on update button
        self.clientAccounts.clear_update_note(updated_note)
        self.clientAccounts.click_update_button()
        # Verify changes saved successfully message is displayed
        self.clientAccounts.verify_changes_saved_successful_message()
        # Verify changes has been reflected in the notes tab
        self.clientAccounts.verify_updated_note(updated_note)
        # Click on delete button
        self.clientAccounts.click_delete_note()
        # Verify if Verification popup window saying 'Are you sure?' is displayed
        self.clientAccounts.verify_confirmation_popup(popup)
        # Click on 'Cancel' button
        self.clientAccounts.click_cancel_button()
        # Click on delete button and click on 'Yes I want to delete' button
        self.clientAccounts.click_delete_note_confirm()
        # Verify changes saved successfully message is displayed
        self.clientAccounts.verify_changes_saved_successful_message()
