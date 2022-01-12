import pytest

from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from src.pages.client_registration_page import ClientRegistrationPage
from src.pages.mailinator_page import MailinatorPage


class CLM020SelectCategoryAddInvestor(BrowserSetup):

    @pytest.mark.clm
    @pytest.mark.pascal
    # @pytest.mark.skip
    def test_clm_020_select_category_add_investor(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        first_name = "Client"
        full_name = "Client " + str(milliseconds)
        social_insurance_number = "560 141 111"
        select_category = "Adventurer"
        investment_knowledge = "Novice"
        risk_score = "50"
        dynamic_range = "2 - 100"
        input_message = "Test"
        update_input_message = "testing"
        updated_input_message = "Testtesting"
        self.dashboard = DashboardPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.clientAccounts = ClientsAccountsPage(self.driver)
        self.clientRegistration = ClientRegistrationPage(self.driver)
        self.mailinator = MailinatorPage(self.driver)
        self.addAccount = AddAccountPage(self.driver)
        self.loginPage.login_to_application(TestData.ADVISOR, TestData.PASSWORD)
        self.dashboard.verify_login()
        # Click on clients and accounts button
        self.dashboard.goto_clients_accounts()
        # Create a single client
        self.clientAccounts.add_single_client(first_name, milliseconds, social_insurance_number,
                                              "zenq" + str(milliseconds) + "@mailinator.com")
        self.clientAccounts.click_edit_client_details_button()
        self.dashboard.goto_clients_accounts()
        # Search for the client on the 'search bar' and click on client
        self.clientAccounts.search_client_accounts(full_name)
        self.clientAccounts.open_investor_account(full_name)
        # Click on define results manually
        self.clientAccounts.click_define_results_manually()
        # Add Investor EQ
        self.clientAccounts.select_investor_list(select_category)
        self.clientAccounts.click_risk_score()
        self.clientAccounts.click_dynamic_risk_score()
        self.clientAccounts.select_investment_knowledge(investment_knowledge)
        self.clientAccounts.submit_investor_details()
        # Verify successful message
        self.clientAccounts.verify_successfully_message()
        # Verify investor selector category
        self.clientAccounts.verify_investor(select_category)
        # Verify risk score
        self.clientAccounts.verify_risk_score(risk_score)
        # Verify dynamic range
        self.clientAccounts.verify_dynamic_range(dynamic_range)
        # Click send investor
        self.clientAccounts.click_send_investor()
        # Enter note message
        self.clientAccounts.enter_note_message(input_message)
        self.clientAccounts.submit_send_investor_message()
        self.clientAccounts.go_to_bank_details()
        # Verify investor notes
        self.clientAccounts.verify_investor_notes(input_message)
        # Send the investor message again
        self.clientAccounts.send_again()
        # Update note message
        self.clientAccounts.update_note_message(update_input_message)
        # Resend the investor message
        self.clientAccounts.submit_re_send_investor_message()
        self.clientAccounts.go_to_bank_details()
        # Verify updated investor notes
        self.clientAccounts.verify_updated_investor_notes(updated_input_message)
