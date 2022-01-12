import pytest

from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage


class CLM021AddAccountWithJointOpen(BrowserSetup):

    @pytest.mark.pascal
    @pytest.mark.clm
    # @pytest.mark.skip
    def test_clm_021_add_account_with_joint_open(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        account_name = "ZenTest_" + str(milliseconds)
        account_type = "Joint Open"
        first_name = "client5"
        social_insurance_number = "560 141 111"
        currency = "CAD"
        survivor_type = "Rights Of Survivorship"
        self.dashboard = DashboardPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.clientAccounts = ClientsAccountsPage(self.driver)
        self.addAccount = AddAccountPage(self.driver)

        self.loginPage.login_to_application(TestData.ADVISOR, TestData.PASSWORD)
        self.dashboard.verify_login()
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
        # Click accounts tab
        self.clientAccounts.click_accounts_tab()
        # Add new account type
        self.clientAccounts.click_add_account_button()
        self.clientAccounts.select_account_type(account_type)
        self.clientAccounts.enter_account_name(account_name)
        self.clientAccounts.select_currency(currency)
        self.addAccount.select_province_survivor_type(survivor_type)
        self.clientAccounts.click_submit_button()
        # Go to client details
        self.clientAccounts.click_goto_account_details_button()
        # Verify created account type
        self.clientAccounts.verify_account_type(account_type)

