import time

import allure
import pytest

from data.constants import Language
from data.user_management import user_management_data
from data.user_management.user_management_datasets import (
    ErrorsMessage,
    Privileges,
    SelfSubscriptionData,
    Texts,
    UsersTypes,
)
from data.user_management.user_management_users import (
    delegator_with_um,
    delegator_without_um,
    owner_account,
    owner_account_with_another_company,
    owner_for_self,
    user_type_three_employee,
)
from src.ui.actions.user_management_actions.user_management import UserManagementActions
from src.ui.qiwa import qiwa
from tests.ui.user_management.conftest import (
    delete_self_subscription,
    log_in_and_open_establishment_account,
    log_in_and_open_user_management,
)
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.USER_MANAGEMENT)


@allure.title("Check Main page UI")
@case_id(7873, 44504, 44516)
def test_main_page_elements():
    user_management = UserManagementActions()
    owner = owner_for_self
    log_in_and_open_user_management(owner, Language.EN)
    qiwa.main_page.check_users_role_is_present().compare_user_name()
    user_management.check_subscription_text_is_present(Texts.subscription_info)


@allure.title("Check the 'Users in _' tab and 'Users in Establishment Group' tab")
@case_id(7880)
def test_all_users_table():
    user_management = UserManagementActions()
    owner = owner_for_self
    log_in_and_open_user_management(owner, Language.EN)
    user_management.check_company_title_in_users_table(
        labor_office_id=owner.labor_office_id, seq_number=owner.sequence_number
    ).compare_number_of_users_in_table()


@allure.title(
    "Check that User redirected to the 'All establishments under your Unified ID' section"
)
@case_id(7877, 7903)
def test_user_is_redirected_to_user_details():
    owner = owner_account
    user_management = UserManagementActions()
    log_in_and_open_user_management(owner, Language.EN)
    user_management.navigate_to_view_details_page()


@allure.title("Check that User redirected to the owner subscription flow")
def test_user_is_redirected_to_owner_flow():
    owner = owner_account
    user_management = UserManagementActions()
    log_in_and_open_user_management(owner, Language.EN)
    user_management.navigate_to_owner_flow()


@allure.title("Check User has access to Establishments than subscription is Active/Inactive")
@case_id(7875, 7876, 39233, 41375, 39228)
def test_active_user_has_access():
    owner = owner_account
    log_in_and_open_user_management(owner, Language.EN)
    qiwa.main_page.check_user_status()


@allure.title("Check 'Users in Establishment Group' table pagination")
@case_id(7878)
def test_pagination_for_users_table():
    owner = owner_account
    log_in_and_open_user_management(owner, Language.EN)
    qiwa.main_page.check_pagination_btns()


@allure.title("Check that Group Manager displayed at the top of the users list")
@case_id(23717)
def test_that_owner_is_first_in_table():
    owner = owner_account
    log_in_and_open_user_management(owner, Language.EN)
    qiwa.main_page.check_owner_role_in_table()


@allure.title("Check that 'User Management' page has AR localization")
@case_id(7879)
def test_localization():
    user_management = UserManagementActions()
    owner = owner_account
    log_in_and_open_user_management(owner, Language.AR)
    user_management.check_localization_for_main_page()


@allure.title("Check that Delegation Manager can not edit his subscription")
@case_id(39230, 39231)
@pytest.mark.parametrize("users", UsersTypes.users)
def test_manager_cannot_edit_his_subscription(users):
    owner = users
    log_in_and_open_user_management(owner, Language.EN)
    qiwa.main_page.confirm_that_action_btn_is_missed()


@allure.title("Check that user without UM privileges can't open UM service")
@case_id(7872, 7882)
# TODO: update test based on test case 7882
def test_error_for_user_without_um_service():
    user = delegator_without_um
    user_management = UserManagementActions()
    log_in_and_open_user_management(user, Language.EN)
    user_management.check_error_message_for_um_page_without_permission(
        ErrorsMessage.user_doesnt_have_access_to_um
    ).click_header_main_menu_btn().click_change_workspace_btn()
    qiwa.workspace_page.select_company_account_with_sequence_number(sequence_number="157949")
    qiwa.open_user_management_page()
    qiwa.main_page.check_page_is_displayed()


@allure.title("Check AR localization for Establishment Delegator details page")
@case_id(7904)
def test_ar_localization_for_delegator_details_page():
    user_management = UserManagementActions()
    owner = owner_account
    log_in_and_open_user_management(owner, Language.EN)
    user_management.check_localization_for_details_page()


@allure.title("Check privileges data on Select Privileges modal")
@case_id(7921, 7922, 7923)
def test_privileges_data():
    user_management = UserManagementActions()
    owner = owner_account
    user = delegator_with_um
    log_in_and_open_user_management(owner, Language.EN)
    user_management.navigate_to_view_details_page(user.personal_number)\
        .open_select_privileges_modal_for_no_access_workspace().check_privileges_are_grouped() \
        .check_default_privileges_are_selected(Privileges.default_ui_privileges) \
        .check_ineligible_privileges_cannot_be_selected(Privileges.ineligible_ui_privileges)


@allure.title("Check that user can select/unselect privileges")
@case_id(7924)
def test_select_and_unselect_privileges():
    user_management = UserManagementActions()
    owner = owner_account_with_another_company
    user = user_type_three_employee
    log_in_and_open_user_management(owner, Language.EN)
    user_management.navigate_to_view_details_page(user.personal_number)\
        .open_select_privileges_modal_for_no_access_workspace()\
        .select_all_privileges().unselect_the_privilege(user_management_data.VISA_ISSUANCE_SERVICE)\
        .select_all_privileges().unselect_all_privileges()


@allure.title("Test self subscription")
@case_id(41783, 41794)
def test_self_subscription():
    user_management = UserManagementActions()
    user = SelfSubscriptionData.self_subscription_data[2]

    delete_self_subscription(user)
    log_in_and_open_establishment_account(user, Language.EN)
    qiwa.workspace_page.click_btn_subscribe()

    user_management\
        .check_establishment_user_details()\
        .check_annual_subscription()\
        .make_establishment_payment()\
        .check_thank_you_page()
    time.sleep(20)


@allure.title("Check open annual subscription page")
@case_id(41780)
@pytest.mark.parametrize("user", SelfSubscriptionData.self_subscription_data)
def test_open_annual_subscription_page(user):
    user_management = UserManagementActions()

    log_in_and_open_establishment_account(user, Language.EN)
    qiwa.workspace_page.click_btn_subscribe()

    user_management\


    time.sleep(20)
