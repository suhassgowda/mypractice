import pytest

import os
from Config import TestData
from Config.Config import rootPath
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage


class CRM0017UploadMultipleDocuments(BrowserSetup):

    @pytest.mark.crm
    @pytest.mark.pascal
    @pytest.mark.xfail(reason='PAS-522 Add document button is not displayed instead displaying as "No document available yet')
    # @pytest.mark.skip
    def test_crm_017_upload_Multiple_document(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        first_name = "Client"
        full_name = "Client " + str(milliseconds)
        document_name = "pdf_document.pdf"
        social_insurance_number = "560 141 111"

        self.dashboard = DashboardPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.clientAccounts = ClientsAccountsPage(self.driver)
        self.addAccount = AddAccountPage(self.driver)
        self.loginPage.login_to_application(TestData.ADVISOR, TestData.PASSWORD)
        self.dashboard.verify_login()
        # Click on clients and accounts button
        self.dashboard.goto_clients_accounts()
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
        self.clientAccounts.click_documents_button()
        self.clientAccounts.select_document_from_dropdown()
        document_path = os.path.join(rootPath, f"resources/{document_name}")
        self.clientAccounts.upload_document(document_path)
        self.clientAccounts.click_submit_button()
        self.clientAccounts.verify_changes_saved_successful_message()
        self.clientAccounts.verify_document_name(document_name)

        self.clientAccounts.click_documents_button()
        self.clientAccounts.select_document_from_dropdown()
        self.clientAccounts.upload_document(document_path)
        self.clientAccounts.click_submit_button()
        self.clientAccounts.verify_changes_saved_successful_message()
        self.clientAccounts.verify_documents_count(2)
