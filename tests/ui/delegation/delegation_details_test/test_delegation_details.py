import allure
import pytest

from data.delegation import general_data
from data.delegation.dataset import delegation_status
from data.delegation.users import (
    establishment_owner_with_two_partners,
    establishment_owner_without_partners,
)
from src.ui.pages.delegations_pages.delegation_details_page import DelegationDetailsPage
from src.ui.qiwa import qiwa
from tests.ui.delegation.delegation_details_test.conftest import (
    get_partners_names_for_delegation_details,
    get_partners_phone_numbers_for_delegation_details,
    get_partners_request_status_for_delegation_details,
    login_and_open_delegation_dashboard_page,
    login_and_open_delegation_details_page,
    login_and_open_delegation_details_page_by_status,
)
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.DELEGATION)


@allure.title("Verify redirect on the Details page")
@case_id(25373)
def test_redirect_to_delegation_details():
    login_and_open_delegation_dashboard_page(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number)
    delegation_id = qiwa.delegation_dashboard_page.get_id_on_delegation_table()
    qiwa.delegation_dashboard_page.click_more_button_on_delegation_dashboard() \
        .select_action_on_delegation_dashboard(general_data.VIEW_DETAILS)
    qiwa.delegation_details_page.check_redirect_to_delegation_details(delegation_id)


@allure.title("Verify action buttons for Active status")
@case_id(25374)
def test_action_buttons_for_active_delegation_on_delegation_details():
    login_and_open_delegation_details_page_by_status(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number,
        status=general_data.ACTIVE)
    qiwa.delegation_details_page.should_action_buttons_be_correct(
        [general_data.PREVIEW_LETTER, general_data.REVOKE])


@allure.title("Verify action button for Rejected status")
@case_id(25375, 26636)
def test_action_buttons_for_rejected_delegation_on_delegation_details():
    delegation_list = login_and_open_delegation_details_page_by_status(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number,
        status=general_data.REJECTED)
    qiwa.delegation_details_page.check_actions_for_rejected_delegation(
        delegation_list.first_delegation_available_for_resending)


@allure.title("Verify the absence of buttons for Expired/Revoked/Pending status")
@case_id(25376, 25377, 25378)
@pytest.mark.parametrize("status", delegation_status)
def test_action_buttons_are_hidden_on_delegation_details(status):
    login_and_open_delegation_details_page_by_status(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number,
        status=status)
    qiwa.delegation_details_page.should_action_buttons_be_hidden()


@allure.title("Verify General information on the delegation details")
@case_id(25380)
def test_general_information_on_delegation_details():
    delegation_details = login_and_open_delegation_details_page(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number)
    qiwa.delegation_details_page.should_general_information_block_be_displayed() \
        .should_delegation_status_be_correct_on_delegation_details(delegation_details.delegation_status) \
        .should_delegation_id_be_correct_on_delegation_details(delegation_details.delegation_id) \
        .should_entity_name_be_correct_on_delegation_details(delegation_details.entity_name_en) \
        .should_permission_be_correct_on_delegation_details(delegation_details.permission) \
        .should_dates_be_correct_on_delegation_details(
        delegation_details.delegation_status, delegation_details.start_date,
        DelegationDetailsPage.start_date_on_delegation_details) \
        .should_dates_be_correct_on_delegation_details(
        delegation_details.delegation_status, delegation_details.expiry_date,
        DelegationDetailsPage.expiry_date_on_delegation_details)


@allure.title("Verify Partners approval information on the delegation details")
@case_id(25381)
def test_partners_information_on_delegation_details():
    delegation_details = login_and_open_delegation_details_page(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number)
    partner_names = get_partners_names_for_delegation_details(delegation_details.partner_list)
    partner_numbers = get_partners_phone_numbers_for_delegation_details(delegation_details.partner_list)
    partner_request_statuses = get_partners_request_status_for_delegation_details(delegation_details.partner_list)
    qiwa.delegation_details_page.should_partners_approval_block_be_displayed()\
        .should_partner_name_be_correct(partner_names)\
        .should_partner_phone_be_correct(partner_numbers)\
        .should_partner_request_status_be_correct(partner_request_statuses)


@allure.title("Verify the absence Partners approval block for establishment without partners"
              " on the delegation details page")
@case_id(25383)
def test_partners_information_is_hidden_on_delegation_details():
    login_and_open_delegation_details_page(
        personal_number=establishment_owner_without_partners.personal_number,
        sequence_number=establishment_owner_without_partners.sequence_number)
    qiwa.delegation_details_page.should_partner_approval_block_be_hidden()\
        .should_general_information_block_be_displayed()\
        .should_delegate_block_be_displayed()


@allure.title("Verify Delegate information on the delegation details")
@case_id(25382)
def test_delegate_information_on_delegation_details():
    delegation_details = login_and_open_delegation_details_page(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number)
    qiwa.delegation_details_page.should_delegate_block_be_displayed()\
        .should_delegate_name_be_correct_on_delegation_details(delegation_details.delegate_name)\
        .should_delegate_nid_be_correct_on_delegation_details(delegation_details.delegate_nid)\
        .should_delegate_nationality_be_correct_on_delegation_details(delegation_details.delegate_nationality)\
        .should_delegate_occupation_be_correct_on_delegation_details(delegation_details.delegate_occupation)
