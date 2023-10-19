import allure
import pytest

from data.delegation import general_data
from data.delegation.dataset import delegation_statuses
from data.delegation.users import (
    establishment_owner_with_one_partner,
    establishment_owner_without_partners,
)
from src.ui.pages.delegations_pages.delegation_dashboard_page import (
    DelegationDashboardPage,
)
from src.ui.qiwa import qiwa
from tests.ui.delegation.conftest import (
    check_sms_after_resend_action,
    get_delegation_request,
    get_old_url_after_resend_action,
    login_and_open_delegation_dashboard_page,
    login_as_establishment_owner,
    open_delegation_dashboard_page,
    open_url_from_sms,
    prepare_data_for_resend_action,
    prepare_data_for_revoke_action,
    resend_rejected_delegation_request,
)
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.DELEGATION)


@allure.title("Delegation dashboard: desktop view")
@case_id(25337)
def test_delegation_dashboard_is_displayed():
    login_and_open_delegation_dashboard_page(
        personal_number=establishment_owner_with_one_partner.personal_number,
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    qiwa.delegation_dashboard_page.should_active_breadcrumb_is_displayed_on_delegation_dashboard() \
        .should_location_breadcrumb_is_displayed_on_delegation_dashboard() \
        .should_page_title_has_correct_text_on_delegation_dashboard() \
        .should_add_delegation_button_has_correct_text() \
        .should_government_tab_has_correct_text() \
        .should_delegations_table_has_correct_title() \
        .should_search_is_displayed_on_delegation_dashboard() \
        .should_sort_by_is_displayed_on_delegation_dashboard() \
        .should_filter_button_has_correct_text() \
        .should_delegations_table_is_displayed() \
        .should_delegation_table_headers_have_correct_titles() \
        .should_rows_per_page_is_displayed_on_delegation_dashboard() \
        .should_pagination_is_displayed_on_delegation_dashboard()


@allure.title("Check Active/Expired/Pending/Revoked/Rejected delegation on dashboard")
@case_id(25339, 25340, 25341, 25342, 25343)
@pytest.mark.parametrize("status, color, action_titles", delegation_statuses)
def test_delegation_statuses_on_dashboard(status, color, action_titles):
    login_and_open_delegation_dashboard_page(
        personal_number=establishment_owner_with_one_partner.personal_number,
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    qiwa.delegation_dashboard_page.filter_delegation_list_by_status(status) \
        .should_status_text_of_filtered_delegation_be_correct(status) \
        .should_background_color_of_filtered_delegation_be_correct(color) \
        .click_more_button_on_delegation_dashboard() \
        .should_correct_actions_be_displayed_on_delegation_dashboard(action_titles)


@allure.title("Verify correct data is shown on the dashboard")
@case_id(25344)
def test_correct_data_on_delegation_dashboard():
    qiwa_api = login_and_open_delegation_dashboard_page(
        personal_number=establishment_owner_with_one_partner.personal_number,
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    headers = qiwa_api.delegation_api.set_headers()
    delegation_list = qiwa_api.delegation_api.get_delegations(headers)
    qiwa.delegation_dashboard_page.should_number_of_delegations_be_correct(delegation_list.total_elements) \
        .should_delegation_id_be_correct(delegation_list.first_delegation_id) \
        .should_employee_name_be_correct(delegation_list.first_delegation_employee_name) \
        .should_entity_name_be_correct(delegation_list.first_delegation_entity_name_en) \
        .should_delegation_permission_be_correct(delegation_list.first_delegation_permission) \
        .should_delegation_dates_be_correct_on_dashboard(
        delegation_list.first_delegation_status, delegation_list.first_delegation_start_date,
        DelegationDashboardPage.start_date_on_delegation_table) \
        .should_delegation_dates_be_correct_on_dashboard(
        delegation_list.first_delegation_status, delegation_list.first_delegation_expiry_date,
        DelegationDashboardPage.expiry_date_on_delegation_table) \
        .should_delegation_status_be_correct(delegation_list.first_delegation_status)


@allure.title("Resend action on the delegation dashboard")
@case_id(41668, 41673, 41666)
def test_resend_action_on_delegation_dashboard():
    qiwa_api = login_as_establishment_owner(personal_number=establishment_owner_with_one_partner.personal_number,
                                            sequence_number=establishment_owner_with_one_partner.sequence_number)
    delegation_data = prepare_data_for_resend_action(qiwa_api=qiwa_api, status=general_data.PENDING,
                                                     employee_nid=general_data.EMPLOYEE_NID_IN_WORKSPACE_WITH_PARTNERS,
                                                     duration=general_data.TWELVE_MONTHS_DURATION)
    open_delegation_dashboard_page(qiwa_api=qiwa_api)
    row_number = qiwa.delegation_dashboard_page.get_delegation_row(delegation_data["delegationId"])
    qiwa.delegation_dashboard_page.should_delegation_status_be_correct(
        status=general_data.REJECTED, row_number=row_number) \
        .click_more_button_on_delegation_dashboard(row_number=row_number) \
        .should_correct_actions_be_displayed_on_delegation_dashboard([general_data.VIEW_DETAILS, general_data.RESEND]) \
        .select_action_on_delegation_dashboard(action=general_data.RESEND) \
        .should_resend_confirmation_modal_be_displayed_on_dashboard() \
        .click_cancel_button_on_resend_modal().should_resend_confirmation_modal_be_hidden() \
        .click_more_button_on_delegation_dashboard(row_number=row_number) \
        .select_action_on_delegation_dashboard(action=general_data.RESEND) \
        .click_resend_request_button_on_dashboard() \
        .should_successful_message_be_displayed_on_dashboard(message=general_data.RESEND_MESSAGE) \
        .wait_delegation_dashboard_page_to_load()
    row_number = qiwa.delegation_dashboard_page.get_delegation_row(delegation_data["delegationId"])
    qiwa.delegation_dashboard_page.should_delegation_status_be_correct(
        status=general_data.PENDING, row_number=row_number) \
        .click_more_button_on_delegation_dashboard(row_number=row_number) \
        .should_correct_actions_be_displayed_on_delegation_dashboard(general_data.VIEW_DETAILS)
    updated_delegation_request = get_delegation_request(delegation_id=delegation_data["delegationId"],
                                                        status=general_data.PENDING)
    sms_url = check_sms_after_resend_action(phone_number=delegation_data["partnerPhoneNumber"],
                                            delegation_id=delegation_data["delegationId"],
                                            establishment_name=general_data.ESTABLISHMENT_NAME,
                                            request_id=updated_delegation_request.id,
                                            formatted_phone_number=delegation_data["formattedPartnerPhone"])
    open_url_from_sms(sms_url)
    qiwa.delegation_partner_approval_page.select_english_localization_on_partner_approval_page() \
        .wait_partner_approval_page_to_load()


@allure.title("Verify that the old link to partner's approval flow is not active (before resending)")
@case_id(41857)
def test_old_link_is_not_active_after_resending():
    qiwa_api = login_as_establishment_owner(personal_number=establishment_owner_with_one_partner.personal_number,
                                            sequence_number=establishment_owner_with_one_partner.sequence_number)
    delegation_data = prepare_data_for_resend_action(qiwa_api=qiwa_api, status=general_data.PENDING,
                                                     employee_nid=general_data.EMPLOYEE_NID_IN_WORKSPACE_WITH_PARTNERS,
                                                     duration=general_data.TWELVE_MONTHS_DURATION)
    resend_rejected_delegation_request(qiwa_api=qiwa_api, delegation_id=delegation_data["delegationId"])
    delegation_request = get_delegation_request(delegation_id=delegation_data["delegationId"],
                                                status=general_data.REJECTED)
    url_from_sms = get_old_url_after_resend_action(request_id=delegation_request.id,
                                                   formatted_phone_number=delegation_data["formattedPartnerPhone"])
    open_url_from_sms(url_from_sms)
    qiwa.delegation_partner_approval_page.select_english_localization_on_partner_approval_page() \
        .should_partner_approval_flow_be_not_available()


@allure.title("Revoke action on the delegation dashboard")
@case_id(41846)
def test_revoke_action_on_delegation_dashboard():
    qiwa_api = login_as_establishment_owner(
        personal_number=establishment_owner_without_partners.personal_number,
        sequence_number=establishment_owner_without_partners.sequence_number)
    delegation_id = prepare_data_for_revoke_action(qiwa_api=qiwa_api,
                                                   employee_nid=general_data.EMPLOYEE_NID_IN_WORKSPACE_WITH_NO_PARTNERS,
                                                   duration=general_data.TWELVE_MONTHS_DURATION)
    open_delegation_dashboard_page(qiwa_api=qiwa_api)
    row_number = qiwa.delegation_dashboard_page.get_delegation_row(delegation_id)
    qiwa.delegation_dashboard_page.should_delegation_status_be_correct(
        status=general_data.ACTIVE, row_number=row_number) \
        .click_more_button_on_delegation_dashboard(row_number=row_number) \
        .should_correct_actions_be_displayed_on_delegation_dashboard(
        [general_data.PREVIEW_LETTER, general_data.VIEW_DETAILS, general_data.REVOKE]) \
        .select_action_on_delegation_dashboard(action=general_data.REVOKE) \
        .should_revoke_confirmation_modal_be_displayed_on_dashboard() \
        .click_revoke_delegation_button_on_dashboard() \
        .should_successful_message_be_displayed_on_dashboard(message=general_data.REVOKE_MESSAGE) \
        .wait_delegation_dashboard_page_to_load()
    row_number = qiwa.delegation_dashboard_page.get_delegation_row(delegation_id)
    qiwa.delegation_dashboard_page.should_delegation_status_be_correct(
        status=general_data.REVOKED, row_number=row_number) \
        .click_more_button_on_delegation_dashboard(row_number=row_number) \
        .should_correct_actions_be_displayed_on_delegation_dashboard(general_data.VIEW_DETAILS)
