import allure
import pytest

from data.constants import Language
from data.establishment_violations.constants import (
    SortingData,
    TableColumns,
    TableFilters,
    UserWithEstablishmentViolations,
    ViolationDetailsPageText,
)
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.VIOLATIONS)


@pytest.fixture(autouse=True)
def navigate_to_establishment_violations():
    qiwa.login_as_user(login=UserWithEstablishmentViolations.ID)
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_company_account_with_sequence_number(
        UserWithEstablishmentViolations.ESTABLISHMENT_SEQUENCE
    )
    qiwa.dashboard_page.wait_dashboard_page_to_load()
    qiwa.meet_qiwa_popup.close_meet_qiwa_popup_if_displayed()
    qiwa.dashboard_page.select_e_services_menu_item()
    qiwa.e_services_page.select_establishment_violations()
    qiwa.violations_page.wait_for_page_to_load()


@allure.title("Search Violations")
@case_id(141755)
def test_search_violations():
    qiwa.violations_page.insert_search_input("7").wait_for_page_to_load().check_search_results("7")


@allure.title("Sort violations")
@case_id(141756)
def test_sort_table():
    for sorting_option in SortingData.SORT_DICT.keys():
        table_index = qiwa.violations_page.find_column_index(
            SortingData.SORT_DICT[sorting_option]["column_name"]
        )
        data_list = (
            qiwa.violations_page.select_sort_filter(sorting_option)
            .wait_for_page_to_load()
            .get_column_data(table_index)
        )
        qiwa.violations_page.verify_data_sorted_correctly(
            data=data_list,
            reverse=SortingData.SORT_DICT[sorting_option]["DSC"],
            is_date=SortingData.SORT_DICT[sorting_option]["is_date"],
            contains_added_string=SortingData.SORT_DICT[sorting_option]["requires_sanitization"],
        )


@allure.title("Filter violations")
@case_id(141757)
def test_violation_filters():
    filtering_types = TableFilters.VISIBLE_FILTERS
    for filter_data in filtering_types.keys():
        for filter_option in filtering_types[filter_data]["filter_options"]:
            column_name = filtering_types[filter_data]["related_column"]
            qiwa.violations_page.click_on_filters_btn().validate_correct_filters_available().expand_filter_options(
                filter_data
            )
            qiwa.violations_page.apply_and_validate_filter(filter_data, filter_option, column_name)


@allure.title("Select results per page")
@case_id(141758)
def test_select_results_per_page():
    qiwa.violations_page.open_pagination_dropdown().validate_pagination_number_of_rows_options()


@allure.title("Change pages")
@case_id(141759)
def test_change_pages():
    qiwa.violations_page.validate_pagination().validate_pagination_arrows()


@allure.title("Check remaining dashboard elements")
@case_id(141760)
def test_check_dashboard_elements():
    qiwa.violations_page.check_page_title()
    qiwa.violations_page.check_page_title()


@allure.title("Table of Violations")
@case_id(141761)
def test_table_of_violations():
    for column_name in TableColumns.COLUMNS.keys():
        qiwa.violations_page.validate_column_data_format(
            column_name, TableColumns.COLUMNS[column_name]["pattern"]
        )


@allure.title("Check Violation Details elements")
@case_id(141762)
def test_violation_details_elements():
    qiwa.violations_page.click_on_view_details_for_first_violation(
        UserWithEstablishmentViolations.AVAILABLE_OBJECT_VIOLATION_ID
    )
    for column_name in ViolationDetailsPageText.KEYS.keys():
        qiwa.violation_details_page.validate_view_details_elements(
            column_name, ViolationDetailsPageText.KEYS[column_name]["pattern"]
        )
    for column_name in ViolationDetailsPageText.OBJECTION_KEYS.keys():
        qiwa.violation_details_page.validate_view_details_elements(
            column_name, ViolationDetailsPageText.OBJECTION_KEYS[column_name]["pattern"]
        )


@allure.title("Print functionality")
@case_id(141764)
def test_print_functionality():
    (
        qiwa.violations_page.click_on_view_details_for_violation_with_no_objection_allowed(
            UserWithEstablishmentViolations.AVAILABLE_OBJECT_VIOLATION_ID
        )
    ).wait_for_page_to_load()
    qiwa.violation_details_page.validate_print_btn_is_clickable()


@allure.title("Objection deadline passed")
@case_id(141765)
def test_objection_deadline_passed():
    (
        qiwa.violations_page.click_on_view_details_for_violation_with_no_objection_allowed(
            UserWithEstablishmentViolations.CANNOT_OBJECT_VIOLATION_ID
        )
    )
    qiwa.violation_details_page.check_cannot_object_message()
