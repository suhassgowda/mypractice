import pytest
from Config import TestData
from src.base.BrowserSetup import BrowserSetup
from src.pages.add_account_page import AddAccountPage
from src.pages.clients_accounts_page import ClientsAccountsPage
from src.pages.dashboard_page import DashboardPage
from src.pages.login_page import LoginPage
from datetime import datetime


class CRM010AddPrivateTaskForTeamMemberInProspect(BrowserSetup):

    @pytest.mark.crm
    @pytest.mark.pascal
    # @pytest.mark.skip
    def test_crm_010_add_private_task_for_team_member_in_prospect(self):
        import time
        milliseconds = int(round(time.time() * 1000))
        date = datetime.utcnow()
        dd = date.strftime('%d')
        mm = date.strftime('%m')
        yyyy = "2000" # Birth Date should be before 2003
        YYYY = date.strftime('%Y')
        first_name = "Prospect"
        full_name = "Prospect " + str(milliseconds)
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
        self.clientAccounts.add_single_prospect(first_name, milliseconds,
                                                "zenq" + str(milliseconds) + "@mailinator.com", yyyy, mm, dd)
        self.clientAccounts.click_edit_prospect_details()
        self.dashboard.goto_clients_accounts()
        self.clientAccounts.search_client_accounts(full_name)
        self.clientAccounts.open_investor_account(full_name)
        # Click on 'CRM' button
        self.clientAccounts.click_crm_tab()
        # Click on task button
        self.clientAccounts.go_to_crm_tasks()
        self.clientAccounts.delete_all_crm_tasks()
        # Click on add task
        self.clientAccounts.click_add_task_button()
        # Assign to a  team member from 'Assign to' dropdown
        self.clientAccounts.select_assignto_team_member()
        # Write the task to be done in the 'task' textfield
        self.clientAccounts.task_message(task_message)
        # Select the status from 'status' drop down
        self.clientAccounts.select_status(task_status)
        # Select a date from 'calender' widget
        self.clientAccounts.select_date(YYYY, mm, dd)
        # Write a note in 'Notes' textfield
        self.clientAccounts.note_message(task_note)
        # Click on save button
        self.clientAccounts.save_task()
        # Verify if changes saved successfully message is displayed in the CRM tab
        self.clientAccounts.verify_changes_saved_successful_message()
        # Click on view task button
        self.clientAccounts.click_view_task()
        # Verify if the selected date is displayed in the task tab
        self.clientAccounts.verify_task_date(YYYY, mm, dd)
        # Verify is the make private check box is enabled/ticked
        self.clientAccounts.verify_task_private_public("Yes")
