import math
from datetime import datetime
import allure
from selene.support.shared.jquery_style import s, ss
from selene import be, query
from data.establishment_violations.constants import (
    TableFilters,
    PageText,
    PaginationOptions,
)
import re


class ViolationsPage:
    PAGE_LOADER = ss(".react-loading-skeleton")
    TABLE_HEADERS = ss("//table//th")
    NO_RESULTS_FOUND_TEXT = s("//*[text()='No results found.']")
    VIOLATION_ID_HEADER = s("//table//th[text()='Violation ID']")
    SORT_DROPDOWN_OPENER = s("//input[@id='violationsSort']")
    TABLE_SEARCH_INPUT = s("//input[@id='violationsSearch']")
    TABLE_SEARCH_INPUT_CLEAR_BTN = s("[aria-label='Delete']")
    TABLE_FILTER_BTN = s("[data-testid='filters-btn']")
    DASHBOARD_HEADER = s("//h1")
    GENERAL_INFO_PARAGRAPH_ONE = s("//header//p[1]")
    GENERAL_INFO_PARAGRAPH_TWO = s("//header//p[2]")

    APPLY_FILTERS_BTN = s("[data-testid='apply-filters']")
    PAYMENT_COLUMN_DATA = ss("[data-testid='payment']")
    OBJECTION_ID_COLUMN_DATA = ss("[data-testid='objection-id']")
    CLEAR_FILTERS_BTNS = ss("//*[text()='CLEAR']")
    PAGINATION_DROPDOWN = s("#violationsPerPage")
    PAGINATION_OPTIONS = ss("[role='option']")
    PAGINATION_TEXT = s("//*[@data-component='Pagination']//p")
    PAGINATION_NEXT_BTN = s("//span[text()='Next']")
    PAGINATION_PREVIOUS_BTN = s("//span[text()='Previous']")
    DATE_OF_VIOLATION_START_DATE_FILTER_INPUT = s(
        "//input[@id='filters.dateOfViolation.startDate']"
    )
    DATE_OF_VIOLATION_END_DATE_FILTER_INPUT = s("//input[@id='filters.dateOfViolation.endDate']")
    DATE_OF_BLOCKING_START_DATE_FILTER_INPUT = s("//input[@id='filters.dueDate.startDate']")
    DATE_OF_BLOCKING_END_DATE_FILTER_INPUT = s("//input[@id='filters.dueDate.endDate']")
    PAGINATION_NUMBERS_LIST = ss("//*[@data-testid='pagination']//li")
    MONTH_SELECT_DROPDOWN = s("[aria-label='Month select']")
    MONTH_OPTIONS_LIST = ss("[role='option']")
    YEAR_SELECT_DROPDOWN = s("[aria-label='Year select']")

    DYNAMIC_YEAR_OPTIONS_LIST = "//*[@role='option']//p[text()='{}']"
    DYNAMIC_DAY_SELECTOR = "//*[@role='gridcell' and @data-testid='undefined-{}']"

    DYNAMIC_TABLE_COL_DATA = "//tbody//td[{}]//*[normalize-space(text()) != '']"
    DYNAMIC_SORT_DROPDOWN_OPTION = (
        "//input[@id='violationsSort']//ancestor::div["
        "@data-component='Select']//li//div//p[text()='{}']"
    )
    DYNAMIC_FILTER_MENU = "//*[@data-component='Accordion']//button//*[text()='{}']"
    DYNAMIC_FILTER_OPTION = "//*[@data-testid='{}']//ancestor::div[@data-component='Checkbox']"

    DYNAMIC_VIOLATION_VIEW_DETAILS_ANCHOR = "//*[@href='/violation/{}']"

    def find_column_index(self, header_text):
        self.TABLE_HEADERS[1].should(be.visible)
        index = 1
        for header in self.TABLE_HEADERS:
            if header.get(query.text) == header_text:
                return index
            index += 1
        return -1

    @allure.step
    def wait_for_page_to_load(self):
        self.PAGE_LOADER[-1].wait_until(be.absent)
        return self

    def get_column_data(self, table_index):
        # Appending column data to list (index is incremented by 1 due to the existence of a hidden column in the table
        return [
            el.get(query.text) for el in ss(self.DYNAMIC_TABLE_COL_DATA.format(table_index + 1))
        ]

    @allure.step
    def select_sort_filter(self, filter_name):
        self.click_on_sort_input()
        el = s(self.DYNAMIC_SORT_DROPDOWN_OPTION.format(filter_name))
        el.wait_until(be.visible)
        el.click()
        return self

    @allure.step
    def click_on_sort_input(self):
        self.SORT_DROPDOWN_OPENER.click()
        return self

    @allure.step
    def verify_data_sorted_correctly(
        self, data, reverse, is_date=False, contains_added_string=False
    ):
        if is_date:
            # Convert date strings to datetime objects
            data = [datetime.strptime(date, "%d/%m/%Y") for date in data if date != "-"]
        if contains_added_string:
            data = [self.extract_numbers(text) for text in data if text != "-"]
        assert data == sorted(data, reverse=reverse)
        return self
    @allure.step
    def validate_date_filter(self, data, date_filter, filter_type):
        date_filter = datetime.strptime(date_filter, "%d/%m/%Y")
        data = [datetime.strptime(date, "%d/%m/%Y") for date in data if date != "-"]
        data.append(date_filter)
        assert sorted(data)[0 if filter_type == "Start date" else -1] == date_filter

    @allure.step
    def extract_numbers(self, input_string):
        return int("".join(char for char in input_string if char.isdigit()))

    @allure.step
    def check_page_title(self):
        assert self.DASHBOARD_HEADER.should(be.visible).get(query.text) == PageText.TITLE

    @allure.step
    def check_page_header(self):
        assert self.GENERAL_INFO_PARAGRAPH_ONE == PageText.GENERAL_INFO_ONE
        assert self.GENERAL_INFO_PARAGRAPH_TWO == PageText.GENERAL_INFO_TWO

    @allure.step
    def go_to_next_pagination_page(self):
        self.PAGINATION_NEXT_BTN.should(be.clickable).click()
        return self

    @allure.step
    def go_to_previous_pagination_page(self):
        self.PAGINATION_PREVIOUS_BTN.should(be.clickable).click()
        return self

    @allure.step
    def click_on_view_details_for_violation_with_no_objection_allowed(self, violation_id):
        view_details_link = s(self.DYNAMIC_VIOLATION_VIEW_DETAILS_ANCHOR.format(violation_id))
        view_details_link.should(be.visible).click()
        return self

    @allure.step
    def click_on_view_details_for_first_violation(self, violation_id):
        VIEW_DETAILS_LINK = s(self.DYNAMIC_VIOLATION_VIEW_DETAILS_ANCHOR.format(violation_id))
        VIEW_DETAILS_LINK.should(be.visible).click()

    @allure.step
    def validate_payment_status_table_data(self, status):
        payment_texts = [element.get(query.text) for element in self.PAYMENT_COLUMN_DATA]
        for text in payment_texts:
            assert text == status

    @allure.step
    def validate_objection_id_table_data(self, status):
        not_expected_result = "-" if status == "Objected" else ""
        objection_ids = [element.get(query.text) for element in self.OBJECTION_ID_COLUMN_DATA]
        for text in objection_ids:
            assert text != not_expected_result

    @allure.step
    def click_on_filters_btn(self):
        self.TABLE_FILTER_BTN.click()
        return self

    @allure.step
    def validate_correct_filters_available(self):
        for violation_filter in TableFilters.VISIBLE_FILTERS.keys():
            s(
                self.DYNAMIC_FILTER_MENU.format(
                    TableFilters.VISIBLE_FILTERS[violation_filter]["filter_header_text"]
                )
            ).should(be.visible)
        return self

    @allure.step
    def expand_filter_options(self, filter_name):
        s(
            self.DYNAMIC_FILTER_MENU.format(
                TableFilters.VISIBLE_FILTERS[filter_name]["filter_header_text"]
            )
        ).click()
        return self

    def choose_filter_option(self, filter_option):
        s(self.DYNAMIC_FILTER_OPTION.format(filter_option)).wait_until(be.visible)
        s(self.DYNAMIC_FILTER_OPTION.format(filter_option)).click()
        return self

    @allure.step
    def open_filter_calendar(self, filter_name, filter_type):
        if filter_name == "date_of_violation":
            if filter_type == "Start date":
                self.DATE_OF_VIOLATION_START_DATE_FILTER_INPUT.wait_until(be.clickable)
                self.DATE_OF_VIOLATION_START_DATE_FILTER_INPUT.click()
            elif filter_type == "End date":
                self.DATE_OF_VIOLATION_END_DATE_FILTER_INPUT.wait_until(be.clickable)
                self.DATE_OF_VIOLATION_END_DATE_FILTER_INPUT.click()
        elif filter_name == "date_of_blocking_the_service":
            if filter_type == "Start date":
                self.DATE_OF_BLOCKING_START_DATE_FILTER_INPUT.wait_until(be.clickable)
                self.DATE_OF_BLOCKING_START_DATE_FILTER_INPUT.click()
            elif filter_type == "End date":
                self.DATE_OF_BLOCKING_END_DATE_FILTER_INPUT.wait_until(be.clickable)
                self.DATE_OF_BLOCKING_END_DATE_FILTER_INPUT.click()

        return self

    @allure.step
    def choose_calendar_date(self, date_string):
        day, month, year = date_string.split("/")
        self.YEAR_SELECT_DROPDOWN.should(be.clickable).click()
        s(self.DYNAMIC_YEAR_OPTIONS_LIST.format(year)).should(be.visible).click()
        self.MONTH_SELECT_DROPDOWN.should(be.clickable).click()
        self.MONTH_OPTIONS_LIST[int(month.lstrip("0"))].should(be.clickable).click()
        s(self.DYNAMIC_DAY_SELECTOR.format(day.lstrip("0"))).should(be.clickable).click()
        return self

    @allure.step
    def click_on_apply_filters(self):
        self.APPLY_FILTERS_BTN.click()
        return self

    @allure.step
    def clear_search_filters(self):
        for btn in self.CLEAR_FILTERS_BTNS:
            btn.click()
        return self

    @allure.step
    def get_number_of_rows_per_page(self):
        self.PAGINATION_DROPDOWN.wait_until(be.visible)
        return int(self.PAGINATION_DROPDOWN.should(be.visible).get(query.value))

    @allure.step
    def get_total_number_of_rows(self):
        self.PAGINATION_TEXT.wait_until(be.visible)
        return int(self.PAGINATION_TEXT.should(be.visible).get(query.text).split()[2])

    @allure.step
    def get_number_of_pages(self):
        self.PAGINATION_NUMBERS_LIST[-1].wait_until(be.visible)
        return int(self.PAGINATION_NUMBERS_LIST[-1].should(be.visible).get(query.text))

    @allure.step
    def validate_pagination(self):
        assert math.ceil(self.get_total_number_of_rows() / self.get_number_of_rows_per_page()) == self.get_number_of_pages()
        return self
    @allure.step
    def validate_pagination_arrows(self):
        if math.ceil(self.get_total_number_of_rows() / self.get_number_of_rows_per_page()) > 1:
            self.go_to_next_pagination_page().wait_for_page_to_load()
            self.go_to_previous_pagination_page()
        return self

    @allure.step
    def insert_search_input(self, search_input):
        self.TABLE_SEARCH_INPUT.should(be.visible).send_keys(search_input)
        return self

    @allure.step
    def check_search_results(self, search_text):
        for violation_data, objection_data in zip(
            self.get_column_data(self.find_column_index("Violation ID")),
            self.get_column_data(self.find_column_index("Objection ID")),
        ):
            assert search_text in violation_data or search_text in objection_data
        return self

    @allure.step
    def clear_search_field(self):
        self.TABLE_SEARCH_INPUT_CLEAR_BTN.click()
        return self

    @allure.step
    def open_pagination_dropdown(self):
        self.PAGINATION_DROPDOWN.click()
        return self

    @allure.step
    def validate_pagination_number_of_rows_options(self):
        self.PAGINATION_OPTIONS[0].wait_until(be.visible)
        for option in self.PAGINATION_OPTIONS:
            assert int(option.get(query.text)) in PaginationOptions.OPTIONS
        return self

    @allure.step
    def validate_column_data_format(self, column_name, pattern):
        self.VIOLATION_ID_HEADER.with_(timeout=50).should(be.visible)
        for data in self.get_column_data(table_index=self.find_column_index(column_name)):
            assert self.validate_format(data, pattern) or data == "-"

    @staticmethod
    def validate_format(input_string, pattern):
        return bool(re.match(pattern, input_string))
