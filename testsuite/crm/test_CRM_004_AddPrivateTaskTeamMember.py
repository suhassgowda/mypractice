import pytest
from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from datetime import datetime


class CRM004AddPrivateTaskTeamMember(BrowserSetup):

    @pytest.mark.crm
    @pytest.mark.pascal
    @pytest.mark.xfail(reason='PAS-444 updated due date not displayed in the task tab')
    def test_crm_004_add_private_task_team_member(self):
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
        # Click on 'CRM' button
        self.clientAccounts.click_crm_tab()
        # Click on task button
        self.clientAccounts.go_to_crm_tasks()
        self.clientAccounts.delete_all_crm_tasks()
        self.clientAccounts.click_add_task_button()
        # Click on add task
        self.clientAccounts.make_task_private()
        # Assign to a  team member from 'Assign to' dropdown
        self.clientAccounts.select_assignto_team_member()
        # Write the task to be done in the 'task' textfield
        self.clientAccounts.task_message(task_message)
        # Select the status from 'status' drop down
        self.clientAccounts.select_status(task_status)
        # Select a date from 'calender' widget
        self.clientAccounts.select_date(yyyy, mm, dd)
        # Write a note in 'Notes' textfield
        self.clientAccounts.note_message(task_note)
        # Click on save button
        self.clientAccounts.save_task()
        # Verify if changes saved successfully message is displayed in the CRM tab
        self.clientAccounts.verify_changes_saved_successful_message()
        # Click on view task button
        self.clientAccounts.click_view_task()
        # Verify if the selected date is displayed in the task tab
        self.clientAccounts.verify_task_date(yyyy, mm, dd)
        # Verify if the task message is displayed in the task tab
        self.clientAccounts.verify_task_message(task_message)
        # Verify if the selected status is displayed in the task tab
        self.clientAccounts.verify_task_status("IN_PROGRESS")
        # Verify if the note written is displayed in the notes tab
        self.clientAccounts.verify_task_notes(task_note)
        # Verify is the make private check box is enabled/ticked
        self.clientAccounts.verify_task_private_public("Yes")
