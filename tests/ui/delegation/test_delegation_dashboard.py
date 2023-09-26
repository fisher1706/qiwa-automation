import allure
import pytest

from data.delegation.dataset import delegation_statuses
from data.delegation.users import establishment_owner_with_one_partner
from src.api.app import QiwaApi
from src.ui.pages.delegations_pages.delegation_dashboard_page import (
    DelegationDashboardPage,
)
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project
from utils.helpers import set_cookies_for_browser

case_id = project(TestmoProject.DELEGATION)


@allure.title("Delegation dashboard: desktop view")
@case_id(25337)
def test_delegation_dashboard_is_displayed():
    qiwa.login_as_user(login=establishment_owner_with_one_partner.personal_number) \
        .workspace_page.select_company_account_with_sequence_number(
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    qiwa.open_delegation_dashboard_page()
    qiwa.delegation_dashboard_page.wait_delegation_dashboard_page_to_load() \
        .select_english_localization_on_delegation_dashboard() \
        .should_active_breadcrumb_is_displayed_on_delegation_dashboard() \
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
    qiwa.login_as_user(login=establishment_owner_with_one_partner.personal_number) \
        .workspace_page.select_company_account_with_sequence_number(
        sequence_number=establishment_owner_with_one_partner.sequence_number)
    qiwa.open_delegation_dashboard_page()
    qiwa.delegation_dashboard_page.wait_delegation_dashboard_page_to_load() \
        .select_english_localization_on_delegation_dashboard() \
        .filter_delegation_list_by_status(status) \
        .should_status_text_of_filtered_delegation_be_correct(status) \
        .should_background_color_of_filtered_delegation_be_correct(color) \
        .click_more_button_on_delegation_dashboard() \
        .should_correct_actions_of_filtered_delegation_be_displayed(action_titles)


@allure.title("Verify correct data is shown on the dashboard")
@case_id(25344)
def test_correct_data_on_delegation_dashboard():
    qiwa_api = QiwaApi.login_as_user(personal_number=establishment_owner_with_one_partner.personal_number) \
        .select_company(sequence_number=int(establishment_owner_with_one_partner.sequence_number))
    headers = qiwa_api.delegation_api.set_headers()
    delegation_list = qiwa_api.delegation_api.get_delegations(headers)
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_delegation_dashboard_page()
    set_cookies_for_browser(cookies)
    qiwa.delegation_dashboard_page.wait_delegation_dashboard_page_to_load() \
        .select_english_localization_on_delegation_dashboard() \
        .should_number_of_delegations_be_correct(delegation_list.total_elements) \
        .should_delegation_id_be_correct(delegation_list.first_delegation_id)\
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
