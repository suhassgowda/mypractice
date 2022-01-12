import pytest

from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from datetime import datetime


class CRM008AddTaskEditAndMakeItPrivateAndDelete(BrowserSetup):

    @pytest.mark.crm
    @pytest.mark.pascal
    # @pytest.mark.skip
    def test_crm_008_add_task_edit_to_private_delete(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        date = datetime.now()
        dd = date.strftime('%d')
        mm = date.strftime('%m')
        yyyy = date.strftime('%Y')
        first_name = "Client"
        social_insurance_number = "560 141 111"
        task_message = "test zenq"
        task_note = "ZENQ Testing"
        task_status = "In Progress"
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
        # Click On 'CRM' button
        self.clientAccounts.click_crm_tab()
        # Click on task button
        self.clientAccounts.go_to_crm_tasks()
        self.clientAccounts.delete_all_crm_tasks()
        self.clientAccounts.click_add_task_button()
        # Create a public task (By unchecking/disabling the Make Private check box )
        self.clientAccounts.mark_task_access("public")
        self.clientAccounts.select_assignto_team_member()
        self.clientAccounts.task_message(task_message)
        self.clientAccounts.select_status(task_status)
        self.clientAccounts.select_date(yyyy, mm, dd)
        self.clientAccounts.note_message(task_note)
        self.clientAccounts.save_task()
        # Click on view task button
        self.clientAccounts.click_view_task()
        # Click on edit button
        self.clientAccounts.click_edit_task_button()
        # Enable/tick the make private checkbox and click on update
        self.clientAccounts.mark_task_access("private")
        self.clientAccounts.click_task_update_button()
        # Verify if the 'changes saved successfully' message is displayed
        self.clientAccounts.verify_changes_saved_successful_message()
        # Verify if the 'Is Private' option is changed to 'Yes' in task tab
        self.clientAccounts.verify_task_private_public("Yes")
        # click on delete button
        self.clientAccounts.click_delete_task_button()
        self.clientAccounts.click_confirm_delete_button()
        # Verify if the 'task deleted' message is displayed
        # self.clientAccounts.verify_successfully_message()
