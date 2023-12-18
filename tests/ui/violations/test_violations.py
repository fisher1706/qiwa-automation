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


class TestViolations:
    @pytest.fixture(autouse=True)
    def pre_test(self):
        qiwa.login_as_user(login=UserWithEstablishmentViolations.ID)
        qiwa.header.change_local(Language.EN)
        qiwa.workspace_page.select_company_account_with_sequence_number(
            UserWithEstablishmentViolations.ESTABLISHMENT_SEQUENCE
        )
        qiwa.dashboard_page.wait_dashboard_page_to_load()
        qiwa.meet_qiwa_popup.close_meet_qiwa_popup()
        qiwa.dashboard_page.select_e_services_menu_item()
        qiwa.e_services_page.select_establishment_violations()
        qiwa.violations_page.wait_for_page_to_load()

    @allure.title("Check remaining dashboard elements")
    @case_id(41112)
    def test_check_dashboard_elements(self):
        qiwa.violations_page.check_page_title()
        qiwa.violations_page.check_page_title()

    @allure.title("Login process")
    @case_id(32054)
    def test_sort_table(self):
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
                contains_added_string=SortingData.SORT_DICT[sorting_option][
                    "requires_sanitization"
                ],
            )

    @allure.title("Objection deadline passed")
    @case_id(33109)
    def test_objection_deadline_passed(self):
        (
            qiwa.violations_page.click_on_view_details_for_violation_with_no_objection_allowed(
                UserWithEstablishmentViolations.CANNOT_OBJECT_VIOLATION_ID
            )
        )
        qiwa.violation_details_page.check_cannot_object_message()

    @allure.title("Print functionality")
    @case_id(41583)
    def test_print_functionality(self):
        (
            qiwa.violations_page.click_on_view_details_for_violation_with_no_objection_allowed(
                UserWithEstablishmentViolations.AVAILABLE_OBJECT_VIOLATION_ID
            )
        ).wait_for_page_to_load()
        qiwa.violation_details_page.validate_print_btn_is_clickable()

    @allure.title("Filter violations")
    @case_id(33100)
    def test_violation_filters(self):
        filtering_types = TableFilters.VISIBLE_FILTERS
        for filter_data in filtering_types.keys():
            for filter_option in filtering_types[filter_data]["filter_options"]:
                column_name = filtering_types[filter_data]["related_column"]
                qiwa.violations_page.click_on_filters_btn().validate_correct_filters_available().expand_filter_options(
                    filter_data
                )
                if "date" not in filter_data:
                    qiwa.violations_page.choose_filter_option(
                        filter_option
                    ).click_on_apply_filters().wait_for_page_to_load()

                    filtered_col_index = qiwa.violations_page.find_column_index(column_name)
                    qiwa.violations_page.get_column_data(table_index=filtered_col_index)
                    if column_name == "Payment status":
                        qiwa.violations_page.validate_payment_status_table_data(filter_option)
                    elif column_name == "Objection ID":
                        qiwa.violations_page.validate_objection_id_table_data(filter_option)
                    qiwa.violations_page.click_on_filters_btn().clear_search_filters().click_on_apply_filters().wait_for_page_to_load()
                else:
                    qiwa.violations_page.open_filter_calendar(
                        filter_name=filter_data, filter_type=filter_option
                    ).choose_calendar_date(
                        TableFilters.START_DATE_FOR_FILTER
                    ).click_on_apply_filters().wait_for_page_to_load()
                    filtered_col_index = qiwa.violations_page.find_column_index(column_name)
                    data = qiwa.violations_page.get_column_data(table_index=filtered_col_index)
                    qiwa.violations_page.validate_date_filter(
                        data, TableFilters.END_DATE_FOR_FILTER, filter_type=filter_option
                    )
                    qiwa.violations_page.click_on_filters_btn().clear_search_filters().click_on_apply_filters().wait_for_page_to_load()

    @allure.title("Pagination")
    @case_id(33106)
    def test_pagination(self):
        qiwa.violations_page.validate_pagination().validate_pagination_arrows()

    @allure.title("Table of Violations")
    @case_id(41113)
    def test_table_of_violations(self):
        for column_name in TableColumns.COLUMNS.keys():
            qiwa.violations_page.validate_column_data_format(
                column_name, TableColumns.COLUMNS[column_name]["pattern"]
            )

    @allure.title("Search Violations")
    @case_id(33095)
    def test_search_violations(self):
        qiwa.violations_page.insert_search_input("7").wait_for_page_to_load().check_search_results(
            "7"
        )
        qiwa.violations_page.clear_search_field().wait_for_page_to_load()

    @allure.title("Select results per page")
    @case_id(33105)
    def test_select_results_per_page(self):
        qiwa.violations_page.open_pagination_dropdown().validate_pagination_number_of_rows_options()

    @allure.title(" Check Violation Details elements ")
    @case_id(41582)
    def test_violation_details_elements(self):
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
