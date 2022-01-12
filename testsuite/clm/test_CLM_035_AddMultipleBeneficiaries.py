import pytest
from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from datetime import datetime


class CLM041AddMultipleBeneficiaries(BrowserSetup):

    @pytest.mark.pascal
    @pytest.mark.clm
    # @pytest.mark.skip
    def test_clm_041_add_multiple_beneficiaries(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        date = datetime.now()
        dd = date.strftime('%d')
        mm = date.strftime('%m')
        yyyy = date.strftime('%Y')
        first_name = "Client"
        beneficiary_first_name = "zenq "
        beneficiary_last_name = "testing"
        beneficiary_full_name = beneficiary_first_name + beneficiary_last_name
        full_name = "Client " + str(milliseconds)
        social_insurance_number = "560141111"
        account_name = "zenqtest"
        account_type = "TFSA"
        currency = "CAD"
        relationship_name = "Brother"
        self.dashboard = DashboardPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.clientAccounts = ClientsAccountsPage(self.driver)
        self.addAccount = AddAccountPage(self.driver)
        self.loginPage.login_to_application(TestData.ADVISOR, TestData.PASSWORD)
        self.dashboard.verify_login()
        # Click on clients and accounts button
        self.dashboard.goto_clients_accounts()
        self.clientAccounts.add_single_client(first_name, milliseconds, social_insurance_number,
                                                  "zenq" + str(milliseconds) + "@mailinator.com")
        self.clientAccounts.click_edit_client_details_button()
        self.dashboard.goto_clients_accounts()
        # Search for the client on the 'search bar' and click on client
        self.clientAccounts.search_client_accounts(full_name)
        self.clientAccounts.open_investor_account(full_name)
        # Click on accounts tab
        self.clientAccounts.click_accounts_tab()
        self.clientAccounts.click_add_account_button()
        # Create new account type
        self.clientAccounts.select_account_type(account_type)
        self.clientAccounts.enter_account_name(account_name)
        self.clientAccounts.select_currency(currency)
        self.clientAccounts.click_submit_button()
        self.clientAccounts.click_goto_account_details_button()
        # Navigate to details tab
        self.clientAccounts.click_details_tab()
        # Add Beneficiary details
        self.clientAccounts.click_add_beneficiary_button()
        self.clientAccounts.enter_first_last_beneficiary_name(beneficiary_first_name, beneficiary_last_name)
        self.clientAccounts.enter_social_insurance_number(social_insurance_number)
        self.clientAccounts.select_date(yyyy, mm, dd)
        self.clientAccounts.select_beneficiary_relationship(relationship_name)
        self.clientAccounts.click_add_button()
        # Verify beneficiary name
        self.clientAccounts.verify_beneficiary_name(beneficiary_full_name)
        # Verify beneficiary relationship name
        self.clientAccounts.verify_beneficiary_relation(relationship_name)
        # Verify beneficiary social insurance number
        self.clientAccounts.verify_social_insurance_number(social_insurance_number)
        # Verify beneficiary date of birth
        self.clientAccounts.verify_beneficiary_date_of_birth(mm, dd, yyyy)
        # Delete beneficiary button
        self.clientAccounts.delete_beneficiary_button()
        self.clientAccounts.click_add_beneficiary_button()
        self.clientAccounts.enter_first_last_beneficiary_name(beneficiary_first_name, beneficiary_last_name)
        self.clientAccounts.enter_social_insurance_number(social_insurance_number)
        self.clientAccounts.select_date(yyyy, mm, dd)
        self.clientAccounts.select_beneficiary_relationship(relationship_name)
        self.clientAccounts.click_add_button()
        self.clientAccounts.verify_beneficiary_name(beneficiary_full_name)
        self.clientAccounts.verify_beneficiary_relation(relationship_name)
        self.clientAccounts.verify_social_insurance_number(social_insurance_number)
        self.clientAccounts.verify_beneficiary_date_of_birth(mm, dd, yyyy)
        self.clientAccounts.delete_beneficiary_button()