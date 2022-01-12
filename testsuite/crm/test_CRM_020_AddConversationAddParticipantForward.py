import pytest

import os
from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from Config.Config import rootPath


class CRM020AddConversationAddParticipantForward(BrowserSetup):

    @pytest.mark.crm
    @pytest.mark.pascal
    @pytest.mark.xfail(reason='PAS-524 Error message is displayed as something went wrong when we upload attachment')
    # @pytest.mark.skip
    def test_crm_020_add_conversation_add_participant_forward(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        first_name = "Client"
        colleague_name = "Kelly Doyle"
        subject = "New Conversation"
        document_name = "pdf_document.pdf"
        message = "Testing"
        new_message = "Test_message"
        social_insurance_number = "560 141 111"
        new_colleague_name = "Mark Doyle"
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
        # Click on 'Add attachment ' and add attachment
        document_path = os.path.join(rootPath, f"resources/{document_name}")
        self.clientAccounts.click_add_attachment(document_path)
        # Click on Submit button
        self.clientAccounts.submit_conversation()
        # Advisor should navigate to 'Inbox' Tab
        self.clientAccounts.verify_inbox_screen()
        # Verify the given subject is reflected  in the conversation
        self.clientAccounts.verify_subject(subject)
        # Verify the given Message is reflected in the conversation
        self.clientAccounts.verify_message(message)
        self.clientAccounts.verify_attachment_name(document_name)
        self.clientAccounts.click_add_participant_button()
        # Select the Colleague name from dropdown
        self.clientAccounts.select_colleague_name(new_colleague_name)
        self.clientAccounts.enter_message(new_message)
        self.clientAccounts.click_forward_button()
