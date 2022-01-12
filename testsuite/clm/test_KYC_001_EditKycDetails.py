import pytest

from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from datetime import datetime, timedelta
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage


class KYC001EditKycDetails(BrowserSetup):

    @pytest.mark.clm
    @pytest.mark.pascal
    # @pytest.mark.skip
    def test_kyc_001_edit_kyc_details(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        tomorrow = datetime.now() + timedelta(1)
        dd = tomorrow.strftime('%d')
        mm = tomorrow.strftime('%m')
        date = datetime.utcnow()
        yyyy = date.strftime('1965')
        # account_name = "ZenTest_1622531522485"
        full_name = "client " + str(milliseconds)
        first_name = "client"
        social_insurance_number = "560 141 111"
        marital_status = "Single"
        document_number = "Zen1000"
        occupation_name = "Business"
        income = "234543"
        fixed_assets = "2345345"
        liquid_assets = "2321"
        liabilities = "434"
        name = "ZenQTest"
        no_of_dependents = "1"
        province = "Alberta"
        employment = "1"
        status = "Completed"
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
        self.clientAccounts.click_kyc_tab()
        self.clientAccounts.click_edit_kyc_button()
        self.clientAccounts.click_marital_status_dropdown(marital_status)
        # select the number of dependents
        self.clientAccounts.select_number_of_dependents(no_of_dependents)
        # select the education dropdown
        self.clientAccounts.select_education_level()
        self.clientAccounts.select_document_type()
        self.clientAccounts.enter_number_document(document_number)
        self.clientAccounts.select_issued_province(province)
        self.clientAccounts.select_date(yyyy, mm, dd)
        self.clientAccounts.enter_employer_name(name)
        self.clientAccounts.select_business_type()
        self.clientAccounts.enter_occupation(occupation_name)
        self.clientAccounts.select_years_of_employment(employment)
        self.clientAccounts.enter_personal_income(income)
        # enter the assets
        self.clientAccounts.enter_approximate_net_worth(fixed_assets, liquid_assets, liabilities)
        self.clientAccounts.click_tax_residency()
        self.clientAccounts.select_province_tax_field(province)
        self.clientAccounts.click_disclosure_consent()
        self.clientAccounts.click_national_instrument()
        # click on submit button
        self.clientAccounts.click_submit_button_kyc()
        self.clientAccounts.verify_successfully_message()
        self.clientAccounts.verify_personal_details_status(status)
        self.clientAccounts.verify_employment_income_status(status)
        self.clientAccounts.verify_tax_residency_status(status)
        self.clientAccounts.verify_disclosures_consent_status(status)
