import allure

from data.delegation.delegation_dashboard import DelegationMain
from data.qiwa_urls import UrlForBreadcrumbs
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

testmo_case_id = project(TestmoProject.DELEGATION)


@allure.title("Delegation dashboard: desktop view")
@testmo_case_id(25337)
def test_check_delegation_dashboard_is_displayed():
    delegation_main = DelegationMain()
    qiwa.login_as_user(login="1049956129") \
        .workspace_page.select_company_account_with_sequence_number(sequence_number="85206")
    qiwa.admin_page.wait_page_to_load()
    qiwa.open_delegation_dashboard_page()
    qiwa.delegation_page.wait_page_to_load()\
        .select_english_localization()\
        .check_active_breadcrumb(index=0, title=delegation_main.services_breadcrumb,
                                 url=UrlForBreadcrumbs.E_SERVICES_URL.value) \
        .check_location_breadcrumb(index=1, title=delegation_main.delegation_main_page_breadcrumb) \
        .check_page_title() \
        .verify_add_delegation_button() \
        .check_government_tab() \
        .verify_delegation_table_title() \
        .check_search_is_displayed() \
        .verify_sort_by_is_displayed() \
        .check_filter_button() \
        .verify_delegations_table_is_displayed()\
        .check_delegation_table_headers_titles()\
        .check_rows_per_page_is_displayed() \
        .verify_pagination_is_displayed()
