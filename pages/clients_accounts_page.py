from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Config import Config
from src.base.BrowserSetup import logger
from src.utils.safe_actions import SafeActions


class ClientsAccountsPage(SafeActions):
    DOCUMENTS_BUTTON = (By.CSS_SELECTOR, "button[data-testid='ContentBoxTab-4.button']")
    ADD_DOCUMENTS_BUTTON = (By.CSS_SELECTOR, "a[data-testid='InvestorDetailCrmDocumentTabBody.add-button']")
    PRIVATE_DOCUMENT_CHECKBOX = (By.CSS_SELECTOR, "span[class='checkbox-input-icon']")
    DOCUMENT_DROPDOWN = (By.CSS_SELECTOR, "span[class='dropdown-header-button-text']")
    DROPDOWN_DOCUMENT = (By.ID, "additional_document_for_cash_withdrawal")
    FILE_NAME_ATTACHMENT = (By.CLASS_NAME, "attachment-list-item-fileName")
    UPLOAD_DOCUMENT_BUTTON = (By.CSS_SELECTOR, "label[class='file-input-label button button-with-icon white-button']")
    ADD_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "a[data-testid*='add-button']")
    APPROVE_BUTTON = (By.CSS_SELECTOR, ".workflow-box-actions [data-testid*='approve']")
    APPLY_BUTTON = (By.CSS_SELECTOR, "[aria-label='Investment Guidelines'] [type='submit']")
    ACCOUNTS_TAB = (By.CSS_SELECTOR, ".tab-view-item [href*='accounts']")
    CRM_TAB = (By.CSS_SELECTOR, ".tab-view-item [href*='crm']")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "[class='investor-table-account-name-link']")
    PROVIDE_GUIDELINES = (By.CLASS_NAME, "provide-investment-guideline-workflow-modal-button")
    CATEGORY_DROPDOWN = (By.CLASS_NAME, "investment-guideline-form-category-type-select-row")
    RULE_DROPDOWN = (By.CLASS_NAME, "investment-guideline-form-category-rule-dropdown")
    ASSET_CATEGORY = (By.ID, "asset_category")
    ADD_CLIENT = (By.CSS_SELECTOR, "#client p")
    ADD_PROSPECT = (By.CSS_SELECTOR, "#prospect p")
    RULE_ALTERNATIVE = (By.ID, "ALTERNATIVE")
    FIRST_NAME = (By.ID, "AddSingleInvestorTab.first-name-input")
    LAST_NAME = (By.ID, "AddSingleInvestorTab.last-name-input")
    SIN = (By.ID, "AddSingleInvestorTab.sin-input")
    EMAIL_INPUT = (By.ID, "AddSingleInvestorTab.email-input")
    APPOINTMENT_TIME_INPUT = (By.ID, "AppointmentForm.time-input.input")
    CREATE_EDIT_SINGLE_CLIENT = (By.CSS_SELECTOR, "[data-testid='AddSingleInvestorTab.create-and-edit-button']")
    MIN_ALLOCATION = (By.NAME, "minimumAllocation")
    MAX_ALLOCATION = (By.NAME, "maximumAllocation")
    CLIENTS_ACCOUNTS_SEARCH_INPUT = (By.NAME, "Client Search")
    CLIENTS_ACCOUNTS_SEARCH_LIST = (By.CLASS_NAME, "investor-table-body-investor-name-cell")
    CREATE_PROSPECT = (By.CSS_SELECTOR, "[data-testid='AddSingleInvestorTab.create-and-invite-button']")

    OPENING_STATUS = (By.CSS_SELECTOR, "div[class*='account-detail-opening-status'] p")
    STATUS = (By.CSS_SELECTOR, "h1>p")
    DD = (By.CSS_SELECTOR, "[placeholder='DD']")
    MM = (By.CSS_SELECTOR, "[placeholder='MM']")
    YYYY = (By.CSS_SELECTOR, "[placeholder='YYYY']")
    INVESTOR_NAME = (By.CSS_SELECTOR, ".investor-table-body-investor-name-container a")
    DURATION_DROPDOWN = (By.CSS_SELECTOR, "[data-testid='AppointmentForm.duration-dropdown.header-button']")
    LOCATION_INPUT = (By.CSS_SELECTOR, "[data-testid='AppointmentForm.location-name-input']")
    DURATION_DROPDOWN_LIST = (By.CSS_SELECTOR, "[data-testid='AppointmentForm.duration-dropdown'] li")
    SAVE_APPOINTMENT = (By.CSS_SELECTOR, "[data-testid='AppointmentForm.submit-button']")
    ACTIVE_DATE = (By.CSS_SELECTOR, "[class*='tile--active']")

    VIDEO_CONFERENCE_SWITCH = (By.CSS_SELECTOR, ".toggle-switch-container label")
    ADD_APPOINTMENT_BUTTON = (By.CSS_SELECTOR, "[data-testid*='add-appointment-button']")
    EDIT_CLIENT_DETAILS = (By.CSS_SELECTOR, "[class*='success-modal-submit-button']")
    ADD_NEW = (By.CSS_SELECTOR, "[data-testid='InvestorListPage.add-new-multi-action-button.header-button']")
    SUCCESS_MODAL_BODY_MESSAGE = (By.CSS_SELECTOR, ".modal-body [data-testid='AddSingleInvestorTabSuccessModal.title']")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "[class*='appointment-list-item-cancel-button']")
    APPOINTMENT_LIST = (By.CSS_SELECTOR, ".upcoming-appointments-list .list-item.appointment-list-item")
    CHANGES_SAVED_SUCCESSFULLY = (By.CLASS_NAME, "floating-message-text")
    UPCOMING_DATE = (By.CSS_SELECTOR, "p[data-testid *= '.date']")
    CREATED_TASK_DATE = (By.CSS_SELECTOR, "[data-testid='CrmTaskDetailPage.creation-date']")
    EDIT_PROSPECT_DETAILS = (By.CSS_SELECTOR, "[class*='success-modal-submit-button']")

    CREATED_TASK_MSG = (By.CSS_SELECTOR, "h3[data-testid*='task-item']+p")
    CREATED_VIEW_TASK = (By.CLASS_NAME, "crm-task-list-item-view-task-text")
    CREATED_TASK_STATUS = (By.CSS_SELECTOR, "h3[data-testid*='status']+p")
    CREATED_TASK_NOTES = (By.CSS_SELECTOR, "h3[data-testid*='notes-row.title']+div p")
    CREATED_TASK_PRIVATE_STATUS = (By.CSS_SELECTOR, "[data-testid='CrmTaskDetailPage.is-private']")

    MAKE_TASK_PRIVATE = (By.CSS_SELECTOR, "label.is-private-task-checkbox span")
    TASK_PRIVATE_CHECK = (By.CSS_SELECTOR, "label.is-private-task-checkbox.selected")
    UPCOMING_TIME = (By.CSS_SELECTOR, "p[data-testid*='.duration']")
    TIME_DURATION = (By.CSS_SELECTOR, "p[data-testid*='.duration-text']")

    # NOTES = (By.CSS_SELECTOR, "p[data-testid*='.appointment-notes']")
    LOCATION = (By.CSS_SELECTOR, "p[data-testid*='.location-cell']")
    CHATS_TAB = (By.CSS_SELECTOR, "button[class*='chats-header']")
    NEW_CONVERSATION = (By.CLASS_NAME, "button-with-icon-icon-container")
    COLLEAGUE_NAME = (By.CSS_SELECTOR, "input[name='colleagueTypeaheadInput']")
    COLLEAGUE_DROPDOWN = (By.CLASS_NAME, "typeahead-select-right-icon-container")
    COLLEAGUE_DROPDOWN_LIST = (
        By.CSS_SELECTOR, "ul[aria-hidden='false'].dropdown-list-item.can-be-selected p[class*='-title']")
    SELECT_COLLEAGUE = (By.CSS_SELECTOR, "p[data-testid='ThreadListSelect.item-0.title']")
    SUBJECT = (By.ID, "NewConversationModal.subject-input")
    MESSAGE = (By.ID, "message")
    SUBMIT_CONVERSATION = (By.CSS_SELECTOR, "button[data-testid='NewConversationModal.submit']")
    INBOX_SCREEN = (By.CSS_SELECTOR, "h1[data-testid='ThreadListSelect.header-text']")
    VERIFY_SUBJECT = (By.CSS_SELECTOR, "h1[data-testid='ThreadDetailHeader.subject']")
    SAVE_TASK = (By.CSS_SELECTOR, "[data-testid='CrmNoteForm.submit-button']")
    VERIFY_MESSAGE = (By.CSS_SELECTOR, "div[class*='message-box-body-content']")

    TASKS_BUTTON = (By.CSS_SELECTOR, "button[class*='tasks-header']")
    ADD_TASK_BUTTON = (By.CSS_SELECTOR, "a[data-testid*='add-button']")
    ASSIGN_TO_DROPDOWN = (By.CSS_SELECTOR, "button[data-testid*='TaskForm.assignedto-dropdown.header-button']")
    ASSIGN_TO_MEMBER = (By.CSS_SELECTOR, "li[data-testid*='TaskForm.assignedto-dropdown.item-1']")
    TASK_TEXTFIELD = (By.ID, "TaskForm.task-input")
    NOTE_TEXTFIELD = (By.CSS_SELECTOR, "[class='ql-editor ql-blank']")
    STATUS_DROPDOWN = (By.CSS_SELECTOR, "button[data-testid='TaskForm.status-dropdown.header-button']")
    STATUS_LIST = (By.CSS_SELECTOR, ".dropdown-list.bottom.visible p")
    NOTES_APPOINTMENT_TEXT = (By.CLASS_NAME, "appointment-list-item-notes")
    ASSET_ACCOUNTS_SEARCH_INPUT = (By.NAME, "asset-search")
    ASSET_ACCOUNTS_SEARCH_LIST = (By.CSS_SELECTOR, "div[class*='add-assets-page-content'] header+ul>li  button+div>button")
    ADD_CLIENT_APPOINTMENT = (By.CSS_SELECTOR, "[data-testid*='ClientSelectionRow.add-participant-button']")
    ADD_CLIENT_APPOINTMENT_INPUT = (By.CSS_SELECTOR,
                                    "[class='label input-label typeahead-input typeahead-select-header']"
                                    " input[name*='ClientSelection']")
    NOTES_INPUT = (By.ID, "appointment-form-notes-textarea")
    EMPLOYER_NAME_TEXTFIELD = (By.CSS_SELECTOR,
                               "div[class='question-form-row-container employer_name']>label>div>textarea")
    BUSINESS_TYPE_DROPDOWN = (By.CSS_SELECTOR, "[class='question-form-row-container business_type']>div>button")
    OCCUPATION_TEXTFIELD = (By.CSS_SELECTOR, "[class='question-form-row-container occupation' ]>label>div>textarea")
    ADD_RECIPIENT = (By.CLASS_NAME, "add-person_svg__plus-path")
    ADD_RECIPIENT_TITLE = (By.CSS_SELECTOR, "h1[data-testid='AddRecipientModal.title']")
    CANCEL_RECIPIENT_WINDOW = (By.CSS_SELECTOR, "button[data-testid='AddRecipientModal.cancel']")

    APPOINTMENT_NOTES = (By.CSS_SELECTOR, "p[data-testid*='.appointment-notes']")
    EDIT_APPOINTMENT = (By.CSS_SELECTOR, "button[data-testid*='.edit-button']")
    UPDATE_TIME = (By.CSS_SELECTOR, "input[id='AppointmentForm.time-input.input']")
    UPDATED_TIME = (By.CSS_SELECTOR, "p[data-testid*='.duration-cell']")
    EDIT_APPOINTMENT_SCREEN = (By.CSS_SELECTOR, "h1[data-testid='PageContentHeader.title']")

    EDIT_TASK = (By.CSS_SELECTOR, "a[class='button button-with-icon link-button white-button edit-button']")
    UPDATE_TASK_BUTTON = (By.CSS_SELECTOR, "[data-testid='CrmNoteForm.submit-button']")
    DELETE_TASK = (By.CSS_SELECTOR, "button[data-testid='CrmTaskDetailPage.delete']")
    CONFIRM_DELETE = (By.CSS_SELECTOR, "button[data-testid='DeleteButtonConfirmationModal.confirm']")
    DASHBOARD_BUTTON = (By.CSS_SELECTOR, "span[data-testid='SideNavMenu.dashboard-link.text']")

    NOTES_BUTTON = (By.CSS_SELECTOR, "button[class*='notes-header']")
    TITLE_HEADER = (By.CLASS_NAME, "content-box-tab-body-header")
    ENTER_NOTES = (By.CSS_SELECTOR, "div[class='ql-editor ql-blank']")
    SAVE_NOTES = (By.CSS_SELECTOR, "button[data-testid*='.submit-button']")
    VIEW_NOTES = (By.CSS_SELECTOR, "p[data-testid*='.view-note-text']")
    EDIT_NOTE = (By.CSS_SELECTOR, "a[data-testid='CrmNoteDetailPage.edit-button']")
    VERIFY_TAB_NAME = (By.CSS_SELECTOR, "h1[data-testid='PageContentHeader.title']")
    UPDATED_TEXTFIELD = (By.CSS_SELECTOR, "div[class='ql-editor']")
    UPDATE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='CrmNoteForm.submit-button']")
    VERIFY_CRM_NOTE = (By.CSS_SELECTOR, "div[class*='-note-body']")
    DELETE_NOTE = (By.CSS_SELECTOR, "button[data-testid='CrmNoteDetailPage.delete']")
    CANCEL_NOTE_DELETION = (By.CSS_SELECTOR, "button[data-testid='DeleteButtonConfirmationModal.cancel']")
    CONFIRMATION_POPUP = (By.CSS_SELECTOR, "h1[data-testid='DeleteButtonConfirmationModal.title']")
    DELETE_NOTES_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='.delete']")
    DELETE_NOTES_CONFIRM_TITLE = (By.CSS_SELECTOR, "h1[data-testid='DeleteButtonConfirmationModal.title']")
    CONFIRM_DELETE_NOTES = (By.CSS_SELECTOR, "button[data-testid*='.confirm']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    UPLOAD_DOCUMENT = (By.ID, "upload-file")
    Add_ATTACHMENT = (By.NAME, "FORM_ATTACHMENT_INPUT")
    ATTACHMENT_NAME = (By.CLASS_NAME, "thread-message-container")
    ADD_PARTICIPANT = (By.CSS_SELECTOR, "button[data-testid*='add-recipient-button']")
    FORWARD_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='submit']")
    ADDED_COLLEAGUE = (By.CSS_SELECTOR, "[class*='thread-detail-container'] div+ul>li")
    MARK_AS_VERIFIED = (By.CSS_SELECTOR, "button[data-testid*='.id-verification']")
    TYPE_MESSAGE_TEXTFIELD = (By.ID, "message-textarea")
    SEND_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='send-button']")
    VERIFY_NEW_MESSAGE = (By.CSS_SELECTOR, "[data-testid*='Item-0'] header+p+div>p")

    ARCHIVE_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='button.header-button']")
    ARCHIVE_CONVERSATION_BUTTON = (By.ID, "archive")
    ARCHIVED_BUTTON = (By.ID, "archived")
    NEW_ADDED_COLLEAGUE = (By.CSS_SELECTOR, "[class*='detail-header-container'] div div+ul>li:nth-child(1)")
    NOTE_ATTACHMENT_NAME = (By.CSS_SELECTOR, "[data-testid*='attachment-row.title']+ul div")

    ADD_INVESTMENT_BUTTON = (By.CSS_SELECTOR, "div[class*='investments-container']>h3+p+button>div")
    INVESTMENT_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "li[class*='item button white-button']")
    ACCOUNT_NAME_TEXTFIELD = (By.CSS_SELECTOR, "input[id*='account-name']")
    ACCOUNT_TYPE = (By.CSS_SELECTOR, "button[data-testid*='account-type-dropdown.header-button']")
    ACCOUNT_TYPE_LIST = (By.CSS_SELECTOR, "ul[data-testid*='account-type-dropdown']>li")
    ENTER_ASSET_AMOUNT = (By.CSS_SELECTOR, "label[data-testid*='cash-row.input.']")
    CURRENCY_DROPDOWN = (By.CSS_SELECTOR, "button[data-testid*='currency-dropdown']")
    CURRENCY_LIST = (By.CSS_SELECTOR, "ul[data-testid*='currency-dropdown']>li")
    ADD_INVESTMENT_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='submit-button']")
    ACCOUNT_CREATED_TITLE = (By.CSS_SELECTOR, "h1[data-testid*='BankFundTransfer.SuccessModal.title']")
    POPUP_TITLE = (By.CSS_SELECTOR, "h1[class*='confirmation-modal-title']")
    GOTO_ACCOUNT_DETAILS_BUTTON = (By.CSS_SELECTOR, "a[class*='button green-button']")
    CASH_DISPLAYED = (By.CSS_SELECTOR, "p[data-testid*='box.value']")
    ACCOUNT_TYPE_DISPLAYED = (By.CSS_SELECTOR, "p[data-testid*='AccountTypeNameRow.name']")
    SEND_TO_CLIENT_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='SendToClientButton']")
    SEND_TO_CLIENT_MESSAGE_TEXTFIELD = (By.ID, "report-message")
    FINAL_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='submit']")
    CONFIRMATION_MESSAGE = (By.CLASS_NAME, "floating-message-text")
    ADVISOR_NOTE = (By.CSS_SELECTOR, "p[class*='panel-advisor']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='delete-button']")
    INVESTMENT_ACCOUNT_LIST = (By.CSS_SELECTOR, "div[class*='investments-container']>h3+ul>li")
    ADD_ASSETS_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='add-button']")
    ADD_SELECTED_ASSETS_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='FooterContent.add-button']")
    ENTER_SELECTED_ASSET_AMOUNT = (By.CSS_SELECTOR, "label[data-testid*='purchase-price.label']")
    FIRST_ASSET_ADDED = (By.CSS_SELECTOR, "div[class*='list-container']>ul+ul>li:nth-child(2)>button+div")
    SECOND_ASSET_ADDED = (By.CSS_SELECTOR, "div[class*='list-container']>ul+ul>li:nth-child(3)>button+div")
    RIF_CALCULATION_DROPDOWN = (By.CSS_SELECTOR, "button[data-testid*='rif-calculation-mode-select.header']")
    RIF_CALCULATION_LIST = (By.CSS_SELECTOR, "ul[data-testid*='rif-calculation-mode-select']>li")
    DETAILS_TAB_BUTTON = (By.CSS_SELECTOR, "ul[class*='header-tab-view']>li:nth-child(2)>a")
    ADD_BENEFICIARY_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='add-beneficiary-button']")
    BENEFICIARY_FIRST_NAME = (By.CSS_SELECTOR, "input[data-testid*='first-name']")
    BENEFICIARY_LAST_NAME = (By.CSS_SELECTOR, "input[data-testid*='last-name']")
    BENEFICIARY_SIN = (By.ID, "AddBeneficiaryModal.sin-input")
    RELATIONSHIP_DROPDOWN = (By.CSS_SELECTOR, "button[data-testid*='relationship-dropdown']")
    RELATIONSHIP_LIST = (By.CSS_SELECTOR, "ul[data-testid*='relationship-dropdown']>li")
    ADD_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='add-button']")
    BENEFICIARY_FULL_NAME = (By.CSS_SELECTOR, "dt[data-testid*='name-term.title']")
    BENEFICIARY_RELATION = (By.CSS_SELECTOR, "dd[data-testid*='name-term.description']")
    SOCIAL_INSURANCE_NUMBER = (By.CSS_SELECTOR, "dt[data-testid*='sin']")
    BENEFICIARY_DATE_OF_BIRTH = (By.CSS_SELECTOR, "dt[data-testid*='dob-term.title']")
    EDIT_BENEFICIARY = (By.CSS_SELECTOR, "button[aria-label='Beneficiary edit button']")
    DELETE_BENEFICIARY_BUTTON = (By.CSS_SELECTOR, "button[data-testid*='remove']")
    JURISDICTION_DROPDOWN = (By.CSS_SELECTOR, "button[data-testid*='jurisdiction-select']")
    JURISDICTION_LIST = (By.CSS_SELECTOR, "ul[data-testid*='jurisdiction-select']>li")
    LOGOUT = (By.ID, "logout")
    HEADER = (By.TAG_NAME, "h1")
    USER_NAME = (By.CLASS_NAME, "auth-user-name")

    ADD_NOTE = (By.CSS_SELECTOR, "button[data-testid*='.summary-column.add-button']")
    ENTER_TEXT = (By.CSS_SELECTOR, "textarea[id *= '.note-textarea']")
    SUBMIT_NOTES_BUTTON = (By.CSS_SELECTOR, "button[data-testid ='UploadIdModal.add-button']")
    VERIFY_NOTES = (By.CSS_SELECTOR, "p[data-testid*='.note-body']")
    EDIT_NOTES = (By.CSS_SELECTOR, "button[class*='-note-box-edit-button']")
    DELETE_NOTES = (By.CSS_SELECTOR, "button[data-testid*='.delete-button']")

    DEFINE_RESULTS_MANUALLY = (By.CSS_SELECTOR, "button[data-testid='SyntoniqQuestionWizardFormStepFooter.next']")
    INVESTOR_CATEGORY = (By.CSS_SELECTOR, "button[data-testid='InvestorDnaDefineResultsModalCategorySection"
                                          ".LabeledContentRow.dropdown.header-button']")
    INVESTOR_DROPDOWN = (By.CSS_SELECTOR, "li[data-testid*='.LabeledContentRow.dropdown.item']")
    RISK_SCORE = (By.ID, "InvestorDnaDefineResultsModalRiskScoreSection.row.slider")
    DYNAMIC_RISK_RANGE = (By.CSS_SELECTOR, "span[id*='RiskRangeSection.row.slider']>span:nth-child(2)+input+span")
    INVESTOR_KNOWLEDGE = (By.CSS_SELECTOR, "button[data-testid='InvestorDnaDefineResultsModal.investment-knowledge"
                                           "-section.LabeledContentRow.dropdown.header-button']")
    INVESTOR_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[data-testid='InvestorDnaDefineResultsModal.submit']")
    VERIFY_INVESTOR_CATEGORY = (By.CSS_SELECTOR, "h2[data-testid='InvestorDnaPanel.category']")
    VERIFY_RISK_SCORE = (By.CSS_SELECTOR, "span[data-testid='InvestorDnaPanel.risk-score']")
    VERIFY_DYNAMIC_RANGE = (By.CSS_SELECTOR, "span[data-testid='InvestorDnaPanel.risk-range']")
    SEND_INVESTOR_EQ_SURVEY = (By.CSS_SELECTOR, "button[data-testid='InvestorDnaPlusSendInvitationBox.send-button']")
    SUBMIT_BUTTON_KYC = (By.CSS_SELECTOR, "button[data-testid*='submit-button']")

    ADD_ACCOUNT_TITLE = (By.CSS_SELECTOR, "h1[data-testid='AccountDetailHeader.title']")
    INPUT_MESSAGE = (By.CSS_SELECTOR, "textarea[data-testid='SendInvestorDnaPlusSurveyModal.message']")
    SUBMIT_SEND_INVESTOR = (By.CSS_SELECTOR, "button[data-testid='SendInvestorDnaPlusSurveyModal.submit']")
    Go_TO_BANK_DETAILS = (By.XPATH, "//*[text()='Go back to Client Details']")
    VERIFY_INVESTOR_NOTES = (By.CSS_SELECTOR, "p[data-testid*='-note-row.content']")
    SEND_AGAIN = (By.CSS_SELECTOR, "button[data-testid*='.send-again-button']")
    SURVEY_TITLE = (By.CSS_SELECTOR, "h1[data-testid='SendInvestorDnaPlusSurveyModal.success-modal-title']")
    RESEND_MESSAGE = (By.CSS_SELECTOR, "textarea[data-testid='ResendInvestorDnaPlusSurveyModal.message']")
    RESEND_SUBMIT = (By.CSS_SELECTOR, "button[data-testid='ResendInvestorDnaPlusSurveyModal.submit']")

    ACCOUNT_NAME_TITLE = (By.CSS_SELECTOR, "h1[data-testid='AccountDetailHeader.title']")
    EDIT_KYC_BUTTON = (By.CSS_SELECTOR, "button[data-testid='InvestorDetailKYCPanel.edit-button']")

    ADD_BANK_ACCOUNT = (By.CSS_SELECTOR, "div[class*='bank-accounts-container']>h3+p+button div")
    INSTITUTION_NUMBER = (By.ID, "AddManualBankAccountModal.institution-number")
    BRANCH_CODE = (By.ID, "AddManualBankAccountModal.branch-code")
    ACCOUNT_NUMBER = (By.ID, "AddManualBankAccountModal.account-number")
    UPLOAD_VOID_CHEQUE = (By.ID, "void-cheque-attachment")
    SUCCESSFULLY_ADDED_MESSAGE = (By.CSS_SELECTOR, "h1[class='confirm-modal-body__title']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[data-testid='ConfirmModal.footer-close-button']")
    BANK_ACCOUNT_ADDED = (By.CSS_SELECTOR, "li[class='list-item investor-household-box-bank-account']")
    KYC_TAB = (By.CSS_SELECTOR, "ul[class*='header-tab-view']>li:nth-child(4)>a")

    MARTIAL_STATUS = (By.CSS_SELECTOR, "[class*='marital-status-question-row']>div>button")
    MARTIAL_STATUS_LIST = (By.CSS_SELECTOR, "div[class*='status-question'] button +ul>li")
    DEPENDENTS_BUTTON = (By.CSS_SELECTOR, "div[class*='number_of_dependents'] button")
    DEPENDENTS_LIST = (By.CSS_SELECTOR, "div[class*='number_of_dependents'] button +ul>li")
    LOGO = (By.CSS_SELECTOR, ".logo")
    CONTAINER_EDUCATION = (By.CSS_SELECTOR, "[class*='container education']>div span")
    BACHELORS = (By.ID, "bachelors")
    DOCUMENT_TYPE_BUTTON = (By.CSS_SELECTOR, "[class*='id-document-question-row']>div>button>div")
    BIRTH_CERTIFICATE = (By.ID, "BIRTH_CERTIFICATE")
    PROVINCE_INPUT = (By.CSS_SELECTOR, "input[data-testid*='.issued-province-input.typeahead"
                                       "-header.search']")
    DOCUMENT_NO = (By.CSS_SELECTOR, "input[placeholder='Add document no']")
    PROVINCE_TYPE = (By.CSS_SELECTOR, "ul.dropdown-list.bottom.visible>li")
    TECHNOLOGY = (By.ID, "technology")
    TAX_RESIDENCY = (By.CSS_SELECTOR, "div[class*='tax-resident-question-row']>div>button")
    TAX_RESIDENCY_NO = (By.ID, "no")
    PROVINCE_TAX = (By.CSS_SELECTOR, "div[class*='province-select question-form-row-canadian-province-select'] input")
    DISCLOSURE = (By.CSS_SELECTOR, "div[class*='person-question-row']>div>button")
    DISCLOSURE_SELECT = (By.CSS_SELECTOR, "ul[data-testid*='item-3.question-0.yes-no-select']>li[id='no']")
    YEARS_OF_EMPLOYMENT = (By.CSS_SELECTOR, "[class*='years_of_employee_experience']>div button")
    PERSONAL_INCOME_TEXTFIELD = (By.CSS_SELECTOR, "div[class*=' personal_income']>label>div>input")
    FIXED_ASSETS = (By.NAME, "fixed_assets")
    LIQUID_ASSETS = (By.NAME, "liquid_assets")
    LIABILITIES = (By.NAME, "liabilities")
    TAX_RESIDENCY_CHECKBOX = (By.CSS_SELECTOR, "[data-testid*= 'canada-residency-certified-checkbox']>span")
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
    PERSONAL_DETAILS_STATUS = (By.CSS_SELECTOR, "ul[class*='panel-body-list']>li:nth-child(1) div+div>p+p")
    EMPLOYMENT_INCOME_STATUS = (By.CSS_SELECTOR, "ul[class*='panel-body-list']>li:nth-child(2) div+div>p+p")
    TAX_RESIDENCY_STATUS = (By.CSS_SELECTOR, "ul[class*='panel-body-list']>li:nth-child(3) div+div>p+p")
    DISCLOSURES_CONSENT_STATUS = (By.CSS_SELECTOR, "ul[class*='panel-body-list']>li:nth-child(4) div+div>p+p")

    def __init__(self, driver):
        super().__init__(driver)
        # self.assertion = Assertions(self.driver)

    def click_add_account_button(self):
        self.safe_click(self.ADD_ACCOUNT_BUTTON, Config.MEDIUM_WAIT)

    def click_save_appointment(self):
        self.safe_click(self.SAVE_APPOINTMENT, Config.MEDIUM_WAIT)

    def click_add_new(self):
        self.safe_click(self.ADD_NEW, Config.MEDIUM_WAIT)

    def toggle_video_conference(self, mode):
        attribute = self.driver.find_element_by_css_selector(".toggle-switch-container label").get_attribute("class")
        if str(attribute).__contains__("on"):
            if str(mode).__contains__("off"):
                self.safe_click(self.VIDEO_CONFERENCE_SWITCH, Config.MEDIUM_WAIT)

    def click_edit_client_details_button(self):
        self.safe_click(self.EDIT_CLIENT_DETAILS, Config.MEDIUM_WAIT)

    def click_edit_prospect_details(self):
        self.safe_click(self.EDIT_PROSPECT_DETAILS, Config.MEDIUM_WAIT)

    def click_create_edit_single_client(self):
        self.safe_click(self.CREATE_EDIT_SINGLE_CLIENT, Config.MEDIUM_WAIT)

    def click_create_prospect(self):
        self.safe_click(self.CREATE_PROSPECT, Config.MEDIUM_WAIT)

    def add_new(self, add_text):
        self.wait_for_time(Config.SHORT_WAIT)
        self.click_add_new()
        if str(add_text).upper().__contains__("CLIENT"):
            self.safe_click(self.ADD_CLIENT, Config.MEDIUM_WAIT)
        else:
            self.safe_click(self.ADD_PROSPECT, Config.MEDIUM_WAIT)

    def fill_client_info(self, first_name, last_name, social_insurance_no, email):
        logger.info("fill client information")
        self.safe_enter_text(self.FIRST_NAME, first_name, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.LAST_NAME, last_name, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.SIN, social_insurance_no, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.EMAIL_INPUT, email, Config.MEDIUM_WAIT)
        self.wait_for_time(3)

    def fill_prospect_info(self, first_name, last_name, email):
        logger.info("fill prospect info details")
        self.safe_enter_text(self.FIRST_NAME, first_name, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.LAST_NAME, last_name, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.EMAIL_INPUT, email, Config.MEDIUM_WAIT)

    def click_accounts_tab(self):
        self.safe_click(self.ACCOUNTS_TAB, Config.MEDIUM_WAIT)

    def click_crm_tab(self):
        logger.info("click om CRM tab")
        self.safe_click(self.CRM_TAB, Config.MEDIUM_WAIT)

    def click_add_appointment_button(self):
        self.safe_click(self.ADD_APPOINTMENT_BUTTON, Config.MEDIUM_WAIT)

    def click_on_provide_guidelines(self):
        self.safe_click(self.PROVIDE_GUIDELINES, Config.MEDIUM_WAIT)

    def click_apply(self):
        self.safe_click(self.APPLY_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.SHORT_WAIT)
        self.driver.refresh()

    def click_approve(self):
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.safe_click(self.APPROVE_BUTTON, Config.MEDIUM_WAIT)

    def select_asset_category(self):
        self.safe_click(self.CATEGORY_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_click(self.ASSET_CATEGORY, Config.MEDIUM_WAIT)

    def select_alternative_rule(self):
        logger.info(" select alternative rule")
        self.safe_click(self.RULE_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_click(self.RULE_ALTERNATIVE, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)

    def set_allocation_limits(self, minimum, maximum):
        logger.info(" set allocation limits")
        self.safe_enter_text(self.MIN_ALLOCATION, minimum, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.MAX_ALLOCATION, maximum, Config.MEDIUM_WAIT)

    def set_location(self, location_name):
        logger.info("set the location" + location_name)
        self.safe_enter_text(self.LOCATION_INPUT, location_name, Config.MEDIUM_WAIT)

    def open_account(self, account_name):
        self.wait_until_visible(self.ACCOUNT_NAME, Config.MEDIUM_WAIT)
        element_names = self.driver.find_elements_by_css_selector("[class='investor-table-account-name-link']")
        flag = False
        for element_name in element_names:
            if element_name.text.upper().__contains__(account_name.upper()):
                element_name.click()
                flag = True
                break
        assert flag, "Account not found " + account_name

    def open_investor_account(self, name):
        full_name1 = self.safe_click_from_list_of_elements(self.INVESTOR_NAME, name, Config.LONG_WAIT)
        return full_name1

    def verify_account_status(self, status):
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.wait_until_visible(self.STATUS, Config.LONG_WAIT)
        text = str(self.get_text(self.STATUS))
        self.assert_contains(text, status)
        logger.info(f"Account status as {status} is verified")

    def verify_account_opening_status_msg(self, status_message):
        self.wait_until_visible(self.OPENING_STATUS, Config.MEDIUM_WAIT)
        text = str(self.get_text(self.OPENING_STATUS))
        self.assert_equal(text, status_message)

    def sign_all_documents(self):
        logger.info("Signing Documents")
        e_sign_locator = "//*[text()='E-sign']"
        e_sign_yellow_box = "[src='/images/ballot_x.png']"
        e_sign_confirm_button = "#bind-dialog+ div span.ui-button-icon.ui-icon.confirm"
        self.wait_until_visible((By.XPATH, e_sign_locator), Config.LONG_WAIT)
        e_sign_buttons = self.driver.find_elements_by_xpath(e_sign_locator)
        for x in range(len(e_sign_buttons)):
            logger.info("Document " + str(x))
            self.safe_click((By.XPATH, e_sign_locator), Config.LONG_WAIT)
            self.wait_until_visible((By.CLASS_NAME, "one-span-iframe"), Config.LONG_WAIT)
            self.driver.switch_to.frame(self.driver.find_element_by_class_name("one-span-iframe"))
            self.wait_until_visible((By.ID, "fields"), Config.LONG_WAIT)
            val = self.driver.find_element_by_css_selector("[class='complete']").text == \
                  self.driver.find_element_by_css_selector("[class='total']").text
            if not val:
                self.wait_for_time(Config.SHORT_WAIT)
                self.wait_until_visible((By.CSS_SELECTOR, e_sign_yellow_box), Config.LONG_WAIT)
                sign_d = self.driver.find_elements_by_css_selector(e_sign_yellow_box)
                for yellow_box in sign_d:
                    self.driver.execute_script("arguments[0].click();", yellow_box)
                self.safe_click((By.CSS_SELECTOR, e_sign_confirm_button), Config.MEDIUM_WAIT)
            else:
                self.wait_until_visible((By.CSS_SELECTOR, "#global-bar span.confirm"), Config.MEDIUM_WAIT)
                self.driver.find_element_by_css_selector("#global-bar span.confirm").click()
                self.safe_click((By.CSS_SELECTOR, e_sign_confirm_button), Config.MEDIUM_WAIT)
            self.wait_for_time(Config.VERY_SHORT_WAIT)
            self.driver.switch_to_default_content()
            WebDriverWait(self.driver, Config.LONG_WAIT).until(
                expected_conditions.url_contains("kyc"))

    def verify_client_created_message(self):
        expected_message = "Client Created!"
        actual_message = self.get_text(self.SUCCESS_MODAL_BODY_MESSAGE)
        self.assert_equal(expected_message, actual_message)
        logger.info("verify client created message")

    def verify_prospect_created_message(self):
        expected_message = "Prospect Created!"
        actual_message = self.get_text(self.SUCCESS_MODAL_BODY_MESSAGE)
        self.assert_equal(expected_message, actual_message)
        logger.info("verify prospect created message")

    def verify_video_conference_switch(self, mode):
        attribute = self.driver.find_element_by_css_selector(".toggle-switch-container label").get_attribute("class")
        assert mode in attribute
        logger.info("video conference switch" + mode)

    def select_date(self, yyyy, mm, dd):
        self.safe_click(self.YYYY, Config.MEDIUM_WAIT)
        self.wait_for_time(2)
        self.safe_enter_text(self.YYYY, yyyy, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.MM, mm, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.DD, dd, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.safe_click(self.ACTIVE_DATE, Config.MEDIUM_WAIT)

    def select_duration(self, time):
        self.safe_click(self.DURATION_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.DURATION_DROPDOWN_LIST, time, Config.MEDIUM_WAIT)
        logger.info(" select duration" + time)

    def cancel_all_appointments(self):
        value = self.safe_wait_for_presence_of_all_elements_located(self.APPOINTMENT_LIST, Config.MEDIUM_WAIT)
        if value:
            elements = self.driver.find_elements(*self.APPOINTMENT_LIST)
            if self.is_element_displayed(self.APPOINTMENT_LIST):
                if len(elements) == 1:
                    self.safe_click(self.APPOINTMENT_LIST, Config.VERY_SHORT_WAIT)
                    self.safe_js_click(self.CANCEL_BUTTON, Config.MEDIUM_WAIT)
                else:
                    for element in elements:
                        self.safe_click(self.APPOINTMENT_LIST, Config.VERY_SHORT_WAIT)
                        self.safe_click(self.CANCEL_BUTTON, Config.MEDIUM_WAIT)
                        self.wait_for_time(2)

    def search_client_accounts(self, milliseconds):
        self.safe_enter_text(self.CLIENTS_ACCOUNTS_SEARCH_INPUT, milliseconds, Config.LONG_WAIT)
        self.wait_until_visible(self.CLIENTS_ACCOUNTS_SEARCH_LIST, Config.MEDIUM_WAIT)

    def set_time(self, time):
        self.safe_enter_text(self.APPOINTMENT_TIME_INPUT, time, Config.MEDIUM_WAIT)

    def verify_changes_saved_successful_message(self):
        expected_message = "Changes saved successfully!"
        actual_message = self.get_text(self.CHANGES_SAVED_SUCCESSFULLY)
        self.assert_equal(expected_message, actual_message)

    def verify_upcoming_date(self, mm, dd, yyyy):
        from datetime import datetime
        month_num = mm
        datetime_object = datetime.strptime(month_num, "%m")
        month_name = datetime_object.strftime("%b")
        if str(dd).startswith("0"):
            dd = dd[1:]
        actual_date = f"{month_name} {dd}, {yyyy}"
        expected_date = self.get_text(self.UPCOMING_DATE)
        self.assert_equal(actual_date, expected_date)

    def verify_upcoming_time(self, scheduled_time):
        expected_time = scheduled_time
        actual_time = self.get_text(self.UPCOMING_TIME)
        self.assert_equal(actual_time, expected_time)
        logger.info(f"schedule upcoming time {scheduled_time} is verified")

    def verify_time_duration(self, duration):
        actual_time_duration = duration
        expected_time_duration = self.get_text(self.TIME_DURATION)
        self.assert_equal(actual_time_duration, expected_time_duration)
        logger.info(f"duration {duration} is verified")

    def verify_location(self, location):
        actual_location = location
        expected_location = self.get_text(self.LOCATION)
        self.assert_equal(actual_location, expected_location)
        logger.info(f"location {location} is verified")

    def click_chats_new_conversation(self):
        logger.info("click on chats tab, add new conversation")
        self.safe_click(self.CHATS_TAB, Config.MEDIUM_WAIT)
        self.safe_click(self.NEW_CONVERSATION, Config.MEDIUM_WAIT)

    def enter_subject(self, subject):
        logger.info("enter message" + subject)
        self.safe_enter_text(self.SUBJECT, subject, Config.MEDIUM_WAIT)

    def enter_message(self, message):
        logger.info("enter message" + message)
        self.safe_enter_text(self.MESSAGE, message, Config.MEDIUM_WAIT)

    def enter_colleague_name(self, colleague_name):
        self.safe_enter_text(self.COLLEAGUE_NAME, colleague_name, Config.MEDIUM_WAIT)
        colleague_dropdown_list = (By.CSS_SELECTOR, "[aria-hidden='false'] .dropdown-list-item-title")
        self.safe_click_from_list_of_elements(colleague_dropdown_list, colleague_name, Config.MEDIUM_WAIT)

    def submit_conversation(self):
        logger.info("submit conversation")
        self.safe_click(self.SUBMIT_CONVERSATION, Config.MEDIUM_WAIT)

    def verify_inbox_screen(self):
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.wait_until_visible(self.INBOX_SCREEN, Config.MEDIUM_WAIT)
        logger.info("verified inbox screen")

    def verify_subject(self, subject):
        expected_subject = subject
        actual_subject = self.get_text(self.VERIFY_SUBJECT)
        self.assert_equal(expected_subject, actual_subject)
        logger.info(f"subject {subject} is verified")

    def verify_message(self, message):
        expected_message = message
        actual_message = self.get_text(self.VERIFY_MESSAGE)
        self.assert_equal(expected_message, actual_message)
        logger.info(f"message {message} is verified")

    def click_tasks_button(self):
        self.safe_click(self.TASKS_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click(self.ADD_TASK_BUTTON, Config.MEDIUM_WAIT)

    def go_to_crm_tasks(self):
        self.safe_click(self.TASKS_BUTTON, Config.MEDIUM_WAIT)

    def click_add_task_button(self):
        self.safe_click(self.ADD_TASK_BUTTON, Config.MEDIUM_WAIT)

    def select_assignto_team_member(self):
        self.safe_click(self.ASSIGN_TO_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_click(self.ASSIGN_TO_MEMBER, Config.MEDIUM_WAIT)

    def task_message(self, task_message):
        self.safe_enter_text(self.TASK_TEXTFIELD, task_message, Config.MEDIUM_WAIT)

    def note_message(self, task_note):
        self.safe_enter_text(self.NOTE_TEXTFIELD, task_note, Config.MEDIUM_WAIT)

    def select_status(self, task_status):
        self.safe_click(self.STATUS_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.STATUS_LIST, task_status, Config.MEDIUM_WAIT)

    def verify_video_conference_on_appointment(self, location):
        actual_time_duration = location
        expected_time_duration = self.get_text(self.LOCATION)
        self.assert_equal(actual_time_duration, expected_time_duration)
        logger.info(f"video conference on appointment {location} is verified")

    def verify_notes(self, notes):
        expected_notes_duration = notes
        actual_notes_duration = self.get_text(self.NOTES_APPOINTMENT_TEXT)
        self.assert_equal(actual_notes_duration, expected_notes_duration)
        logger.info(f"notes {notes} is verified")

    def enter_notes(self, notes_text):
        self.safe_enter_text(self.NOTES_INPUT, notes_text, Config.MEDIUM_WAIT)

    def add_client_appointment(self, client_name):
        self.safe_click(self.ADD_CLIENT_APPOINTMENT, Config.MEDIUM_WAIT)
        self.wait_for_time(3)
        # self.safe_click(self.ADD_CLIENT_APPOINTMENT_INPUT, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.ADD_CLIENT_APPOINTMENT_INPUT, client_name, Config.MEDIUM_WAIT)
        client_dropdown_list = (By.CSS_SELECTOR, "[aria-hidden='false'] .dropdown-list-item-title")
        self.safe_click_from_list_of_elements(client_dropdown_list, client_name, Config.MEDIUM_WAIT)

    def add_single_client(self, first_name, milliseconds, social_insurance_number, mail):
        self.add_new("Client")
        self.fill_client_info(first_name, milliseconds, social_insurance_number,
                              mail)
        self.click_create_edit_single_client()
        self.verify_client_created_message()

    def add_single_prospect(self, first_name, milliseconds, mail, yyyy, mm, dd):
        self.add_new("Prospect")
        self.fill_prospect_info(first_name, milliseconds, mail)
        self.select_date(yyyy, mm, dd)
        self.click_create_prospect()
        self.verify_prospect_created_message()

    def save_task(self):
        self.safe_click(self.SAVE_TASK, Config.MEDIUM_WAIT)
        logger.info("Saved Task Form")

    def click_view_task(self):
        self.safe_click(self.CREATED_VIEW_TASK, Config.MEDIUM_WAIT)
        logger.info("Opened Created Task")
        self.wait_for_time(Config.VERY_SHORT_WAIT)

    def verify_task_date(self, yyyy, mm, dd):
        from datetime import datetime
        month_num = mm
        datetime_object = datetime.strptime(month_num, "%m")
        month_name = datetime_object.strftime("%b")
        if str(dd).startswith("0"):
            dd = dd[1:]
        expected_date = f"{dd} {month_name.upper()} {yyyy}"
        actual_date = self.get_text(self.CREATED_TASK_DATE)
        self.assert_contains(actual_date, expected_date)

    def verify_task_message(self, task_message):
        actual_message = self.get_text(self.CREATED_TASK_MSG)
        self.assert_equal(task_message, actual_message)
        logger.info(f"task message {task_message} is verified")

    def verify_task_status(self, task_status):
        actual_message = self.get_text(self.CREATED_TASK_STATUS)
        self.assert_equal(task_status, actual_message)
        logger.info(f"task status {task_status} is verified")

    def verify_task_notes(self, task_notes):
        actual_message = self.get_text(self.CREATED_TASK_NOTES)
        self.assert_equal(task_notes, actual_message)
        logger.info(f"task notes {task_notes} is verified")

    def make_task_private(self):
        value = True
        try:
            value = self.driver.find_element(*self.TASK_PRIVATE_CHECK).is_displayed()
        except NoSuchElementException:
            value = False
        if value:
            pass
        else:
            self.safe_click(self.MAKE_TASK_PRIVATE, Config.MEDIUM_WAIT)

    def make_task_public(self):
        value = False
        try:
            value = self.driver.find_element(*self.TASK_PRIVATE_CHECK).is_displayed()
        except NoSuchElementException:
            value = True
        if value:
            self.safe_click(self.MAKE_TASK_PRIVATE, Config.MEDIUM_WAIT)
        else:
            pass

    def verify_task_private(self, status):
        actual_message = self.get_text(self.CREATED_TASK_PRIVATE_STATUS)
        self.assert_equal(status, actual_message)
        logger.info(f"task private public {status} is verified")

    def select_colleague_name(self, colleague_name):
        self.safe_click(self.COLLEAGUE_NAME, Config.MEDIUM_WAIT)
        self.wait_for_time(3)
        self.safe_enter_text(self.COLLEAGUE_NAME, colleague_name, Config.MEDIUM_WAIT)
        client_dropdown_list = (By.CSS_SELECTOR, "[aria-hidden='false'] .dropdown-list-item-title")
        self.safe_click_from_list_of_elements(client_dropdown_list, colleague_name, Config.MEDIUM_WAIT)
        logger.info("select colleague name" + colleague_name)

    def verify_task_private_public(self, status):
        actual_message = self.get_text(self.CREATED_TASK_PRIVATE_STATUS)
        self.assert_equal(status, actual_message)
        logger.info(f"task private public {status} is verified")

    def click_edit_task_button(self):
        self.safe_click(self.EDIT_TASK, Config.MEDIUM_WAIT)

    def mark_task_access(self, status):
        if str(status).upper() == "PRIVATE":
            self.make_task_private()
        else:
            self.make_task_public()

    def select_status_updated(self, update_task_status):
        self.safe_click(self.STATUS_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.STATUS_LIST, update_task_status, Config.MEDIUM_WAIT)

    def click_task_update_button(self):
        self.safe_click(self.UPDATE_TASK_BUTTON, Config.MEDIUM_WAIT)

    def add_recipient(self):
        self.safe_click(self.ADD_RECIPIENT, Config.MEDIUM_WAIT)

    def verify_add_recipient_window(self):
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.wait_until_visible(self.ADD_RECIPIENT_TITLE, Config.MEDIUM_WAIT)

    def cancel_recipient_window(self):
        self.safe_click(self.CANCEL_RECIPIENT_WINDOW, Config.MEDIUM_WAIT)

    def click_edit_appointment(self):
        self.safe_click(self.APPOINTMENT_NOTES, Config.VERY_SHORT_WAIT)
        self.safe_click(self.EDIT_APPOINTMENT, Config.MEDIUM_WAIT)

    def verify_edit_appointment_screen(self):
        self.wait_until_visible(self.EDIT_APPOINTMENT_SCREEN, Config.MEDIUM_WAIT)

    def clear_time(self):
        self.safe_enter_text(self.UPDATE_TIME, "10:30 AM", Config.VERY_SHORT_WAIT)
        self.safe_click(self.DURATION_DROPDOWN, Config.MEDIUM_WAIT)

    def update_time(self, update_time, ):
        self.safe_enter_text(self.UPDATE_TIME, update_time, Config.VERY_SHORT_WAIT)

    def verify_updated_duration(self, updated_duration):
        actual_time_duration = updated_duration
        expected_time_duration = self.get_text(self.TIME_DURATION)
        self.assert_equal(actual_time_duration, expected_time_duration)
        logger.info(f"updated duration {updated_duration} is verified")

    def verify_updated_time(self, updated_time):
        actual_time_duration = updated_time
        expected_time_duration = self.get_text(self.UPDATED_TIME)
        self.assert_equal(actual_time_duration, expected_time_duration)
        logger.info(f"updated item {updated_time} is verified")

    def click_delete_task_button(self):
        self.safe_click(self.DELETE_TASK, Config.MEDIUM_WAIT)

    def click_confirm_delete_button(self):
        self.safe_click(self.CONFIRM_DELETE, Config.MEDIUM_WAIT)

    def update_location(self, add_location):
        self.safe_enter_text(self.LOCATION_INPUT, add_location, Config.MEDIUM_WAIT)

    def verify_updated_location(self, updated_location):
        expected_updated_location = updated_location
        actual_updated_location = self.get_text(self.LOCATION)
        self.assert_equal(expected_updated_location, actual_updated_location)
        logger.info(f"updated location {updated_location} is verified")

    def click_dashboard(self):
        self.safe_click(self.DASHBOARD_BUTTON, Config.MEDIUM_WAIT)

    def click_on_notes_button(self):
        self.safe_click(self.NOTES_BUTTON, Config.MEDIUM_WAIT)

    def click_add_note(self):
        self.wait_until_visible(self.TITLE_HEADER, Config.MEDIUM_WAIT)
        self.safe_click(self.NEW_CONVERSATION, Config.MEDIUM_WAIT)

    def type_notes(self, sample_note):
        self.safe_enter_text(self.ENTER_NOTES, sample_note, Config.MEDIUM_WAIT)

    def save_notes(self):
        self.safe_click(self.SAVE_NOTES, Config.MEDIUM_WAIT)

    def view_crm_notes(self):
        self.safe_click(self.VIEW_NOTES, Config.MEDIUM_WAIT)

    def click_edit_button(self):
        self.safe_click(self.EDIT_NOTE, Config.MEDIUM_WAIT)

    def verify_update_note_tab(self, tab_name):
        expected_tab_name = tab_name
        actual_tab_name = self.get_text(self.VERIFY_TAB_NAME)
        self.assert_equal(expected_tab_name, actual_tab_name)
        logger.info(f"update note tab {tab_name} is verified")

    def clear_update_note(self, updated_note):
        self.wait_until_visible(self.UPDATED_TEXTFIELD, Config.MEDIUM_WAIT).clear()
        self.safe_enter_text(self.ENTER_NOTES, updated_note, Config.MEDIUM_WAIT)

    def upload_document(self, document_path):
        self.wait_until_visible(self.UPLOAD_DOCUMENT, Config.MEDIUM_WAIT)
        self.driver.find_element(*self.UPLOAD_DOCUMENT).send_keys(document_path)
        # self.safe_enter_text(self.UPLOAD_DOCUMENT, document_path, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        logger.info("upload the document" + document_path)

    def click_update_button(self):
        self.safe_click(self.UPDATE_BUTTON, Config.MEDIUM_WAIT)

    def verify_updated_note(self, updated_note):
        expected_note = updated_note
        actual_note = self.get_text(self.VERIFY_CRM_NOTE)
        self.assert_equal(expected_note, actual_note)
        logger.info(f"Confirmation popup message {updated_note} is verified")

    def click_delete_note(self):
        self.safe_click(self.DELETE_NOTE, Config.MEDIUM_WAIT)

    def verify_confirmation_popup(self, popup):
        expected_popup = popup
        actual_popup = self.get_text(self.CONFIRMATION_POPUP)
        self.assert_equal(expected_popup, actual_popup)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        logger.info(f"Confirmation popup message {popup} is verified")

    def verify_document_name(self, name):
        expected_name = name
        actual_name = self.get_text(self.FILE_NAME_ATTACHMENT)
        self.assert_contains(actual_name, expected_name)
        logger.info(f"document name {name} is verified")

    def verify_documents_count(self, count):
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        expected_count = count
        actual_count = len(self.driver.find_elements(*self.FILE_NAME_ATTACHMENT))
        self.assert_equal(expected_count, actual_count)
        logger.info(f" document count {count} is verified")

    def click_cancel_button(self):
        self.safe_click(self.CANCEL_NOTE_DELETION, Config.MEDIUM_WAIT)

    def click_delete_note_confirm(self):
        self.safe_click(self.DELETE_NOTE, Config.MEDIUM_WAIT)
        self.safe_click(self.CONFIRM_DELETE, Config.MEDIUM_WAIT)

    def verify_crm_note(self, sample_notes):
        expected_notes = sample_notes
        actual_notes = self.get_text(self.VERIFY_CRM_NOTE)
        self.assert_equal(expected_notes, actual_notes)
        logger.info(f"crm note {sample_notes} is verified")

    def delete_all_crm_notes(self):
        value = self.safe_wait_for_presence_of_all_elements_located(self.VIEW_NOTES, Config.MEDIUM_WAIT)
        if value:
            list = self.driver.find_elements(*self.VIEW_NOTES)
            for element in list:
                self.safe_click(self.VIEW_NOTES, Config.MEDIUM_WAIT)
                self.delete_crm_notes()
                self.wait_for_time(2)
                list = self.driver.find_elements(*self.VIEW_NOTES)

    def delete_all_crm_tasks(self):
        value = self.safe_wait_for_presence_of_all_elements_located(self.CREATED_VIEW_TASK, Config.VERY_SHORT_WAIT)
        if value:
            list = self.driver.find_elements(*self.CREATED_VIEW_TASK)
            for element in list:
                self.safe_click(self.CREATED_VIEW_TASK, Config.MEDIUM_WAIT)
                self.delete_crm_notes()
                self.wait_until_visible(self.TASKS_BUTTON, Config.MEDIUM_WAIT)
                list = self.driver.find_elements(*self.CREATED_VIEW_TASK)

    def delete_crm_notes(self):
        self.safe_click(self.DELETE_NOTES_BUTTON, Config.MEDIUM_WAIT)
        self.wait_until_visible(self.DELETE_NOTES_CONFIRM_TITLE, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.safe_click(self.CONFIRM_DELETE_NOTES, Config.MEDIUM_WAIT)
        logger.info("delete crm notes")

    def click_documents_button(self):
        self.safe_click(self.DOCUMENTS_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click(self.ADD_DOCUMENTS_BUTTON, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.SHORT_WAIT)
        logger.info("click documents button")

    def private_document_checkbox(self):
        self.safe_click(self.PRIVATE_DOCUMENT_CHECKBOX, Config.MEDIUM_WAIT)
        logger.info("Click on private document checkbox")

    def select_document_from_dropdown(self):
        self.safe_click(self.DOCUMENT_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_click(self.DROPDOWN_DOCUMENT, Config.MEDIUM_WAIT)
        logger.info("select document from dropdown")

    def click_submit_button(self):
        logger.info(" click submit button")
        self.safe_click(self.SUBMIT_BUTTON, Config.MEDIUM_WAIT)

    def click_add_attachment(self, document_path):
        self.driver.find_element(*self.Add_ATTACHMENT).send_keys(document_path)
        # self.safe_enter_text(self.UPLOAD_DOCUMENT, document_path, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        logger.info("click add attachment" + document_path)

    def verify_attachment_name(self, name):
        expected_name = name
        actual_name = self.get_text(self.ATTACHMENT_NAME)
        self.assert_contains(actual_name, expected_name)
        logger.info(f"Attachment name {name} is verified")

    def click_add_participant_button(self):
        self.safe_click(self.ADD_PARTICIPANT, Config.SHORT_WAIT)

    def click_forward_button(self):
        self.safe_click(self.FORWARD_BUTTON, Config.SHORT_WAIT)

    def verify_new_colleague_name(self, new_colleague_name):
        actual_message = new_colleague_name
        expected_message = self.get_text(self.ADDED_COLLEAGUE)
        self.assert_contains(expected_message, actual_message)
        logger.info(f"new colleague name {new_colleague_name} is verified")

    def navigate_to_investor_window_click_mark_as_verified(self):
        logger.info("navigate to investor window")
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.safe_click(self.MARK_AS_VERIFIED, Config.MEDIUM_WAIT)

    def navigate_to_id_verification_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def click_approval_button(self):
        self.wait_until_visible(self.APPROVE_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click(self.APPROVE_BUTTON, Config.MEDIUM_WAIT)

    def send_message(self, new_message):
        self.safe_enter_text(self.TYPE_MESSAGE_TEXTFIELD, new_message, Config.VERY_SHORT_WAIT)
        self.safe_click(self.SEND_BUTTON, Config.VERY_SHORT_WAIT)
        self.wait_for_time(Config.SHORT_WAIT)
        logger.info("send message" + new_message)

    def verify_new_message(self, new_message):
        expected_message = new_message
        actual_message = self.get_text(self.VERIFY_NEW_MESSAGE)
        self.assert_equal(expected_message, actual_message)
        logger.info(f"new message {new_message} is verified")

    def click_archive_conversation_button(self):
        self.safe_click(self.ARCHIVE_BUTTON, Config.SHORT_WAIT)
        self.safe_click(self.ARCHIVE_CONVERSATION_BUTTON, Config.SHORT_WAIT)

    def open_archived_conversation(self):
        self.safe_click(self.INBOX_SCREEN, Config.SHORT_WAIT)
        self.safe_click(self.ARCHIVED_BUTTON, Config.SHORT_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)

    def verify_new_added_colleague(self, new_colleague_name):
        expected_message = new_colleague_name
        actual_message = self.get_text(self.NEW_ADDED_COLLEAGUE)
        self.assert_equal(expected_message, actual_message)
        logger.info(f"new colleague name {new_colleague_name} is verified")

    def click_new_conversation(self):
        self.safe_click(self.NEW_CONVERSATION, Config.VERY_SHORT_WAIT)

    def verify_successfully_message(self):
        expected_message = "Changes saved successfully!"
        actual_message = self.get_text(self.CHANGES_SAVED_SUCCESSFULLY)
        self.assert_equal(expected_message, actual_message)
        logger.info("verify successful message")

    def verify_note_attachment_name(self, name):
        expected_name = name
        actual_name = self.get_text(self.NOTE_ATTACHMENT_NAME)
        self.assert_equal(expected_name, actual_name)
        self.wait_for_time(Config.SHORT_WAIT)
        logger.info(f"Note attachment name {name} is verified")

    def delete_existing_investment_account(self):
        value = self.safe_wait_for_presence_of_all_elements_located(self.INVESTMENT_ACCOUNT_LIST, Config.MEDIUM_WAIT)
        if value:
            elements = self.driver.find_elements(*self.INVESTMENT_ACCOUNT_LIST)
            if self.is_element_displayed(self.INVESTMENT_ACCOUNT_LIST):
                if len(elements) == 1:
                    self.safe_click(self.INVESTMENT_ACCOUNT_LIST, Config.VERY_SHORT_WAIT)
                    self.safe_click(self.DELETE_BUTTON, Config.MEDIUM_WAIT)
                    self.safe_click(self.CONFIRM_DELETE, Config.MEDIUM_WAIT)
                else:
                    for element in elements:
                        self.safe_click(self.INVESTMENT_ACCOUNT_LIST, Config.VERY_SHORT_WAIT)
                        self.safe_click(self.DELETE_BUTTON, Config.MEDIUM_WAIT)
                        self.safe_click(self.CONFIRM_DELETE, Config.MEDIUM_WAIT)
                        self.wait_for_time(2)

    def click_add_assets_button(self):
        self.safe_click(self.ADD_ASSETS_BUTTON, Config.MEDIUM_WAIT)

    def search_assets_accounts(self, asset_full_name):
        self.safe_enter_text(self.ASSET_ACCOUNTS_SEARCH_INPUT, asset_full_name, Config.LONG_WAIT)
        self.wait_until_visible(self.ASSET_ACCOUNTS_SEARCH_LIST, Config.MEDIUM_WAIT)

    def select_asset_account(self, asset_name):
        self.safe_click_from_list_of_elements(self.ASSET_ACCOUNTS_SEARCH_LIST, asset_name, Config.MEDIUM_WAIT)

    def click_add_to_basket_button(self):
        logger.info("click add to basket button")
        self.wait_until_visible(self.FINAL_SUBMIT_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click(self.FINAL_SUBMIT_BUTTON, Config.MEDIUM_WAIT)

    def click_add_assets_selected_button(self):
        logger.info(" click add assets button")
        self.safe_click(self.ADD_SELECTED_ASSETS_BUTTON, Config.MEDIUM_WAIT)

    def enter_selected_asset_market_value(self, asset_market_value):
        logger.info("enter selected market value" + asset_market_value)
        self.safe_enter_text(self.ENTER_SELECTED_ASSET_AMOUNT, asset_market_value, Config.MEDIUM_WAIT)

    def verify_first_asset_added(self, verify_first_asset_value):
        expected_value = verify_first_asset_value
        actual_value = self.get_text(self.FIRST_ASSET_ADDED)
        self.assert_equal(expected_value, actual_value)
        logger.info(f"first assest added {verify_first_asset_value} is verified")

    def select_rip_calulation_based_on(self, rif_based_on):
        logger.info("select rip calculation" + rif_based_on)
        self.safe_click(self.RIF_CALCULATION_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.RIF_CALCULATION_LIST, rif_based_on, Config.MEDIUM_WAIT)

    def click_details_tab(self):
        logger.info("click the details tab")
        self.safe_click(self.DETAILS_TAB_BUTTON, Config.MEDIUM_WAIT)

    def click_add_beneficiary_button(self):
        logger.info("click and beneficiary")
        self.safe_click(self.ADD_BENEFICIARY_BUTTON, Config.MEDIUM_WAIT)

    def enter_first_last_beneficiary_name(self, beneficiary_first_name, beneficiary_last_name):
        self.safe_enter_text(self.BENEFICIARY_FIRST_NAME, beneficiary_first_name, Config.SHORT_WAIT)
        self.safe_enter_text(self.BENEFICIARY_LAST_NAME, beneficiary_last_name, Config.SHORT_WAIT)
        logger.info("enter first and last beneficiary name")

    def enter_social_insurance_number(self, social_insurance_number):
        logger.info("enter social insurance number" + social_insurance_number)
        self.safe_enter_text(self.BENEFICIARY_SIN, social_insurance_number, Config.SHORT_WAIT)

    def select_beneficiary_relationship(self, relationship_name):
        logger.info("select beneficiary relationship" + relationship_name)
        self.safe_click(self.RELATIONSHIP_DROPDOWN, Config.SHORT_WAIT)
        self.safe_click_from_list_of_elements(self.RELATIONSHIP_LIST, relationship_name, Config.SHORT_WAIT)

    def click_add_button(self):
        logger.info("click add button")
        self.safe_click(self.ADD_BUTTON, Config.SHORT_WAIT)

    def verify_beneficiary_name(self, beneficiary_full_name):
        expected_name = beneficiary_full_name
        actual_name = self.get_text(self.BENEFICIARY_FULL_NAME)
        self.assert_equal(expected_name, actual_name)
        logger.info(f"beneficiary name {beneficiary_full_name} is verified")

    def verify_beneficiary_relation(self, relationship_name):
        expected_name = relationship_name
        actual_name = self.get_text(self.BENEFICIARY_RELATION)
        self.assert_equal(expected_name, actual_name)
        logger.info(f"relationship name {relationship_name} is verified")

    def verify_social_insurance_number(self, social_insurance_number):
        expected_number = social_insurance_number
        actual_number = self.get_text(self.SOCIAL_INSURANCE_NUMBER)
        self.assert_equal(expected_number, actual_number)
        logger.info(f"Social insurance number {social_insurance_number} is verified")

    def verify_beneficiary_date_of_birth(self, mm, dd, yyyy):
        from datetime import datetime
        month_num = mm
        datetime_object = datetime.strptime(month_num, "%m")
        month_name = datetime_object.strftime("%b")
        if str(dd).startswith("0"):
            dd = dd[1:]
        actual_date = f"{month_name} {dd}, {yyyy}"
        expected_date = self.get_text(self.BENEFICIARY_DATE_OF_BIRTH)
        self.assert_equal(actual_date, expected_date)

    def click_edit_beneficiary_button(self):
        logger.info("click edit beneficiary ")
        self.safe_click(self.EDIT_BENEFICIARY, Config.MEDIUM_WAIT)

    def delete_beneficiary_button(self):
        logger.info("delete and confirm beneficiary")
        self.safe_click(self.DELETE_BENEFICIARY_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click(self.CONFIRM_DELETE, Config.MEDIUM_WAIT)

    def select_jurisdiction(self, jurisdiction):
        logger.info("select jurisdiction dropdown" + jurisdiction)
        self.safe_click(self.JURISDICTION_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.JURISDICTION_LIST, jurisdiction, Config.MEDIUM_WAIT)

    def logout(self):
        logger.info("logout from the account")
        self.safe_click(self.USER_NAME, Config.MEDIUM_WAIT)
        self.safe_click(self.LOGOUT, Config.MEDIUM_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)

    def click_add_investment_button(self):
        logger.info("click add investment button")
        self.driver.execute_script("window.scrollBy(0, 250)")
        self.wait_until_visible(self.ADD_INVESTMENT_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click(self.ADD_INVESTMENT_BUTTON, Config.MEDIUM_WAIT)

    def click_investment_account_button(self):
        logger.info("click investment account button")
        self.safe_click(self.INVESTMENT_ACCOUNT_BUTTON, Config.MEDIUM_WAIT)

    def enter_account_name(self, account_name):
        logger.info("enter account name" + account_name)
        self.safe_enter_text(self.ACCOUNT_NAME_TEXTFIELD, account_name, Config.MEDIUM_WAIT)

    def select_account_type(self, account_type):
        logger.info("select account type" + account_type)
        self.safe_click(self.ACCOUNT_TYPE, Config.SHORT_WAIT)
        self.safe_click_from_list_of_elements(self.ACCOUNT_TYPE_LIST, account_type, Config.SHORT_WAIT)

    def enter_asset_market_value(self, market_value):
        logger.info("enter asset market value" + market_value)
        self.safe_enter_text(self.ENTER_ASSET_AMOUNT, market_value, Config.SHORT_WAIT)

    def select_currency(self, currency):
        logger.info(" select currency dropdown" + currency)
        self.safe_click(self.CURRENCY_DROPDOWN, Config.SHORT_WAIT)
        self.safe_click_from_list_of_elements(self.CURRENCY_LIST, currency, Config.SHORT_WAIT)

    def click_add_investment_account_button(self):
        logger.info("click add investment account")
        self.safe_click(self.ADD_INVESTMENT_ACCOUNT_BUTTON, Config.MEDIUM_WAIT)

    def verify_investment_account_created(self, popup_message):
        self.wait_until_visible(self.POPUP_TITLE, Config.MEDIUM_WAIT)
        expected_message = popup_message
        actual_message = self.get_text(self.ACCOUNT_CREATED_TITLE)
        self.assert_equal(expected_message, actual_message)
        logger.info(f"Investment account popup message {popup_message} is verified")

    def click_goto_account_details_button(self):
        logger.info("click on goto account details")
        self.safe_click(self.GOTO_ACCOUNT_DETAILS_BUTTON, Config.SHORT_WAIT)

    def verify_market_value(self, total_market_value):
        print(total_market_value)
        expected_value = total_market_value
        actual_value = self.get_text(self.CASH_DISPLAYED)
        self.assert_equal(expected_value, actual_value)
        logger.info(f"Market place value {total_market_value} is verified")

    def verify_account_type(self, account_type):
        expected_type = account_type
        actual_type = self.get_text(self.ACCOUNT_TYPE_DISPLAYED)
        self.assert_equal(expected_type, actual_type)
        logger.info(f"Account type {account_type} is verified")

    def click_send_to_client_button(self):
        self.safe_click(self.SEND_TO_CLIENT_BUTTON, Config.MEDIUM_WAIT)
        logger.info("clicked on send client button")

    def enter_message_to_client(self, message):
        logger.info("enter message to client")
        self.safe_enter_text(self.SEND_TO_CLIENT_MESSAGE_TEXTFIELD, message, Config.MEDIUM_WAIT)

    def click_send_button(self):
        logger.info("click on send button")
        self.safe_click(self.FINAL_SUBMIT_BUTTON, Config.MEDIUM_WAIT)

    def verify_report_sent_successfully_message(self, confirmation_message):
        expected_message = confirmation_message
        actual_message = self.get_text(self.CONFIRMATION_MESSAGE)
        self.assert_equal(expected_message, actual_message)
        logger.info(f"Report sent successfully message {confirmation_message} is verified")

    def verify_message_sent(self, message):
        expected_message = message
        actual_message = self.get_text(self.ADVISOR_NOTE)
        self.assert_equal(expected_message, actual_message)
        logger.info(f"Message sent {message} is verified")

    def delete_investment_account(self):
        logger.info("delete the investment account and confirm")
        self.safe_click(self.DELETE_BUTTON, Config.MEDIUM_WAIT)
        self.safe_click(self.CONFIRM_DELETE, Config.MEDIUM_WAIT)

    def add_note(self):
        logger.info("add the note")
        self.safe_click(self.ADD_NOTE, Config.MEDIUM_WAIT)

    def enter_note(self, notes):
        logger.info("enter the notes" + notes)
        self.safe_enter_text(self.ENTER_TEXT, notes, Config.MEDIUM_WAIT)

    def submit_notes(self):
        logger.info("submit the notes")
        self.safe_click(self.SUBMIT_NOTES_BUTTON, Config.MEDIUM_WAIT)

    def edit_notes(self):
        logger.info("edit the notes")
        self.safe_click(self.EDIT_NOTES, Config.MEDIUM_WAIT)

    def update_notes(self, update_notes):
        logger.info("update the notes")
        self.safe_enter_text(self.ENTER_TEXT, update_notes, Config.MEDIUM_WAIT)

    def delete_notes(self):
        self.safe_click(self.DELETE_NOTES, Config.MEDIUM_WAIT)
        self.safe_click(self.CONFIRM_DELETE, Config.MEDIUM_WAIT)
        logger.info("delete the notes and confirm delete")

    def verify_client_notes(self, notes):
        expected_notes_duration = notes
        actual_notes_duration = self.get_text(self.VERIFY_NOTES)
        self.assert_equal(actual_notes_duration, expected_notes_duration)
        logger.info(f"verify client {notes} is verified")

    def verify_updated_client_notes(self, notes):
        expected_notes_duration = notes
        actual_notes_duration = self.get_text(self.VERIFY_NOTES)
        self.assert_equal(actual_notes_duration, expected_notes_duration)
        logger.info(f"verify client {notes} is verified")

    def click_define_results_manually(self):
        logger.info("click define results manually")
        self.safe_click(self.DEFINE_RESULTS_MANUALLY, Config.MEDIUM_WAIT)

    def select_investor_list(self, select_category):
        logger.info("select investor list category" + select_category)
        self.safe_click(self.INVESTOR_CATEGORY, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.INVESTOR_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.INVESTOR_DROPDOWN, select_category, Config.MEDIUM_WAIT)

    def select_investment_knowledge(self, investment_knowledge):
        logger.info("select investor knowledge" + investment_knowledge)
        self.safe_click(self.INVESTOR_KNOWLEDGE, Config.MEDIUM_WAIT)
        self.wait_for_presence_of_all_elements_located(self.INVESTOR_DROPDOWN, Config.MEDIUM_WAIT)
        self.safe_click_from_list_of_elements(self.INVESTOR_DROPDOWN, investment_knowledge, Config.MEDIUM_WAIT)

    def click_risk_score(self):
        logger.info("click on risk score button")
        self.safe_click(self.RISK_SCORE, Config.MEDIUM_WAIT)

    def click_dynamic_risk_score(self):
        logger.info("click on dynamic risk score")
        self.safe_click(self.DYNAMIC_RISK_RANGE, Config.MEDIUM_WAIT)

    def submit_investor_details(self):
        logger.info("submit investor details")
        self.safe_click(self.INVESTOR_SUBMIT_BUTTON, Config.MEDIUM_WAIT)

    def verify_investor(self, select_category):
        self.wait_for_time(3)
        self.driver.execute_script("window.scrollBy(0, 270)")
        expected_investor_name = select_category
        actual_investor_name = self.get_text(self.VERIFY_INVESTOR_CATEGORY)
        self.assert_equal(expected_investor_name, actual_investor_name)
        logger.info(f"verify investor {select_category} is verified")

    def verify_risk_score(self, risk_score):
        expected_investor_name = risk_score
        actual_investor_name = self.get_text(self.VERIFY_RISK_SCORE)
        self.assert_equal(expected_investor_name, actual_investor_name)
        logger.info(f"verify risk score is {risk_score} is verified")

    def verify_dynamic_range(self, dynamic_range):
        logger.info("verify dynamic range" + dynamic_range)
        expected_investor_name = dynamic_range
        actual_investor_name = self.get_text(self.VERIFY_DYNAMIC_RANGE)
        self.assert_equal(expected_investor_name, actual_investor_name)

    def click_send_investor(self):
        self.safe_click(self.SEND_INVESTOR_EQ_SURVEY, Config.MEDIUM_WAIT)
        logger.info("send investor EQ")

    def enter_note_message(self, input_message):
        logger.info("enter notes message" + input_message)
        self.safe_enter_text(self.INPUT_MESSAGE, input_message, Config.MEDIUM_WAIT)

    def submit_send_investor_message(self):
        logger.info("submit send investor message")
        self.safe_click(self.SUBMIT_SEND_INVESTOR, Config.MEDIUM_WAIT)

    def go_to_bank_details(self):
        self.wait_for_time(2)
        self.safe_click(self.Go_TO_BANK_DETAILS, Config.MEDIUM_WAIT)
        logger.info("navigated to bank details")

    def verify_investor_notes(self, input_message):
        logger.info("verified investor notes" + input_message)
        expected_investor_name = input_message
        actual_investor_name = self.get_text(self.VERIFY_INVESTOR_NOTES)
        self.assert_equal(expected_investor_name, actual_investor_name)

    def send_again(self):
        logger.info("send investor message again")
        self.safe_click(self.SEND_AGAIN, Config.MEDIUM_WAIT)

    def update_note_message(self, update_input_message):
        logger.info("update note message" + update_input_message)
        self.safe_enter_text(self.RESEND_MESSAGE, update_input_message, Config.MEDIUM_WAIT)

    def submit_re_send_investor_message(self):
        logger.info("submit resend investor message")
        self.safe_click(self.RESEND_SUBMIT, Config.MEDIUM_WAIT)

    def verify_test(self):
        title = self.get_text(self.SURVEY_TITLE)
        print(title)
        logger.info("verify title " + title)

    def verify_updated_investor_notes(self, updated_input_message):
        expected_investor_name = updated_input_message
        actual_investor_name = self.get_text(self.VERIFY_INVESTOR_NOTES)
        self.assert_equal(expected_investor_name, actual_investor_name)
        logger.info(f"updated investor notes {updated_input_message} is verified")

    def click_submit_button_kyc(self):
        self.safe_click(self.SUBMIT_BUTTON_KYC, Config.MEDIUM_WAIT)

    def select_currecy(self, currency):
        self.safe_click(self.CURRENCY_DROPDOWN, Config.SHORT_WAIT)
        self.safe_click_from_list_of_elements(self.CURRENCY_LIST, currency, Config.SHORT_WAIT)

    def click_add_invesment_account_button(self):
        self.safe_click(self.ADD_INVESTMENT_ACCOUNT_BUTTON, Config.MEDIUM_WAIT)

    def select_assect_account(self, asset_name):
        self.safe_click_from_list_of_elements(self.ASSET_ACCOUNTS_SEARCH_LIST, asset_name, Config.MEDIUM_WAIT)

    def select_open_account_type(self, account_type):
        self.safe_click(self.ACCOUNT_TYPE, Config.SHORT_WAIT)
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        try:
            self.wait_for_presence_of_all_elements_located(self.ACCOUNT_TYPE_LIST, Config.MEDIUM_WAIT)
        except TimeoutException:
            pass
        element_list = self.driver.find_elements(*self.ACCOUNT_TYPE_LIST)
        if len(element_list) == 0:
            full_name = "null"
        else:
            for web_element in element_list:
                if web_element.text.upper() == (str(account_type).upper()):
                    full_name = web_element.text
                    web_element.click()
                    logger.info(f"Clicked on {self.ACCOUNT_TYPE_LIST} with {account_type}")
                    break
        return full_name

    def click_add_bank_account_button(self):
        logger.info("CLick on Add Bank Account Button")
        self.safe_click(self.ADD_BANK_ACCOUNT, Config.MEDIUM_WAIT)

    def enter_bank_details(self, institution_number, branch_code, account_number):
        logger.info("Enter Bank Details:" + institution_number + branch_code + account_number)
        self.safe_enter_text(self.INSTITUTION_NUMBER, institution_number, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.BRANCH_CODE, branch_code, Config.MEDIUM_WAIT)
        self.safe_enter_text(self.ACCOUNT_NUMBER, account_number, Config.MEDIUM_WAIT)

    def upload_void_cheque(self, document_path):
        logger.info("Upload Void Cheque:" + document_path)
        self.driver.find_element(*self.UPLOAD_VOID_CHEQUE).send_keys(document_path)
        self.wait_for_time(Config.VERY_SHORT_WAIT)

    def verify_account_added_successfully(self, added_message):
        logger.info("Verify Account Added" + added_message)
        expected_message = added_message
        actual_message = self.get_text(self.SUCCESSFULLY_ADDED_MESSAGE)
        self.assert_equal(expected_message, actual_message)

    def click_close_button(self):
        logger.info("Click On Close Button")
        self.safe_click(self.CLOSE_BUTTON, Config.MEDIUM_WAIT)

    def verify_currency(self, currency):
        expected_message = currency
        actual_message = self.get_text(self.BANK_ACCOUNT_ADDED)
        self.assert_contains(actual_message, expected_message)

    def click_kyc_tab(self):
        self.safe_click(self.KYC_TAB, Config.MEDIUM_WAIT)

    def click_edit_kyc_button(self):
        self.safe_click(self.EDIT_KYC_BUTTON, Config.MEDIUM_WAIT)

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
        self.wait_for_time(Config.VERY_SHORT_WAIT)
        self.safe_js_click(self.CONTAINER_EDUCATION, Config.MEDIUM_WAIT)
        self.safe_js_click(self.BACHELORS, Config.MEDIUM_WAIT)

    def select_document_type(self):
        logger.info("Select The Document Type ")
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

    def verify_personal_details_status(self, status):
        logger.info("Verify Personal Details Status:" + status)
        expected_message = status
        actual_message = self.get_text(self.PERSONAL_DETAILS_STATUS)
        self.assert_equal(expected_message, actual_message)

    def verify_employment_income_status(self, status):
        logger.info("Verify Employment Income Status:" + status)
        expected_message = status
        actual_message = self.get_text(self.EMPLOYMENT_INCOME_STATUS)
        self.assert_equal(expected_message, actual_message)

    def verify_tax_residency_status(self, status):
        logger.info("Verify Tax Residency Status:" + status)
        expected_message = status
        actual_message = self.get_text(self.TAX_RESIDENCY_STATUS)
        self.assert_equal(expected_message, actual_message)

    def verify_disclosures_consent_status(self, status):
        logger.info("Verify Disclosures Consent Status:" + status)
        expected_message = status
        actual_message = self.get_text(self.DISCLOSURES_CONSENT_STATUS)
        self.assert_equal(expected_message, actual_message)
