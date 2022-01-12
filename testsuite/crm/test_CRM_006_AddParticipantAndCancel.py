import pytest

from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage


class CRM006AddParticipantAndCancel(BrowserSetup):

    @pytest.mark.crm
    @pytest.mark.pascal
    # @pytest.mark.skip
    def test_crm_006_add_Participant_Cancel(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        first_name = "Client"
        # full_name = "Client "
        colleague_name = "Kelly Doyle"
        subject = "New Conversation"
        message = "Testing"
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
        # Click On chats and new Conversation button
        self.clientAccounts.click_chats_new_conversation()
        # Select the Colleague name from dropdown
        self.clientAccounts.select_colleague_name(colleague_name)
        # Write a subject in the 'Subject' text field
        self.clientAccounts.enter_subject(subject)
        # Write a message in the 'Message' text field
        self.clientAccounts.enter_message(message)
        # Click on Submit button
        self.clientAccounts.submit_conversation()
        # Advisor should navigate to 'Inbox' Tab
        self.clientAccounts.verify_inbox_screen()
        # Verify the given subject is reflected  in the conversation
        self.clientAccounts.verify_subject(subject)
        # Verify the given Message is reflected in the conversation
        self.clientAccounts.verify_message(message)
        # CLick on add recipient button
        self.clientAccounts.add_recipient()
        # Verify new recipient screen has been displayed
        self.clientAccounts.verify_add_recipient_window()
        # click on cancel button in the recipient window
        self.clientAccounts.cancel_recipient_window()
        # Verify advisor navigated back to inbox screen
        self.clientAccounts.verify_inbox_screen()
