import pytest

from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage


class VerifyClientESigningDocuments(BrowserSetup):

    # @pytest.mark.pascal
    @pytest.mark.skip
    def test_001_esign_documents(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        account_name = "ZenTest_" + str(milliseconds)
        # account_name = "ZenTest_1622531522485"
        self.dashboard = DashboardPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.clientAccounts = ClientsAccountsPage(self.driver)
        self.addAccount = AddAccountPage(self.driver)

        self.loginPage.login_to_application(TestData.ADVISOR, TestData.PASSWORD)
        self.dashboard.verify_login()
        self.dashboard.goto_clients_accounts()
        self.dashboard.open_investor_account(TestData.INVESTOR_ACCOUNT)
        self.clientAccounts.click_accounts_tab()
        self.clientAccounts.click_add_account_button()

        self.addAccount.select_account_details(TestData.ACCOUNT_TYPE, account_name, TestData.CURRENCY)
        self.addAccount.click_add_account_submit_button()
        self.addAccount.verify_account_created()
        self.addAccount.click_account_details()
        self.dashboard.click_details_tab()
        self.dashboard.click_edit_button()

        self.dashboard.select_risk_exposure(TestData.TIME_HORIZON, TestData.CRITICALITY, TestData.USE_OF_ACCOUNT)
        self.dashboard.select_disclosures_no()
        self.dashboard.click_submit_button()
        self.dashboard.logout()

        self.loginPage.login_to_application(TestData.CLIENT, TestData.PASSWORD)
        self.dashboard.verify_login()
        self.dashboard.open_account(account_name)
        self.dashboard.click_details_tab()
        # self.driver.get("https://marksman.staging.pascalfinancial.com/my-accounts/3401818555604211295/kyc")
        self.clientAccounts.sign_all_documents()
        self.clientAccounts.verify_account_status("In Review")
        self.dashboard.logout()
        self.loginPage.login_to_application(TestData.ADVISOR, TestData.PASSWORD)
        self.dashboard.verify_login()
        self.dashboard.goto_clients_accounts()
        self.dashboard.open_investor_account(TestData.INVESTOR_ACCOUNT)
        self.clientAccounts.click_accounts_tab()
        self.clientAccounts.open_account(account_name)
        self.clientAccounts.click_on_provide_guidelines()
        self.clientAccounts.select_asset_category()
        self.clientAccounts.select_alternative_rule()
        self.clientAccounts.set_allocation_limits(TestData.MIN_ALLOCATION, TestData.MAX_ALLOCATION)
        self.clientAccounts.click_apply()
        self.clientAccounts.click_approve()
        self.clientAccounts.verify_account_status("In Progress")
        self.clientAccounts.verify_account_opening_status_msg("Account is being processed by the custodian.")
