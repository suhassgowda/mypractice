from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Config import Config
from src.base.BrowserSetup import logger
from src.utils.safe_actions import SafeActions


class ClientRegistrationPage(SafeActions):

    INVESTOR_EMAIL = (By.CSS_SELECTOR, "dd[data-testid*='.email.description']")
    INVITE_CLIENT = (By.CSS_SELECTOR, "button[class*='invite-client-button']")
    INVITATION_SENT = (By.CSS_SELECTOR, "span[data-testid='FloatingMessage.text']")
    REGISTRATION = (By.XPATH, "//a[text()='Register']")
    CLIENT_REGISTRATION_TITLE = (By.CSS_SELECTOR, "h1[data-testid='ClientRegistrationPage.title']")
    REGISTRATION_PASSWORD = (By.ID, "ClientRegistrationPage.password-input")
    REGISTRATION_CONFIRM_PASSWORD = (By.ID, "ClientRegistrationPage.confirm-password-input")
    REGISTRATION_PREFIX_PH = (By.ID, "ClientRegistrationPage.phone-input.carrierPrefixInput")
    REGISTRATION_PHONE_NUM = (By.ID, "ClientRegistrationPage.phone-input.phoneNumberInput")
    SIGNUP_REGISTRATION = (By.CSS_SELECTOR, "button[class*='submit-button']")
    SKIP_PH_VERIFICATION = (By.CLASS_NAME, "client-onboarding-skip-step-icon")
    GENDER_DROPDOWN = (By.CLASS_NAME, "dropdown-header-button-icon")
    GENDER_DROPDOWN_LIST = (By.CSS_SELECTOR, "p[data-testid*='.gender-select.item']")
    REGISTER_FRAME = (By.CSS_SELECTOR, "div[class='content-body']")
    DD = (By.CSS_SELECTOR, "[placeholder='DD']")
    MM = (By.CSS_SELECTOR, "[placeholder='MM']")
    YYYY = (By.CSS_SELECTOR, "[placeholder='YYYY']")
    ACTIVE_DATE = (By.CSS_SELECTOR, "[class*='tile--active']")
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "input[placeholder='Add Country']")
    COUNTRY_DROPDOWN_LIST = (By.CSS_SELECTOR, "[aria-hidden='false'] .dropdown-list-item-title")
    STREET_NUMBER = (By.ID, "ClientOnboardingPersonalDetailsStep.address-input.street-inputs.street-number")
    STREET_NAME = (By.ID, "ClientOnboardingPersonalDetailsStep.address-input.street-inputs.street-name")
    STREET_TYPE = (By.CSS_SELECTOR, "input[placeholder='Street Type']")
    CITY = (By.ID, "ClientOnboardingPersonalDetailsStep.address-input.city")
    POSTAL_CODE = (By.ID, "ClientOnboardingPersonalDetailsStep.address-input.postal-code")
    PROVINCE = (By.ID, "ClientOnboardingPersonalDetailsStep.address-input.province.typeahead-header.search")
    COUNTRY_TYPE = (By.XPATH, "//p[text()='Canada']")
    STREET_TYPE_DROPDOWN = (By.XPATH, "//p[text()='Quay']")
    PROVINCE_DROPDOWN = (By.XPATH, "//p[text()='Ontario']")
    SUBMIT_ID_VERIFICATION = (By.CSS_SELECTOR, "button[data-testid*='.submit-button']")
    BANK_ACCOUNT_TITLE = (By.CSS_SELECTOR, "h1[data-testid*='.title']")
    ID_DOCUMENT = (By.CSS_SELECTOR, "button[data-testid='ClientOnboardingIdProvisionStep.upload-id-button']")
    UPLOAD_ID_DOCUMENT = (By.ID, "id-upload")
    CONFIRM_UPLOAD_ID_DOCUMENT = (By.CSS_SELECTOR, "button[data-testid='UploadIdModal.confirm']")
    LETS_CONTINUE = (By.CSS_SELECTOR, "button[class*='-continue-button']")
    KYC_QUESTIONNAIRE = (By.CSS_SELECTOR, "h1[data-testid='ClientKycStep.title']")
    MARTIAL_STATUS = (By.CSS_SELECTOR, "[class*='marital-status-question-row']>div>button")
    MARTIAL_STATUS_LIST = (By.CSS_SELECTOR, "div[class*='status-question'] button +ul>li")
    DEPENDENTS_BUTTON = (By.CSS_SELECTOR, "div[class*='number_of_dependents'] button")
    DEPENDENTS_LIST = (By.CSS_SELECTOR, "div[class*='number_of_dependents'] button +ul>li")
    EDUCATION_LEVEL_BUTTON = (By.CSS_SELECTOR, "[class*='container education']>div>button>div")
    BACHELORS = (By.ID, "bachelors")
    DOCUMENT_TYPE_BUTTON = (By.CSS_SELECTOR, "[class*='id-document-question-row']>div>button>div")
    DOCUMENT_NO = (By.CSS_SELECTOR, "input[placeholder='Add document no']")
    ISSUED_PROVINCE = (By.CSS_SELECTOR, "input[data-testid*='.issued-province-input.typeahead-header.search']")
    EMPLOYER_NAME_TEXTFIELD = (By.CSS_SELECTOR,
                               "div[class='question-form-row-container employer_name']>label>div>textarea")
    BUSINESS_TYPE_DROPDOWN = (By.CSS_SELECTOR, "[class='question-form-row-container business_type']>div>button")
    OCCUPATION_TEXTFIELD = (By.CSS_SELECTOR, "[class='question-form-row-container occupation' ]>label>div>textarea")
    YEARS_OF_EMPLOYMENT_BUTTON = (By.CSS_SELECTOR,
                                  "[class='question-form-row-container years_of_employee_experience']>div>div>button")
    PERSONAL_INCOME_TEXTFIELD = (By.CSS_SELECTOR, "div[class*=' personal_income']>label>div>input")
    FIXED_ASSETS = (By.NAME, "fixed_assets")
    LIQUID_ASSETS = (By.NAME, "liquid_assets")
    LIABILITIES = (By.NAME, "liabilities")
    TAX_RESIDENCY_CHECKBOX = (By.CSS_SELECTOR, "[data-testid*= 'canada-residency-certified-checkbox']>span")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[class*='button green-button']")
    BENEFICIAL_OWNERSHIP_INFORMATION_RADIOBUTTON = (By.CSS_SELECTOR, "label[data-testid*='information.choice-list"
                                                                     ".true']>span")
    SECURITY_HOLDER_MATERIAL_RADIOBUTTON = (By.CSS_SELECTOR, "label[data-testid*='holder-material.choice-list"
                                                             ".i_want_all']>span")
    ELECTRONIC_DELIVERY_RADIOBUTTON = (By.CSS_SELECTOR, "label[data-testid*='electronic-delivery.choice-list.true"
                                                        "']>span")
    REPORTING_INSIDER_RADIOBUTTON = (By.CSS_SELECTOR, "[class*='container insider']>div li+li input+span")
    VOTING_RIGHTS_RADIOBUTTON1 = (By.CSS_SELECTOR, "[class*='10_percent']>div li+li input+span")
    VOTING_RIGHTS_RADIOBUTTON2 = (By.CSS_SELECTOR, "[class*='20_percent']>div li+li input+span")
    IIROC_MEMBER_FIRM_RADIOBUTTON = (By.CSS_SELECTOR, "[class*='is_pro']>div li+li input+span")
    DOCUMENT_TYPE_DROPDOWN = (By.CSS_SELECTOR, "p[data-testid*='.type-select.item']")
    YEARS_OF_EMPLOYMENT = (By.CSS_SELECTOR, "[class*='years_of_employee_experience']>div button")

    AGREEMENT = (By.CSS_SELECTOR, "h1[data-testid='ClientOnboardingAgreementStep.title']")
    NEXT_BUTTON = (By.CSS_SELECTOR, "span[data-test-id*='-Button-Text']")
    INITIAL = (By.CSS_SELECTOR, "button[data-test-id*='InitialButton']")
    SIGN_IN = (By.CSS_SELECTOR, "button[data-test-id*='SignButton']")
    CONFIRM_AGREEMENT = (By.CSS_SELECTOR, "[data-test-id='ConfirmButton']")
    VERIFY_INVESTOR_TITLE = (By.CSS_SELECTOR, "h1[data-testid='ClientOnboardingInvestorDNAStep.title']")
    GOT_IT_LETS_GO = (By.CSS_SELECTOR, "button[data-testid='InvestorDNAStepInitialView.continue-button']")
    MORE_ACTIONS = (By.ID, "MenuOpenButton")
    CONTINUE_WITHOUT_SELECTION = (By.CSS_SELECTOR, "button[data-testid*='.continue-button']")
    LESS_RADIO_BUTTON = (By.XPATH, "//*[text()='LESS']")
    LESS_INPUT = (By.ID, "SyntoniqQuestionInputRow.number-input")
    NEXT_ONE = (By.CSS_SELECTOR, "button[data-testid='SyntoniqQuestionWizardFormStepFooter.next']")
    SLIDER = (By.CSS_SELECTOR, "span[role='slider']")
    # GAME_OF_CHANCE_QUESTION_ONE = (By.CSS_SELECTOR, "input[name*='1']+span")
    GAME_OF_CHANCE_QUESTION_ONE = (By.CSS_SELECTOR, "div[class*='input-row'] ul:nth-child(1) li label")
    GAME_OF_CHANCE_QUESTION_TWO = (By.CSS_SELECTOR, "input[name*='3']+span")
    GAME_OF_CHANCE_QUESTION_THREE = (By.CSS_SELECTOR, "input[name*='5']+span")
    SELECT_RADIO_BUTTON = (By.CSS_SELECTOR, "label[class='radio-input-label']")
    INVESTOR_EQ_SUB_TITLE = (By.CSS_SELECTOR, "h1[data-testid*='.question-title']")
    DETERMINE_INVESTOR_EQ_AND_ACCOUNT_OPENING_TITLE = (By.CSS_SELECTOR, "h1[data-testid*='.title']")
    CURRENT_PORTFOLIO_RADIOBUTTON = (By.CSS_SELECTOR, "div[class*='syntoniq-question-input-row'] label>input")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='continue-button']")

    LOGO = (By.CSS_SELECTOR, ".logo")
    CONTAINER_EDUCATION = (By.CSS_SELECTOR, "[class*='container education']>div span")
    BIRTH_CERTIFICATE = (By.ID, "BIRTH_CERTIFICATE")
    PROVINCE_INPUT = (By.CSS_SELECTOR, "input[data-testid*='.issued-province-input.typeahead"
                                       "-header.search']")
    PROVINCE_TYPE = (By.CSS_SELECTOR, "ul.dropdown-list.bottom.visible>li")
    TECHNOLOGY = (By.ID, "technology")
    TAX_RESIDENCY = (By.CSS_SELECTOR, "div[class*='tax-resident-question-row']>div>button")
    TAX_RESIDENCY_NO = (By.ID, "no")
    PROVINCE_TAX = (By.CSS_SELECTOR, "div[class*='province-select question-form-row-canadian-province-select'] input")
    DISCLOSURE = (By.CSS_SELECTOR, "div[class*='person-question-row']>div>button")
    DISCLOSURE_SELECT = (By.CSS_SELECTOR, "ul[data-testid*='item-3.question-0.yes-no-select']>li[id='no']")
    SPAN_FRAME = "one-span-iframe"

    OPEN_ACCOUNT = (By.CSS_SELECTOR, "p[data-testid*='title-message']+ul>li:nth-child(2)>button")
    ACCOUNT_NAME_TEXTFIELD = (By.CSS_SELECTOR, "input[id*='account-name']")
    DRAWING_FUNDS = (By.CSS_SELECTOR, "div[class*='container time_horizon']>h3+ul label")
    CRITICAL_DRAWFUNDS_WITHIN_TIMEFRAME = (By.CSS_SELECTOR, ".criticality label .radio-input-icon+p")
    INTENDED_USE_OF_ACCOUNT = (By.CSS_SELECTOR, ".intended_use_of_account label")
    ADDITIONAL_DOCUMENT_TITLE = (By.CSS_SELECTOR, "h1[data-testid*='AdditionalDocumentsStep.title']")
    HEADER = (By.TAG_NAME, "h1")
    ESIGN_LOCATOR = (By.XPATH, "//*[text()='E-sign']")

    LINK_BANK_ACCOUNT = (By.CSS_SELECTOR, "button[data-testid*='.link-your-bank-account-button']")
    CONTINUE_PLAID_LINK = (By.CSS_SELECTOR, "button[class*='plaid-button']")
    CONTINUE_PLAID_ACCOUNT = (By.ID, "aut-continue-button")
    DISCLAIMER_TITLE = (By.CSS_SELECTOR, "h1[data-testid='PlaidDisclaimerView.title']")
    FRAME = "plaid-link-iframe-1"
    NAVIGATE_BACK = (By.CSS_SELECTOR, "button[class*='Navbar__button--is-left']")
    SELECT_YOUR_BANK = (By.CSS_SELECTOR, "li[class*='InstitutionSearchResult InstitutionSearchResult']")
    BANK_USER_NAME = (By.CSS_SELECTOR, "input[id='username']")
    BANK_PASSWORD = (By.CSS_SELECTOR, "input[id='password']")
    SUBMIT_BANK_DETAILS = (By.ID, "aut-submit-button")
    PLAID_CHECKING = (By.CSS_SELECTOR, "div[aria-label*='Plaid Checking']")
    PLAID_SINGLE = (By.CSS_SELECTOR, "div[aria-label*='Plaid Saving']")

    SELECT_ACCOUNT_TYPE = (By.CSS_SELECTOR, "p[class='account-type-name']")
    ENTER_ACCOUNT_NAME = (By.ID, "AccountSetupStepAccountDetailsView.account-name")
    ON_BOARDING_TITLE = (By.CSS_SELECTOR, "h1[data-testid='ClientOnboardingAccountQuestionsStep.title']")
    ACCOUNT_STATUS_LABEL = (By.CSS_SELECTOR, "p[data-testid*='.account-status-label']")
    SPOUSE_FIRST_NAME = (By.CSS_SELECTOR, "input[id*='.spouseFirstName']")
    SPOUSE_LAST_NAME = (By.CSS_SELECTOR, "input[id*='.spouseLastName']")
    SPOUSE_INS_NUMBER = (By.CSS_SELECTOR, "input[id*='.spouseSIN']")
    SPOUSE_OCCUPATION = (By.CSS_SELECTOR, "input[id*='.spouseOccupation']")
    SPOUSE_BUSINESS_TYPE = (By.CSS_SELECTOR, "div[class*='select marital-status']>div+button")
    SPOUSE_DROPDOWN_BUSINESS_TYPE = (By.CSS_SELECTOR, "[data-testid*='.BusinessTypeSelect.item'] p")
    AGRICULTURE = (By.ID, "agriculture")
    SPOUSE_EMPLOYEE_NAME = (By.CSS_SELECTOR, "input[id*='.spouseEmployerName']")
    YEARS_OF_EXPERIENCE_DROP_DOWN = (By.CSS_SELECTOR, "button[data-testid*='.years-of-experience-select']")
    YEARS_OF_EXPERIENCE_LIST = (By.CSS_SELECTOR, "ul[data-testid*='.years-of-experience-select']>li")
    ISSUE_DATE_YEAR = (By.CSS_SELECTOR, "div[class*='issue-date'] Input:nth-child(2)")
    ISSUE_DATE_MONTH = (By.CSS_SELECTOR, "div[class*='issue-date'] Input:nth-child(2)+span+input")
    ISSUE_DATE_DAY = (By.CSS_SELECTOR, "div[class*='issue-date'] Input:nth-child(2)+span+span+input+span+input")
    ISSUE_CURRENT_DATE = (By.CSS_SELECTOR, "[class*='tile--now']")
    BUSINESS_EMPLOYMENT = (By.CSS_SELECTOR, "div[class*=' business_type']>h3+div button+ul>li:nth-child(1)")
    RIF_CALCULATION_DROPDOWN = (By.CSS_SELECTOR, "button[data-testid*='mode-select.header-button']")
    RIF_DROP_DOWN_LIST = (By.CSS_SELECTOR, "li[data-testid*='mode-select.item']")
    ACCOUNT_TYPES = (By.CSS_SELECTOR, "ul[class*='types-list']>li ")
    JURISDICTION_DROPDOWN = (By.CSS_SELECTOR, "button[data-testid*='jurisdiction']")
    JURISDICTION_LIST = (By.CSS_SELECTOR, "ul[data-testid*='jurisdiction']>li")

    def __init__(self, driver):
        super().__init__(driver)

    def invite_client(self):
        logger.info("Send Invitation")
        self.safe_click(self.INVITE_CLIENT, Config.MEDIUM_WAIT)
        self.wait_until_visible(self.INVITATION_SENT, Config.MEDIUM_WAIT)

    def signup_assest_management(self, registration_link, reg_password, conf_password, ph_prefix, ph_num):
        logger.info("Sign up for asset management" + reg_password + conf_password + ph_prefix + ph_num)
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(registration_link)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.wait_until_visible(self.CLIENT_REGISTRATION_TITLE, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.REGISTRATION_PASSWORD, reg_password, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.REGISTRATION_CONFIRM_PASSWORD, conf_password, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.REGISTRATION_PREFIX_PH, ph_prefix, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.REGISTRATION_PHONE_NUM, ph_num, Config.MEDIUM_WAIT)
        self.safe_click(self.SIGNUP_REGISTRATION, Config.MEDIUM_WAIT)

    def skip_phone_validation(self):
        logger.info("Skip Phone Validation")
        self.wait_until_visible(self.SKIP_PH_VERIFICATION, Config.MEDIUM_WAIT)
        self.safe_click(self.SKIP_PH_VERIFICATION, Config.MEDIUM_WAIT)

    def select_gender(self, gender):
        logger.info("Select Gender From The Dropdown:" + gender)
        self.safe_click(self.GENDER_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.GENDER_DROPDOWN_LIST, gender, Config.MEDIUM_WAIT)

    def select_date(self, yyyy, mm, dd):
        logger.info("Select The Date:" + yyyy + mm + dd)
        self.safe_click(self.YYYY, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.YYYY, yyyy, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.MM, mm, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.DD, dd, Config.MEDIUM_WAIT)
        self.safe_click(self.ACTIVE_DATE, Config.MEDIUM_WAIT)

    def select_country(self, country_name):
        logger.info("Select The Country" + country_name)
        self.safe_click(self.COUNTRY_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.COUNTRY_DROPDOWN, country_name, Config.MEDIUM_WAIT)
        self.safe_click(self.COUNTRY_TYPE, Config.MEDIUM_WAIT)

    def submit_id_verification(self):
        logger.info("Submit Id Verification")
        self.safe_click(self.SUBMIT_ID_VERIFICATION, Config.MEDIUM_WAIT)
        self.wait_until_visible(self.BANK_ACCOUNT_TITLE, Config.MEDIUM_WAIT)

    def select_address(self, street_number, street_name, street_type, city_name, postal_code, province):
        logger.info("Select Id Verification Address:" + street_number + street_name + street_type + city_name + postal_code + province)
        self.safe_enter_text(self.STREET_NUMBER, street_number, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.STREET_NAME, street_name, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.STREET_TYPE, street_type, Config.MEDIUM_WAIT)
        self.safe_click(self.STREET_TYPE_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.CITY, city_name, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.POSTAL_CODE, postal_code, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.PROVINCE, province, Config.MEDIUM_WAIT)
        self.safe_click(self.PROVINCE_DROPDOWN, Config.MEDIUM_WAIT)

    def click_upload_id_document(self):
        logger.info("Click On Id Document Button")
        self.safe_click(self.ID_DOCUMENT, Config.MEDIUM_WAIT)

    def upload_id_document(self, document_path):
        logger.info("Upload document" + document_path)
        self.driver.find_element(*self.UPLOAD_ID_DOCUMENT).send_keys(document_path)
        self.wait_for_time(Config.VERY_SHORT_WAIT)

    def confirm_upload_id_document(self):
        logger.info("Confirm Upload Document")
        self.safe_click(self.CONFIRM_UPLOAD_ID_DOCUMENT, Config.MEDIUM_WAIT)

    def continue_uploading_document(self):
        logger.info("Continue Uploading")
        self.safe_click(self.LETS_CONTINUE, Config.MEDIUM_WAIT)
        self.wait_until_visible(self.KYC_QUESTIONNAIRE, Config.MEDIUM_WAIT)

    def click_marital_status_dropdown(self, martial_status):
        logger.info("Select The Marital status" + martial_status)
        self.safe_click(self.MARTIAL_STATUS, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.MARTIAL_STATUS_LIST, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.MARTIAL_STATUS_LIST, martial_status, Config.MEDIUM_WAIT)

    def select_number_of_dependents(self, no_of_dependents):
        logger.info("Select The Number Of Dependents" + no_of_dependents)
        self.safe_click(self.DEPENDENTS_BUTTON, Config.MEDIUM_WAIT)
        element = self.wait_until_visible(self.DEPENDENTS_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        element.send_keys(no_of_dependents)
        element.send_keys(keys.Keys.ENTER)

    def select_education_level(self):
        logger.info("Select Education Level")
        self.safe_click(self.LOGO, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.safe_js_click(self.CONTAINER_EDUCATION, Config.MEDIUM_WAIT)
        self.safe_js_click(self.BACHELORS, Config.MEDIUM_WAIT)

    def select_document_type(self):
        logger.info("Select The Document Type ")
        self.safe_click(self.LOGO, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.safe_js_click(self.DOCUMENT_TYPE_BUTTON, Config.MEDIUM_WAIT)
        self.safe_js_click(self.BIRTH_CERTIFICATE, Config.MEDIUM_WAIT)

    def enter_number_document(self, document_number):
        logger.info("Enter The Document Number:" + document_number)
        self.safe_enter_text(self.DOCUMENT_NO, document_number, Config.MEDIUM_WAIT)

    def select_issued_province(self, province):
        logger.info("Select The Issued Province:" + province)
        self.safe_js_click(self.PROVINCE_INPUT, Config.MEDIUM_WAIT)
        element = self.wait_until_visible(self.PROVINCE_INPUT, Config.MEDIUM_WAIT)
        element.send_keys(province)
        self.wait_for_time(3)
        self.safe_js_click(self.PROVINCE_TYPE, Config.MEDIUM_WAIT)

    def enter_employer_name(self, name):
        logger.info("Enter The Employer Name" + name)
        self.safe_enter_text(self.EMPLOYER_NAME_TEXTFIELD, name, Config.MEDIUM_WAIT)

    def select_business_type(self):
        logger.info("Select Business Type")
        business_type_dropdown = self.BUSINESS_TYPE_DROPDOWN
        self.safe_js_click(business_type_dropdown, Config.MEDIUM_WAIT)
        self.safe_js_click(self.TECHNOLOGY, Config.MEDIUM_WAIT)

    def enter_occupation(self, occupation_name):
        logger.info("Enter Occupation Name" + occupation_name)
        self.safe_enter_text(self.OCCUPATION_TEXTFIELD, occupation_name, Config.MEDIUM_WAIT)
        self.wait_for_time(6)

    def select_years_of_employment(self, employment):
        logger.info("Select Years Of Employment" + employment)
        years_of_employment = self.YEARS_OF_EMPLOYMENT
        element = self.wait_until_visible(years_of_employment, Config.MEDIUM_WAIT)
        self.safe_js_click(years_of_employment, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        element.send_keys(employment)
        element.send_keys(keys.Keys.ENTER)

    def enter_personal_income(self, income):
        logger.info("Enter Personal Income" + income)
        self.safe_enter_text(self.PERSONAL_INCOME_TEXTFIELD, income, Config.MEDIUM_WAIT)

    def enter_approximate_net_worth(self, fixed_assets, liquid_assets, liabilities):
        logger.info("Enter Approximate Net Worth:" + fixed_assets + liquid_assets + liabilities)
        self.safe_enter_text(self.FIXED_ASSETS, fixed_assets, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.LIQUID_ASSETS, liquid_assets, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.LIABILITIES, liabilities, Config.MEDIUM_WAIT)

    def click_tax_residency(self):
        logger.info("Click Tax Residency Checkbox")
        self.safe_js_click(self.TAX_RESIDENCY, Config.MEDIUM_WAIT)
        self.safe_js_click(self.TAX_RESIDENCY_NO, Config.MEDIUM_WAIT)
        self.safe_js_click(self.TAX_RESIDENCY_CHECKBOX, Config.MEDIUM_WAIT)

    def select_province_tax_field(self, province):
        logger.info("Select Province Tax Field:" + province)
        self.safe_js_click(self.PROVINCE_TAX, Config.MEDIUM_WAIT)
        element = self.wait_until_visible(self.PROVINCE_TAX, Config.MEDIUM_WAIT)
        self.wait_for_time(3)
        element.send_keys(province)
        self.safe_js_click(self.PROVINCE_TYPE, Config.MEDIUM_WAIT)

    def click_disclosure_consent(self):
        logger.info("Click Disclosure Consent")
        self.safe_js_click(self.DISCLOSURE, Config.MEDIUM_WAIT)
        self.safe_js_click(self.DISCLOSURE_SELECT, Config.MEDIUM_WAIT)

    def click_national_instrument(self):
        logger.info("Click National Instrument")
        self.safe_js_click(self.BENEFICIAL_OWNERSHIP_INFORMATION_RADIOBUTTON, Config.MEDIUM_WAIT)
        self.safe_js_click(self.SECURITY_HOLDER_MATERIAL_RADIOBUTTON, Config.MEDIUM_WAIT)
        self.safe_js_click(self.ELECTRONIC_DELIVERY_RADIOBUTTON, Config.MEDIUM_WAIT)
        self.safe_js_click(self.REPORTING_INSIDER_RADIOBUTTON, Config.MEDIUM_WAIT)
        self.safe_js_click(self.VOTING_RIGHTS_RADIOBUTTON1, Config.MEDIUM_WAIT)
        self.safe_js_click(self.VOTING_RIGHTS_RADIOBUTTON2, Config.MEDIUM_WAIT)
        self.safe_js_click(self.IIROC_MEMBER_FIRM_RADIOBUTTON, Config.MEDIUM_WAIT)

    # def submit_button(self):
    #     self.safe_click(self.SUBMIT_BUTTON, Config.MEDIUM_WAIT)

    def perform_agreement(self):
        logger.info("Perform Signup Agreement")
        self.wait_until_visible(self.AGREEMENT, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.MEDIUM_WAIT)
        self.wait_until_visible((By.CLASS_NAME, self.SPAN_FRAME), Config.LONG_WAIT)
        self.driver.switch_to.frame(self.driver.find_element_by_class_name(self.SPAN_FRAME))
        self.safe_click(self.NEXT_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(2)
        self.safe_click(self.SIGN_IN, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(2)
        self.safe_click(self.SIGN_IN, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(2)
        self.safe_click(self.INITIAL, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(2)
        self.safe_click(self.INITIAL, Config.MEDIUM_WAIT)
        self.safe_click(self.CONFIRM_AGREEMENT, Config.MEDIUM_WAIT)
        self.driver.switch_to.default_content()

    def navigate_to_investor_eq(self):
        logger.info("Navigate To Investor EQ")
        self.wait_until_visible(self.VERIFY_INVESTOR_TITLE, Config.MEDIUM_WAIT)
        self.safe_click(self.GOT_IT_LETS_GO, Config.MEDIUM_WAIT)

    def continue_as_investor_eq(self):
        logger.info("Continue As Investor EQ")
        self.wait_until_visible(self.CONTINUE_WITHOUT_SELECTION, Config.MEDIUM_WAIT)
        self.safe_click(self.CONTINUE_WITHOUT_SELECTION, Config.MEDIUM_WAIT)

    def select_perform_investor_eq(self, less_input):
        logger.info("Select Perform Investor EQ" + less_input)
        self.safe_click(self.LESS_RADIO_BUTTON, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.LESS_INPUT, less_input, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def click_confident_slider(self):
        logger.info("Click and Slide Confident Slider")
        self.safe_click(self.SLIDER, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def click_roulette_slider(self):
        logger.info("Click And Slide Roulette Slider")
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.safe_js_click(self.SLIDER, Config.MEDIUM_WAIT)
        for i in range(5):  # adjust integer value for need
            self.driver.execute_script("window.scrollBy(0, 250)")
        self.safe_click(self.SLIDER, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def click_peer_comparision_slider(self):
        logger.info("Click And Slide Peer Comparision Slider")
        self.safe_js_click(self.SLIDER, Config.MEDIUM_WAIT)
        for i in range(5):  # adjust integer value for need
            self.driver.execute_script("window.scrollBy(0, 250)")
        self.safe_click(self.SLIDER, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def select_game_of_chance(self):
        logger.info("Select Game Of Change")
        self.safe_js_click(self.GAME_OF_CHANCE_QUESTION_ONE, Config.MEDIUM_WAIT)
        self.safe_js_click(self.GAME_OF_CHANCE_QUESTION_TWO, Config.MEDIUM_WAIT)
        self.safe_js_click(self.GAME_OF_CHANCE_QUESTION_THREE, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def select_friend_describes_you(self, friend):
        logger.info("Select An Option Under Friend Describes you:" + friend)
        self.wait_until_visible(self.INVESTOR_EQ_SUB_TITLE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SELECT_RADIO_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SELECT_RADIO_BUTTON, friend, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def select_current_portfolio(self, current_portfolio):
        logger.info("Select Current Portfolio" + current_portfolio)
        self.wait_until_visible(self.INVESTOR_EQ_SUB_TITLE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SELECT_RADIO_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SELECT_RADIO_BUTTON, current_portfolio, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def select_inflation_and_income(self, inflation_and_income):
        logger.info("Select An Option Under Inflation And Income" + inflation_and_income)
        self.wait_until_visible(self.INVESTOR_EQ_SUB_TITLE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SELECT_RADIO_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SELECT_RADIO_BUTTON, inflation_and_income, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def select_buying_a_bond(self, buying_a_bond):
        logger.info("Select An Option Under Buying A Bond" + buying_a_bond)
        self.wait_until_visible(self.INVESTOR_EQ_SUB_TITLE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SELECT_RADIO_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SELECT_RADIO_BUTTON, buying_a_bond, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def select_compounding_wealth(self, compound_wealth):
        logger.info("Select An Option Under Compound Wealth" + compound_wealth)
        self.wait_until_visible(self.INVESTOR_EQ_SUB_TITLE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SELECT_RADIO_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SELECT_RADIO_BUTTON, compound_wealth, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def select_question_of_correlation(self, correlation):
        logger.info("Select An Option Under Questions Of Correlation" + correlation)
        self.wait_until_visible(self.INVESTOR_EQ_SUB_TITLE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SELECT_RADIO_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SELECT_RADIO_BUTTON, correlation, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def select_central_banks_playbook(self, playbook):
        logger.info("Select An Option Under Central Banks Playbook" + playbook)
        self.wait_until_visible(self.INVESTOR_EQ_SUB_TITLE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SELECT_RADIO_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SELECT_RADIO_BUTTON, playbook, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def select_your_preferred_portfolio(self, preferred_portfolio):
        logger.info("Select An Option Under Your Preferred Portfolio" + preferred_portfolio)
        self.wait_until_visible(self.INVESTOR_EQ_SUB_TITLE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SELECT_RADIO_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.driver.execute_script("window.scrollBy(0, 260)")
        self.safe_click_from_list_of_elements(self.SELECT_RADIO_BUTTON, preferred_portfolio, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def select_market_crashes(self, crashes):
        logger.info("Select An Option Under Market Crashes" + crashes)
        self.wait_until_visible(self.INVESTOR_EQ_SUB_TITLE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SELECT_RADIO_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SELECT_RADIO_BUTTON, crashes, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def select_larger_drop(self, larger_drop):
        logger.info("Select An Option Under Larger Drop:" + larger_drop)
        self.wait_until_visible(self.INVESTOR_EQ_SUB_TITLE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SELECT_RADIO_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SELECT_RADIO_BUTTON, larger_drop, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def select_my_risk_preference(self, risk_preference):
        logger.info("Select An Option Under My Risk Preference:" + risk_preference)
        self.wait_until_visible(self.INVESTOR_EQ_SUB_TITLE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SELECT_RADIO_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SELECT_RADIO_BUTTON, risk_preference, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)

    def navigate_to_account_opening(self):
        logger.info("Navigate To Account Opening")
        self.wait_until_visible(self.DETERMINE_INVESTOR_EQ_AND_ACCOUNT_OPENING_TITLE, Config.MEDIUM_WAIT)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)
        self.wait_until_visible(self.DETERMINE_INVESTOR_EQ_AND_ACCOUNT_OPENING_TITLE, Config.MEDIUM_WAIT)

    def select_account_type(self):
        logger.info("Select Account type")
        self.safe_click(self.OPEN_ACCOUNT, Config.MEDIUM_WAIT)

    def enter_account_name(self, account_name):
        logger.info("Enter Account Name" + account_name)
        self.safe_enter_text(self.ACCOUNT_NAME_TEXTFIELD, account_name, Config.MEDIUM_WAIT)

    def click_continue_button(self):
        logger.info("Click On Continue Button")
        self.safe_click(self.CONTINUE_BUTTON, Config.MEDIUM_WAIT)

    def select_risk_exposure(self, time_horizon, criticality, use_of_account):
        logger.info("Select The Risk Exposures:" + time_horizon + criticality + use_of_account)
        self.wait_for_time(Config.SHORT_WAIT)
        wait = WebDriverWait(self.driver, Config.MEDIUM_WAIT)
        from selenium.webdriver.support import expected_conditions as ec
        wait.until(ec.presence_of_element_located(self.HEADER))
        q1 = self.driver.find_elements_by_css_selector(".time_horizon li label")
        for option1 in q1:
            if option1.text.__contains__(time_horizon):
                option1.click()
                break
        q2 = self.driver.find_elements_by_css_selector(".criticality label .radio-input-icon+p")
        self.driver.execute_script("arguments[0].scrollIntoView();", q2[0])
        # print(str(len(q2)))
        for option2 in q2:
            # print(option2.text)
            if option2.text.__contains__(criticality):
                # option2.click()
                self.driver.execute_script("arguments[0].click();", option2)
                break
        q3 = self.driver.find_elements_by_css_selector(".intended_use_of_account label")
        # print(str(len(q3)))
        for option3 in q3:
            print(option3.text)
            if option3.text.__contains__(use_of_account):
                self.driver.execute_script("arguments[0].click();", option3)
                break

    def select_disclosures_no(self):
        logger.info("Select Disclosures No")
        no_buttons = self.driver.find_elements_by_css_selector("[value='no']")
        for button in no_buttons:
            self.driver.execute_script("arguments[0].click();", button)

    def click_submit_button(self):
        logger.info("Click Submit Button")
        self.safe_click(self.SUBMIT_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)

    def sign_all_documents(self):
        logger.info("Signing Documents")
        self.wait_for_presence_of_all_elements_located(self.ESIGN_LOCATOR, Config.MEDIUM_WAIT)
        e_sign_buttons = self.driver.find_elements(*self.ESIGN_LOCATOR)
        for x in range(len(e_sign_buttons)):
            logger.info("Document " + str(x))
            # self.wait_until_visible(self.ESIGN_LOCATOR, Config.LONG_WAIT)
            self.safe_click(self.ESIGN_LOCATOR, Config.MEDIUM_WAIT)
            val = False
            self.wait_until_visible((By.CLASS_NAME, "one-span-iframe"), Config.LONG_WAIT)
            self.driver.switch_to.frame(self.driver.find_element_by_class_name("one-span-iframe"))
            while not val:
                try:
                    val = self.driver.find_element(*self.CONFIRM_AGREEMENT).is_displayed()
                except Exception:
                    pass
                if val:
                    self.safe_click(self.CONFIRM_AGREEMENT, Config.MEDIUM_WAIT)
                    self.driver.switch_to_default_content()
                else:
                    self.safe_click(self.NEXT_BUTTON, Config.MEDIUM_WAIT)
                    self.wait_for_presence_of_all_elements_located(self.SIGN_IN, Config.MEDIUM_WAIT)
                    self.safe_click(self.NEXT_BUTTON, Config.MEDIUM_WAIT)
                    self.wait_for_time(Config.VERY_SHORT_WAIT)
                    sign_in_buttons = self.driver.find_elements(*self.SIGN_IN)
                    for button in sign_in_buttons:
                        self.driver.execute_script("arguments[0].click();",
                                                   button)
                        self.wait_for_time(Config.VERY_SHORT_WAIT)
                        self.safe_click(self.NEXT_BUTTON, Config.MEDIUM_WAIT)

    def click_finish_onboarding(self):
        logger.info("Click Finish Onboarding")
        self.safe_click(self.CONTINUE_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.SHORT_WAIT)

    def link_add_bank_account(self):
        logger.info("Link Add Bank Account")
        self.safe_click(self.LINK_BANK_ACCOUNT, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.wait_until_visible(self.DISCLAIMER_TITLE, Config.MEDIUM_WAIT)
        self.safe_click(self.CONTINUE_PLAID_LINK, Config.MEDIUM_WAIT)
        self.driver.switch_to.frame(self.FRAME)
        self.safe_click(self.CONTINUE_PLAID_ACCOUNT, Config.MEDIUM_WAIT)

    def select_your_bank(self, select_your_bank):
        logger.info("Select Your Bank:" + select_your_bank)
        title = self.get_text(self.SELECT_YOUR_BANK)
        print(title)
        self.wait_for_presence_of_all_elements_located(self.SELECT_YOUR_BANK, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SELECT_YOUR_BANK, select_your_bank, Config.MEDIUM_WAIT)

    def enter_bank_credentials(self, user_name, password):
        logger.info("Enter Bank Credentials:" + user_name + password)
        self.safe_enter_text(self.BANK_USER_NAME, user_name, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.BANK_PASSWORD, password, Config.MEDIUM_WAIT)
        self.safe_click(self.SUBMIT_BANK_DETAILS, Config.MEDIUM_WAIT)

    def click_check_boxes(self):
        logger.info("Click Check Boxes For Account Type")
        self.safe_click(self.PLAID_CHECKING, Config.MEDIUM_WAIT)
        self.safe_click(self.PLAID_SINGLE, Config.MEDIUM_WAIT)
        self.safe_click(self.CONTINUE_PLAID_ACCOUNT, Config.MEDIUM_WAIT)
        self.wait_for_time(2)
        self.driver.switch_to_default_content()

    def select_on_boarding_account_type(self, account_type):
        logger.info("Select On Boarding Account Type" + account_type)
        self.safe_click(self.NEXT_ONE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.SELECT_ACCOUNT_TYPE, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.SELECT_ACCOUNT_TYPE, account_type, Config.MEDIUM_WAIT)

    def enter_onboarding_account_name(self, account_name):
        logger.info("Enter On Boarding Account Name" + account_name)
        self.safe_enter_text(self.ENTER_ACCOUNT_NAME, account_name, Config.MEDIUM_WAIT)

    def navigate_to_account_questionnaire(self):
        logger.info("Navigate To Account Questionnaire")
        self.safe_click(self.CONTINUE_BUTTON, Config.MEDIUM_WAIT)
        self.wait_until_visible(self.ON_BOARDING_TITLE, Config.MEDIUM_WAIT)

    def click_on_review(self):
        logger.info("Click On Review")
        self.safe_click(self.ACCOUNT_STATUS_LABEL, Config.MEDIUM_WAIT)

    def enter_spouse_first_last_name(self, spouse_first_name, spouse_last_name):
        logger.info("Enter Spouse Name:" + spouse_first_name + spouse_last_name)
        self.safe_enter_text(self.SPOUSE_FIRST_NAME, spouse_first_name, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.SPOUSE_LAST_NAME, spouse_last_name, Config.MEDIUM_WAIT)

    def enter_spouse_insurance_number(self, social_insurance_number):
        logger.info("Enter Spouse Insurance Number:" + social_insurance_number)
        self.safe_enter_text(self.SPOUSE_INS_NUMBER, social_insurance_number, Config.MEDIUM_WAIT)

    def enter_spouse_occupation(self, spouse_occupation):
        logger.info("Enter Spouse Occupation" + spouse_occupation)
        self.safe_enter_text(self.SPOUSE_OCCUPATION, spouse_occupation, Config.MEDIUM_WAIT)

    def select_spouse_business_type(self):
        logger.info("Select Spouse Business Type")
        business_type_dropdown = self.SPOUSE_BUSINESS_TYPE
        self.safe_click(business_type_dropdown, Config.MEDIUM_WAIT)
        self.safe_js_click(self.AGRICULTURE, Config.MEDIUM_WAIT)

    def enter_spouse_employee_name(self, spouse_employee_name):
        logger.info("Enter Spouse Employee Name" + spouse_employee_name)
        self.safe_enter_text(self.SPOUSE_EMPLOYEE_NAME, spouse_employee_name, Config.MEDIUM_WAIT)

    def select_years_of_experience(self, years_of_experience):
        logger.info("Select The Years Of Experience:" + years_of_experience)
        self.driver.execute_script("window.scrollBy(0, 280)")
        self.safe_click(self.YEARS_OF_EXPERIENCE_DROP_DOWN, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.YEARS_OF_EXPERIENCE_LIST, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.YEARS_OF_EXPERIENCE_LIST, years_of_experience, Config.MEDIUM_WAIT)

    def select_issue_date(self, yyyy, mm, dd):
        logger.info("Select Issue Date:" + yyyy + mm + dd)
        self.driver.execute_script("window.scrollBy(0, 250)")
        self.safe_click(self.ISSUE_DATE_YEAR, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.ISSUE_DATE_YEAR, yyyy, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.ISSUE_DATE_MONTH, mm, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.ISSUE_DATE_DAY, dd, Config.MEDIUM_WAIT)
        self.safe_click(self.ISSUE_CURRENT_DATE, Config.MEDIUM_WAIT)

    def select_rif_dropdown(self, rif_calculation):
        logger.info("Select RIF:" + rif_calculation)
        self.safe_click(self.RIF_CALCULATION_DROPDOWN, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.RIF_DROP_DOWN_LIST, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.RIF_DROP_DOWN_LIST, rif_calculation, Config.MEDIUM_WAIT)

    def click_account_type(self, account_type):
        logger.info("Click On Account Type:" + account_type)
        self.safe_click_from_list_of_elements(self.ACCOUNT_TYPES, account_type, Config.SHORT_WAIT)

    def select_jurisdiction(self, jurisdiction):
        logger.info("Select Jurisdiction:" + jurisdiction)
        self.safe_click(self.JURISDICTION_DROPDOWN, Config.SHORT_WAIT)
        self.safe_click_from_list_of_elements(self.JURISDICTION_LIST, jurisdiction, Config.MEDIUM_WAIT)