import os

import pytest

from Config import TestData
from Config.Config import rootPath
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from datetime import datetime, timedelta
from src.pages.client_registration_page import ClientRegistrationPage
from src.pages.mailinator_page import MailinatorPage
from src.utils.mailinator import MailinatorAPI


class AOP001AccountOpeningRRSP(BrowserSetup):

    @pytest.mark.aop
    @pytest.mark.pascal
    @pytest.mark.xfail(reason='PAS-523 Error message is displayed as something went wrong when clicked on see my risk profile summary  button')
    # @pytest.mark.skip
    def test_aop_001_account_opening_RRSP(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        tomorrow = datetime.now() + timedelta(1)
        dd = tomorrow.strftime('%d')
        mm = tomorrow.strftime('%m')
        date = datetime.utcnow()
        yyyy = date.strftime('1965')
        name = "ZenQTest"
        first_name = "Client"
        email = "zenq" + str(milliseconds)
        full_name = "Client " + str(milliseconds)
        social_insurance_number = "560 141 111"
        ph_prefix = "416"
        ph_num = "716 2567"
        gender = "Male"
        country_name = "Canada"
        street_number = "550"
        street_name = "Queens"
        street_type = "Quay"
        city_name = "Mississauga"
        postal_code = "M5V 3M8"
        document_name = "pdf_document.pdf"
        marital_status = "Single"
        document_number = "Zen1000"
        occupation_name = "Business"
        income = "234543"
        fixed_assets = "2345345"
        liquid_assets = "2321"
        liabilities = "434"
        less_input = "45"
        account_name = "Zentest"
        no_of_dependents = "1"
        province = "Alberta"
        employment = "1"
        current_portfolio = "35%"
        friend = "A real gambler"
        inflation_and_income = "More than today"
        buying_a_bond = "She owns part of Firm B"
        compound_wealth = "More than $2000 at the end of the 10 years"
        correlation = "Increases"
        play_book = "Borrowing more attractive and saving less attractive"
        preferred_portfolio = "A"
        crashes = "Sell all of the remaining investment"
        larger_drop = "0%"
        risk_preference = "I am most concerned with risk. I am willing to accept the lower returns in order to limit my chance of loss."
        time_horizon = "1 year"
        criticality = "High"
        use_of_account = "Pay for education"
        status = "In Review"
        account_type = "RRSP"
        account_opening_status = "Your account is under review by your advisor team."
        self.dashboard = DashboardPage(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.clientAccounts = ClientsAccountsPage(self.driver)
        self.clientRegistration = ClientRegistrationPage(self.driver)
        self.mailinator = MailinatorPage(self.driver)
        self.addAccount = AddAccountPage(self.driver)
        self.mailinatorApi = MailinatorAPI()

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
        # invite the client
        self.clientRegistration.invite_client()
        time.sleep(2)
        registration_link = self.mailinatorApi.get_invited_link(email)
        self.clientRegistration.signup_assest_management(registration_link, TestData.Registration_password,
                                                         TestData.Confirm_Registration_password, ph_prefix, ph_num)
        self.clientRegistration.skip_phone_validation()
        # select the gender from dropdown
        self.clientRegistration.select_gender(gender)
        # select date from dropdown
        self.clientRegistration.select_date(yyyy, mm, dd)
        # select the country from dropdown
        self.clientRegistration.select_country(country_name)
        # Enter the address
        self.clientRegistration.select_address(street_number, street_name, street_type, city_name, postal_code, province)
        # submit ID verification
        self.clientRegistration.submit_id_verification()
        # switch to the investor window and click mark as verified
        self.clientAccounts.navigate_to_investor_window_click_mark_as_verified()
        # verify successfully message
        self.clientAccounts.verify_changes_saved_successful_message()
        # Switch to id verification window
        self.clientAccounts.navigate_to_id_verification_window()
        # upload the add id document
        self.clientRegistration.click_upload_id_document()
        document_path = os.path.join(rootPath, f"resources/{document_name}")
        # upload the document
        self.clientRegistration.upload_id_document(document_path)
        self.clientRegistration.confirm_upload_id_document()
        self.clientRegistration.continue_uploading_document()
        # enter KYC module and select the marital status
        self.clientRegistration.click_marital_status_dropdown(marital_status)
        # select the number of dependents
        self.clientRegistration.select_number_of_dependents(no_of_dependents)
        # select the education dropdown
        self.clientRegistration.select_education_level()
        # Select the document type from the dropdown
        self.clientRegistration.select_document_type()
        # Enter document number in the document number textfield
        self.clientRegistration.enter_number_document(document_number)
        # Select the issues province from the dropdown
        self.clientRegistration.select_issued_province(province)
        # Select the expiration date from calender widget
        self.clientRegistration.select_date(yyyy, mm, dd)
        # Enter valid employer name in 'Employer text field'
        self.clientRegistration.enter_employer_name(name)
        # Select business type from the dropdown
        self.clientRegistration.select_business_type()
        # Enter occupation in the 'Occupation textfield'
        self.clientRegistration.enter_occupation(occupation_name)
        # Select years of employment from the dropdown
        self.clientRegistration.select_years_of_employment(employment)
        # Enter Annual person income in the 'What is your annual personal income?' textfield
        self.clientRegistration.enter_personal_income(income)
        # enter the assets
        self.clientRegistration.enter_approximate_net_worth(fixed_assets, liquid_assets, liabilities)
        self.clientRegistration.click_tax_residency()
        self.clientRegistration.select_province_tax_field(province)
        self.clientRegistration.click_disclosure_consent()
        self.clientRegistration.click_national_instrument()
        # click on submit button
        self.clientRegistration.click_submit_button()
        self.clientRegistration.perform_agreement()
        self.clientRegistration.navigate_to_investor_eq()
        self.clientRegistration.continue_as_investor_eq()
        self.clientRegistration.select_perform_investor_eq(less_input)
        self.clientRegistration.click_confident_slider()
        self.clientRegistration.click_roulette_slider()
        self.clientRegistration.click_peer_comparision_slider()
        self.clientRegistration.select_game_of_chance()
        self.clientRegistration.select_friend_describes_you(friend)
        self.clientRegistration.select_current_portfolio(current_portfolio)
        self.clientRegistration.select_inflation_and_income(inflation_and_income)
        self.clientRegistration.select_buying_a_bond(buying_a_bond)
        self.clientRegistration.select_compounding_wealth(compound_wealth)
        self.clientRegistration.select_question_of_correlation(correlation)
        self.clientRegistration.select_central_banks_playbook(play_book)
        self.clientRegistration.select_your_preferred_portfolio(preferred_portfolio)
        self.clientRegistration.select_market_crashes(crashes)
        self.clientRegistration.select_larger_drop(larger_drop)
        self.clientRegistration.select_my_risk_preference(risk_preference)
        self.clientRegistration.navigate_to_account_opening()

        self.clientRegistration.click_account_type(account_type)
        self.clientRegistration.enter_account_name(account_name)
        self.clientRegistration.click_continue_button()
        self.clientRegistration.select_risk_exposure(time_horizon, criticality, use_of_account)
        self.clientRegistration.select_disclosures_no()
        self.clientRegistration.click_submit_button()

        self.clientRegistration.sign_all_documents()
        # Click on 'Finish on boarding' button
        self.clientRegistration.click_finish_onboarding()
        # Verify if the 'Dashboard' page is displayed with the 'client name' under accounts
        self.dashboard.verify_client_name(account_name)
        # Click on 'Client account' displayed  under accounts
        self.dashboard.open_account(account_name)
        self.dashboard.verify_account_status(status)
        self.dashboard.verify_account_opening_status(account_opening_status)
        self.dashboard.verify_onboarding_account_type(account_type)
        self.dashboard.logout_from_client_account()
        self.loginPage.login_to_application(TestData.ADVISOR, TestData.PASSWORD)
        self.dashboard.verify_login()
        # Click on clients and accounts button
        self.dashboard.goto_clients_accounts()
        # Create a single client
        self.clientAccounts.search_client_accounts(full_name)
        self.clientAccounts.open_investor_account(full_name)
        self.clientAccounts.click_approval_button()
        # Verify changes saved successfully message
        self.clientAccounts.verify_changes_saved_successful_message()
