import pytest

from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage


class CLM033AddAccountTypeRRIF(BrowserSetup):

    @pytest.mark.clm
    @pytest.mark.pascal
    # @pytest.mark.skip
    def test_clm_033_add_Account_rrif_type(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        account_name = "ZenTest_" + str(milliseconds)
        # account_name = "ZenTest_1622531522485"
        full_name = "Client " + str(milliseconds)
        account_type = "RRIF"
        first_name = "client"
        social_insurance_number = "560 141 111"
        currency = "CAD"
        rif_based_on = "Account holder’s age"
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
        self.clientAccounts.click_accounts_tab()
        self.clientAccounts.click_add_account_button()
        self.clientAccounts.select_open_account_type(account_type)
        self.clientAccounts.enter_account_name(account_name)
        self.clientAccounts.select_currecy(currency)
        self.clientAccounts.select_rip_calulation_based_on(rif_based_on)
        self.clientAccounts.click_submit_button()
        self.clientAccounts.click_goto_account_details_button()
        self.clientAccounts.verify_account_type(account_type)

