import allure
import pytest

from data.user_management.user_management_datasets import (
    ErrorsMessage,
    Texts,
    UsersTypes,
)
from data.user_management.user_management_users import (
    delegator_without_um,
    owner_account,
    owner_for_self,
)
from src.ui.actions.user_management_actions.user_management import UserManagementActions
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.USER_MANAGEMENT)


@allure.title("Check Main page UI")
@case_id(7873, 44504, 44516)
def test_main_page_elements():
    user_management = UserManagementActions()
    owner = owner_for_self
    user_management.log_in_and_navigate_to_um(owner.personal_number, owner.sequence_number)
    qiwa.main_page.wait_until_page_is_loaded().check_users_role_is_present().compare_user_name()
    user_management.check_subscription_text_is_present(Texts.subscription_info)


@allure.title("Check the 'Users in _' tab and 'Users in Establishment Group' tab")
@case_id(7880)
def test_all_users_table():
    user_management = UserManagementActions()
    owner = owner_for_self
    user_management.log_in_and_navigate_to_um(
        owner.personal_number, owner.sequence_number
    ).check_company_title_in_users_table(
        labor_office_id=owner.labor_office_id, seq_number=owner.sequence_number
    ).compare_number_of_users_in_table()


@allure.title(
    "Check that User redirected to the 'All establishments under your Unified ID' section"
)
@case_id(7877, 7903)
def test_user_is_redirected_to_user_details():
    owner = owner_account
    user_management = UserManagementActions()
    user_management.log_in_and_navigate_to_um(owner.personal_number, owner.sequence_number)
    qiwa.main_page.wait_until_page_is_loaded()
    user_management.navigate_to_view_details_page()


@allure.title("Check that User redirected to the owner subscription flow")
def test_user_is_redirected_to_owner_flow():
    owner = owner_account
    user_management = UserManagementActions()
    user_management.log_in_and_navigate_to_um(owner.personal_number, owner.sequence_number)
    qiwa.main_page.wait_until_page_is_loaded()
    user_management.navigate_to_owner_flow()


@allure.title("Check User has access to Establishments than subscription is Active/Inactive")
@case_id(7875, 7876, 39233, 41375, 39228)
def test_active_user_has_access():
    owner = owner_account
    user_management = UserManagementActions()
    user_management.log_in_and_navigate_to_um(owner.personal_number, owner.sequence_number)
    qiwa.main_page.wait_until_page_is_loaded().check_user_status()


@allure.title("Check 'Users in Establishment Group' table pagination")
@case_id(7878)
def test_pagination_for_users_table():
    owner = owner_account
    user_management = UserManagementActions()
    user_management.log_in_and_navigate_to_um(owner.personal_number, owner.sequence_number)
    qiwa.main_page.wait_until_page_is_loaded().check_pagination_btns()


@allure.title("Check that Group Manager displayed at the top of the users list")
@case_id(23717)
def test_that_owner_is_first_in_table():
    owner = owner_account
    user_management = UserManagementActions()
    user_management.log_in_and_navigate_to_um(owner.personal_number, owner.sequence_number)
    qiwa.main_page.wait_until_page_is_loaded().check_owner_role_in_table()


@allure.title("Check that 'User Management' page has AR localization")
@case_id(7879)
def test_localization():
    user_management = UserManagementActions()
    owner = owner_account
    user_management.log_in_and_navigate_to_um(owner.personal_number, owner.sequence_number)
    qiwa.main_page.wait_until_page_is_loaded()
    user_management.check_localization_for_main_page()


@allure.title("Check that Delegation Manager can not edit his subscription")
@case_id(39230, 39231)
@pytest.mark.parametrize("users", UsersTypes.users)
def test_manager_cannt_edit_his_subscription(users):
    owner = users
    user_management = UserManagementActions()
    user_management.log_in_and_navigate_to_um(owner.personal_number, owner.sequence_number)
    qiwa.main_page.wait_until_page_is_loaded().confirm_that_action_btn_is_missed()


@allure.title("Check that user without UM privileges can't open UM service")
@case_id(7872, 7882)
def test_error_for_user_without_um_service():
    user = delegator_without_um
    user_management = UserManagementActions()
    user_management.log_in_and_navigate_to_um(user.personal_number, user.sequence_number)
    qiwa.main_page.wait_until_page_is_loaded().check_error_message_for_um_page_without_permission(
        ErrorsMessage.user_doesnt_have_access_to_um
    ).click_header_main_menu_btn().click_change_workspace_btn()
    qiwa.workspace_page.select_company_account_with_sequence_number(sequence_number="11871")
    qiwa.open_user_management_page()
    qiwa.main_page.wait_until_page_is_loaded()


@allure.title("Check AR localization for Establishment Delegator details page")
@case_id(7904)
def test_ar_localization_for_delegator_details_page():
    user_management = UserManagementActions()
    owner = owner_account
    user_management.log_in_and_navigate_to_um(
        owner.personal_number, owner.sequence_number
    ).check_localization_for_details_page()
