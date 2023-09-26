import allure
import pytest

from data.delegation.constants import DelegationAction, DelegationStatus
from data.delegation.dataset import delegation_status
from data.delegation.users import (
    establishment_owner_with_two_partners,
    establishment_owner_without_partners,
)
from src.api.app import QiwaApi
from src.ui.pages.delegations_pages.delegation_details_page import DelegationDetailsPage
from src.ui.qiwa import qiwa
from tests.ui.delegation.conftest import (
    login_and_open_delegation_details_page,
    login_and_open_delegation_details_page_by_status,
)
from utils.allure import TestmoProject, project
from utils.helpers import set_cookies_for_browser

case_id = project(TestmoProject.DELEGATION)


@allure.title("Verify redirect on the Details page")
@case_id(25373)
def test_redirect_to_delegation_details():
    qiwa_api = QiwaApi.login_as_user(personal_number=establishment_owner_with_two_partners.personal_number) \
        .select_company(sequence_number=int(establishment_owner_with_two_partners.sequence_number))
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_delegation_dashboard_page()
    set_cookies_for_browser(cookies)
    qiwa.delegation_dashboard_page.select_english_localization_on_delegation_dashboard() \
        .wait_delegation_dashboard_page_to_load()
    delegation_id = qiwa.delegation_dashboard_page.get_id_on_delegation_table()
    qiwa.delegation_dashboard_page.click_more_button_on_delegation_dashboard() \
        .select_action_on_delegation_dashboard(DelegationAction.VIEW_DETAILS)
    qiwa.delegation_details_page.check_redirect_to_delegation_details(delegation_id)


@allure.title("Verify action buttons for Active status")
@case_id(25374)
def test_action_buttons_for_active_delegation_on_delegation_details():
    login_and_open_delegation_details_page_by_status(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number,
        status=DelegationStatus.ACTIVE)
    qiwa.delegation_details_page.wait_delegation_details_page_to_load()\
        .select_english_localization_on_delegation_details() \
        .should_action_buttons_be_correct([DelegationAction.PREVIEW_LETTER, DelegationAction.REVOKE])


@allure.title("Verify action button for Rejected status")
@case_id(25375, 25376)
def test_action_buttons_for_rejected_delegation_on_delegation_details():
    delegation_list = login_and_open_delegation_details_page_by_status(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number,
        status=DelegationStatus.REJECTED)
    qiwa.delegation_details_page.wait_delegation_details_page_to_load() \
        .select_english_localization_on_delegation_details() \
        .check_actions_for_rejected_delegation(delegation_list.first_delegation_available_for_resending)


@allure.title("Verify the absence of buttons for Expired/Revoked/Pending status")
@case_id(25376, 25377, 25378)
@pytest.mark.parametrize("status", delegation_status)
def test_action_buttons_are_hidden_on_delegation_details(status):
    login_and_open_delegation_details_page_by_status(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number,
        status=status)
    qiwa.delegation_details_page.wait_delegation_details_page_to_load() \
        .select_english_localization_on_delegation_details() \
        .should_action_buttons_be_hidden()


@allure.title("Verify General information on the delegation details")
@case_id(25380)
def test_general_information_on_delegation_details():
    delegation_details = login_and_open_delegation_details_page(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number)
    qiwa.delegation_details_page.wait_delegation_details_page_to_load() \
        .select_english_localization_on_delegation_details() \
        .should_general_information_block_be_displayed() \
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
    qiwa.delegation_details_page.wait_delegation_details_page_to_load()\
        .select_english_localization_on_delegation_details()\
        .should_partners_approval_block_be_displayed()\
        .should_partner_name_be_correct(delegation_details.partner_list)\
        .should_partner_phone_be_correct(delegation_details.partner_list)\
        .should_partner_request_status_be_correct(delegation_details.partner_list)


@allure.title("Verify the absence Partners approval block for establishment without partners"
              " on the delegation details page")
@case_id(25383)
def test_partners_information_is_hidden_on_delegation_details():
    login_and_open_delegation_details_page(
        personal_number=establishment_owner_without_partners.personal_number,
        sequence_number=establishment_owner_without_partners.sequence_number)
    qiwa.delegation_details_page.wait_delegation_details_page_to_load()\
        .select_english_localization_on_delegation_details()\
        .should_partner_approval_block_be_hidden()\
        .should_general_information_block_be_displayed()\
        .should_delegate_block_be_displayed()


@allure.title("Verify Delegate information on the delegation details")
@case_id(25382)
def test_delegate_information_on_delegation_details():
    delegation_details = login_and_open_delegation_details_page(
        personal_number=establishment_owner_with_two_partners.personal_number,
        sequence_number=establishment_owner_with_two_partners.sequence_number)
    qiwa.delegation_details_page.wait_delegation_details_page_to_load()\
        .select_english_localization_on_delegation_details()\
        .should_delegate_block_be_displayed()\
        .should_delegate_name_be_correct_on_delegation_details(delegation_details.delegate_name)\
        .should_delegate_nid_be_correct_on_delegation_details(delegation_details.delegate_nid)\
        .should_delegate_nationality_be_correct_on_delegation_details(delegation_details.delegate_nationality)\
        .should_delegate_occupation_be_correct_on_delegation_details(delegation_details.delegate_occupation)
