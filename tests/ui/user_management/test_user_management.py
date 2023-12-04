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
    delegator_for_add_and_terminate_subscription_flow,
    delegator_without_um,
    owner_account,
    owner_account_with_another_company,
    owner_for_self,
    user_type_three_employee,
    user_type_three_employee_for_add_access,
)
from src.ui.actions.user_management_actions.user_management import UserManagementActions
from src.ui.qiwa import qiwa
from tests.ui.user_management.conftest import (
    delete_self_subscription,
    log_in_and_open_establishment_account,
    log_in_and_open_user_management,
    prepare_data_for_add_access_to_company,
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
@case_id(165303, 7922, 7923)
def test_privileges_data():
    user_management = UserManagementActions()
    owner = owner_account
    user = delegator_for_add_and_terminate_subscription_flow
    log_in_and_open_user_management(owner, Language.EN)
    user_management.navigate_to_view_details_page(user.personal_number) \
        .open_select_privileges_modal_for_no_access_workspace(user.sequence_number).check_privileges_are_grouped() \
        .check_privileges_are_selected(privilege_names=Privileges.default_ui_privileges, active_state=False) \
        .check_privileges_are_unselected(privilege_names=Privileges.ineligible_ui_privileges, active_state=False)


@allure.title("Check interaction with privileges list")
@case_id(7924, 165306, 7927, 7926)
def test_interaction_with_privileges_list():
    user_management = UserManagementActions()
    owner = owner_account_with_another_company
    user = user_type_three_employee
    log_in_and_open_user_management(owner, Language.EN)
    user_management.navigate_to_view_details_page(user.personal_number) \
        .open_select_privileges_modal_for_no_access_workspace(user.sequence_number) \
        .select_all_privileges().unselect_the_privilege(user_management_data.VISA_ISSUANCE_SERVICE) \
        .select_all_privileges().unselect_all_privileges() \
        .select_paired_privileges([user_management_data.OCCUPATION_MANAGEMENT],
                                  [user_management_data.EMPLOYEE_INFORMATION]) \
        .select_paired_privileges([user_management_data.ISSUE_AND_RENEW_WORKING_PERMITS],
                                  [user_management_data.EMPLOYEE_INFORMATION]) \
        .select_paired_privileges([user_management_data.EMPLOYEE_TRANSFER],
                                  [user_management_data.EMPLOYEE_INFORMATION,
                                   user_management_data.CONTRACT_MANAGEMENT]) \
        .check_expanding_privilege_group_list().check_collapsing_privilege_group_list().close_select_privileges_modal()


@allure.title("test_add_access_to_establishment")
@pytest.mark.skip("test is skipped due to issue UM-5868")
@case_id(7928, 7932)
def test_add_access_to_establishment():
    user_management = UserManagementActions()
    owner = owner_account_with_another_company
    user = user_type_three_employee
    user_for_add_access = user_type_three_employee_for_add_access
    qiwa_api = log_in_and_open_user_management(owner, Language.EN)
    prepare_data_for_add_access_to_company(owner, qiwa_api, [user, user_for_add_access])
    user_management.navigate_to_view_details_page(user.personal_number) \
        .open_select_privileges_modal_for_no_access_workspace(user.sequence_number)\
        .add_access_with_fundamental_privileges(user.sequence_number) \
        .open_select_privileges_modal_for_no_access_workspace(user_for_add_access.sequence_number)\
        .add_access_with_not_fundamental_privileges(user_for_add_access.sequence_number)
    row_number = user_management.get_row_with_allowed_establishment(user_for_add_access.labor_office_id,
                                                                    user_for_add_access.sequence_number)
    user_management.check_success_message_and_privileges_after_add_access(row_number)
    prepare_data_for_add_access_to_company(owner, qiwa_api, [user, user_for_add_access])


@allure.title("Test self subscription")
@case_id(41783, 41794, 41780, 41785, 41790)
@pytest.mark.parametrize("user_type, user", SelfSubscriptionData.self_subscription_data)
def test_self_subscription(user_type, user):
    user_management = UserManagementActions()
    log_in_and_open_establishment_account(user, Language.EN)

    if user_type == 'without':
        user_management\
            .possibility_switch_to_establishment_page(user_type)\
            .check_establishment_user_details()\
            .check_annual_subscription()\
            .make_establishment_payment()\
            .check_thank_you_page()
        delete_self_subscription(user)

    elif user_type in ['expired', 'terminated']:
        user_management\
            .possibility_switch_to_establishment_page(user_type)\
            .check_establishment_user_details()\
            .check_renew_subscription()\

    else:
        user_management\
            .possibility_switch_to_establishment_page(user_type)
