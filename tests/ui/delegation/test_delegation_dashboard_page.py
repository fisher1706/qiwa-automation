import allure

from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.DELEGATION)


@allure.title("Delegation dashboard: desktop view")
@case_id(25337)
def test_check_delegation_dashboard_is_displayed():
    qiwa.login_as_user(login="1049956129") \
        .workspace_page.select_company_account_with_sequence_number(sequence_number="85206")
    qiwa.admin_page.wait_page_to_load()
    qiwa.open_delegation_dashboard_page()
    qiwa.delegation_dashboard_page.wait_delegation_dashboard_page_to_load()\
        .select_english_localization_on_delegation_dashboard()\
        .should_active_breadcrumb_is_displayed_on_delegation_dashboard() \
        .should_location_breadcrumb_is_displayed_on_delegation_dashboard() \
        .should_page_title_has_correct_text_on_delegation_dashboard() \
        .should_add_delegation_button_has_correct_text() \
        .should_government_tab_has_correct_text() \
        .should_delegations_table_has_correct_title() \
        .should_search_is_displayed_on_delegation_dashboard() \
        .should_sort_by_is_displayed_on_delegation_dashboard() \
        .should_filter_button_has_correct_text() \
        .should_delegations_table_is_displayed()\
        .should_delegation_table_headers_have_correct_titles()\
        .should_rows_per_page_is_displayed_on_delegation_dashboard() \
        .should_pagination_is_displayed_on_delegation_dashboard()
