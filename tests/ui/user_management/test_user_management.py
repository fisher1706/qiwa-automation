
import allure
import pytest

from data.constants import Language
from data.user_management import user_management_data
from data.user_management.user_management_datasets import (
    ErrorsMessage,
    EstablishmentAddresses,
    Privileges,
    SelfSubscriptionData,
    SelfSubscriptionType,
    Texts,
    UserAccess,
    UsersTypes,
    AddEstablishmentDelegatorData,
)
from data.user_management.user_management_users import (
    delegator_type_three,
    delegator_type_three_1,
    delegator_type_three_2,
    delegator_without_um,
    owner_account,
    owner_account_with_another_company,
    owner_for_changing_address_data,
    owner_for_self,
    owner_in_establishment_with_not_allowed_activities,
    owner_with_active_subscription,
    owner_with_expired_subscription,
    owner_with_expired_subscription_always,
    owner_without_subscription,
    owner_without_vat_number_and_address,
    user_type_1,
    user_type_three,
    user_type_three_1,
    user_type_three_2,
    user_type_three_3,
    user_type_three_4,
    user_type_three_employee,
    user_type_three_employee_1,
    user_type_three_employee_2,
    user_type_three_in_establishment_with_not_allowed_activities,
)
from src.ui.actions.user_management_actions.user_management import UserManagementActions
from src.ui.qiwa import qiwa
from tests.conftest import (
    prepare_data_for_free_subscription,
    prepare_data_for_terminate_company,
)
from tests.ui.user_management.conftest import (
    delete_subscriptions,
    check_access_and_update_permissions,
    check_establishment_data_are_identical_for_both_localizations,
    check_vat_number_is_empty,
    clear_establishment_data,
    expire_user_subscription,
    get_subscription_cookie,
    log_in_and_open_establishment_account,
    log_in_and_open_user_management,
    prepare_data_for_checking_the_confirmation_page,
    prepare_data_for_owner_extend_active_subscription_flow,
    prepare_data_for_owner_subscriptions_flows,
    prepare_data_for_updating_establishment_data,
    remove_establishment_from_subscription,
    renew_owner_subscriptions,
    renew_self_subscriptions,
    subscribe_user_to_establishment,
    terminate_user_subscription,
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
@case_id(7872, 7882, 7931)
# TODO: update test based on test case 7882
def test_error_for_user_without_um_service():
    user = delegator_without_um
    employee = user_type_three_employee
    user_management = UserManagementActions()
    log_in_and_open_user_management(user, Language.EN, False)
    user_management.check_error_message_for_um_page_without_permission(
        ErrorsMessage.user_doesnt_have_access_to_um, ErrorsMessage.no_access_error_description
    ).navigate_to_user_details_without_um_permission(employee.personal_number) \
        .click_header_main_menu_btn().click_change_workspace_btn()
    qiwa.workspace_page.select_company_account_with_sequence_number(sequence_number="157949")
    qiwa.open_user_management_page()
    qiwa.main_page.check_page_is_displayed()
    user_management.navigate_to_user_details(employee.personal_number)


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
    user = user_type_three_employee
    qiwa_api = log_in_and_open_user_management(owner, Language.EN)
    cookie = get_subscription_cookie(owner)
    check_access_and_update_permissions(qiwa_api, cookie, user, Privileges.default_privileges)
    remove_establishment_from_subscription(owner, qiwa_api, [user])
    user_management.navigate_to_user_details(user.personal_number) \
        .open_select_privileges_modal_for_no_access_workspace(user.sequence_number) \
        .check_privileges_are_grouped(Privileges.groups_data) \
        .check_privileges_are_selected(privilege_names=Privileges.default_ui_privileges, active_state=False) \
        .check_privileges_are_unselected(privilege_names=Privileges.ineligible_ui_privileges, active_state=False)


@allure.title("Check interaction with privileges list")
@case_id(7924, 165306, 7927, 7926)
def test_interaction_with_privileges_list():
    user_management = UserManagementActions()
    owner = owner_account
    user = user_type_three_employee
    user_another_establishment = user_type_three_employee_2
    qiwa_api = log_in_and_open_user_management(owner, Language.EN)
    cookie = get_subscription_cookie(owner)
    check_access_and_update_permissions(qiwa_api, cookie, user, Privileges.all_privileges)
    remove_establishment_from_subscription(owner, qiwa_api, [user_another_establishment])
    user_management.navigate_to_view_details_page(user_another_establishment.personal_number) \
        .open_select_privileges_modal_for_no_access_workspace(user_another_establishment.sequence_number) \
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


@allure.title("Check add access to establishment")
@case_id(7928, 7932)
def test_add_access_to_establishment():
    user_management = UserManagementActions()
    owner = owner_account_with_another_company
    user = user_type_three_employee
    user_for_add_access = user_type_three_employee_1
    user_2 = user_type_three_employee_2
    qiwa_api = log_in_and_open_user_management(owner, Language.EN)
    cookie = get_subscription_cookie(owner)
    prepare_data_for_terminate_company(qiwa_api, cookie, user_2)
    remove_establishment_from_subscription(owner, qiwa_api, [user, user_for_add_access])
    user_management.navigate_to_user_details(user.personal_number) \
        .open_select_privileges_modal_for_no_access_workspace(user.sequence_number) \
        .add_access_with_fundamental_privileges(user.sequence_number) \
        .open_select_privileges_modal_for_no_access_workspace(user_for_add_access.sequence_number) \
        .add_access_with_not_fundamental_privileges(user_for_add_access) \
        .check_privileges_after_add_access_with_not_fundamental_privileges(user_for_add_access.sequence_number)
    remove_establishment_from_subscription(owner, qiwa_api, [user, user_for_add_access])


@allure.title("Check remove establishment from subscription")
@case_id(7936, 34197)
def test_remove_access_flow():
    user_management = UserManagementActions()
    owner = owner_account
    user = user_type_three_employee
    qiwa_api = log_in_and_open_user_management(owner, Language.EN)
    cookie = get_subscription_cookie(owner)
    prepare_data_for_terminate_company(qiwa_api, cookie, user)
    user_management.navigate_to_user_details(user.personal_number) \
        .check_remove_access_modal(user).remove_access_for_establishment(user)
    prepare_data_for_terminate_company(qiwa_api, cookie, user)


@allure.title("Check remove access to all establishments")
@pytest.mark.skip("confirm payment is unavailable on api side")
# TODO: add renew subscription and payment after the test
@case_id(7930, 12405)
def test_terminate_flow():
    user_management = UserManagementActions()
    owner = owner_account
    user = user_type_three
    log_in_and_open_user_management(owner, Language.EN)
    user_management.navigate_to_user_details(user.personal_number).terminate_user_from_all_establishments(user.name)\
        .check_user_is_terminated(user.personal_number)


@allure.title("Check interaction with establishments list")
@case_id(7929, 7935)
def test_interaction_with_establishments_list():
    user_management = UserManagementActions()
    owner = owner_account
    user = user_type_three_employee
    user1 = user_type_three_employee_1
    qiwa_api = log_in_and_open_user_management(owner, Language.EN)
    cookie = get_subscription_cookie(owner)
    subscribe_user_to_establishment(qiwa_api, cookie, [user, user1])
    user_management.navigate_to_user_details(user.personal_number) \
        .select_all_allowed_access_establishments_checkbox() \
        .unselect_all_allowed_access_establishments_checkbox() \
        .select_allowed_access_establishment_checkbox() \
        .check_establishment_checkbox_is_selected_after_switching_between_tabs()


@allure.title("Check AR localization for Add access/Edit privileges modals")
@case_id(7933)
def test_ar_localization_for_add_access_and_edit_privileges_modals():
    user_management = UserManagementActions()
    owner = owner_account
    user = user_type_three_employee
    user1 = user_type_three_employee_1
    cookie = get_subscription_cookie(owner)
    qiwa_api = log_in_and_open_user_management(owner, Language.AR)
    check_access_and_update_permissions(qiwa_api, cookie, user, Privileges.default_privileges)
    prepare_data_for_free_subscription(qiwa_api, cookie, user1)
    user_management.navigate_to_user_details(user.personal_number) \
        .check_localization_for_add_access_modal(user1.sequence_number) \
        .check_privileges_are_grouped(Privileges.groups_data_ar).close_select_privileges_modal() \
        .check_localization_for_edit_privileges_modal(user.sequence_number) \
        .check_privileges_are_grouped(Privileges.groups_data_ar)


@allure.title("Test self subscription user without subscription")
@case_id(41783, 41794, 41785, 41790)
def test_self_subscription_user_without_subscription(user_type="without", user=owner_without_subscription):
    delete_subscriptions(user)
    user_management = UserManagementActions()
    log_in_and_open_establishment_account(user, Language.EN)

    user_management \
        .possibility_switch_to_establishment_page(user_type) \
        .check_establishment_user_details() \
        .check_annual_subscription() \
        .make_establishment_payment() \
        .check_thank_you_page(user_type)


@allure.title("Test self subscription user with expired or terminated subscription")
@case_id(41780)
def test_self_subscription_user_with_expired_terminated_subscription(user_type="expired",
                                                                     user=owner_with_expired_subscription_always):
    user_management = UserManagementActions()
    log_in_and_open_establishment_account(user, Language.EN)

    user_management \
        .possibility_switch_to_establishment_page(user_type) \
        .check_establishment_user_details() \
        .check_renew_subscription()


@allure.title("Test self subscription user with active subscription")
@case_id(41780)
def test_self_subscription_user_with_active_subscription(user_type="active", user=owner_with_active_subscription):
    user_management = UserManagementActions()
    log_in_and_open_establishment_account(user, Language.EN)

    user_management \
        .possibility_switch_to_establishment_page(user_type)


@allure.step("Test renew expired subscription")
@case_id(41781, 41800, 43159)
def test_update_self_expired_subscription(user_type="expired", user=owner_with_expired_subscription):
    expire_user_subscription(user)
    user_management = UserManagementActions()
    log_in_and_open_establishment_account(user, Language.EN)

    user_management \
        .possibility_switch_to_establishment_page(user_type) \
        .check_establishment_user_details() \
        .check_renew_subscription() \
        .make_establishment_payment() \
        .check_thank_you_page(user_type) \
        .check_db_subscription_date(user)


@allure.step("Test possibility open 'Renew expired page'")
@case_id(41795, 41798)
@pytest.mark.parametrize("user_type, user", SelfSubscriptionData.all_users)
def test_possibility_open_renew_expired_page_self_subscription(user_type, user):
    user_management = UserManagementActions()
    log_in_and_open_establishment_account(user, Language.EN)

    user_management \
        .navigate_to_establishment_information(user) \
        .possibility_open_renew_subscription_page() \
        .check_opened_page(user_type)


@allure.title("Test confirmation page for owner subscriptions")
@case_id(17410)
def test_confirmation_page_for_owner_subscriptions():
    user_management = UserManagementActions()
    owner = owner_account
    user_for_extend_subscription = delegator_type_three
    user_for_renew_expired_flow = delegator_type_three_1
    user_for_renew_terminated_flow = delegator_type_three_2
    qiwa_api = log_in_and_open_user_management(owner, Language.EN)
    prepare_data_for_owner_subscriptions_flows(
        owner, qiwa_api, user_for_extend_subscription, user_for_renew_expired_flow, user_for_renew_terminated_flow)
    user_management.check_confirmation_page_on_add_new_user_flow().return_to_main_page_from_owner_subscription_flow() \
        .check_confirmation_page_is_opened(
        user_for_extend_subscription.personal_number, user_management_data.EXTEND_ACTION) \
        .return_to_main_page_from_owner_subscription_flow() \
        .check_confirmation_page_is_opened(
        user_for_renew_expired_flow.personal_number, user_management_data.RENEW_ACTION) \
        .return_to_main_page_from_owner_subscription_flow() \
        .check_confirmation_page_is_opened(
        user_for_renew_terminated_flow.personal_number, user_management_data.RENEW_ACTION) \
        .return_to_main_page_from_owner_subscription_flow()
    renew_owner_subscriptions(owner, [user_for_extend_subscription, user_for_renew_expired_flow,
                                      user_for_renew_terminated_flow], qiwa_api, user_management,
                              SelfSubscriptionType.subscription_type)


@allure.title("Test content on confirmation page")
@case_id(17411, 41496, 41498)
def test_content_on_confirmation_page():
    user_management = UserManagementActions()
    owner = owner_account
    qiwa_api = log_in_and_open_user_management(owner, Language.EN)
    establishment_data = prepare_data_for_checking_the_confirmation_page(owner, qiwa_api)
    user_management.check_confirmation_page_on_add_new_user_flow() \
        .check_content_on_confirmation_page_english_localization(establishment_data, owner) \
        .check_content_on_confirmation_page_arabic_localization(establishment_data) \
        .update_establishment_data_for_both_localizations()
    check_establishment_data_are_identical_for_both_localizations(owner, qiwa_api)


#

@allure.title("Check confirmation page is hidden after subscription was started in the current session")
@case_id(17412, 41497)
def test_confirmation_page_is_hidden_after_subscription_was_started_in_the_current_session():
    user_management = UserManagementActions()
    owner = owner_account
    user = delegator_type_three_2
    qiwa_api = log_in_and_open_user_management(owner, Language.EN)
    terminate_user_subscription(owner, qiwa_api, user)
    user_management.check_confirmation_page_is_hidden_after_opening_subscription_page(user) \
        .check_confirmation_page_is_opened_after_changing_workspace(user)
    qiwa.header.click_on_menu().click_on_logout()
    qiwa.login_page.wait_login_page_to_load()
    log_in_and_open_user_management(owner, Language.EN)
    user_management.check_confirmation_page_is_opened_after_relogin(user)
    renew_owner_subscriptions(owner, [user], qiwa_api, user_management, [SelfSubscriptionType.subscription_type[2]])


@allure.title("Check that warning messages displayed if required data is missing on the confirmation page")
@pytest.mark.skip("test is skipped due to UM-6527")
@case_id(17413)
def test_warning_messages_if_required_data_is_missing_on_confirmation_page():
    user_management = UserManagementActions()
    owner = owner_without_vat_number_and_address
    log_in_and_open_user_management(owner, Language.EN)
    user_management.check_confirmation_page_on_add_new_user_flow() \
        .check_english_localization_for_errors_on_confirmation_page()
    qiwa.header.change_local(Language.AR)
    user_management.check_arabic_localization_for_errors_on_confirmation_page()


@allure.title("Check update Establishment address on the Confirmation page")
@case_id(17414, 141722)
def test_update_establishment_address_on_confirmation_page():
    user_management = UserManagementActions()
    user1 = user_type_1
    user2 = owner_for_changing_address_data
    log_in_and_open_user_management(user1, Language.EN)
    prepare_data_for_updating_establishment_data(user1, user2)
    user_management.update_establishment_data_for_owner_subscription_flow()
    qiwa.header.click_on_menu().click_on_logout()

    qiwa.login_page.wait_login_page_to_load()
    qiwa_api = log_in_and_open_establishment_account(user2, Language.EN)
    user_management.update_establishment_data_for_self_subscription_flow("expired", user2)
    renew_self_subscriptions(user2, qiwa_api, user_management, SelfSubscriptionType.subscription_type[1], "expired")


@allure.title("Check user can proceed with subscription without VAT number")
@case_id(41495)
def test_user_can_proceed_with_subscription_without_vat_number():
    user_management = UserManagementActions()
    owner = owner_without_vat_number_and_address
    qiwa_api = log_in_and_open_user_management(owner, Language.EN)
    qiwa_api.user_management_api.post_update_establishment_address(EstablishmentAddresses.updated_address)
    user_management.check_vat_error_is_displayed().select_proceed_without_vat_on_confirmation_page()
    check_vat_number_is_empty(owner, qiwa_api)
    user_management.proceed_owner_subscription_on_confirmation_page()
    clear_establishment_data(owner)


@allure.title("Check that Establishments with not allowed activities are excluded from the Owner "
              "Extend subscription flow")
@case_id(141018, 141020)
def test_establishments_with_not_allowed_activities_are_excluded_from_owner_extend_flow():
    user_management = UserManagementActions()
    owner = owner_in_establishment_with_not_allowed_activities
    user = user_type_three_1
    user_with_not_allowed_activities = user_type_three_in_establishment_with_not_allowed_activities
    cookie = get_subscription_cookie(owner)
    qiwa_api = log_in_and_open_user_management(owner, Language.EN)
    qiwa_api.user_management.update_expiry_date_for_owner_subscription(user)
    qiwa_api.user_management.check_error_on_renew_owner_subscription_for_not_allowed_establishment(
        cookie, user_with_not_allowed_activities, SelfSubscriptionType.subscription_type[0])
    user_management.check_establishment_with_not_allowed_activities_is_hidden_from_owner_subscription_flow(user)


@allure.title("Verify users can provide access to establishments only where they have User Management Permission for "
              "Extend Active Subscription flow")
@case_id(141591)
@pytest.mark.parametrize("user, users_list, establishments_list", UserAccess.users)
def test_users_can_provide_access_to_establishments_where_they_have_UM_privilege(user, users_list, establishments_list):
    user_management = UserManagementActions()
    owner = owner_account
    subscribed_user = [user_type_three_2, user_type_three_3, user_type_three_4]
    prepare_data_for_owner_extend_active_subscription_flow(user, subscribed_user, owner, users_list)
    log_in_and_open_user_management(user, Language.EN)
    user_management.extend_owner_subscription_and_check_added_establishments(subscribed_user[0], establishments_list)


@allure.step("Test 'Add new Establishment Delegator' flow")
@case_id(41421, 41592, 7890, 7892, 7981, 7889, 7898)
@pytest.mark.parametrize("subscriber, user_one, user_two", AddEstablishmentDelegatorData.users)
def test_establishment_delegator_flow(subscriber, user_one, user_two):
    user_management = UserManagementActions()
    log_in_and_open_user_management(subscriber, Language.EN)

    user_management\
        .check_open_add_establishment_delegator_page()\
        .verify_possibility_upload_data_of_few_users_as_delegator(user_one, user_two)\
        .verify_possibility_add_few_users_as_delegator(user_one, user_two)\
        .delete_establishment_delegator(user_two)\
        .verify_possibility_add_additional_users_as_delegator(user_two)\
        .verify_establishment_user_have_access(user_one, user_two)\
        .go_to_payment_page()


@allure.step("Test verify the 'New Establishment Delegator selected' section and ability to Edit it")
@case_id(7894, 7895, 7897, 7934)
@pytest.mark.parametrize("subscriber, user_one, user_two", AddEstablishmentDelegatorData.users)
def test_verify_btn_edit(subscriber, user_one, user_two):
    user_management = UserManagementActions()
    log_in_and_open_user_management(subscriber, Language.EN)

    user_management\
        .check_open_add_establishment_delegator_page()\
        .verify_edit_establishment_delegator_section(user_one, user_two)\
        .select_deselect_all_establishment()\
        .check_field_search(user_management_data.INCORRECT_ESTABLISHMENT, subscriber.sequence_number)


@allure.step("Test verify the 'New Establishment Delegator selected' section and ability to Edit it")
@case_id(7899, 33014, 43165, 71517, 71518)
@pytest.mark.parametrize("subscriber, user_one, user_two", AddEstablishmentDelegatorData.users)
def test_verify_select_all(subscriber, user_one, user_two):
    user_management = UserManagementActions()
    log_in_and_open_user_management(subscriber, Language.EN)

    user_management\
        .check_open_add_establishment_delegator_page()\
        .verify_possibility_add_few_users_as_delegator(user_one, user_two)\
        .verify_ability_select_all_privileges_for_all_establishment()\
        .verify_warning_message()\
        .go_to_payment_page()
