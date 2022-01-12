import pytest

import os
from Config import TestData
from Config.Config import rootPath
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage


class CLM001AddBankAccountCurrencyCAD(BrowserSetup):

    @pytest.mark.clm
    @pytest.mark.pascal
    @pytest.mark.xfail(reason='PAS-525 Error message is displayed as something went wrong when clicked on upload document')
    # @pytest.mark.skip
    def test_clm_001_add_bank_account_currency_cad(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        full_name = "Client " + str(milliseconds)
        first_name = "client"
        social_insurance_number = "560 141 111"
        currency = "CAD"
        added_message = "Account Successfully Added!"
        document_name = "pdf_document.pdf"
        institution_number = "003"
        branch_code = "42545"
        account_number = "424242545454"
        self.dashboard = DashboardPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.clientAccounts = ClientsAccountsPage(self.driver)
        self.addAccount = AddAccountPage(self.driver)

        self.loginPage.login_to_application(TestData.ADVISOR, TestData.PASSWORD)
        self.dashboard.verify_login()
        self.dashboard.goto_clients_accounts()
        self.clientAccounts.add_single_client(first_name, milliseconds, social_insurance_number,
                                              "zenq" + str(milliseconds) + "@mailinator.com")
        self.clientAccounts.click_edit_client_details_button()
        self.dashboard.goto_clients_accounts()
        # Search for the client on the 'search bar' and click on client
        self.clientAccounts.search_client_accounts(full_name)
        self.clientAccounts.open_investor_account(full_name)
        self.clientAccounts.click_add_bank_account_button()
        # Enter bank details
        self.clientAccounts.enter_bank_details(institution_number, branch_code, account_number)
        self.clientAccounts.select_currecy(currency)
        document_path = os.path.join(rootPath, f"resources/{document_name}")
        # Upload void cheque
        self.clientAccounts.upload_void_cheque(document_path)
        self.clientAccounts.click_submit_button()
        # Verify added account successfully
        self.clientAccounts.verify_account_added_successfully(added_message)
        self.clientAccounts.click_close_button()
        # Verify currency
        self.clientAccounts.verify_currency(currency)
