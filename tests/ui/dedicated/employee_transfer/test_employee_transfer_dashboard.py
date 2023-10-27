import allure
import pytest

from data.constants import Language
from data.dedicated.employee_trasfer.employee_transfer import employer_old
from data.dedicated.transfer_requests import request
from src.ui.actions.old_employee_transfer import EmployeeTransferActionsOld
from src.ui.components.footer import Footer


@allure.feature('Employee Transfer Dashboard')
@pytest.mark.skip("Old design")
class TestEmployeeTransfer:  # pylint: disable=unused-argument

    @pytest.fixture(autouse=True)
    def pre_test(self):
        self.employee_transfer_actions = EmployeeTransferActionsOld()
        self.footer = Footer()

    @allure.title('Create the Dashboard page | Block 1 UI test')
    def test_view_employee_transfer_dashboard(self):
        self.employee_transfer_actions.navigate_to_et_service(employer_old)
        self.employee_transfer_actions.verify_info_banner(Language.EN)
        self.footer.click_on_lang_button(Language.AR)
        self.employee_transfer_actions.verify_info_banner(Language.AR)

    @allure.title('Create the Dashboard page | Terms & Conditions pop-up UI test')
    def test_terms_and_conditions_pop_up_ui_test(self):
        self.employee_transfer_actions.navigate_to_et_service(employer_old)
        self.employee_transfer_actions.verify_terms_conditions_popup(Language.EN)
        self.footer.click_on_lang_button(Language.AR)
        self.employee_transfer_actions.verify_terms_conditions_popup(Language.AR)

    @allure.title('Create Transfer Requests | Sent Requests General UI test')
    def test_sent_requests_general_ui_test(self):
        self.employee_transfer_actions.navigate_to_et_service(employer_old)
        self.employee_transfer_actions.verify_sent_requests_tab(Language.EN)
        self.footer.click_on_lang_button(Language.AR)
        self.employee_transfer_actions.verify_sent_requests_tab(Language.AR)

    @allure.title('Create Transfer Requests | Received Requests General UI test')
    def test_received_requests_general_ui_test(self):
        self.employee_transfer_actions.navigate_to_et_service(employer_old)
        self.employee_transfer_actions.verify_received_requests_tab(Language.EN)
        self.footer.click_on_lang_button(Language.AR)
        self.employee_transfer_actions.verify_received_requests_tab(Language.AR)

    @allure.title('Create Transfer Requests | Pagination and counters UI test')
    def test_pagination_and_counters_ui_test(self):
        self.employee_transfer_actions.navigate_to_et_service(employer_old)
        self.employee_transfer_actions.verify_next_arrow_is_clickable()
        self.employee_transfer_actions.verify_pagination()
        self.employee_transfer_actions.click_received_requests_tab()
        self.employee_transfer_actions.verify_pagination()

    @allure.title('Create Transfer Requests | Search fields and Clear filters UI test')
    def test_search_fields_and_clear_filters_ui_test(self):
        self.employee_transfer_actions.navigate_to_et_service(employer_old)
        self.employee_transfer_actions.verify_filters()
        self.employee_transfer_actions.click_clear_filter_btn()
        self.employee_transfer_actions.verify_disabling_filters_fields()
        self.employee_transfer_actions.click_received_requests_tab()
        self.employee_transfer_actions.verify_filters()
        self.employee_transfer_actions.click_clear_filter_btn()
        self.employee_transfer_actions.verify_disabling_filters_fields()

    @allure.title('Create Transfer Requests | Request historic dates UI test')
    def test_request_historic_dates_ui_test(self):
        self.employee_transfer_actions.navigate_to_et_service(employer_old)
        self.employee_transfer_actions.fill_req_number(request.req_number)
        self.employee_transfer_actions.select_first_row()
        self.employee_transfer_actions.verify_expected_dates()
        # TODO(dp): Add verification of the expected dates after providing correct request
        # self.employee_transfer_actions.click_received_requests_tab()

    @allure.title('Create Transfer Requests | Request status filter dropdown UI test')
    def test_request_status_filter_dropdown_ui_test(self):
        self.employee_transfer_actions.navigate_to_et_service(employer_old)
        self.employee_transfer_actions.verify_statuses_in_dropdown()
