import pytest

from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage


class CLM003AddInvestmentAccount(BrowserSetup):

    @pytest.mark.crm
    @pytest.mark.pascal
    # @pytest.mark.skip
    def test_clm_003_add_investment_account(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        first_name = "Client"
        # full_name = "Client " + str(milliseconds)
        social_insurance_number = "560 141 111"
        account_name = "zenqtest"
        account_type = "LIRA"
        market_value = "24,486"
        total_market_value = ("$" + market_value)
        currency = "CAD"
        popup_message = "Investment account created"
        message = "Testing_ZenQ"
        confirmation_message = "Report has been sent successfully."
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
        # Delete existing investment
        self.clientAccounts.delete_existing_investment_account()
        # Click add investment button
        self.clientAccounts.click_add_investment_button()
        self.clientAccounts.click_investment_account_button()
        self.clientAccounts.enter_account_name(account_name)
        self.clientAccounts.select_account_type(account_type)
        self.clientAccounts.enter_asset_market_value(market_value)
        # Select currency
        self.clientAccounts.select_currecy(currency)
        self.clientAccounts.click_add_invesment_account_button()
        self.clientAccounts.verify_investment_account_created(popup_message)
        # Go to account details button
        self.clientAccounts.click_goto_account_details_button()
        self.clientAccounts.verify_market_value(total_market_value)
        # Verify account type
        self.clientAccounts.verify_account_type(account_type)
        self.clientAccounts.click_send_to_client_button()
        # Enter message to client
        self.clientAccounts.enter_message_to_client(message)
        self.clientAccounts.click_send_button()
        # Verify successful confirmation message
        self.clientAccounts.verify_report_sent_successfully_message(confirmation_message)
        # Verify sent message
        self.clientAccounts.verify_message_sent(message)
        # Delete investment account
        self.clientAccounts.delete_investment_account()
