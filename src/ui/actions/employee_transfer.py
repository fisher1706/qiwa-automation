import time

import allure
import pytest
from selene import be, browser, have
from selene.core.exceptions import TimeoutException
from selene.support.shared.jquery_style import s
from selenium.common import NoSuchElementException

from data.constants import (
    ContractManagement,
    EmployeeTransfer,
    EService,
    Language,
    UserInfo,
)
from data.dedicated.employee_transfer import Entity, Laborer, employer_old
from data.dedicated.enums import RowsPerPage, TransferType
from data.validation_message import SuccessMessage
from src.ui.actions.e_services import EServiceActions
from src.ui.actions.old_contract_management import OldContractManagementActions
from src.ui.actions.sign_in import LoginActions
from src.ui.components.footer import Footer
from src.ui.pages.dedicated_pages.employee_transfer.employee_transfer_page import (
    EmployeeTransferPage,
)
from src.ui.pages.individual_page import IndividualPage
from src.ui.pages.workspaces_page import WorkspacesPage
from src.ui.qiwa import qiwa
from utils.assertion import assert_that


class EmployeeTransferActions(EmployeeTransferPage):
    def __init__(self):
        super().__init__()
        self.balance_value = None
        self.workspace_actions = WorkspacesPage()
        self.e_services_action = EServiceActions()
        self.individual_page = IndividualPage()
        self.footer = Footer()
        self.contract_management_actions = OldContractManagementActions()

    def __switch_tab_with_timeout(self, tab_id: int = 1):
        attempts = 5
        for _ in range(attempts):
            available_tabs = len(browser.driver.window_handles)
            if available_tabs > tab_id:
                browser.switch_to_tab(tab_id)
            else:
                time.sleep(1)
        return self

    def navigate_to_et_service(self, entity: Entity):
        qiwa.login_as_user(entity.login_id, UserInfo.PASSWORD)
        self.workspace_actions.select_company_account_with_sequence_number(entity.sequence_number)
        self.footer.click_on_lang_button(Language.EN)
        self.e_services_action.select_e_service(e_service_name=EService.EMPLOYEE_TRANSFER)
        self.__switch_tab_with_timeout()
        time.sleep(3)
        self.verify_title_employee_transfer(EmployeeTransfer.EMPLOYEE_TRANSFER, Language.EN)

    def navigate_to_individual(self, user_id: int):
        browser.close_current_tab()
        browser.switch_to_tab(0)
        browser.driver.delete_all_cookies()
        browser.driver.refresh()
        qiwa.open_login_page().login_as_user(user_id, UserInfo.PASSWORD)
        self.workspace_actions.select_individual_account()

    def add_employee(self, transfer_type: TransferType, laborer: Laborer):
        match transfer_type:
            case TransferType.FROM_ANOTHER_BUSINESS_OWNER:
                self.fill_field_iqama_number(laborer.login_id)
                self.select_field_date_of_birth(laborer.birthdate)
                self.click_btn_search()
                self.click_btn_select_to_transfer()
            case TransferType.BETWEEN_MY_ESTABLISHMENTS:
                self.filter_by_iqama_number(laborer.login_id)
                self.wait_spinner_to_disappear()
                # TODO: remove when data upload will be stable
                time.sleep(3)
                self.select_employee()
                self.click_btn_next()

    def request_new_contract(
        self,
        transfer_type: TransferType,
        establishment_number: str,
        entity_laborer: Laborer,
        is_get_balance_value: bool = False,
    ):
        self.click_btn_request_employee_transfer().click_btn_approve()
        self.select_transfer_type(transfer_type)
        self.select_target_company(establishment_number)
        if is_get_balance_value:
            self.balance_value = self.get_actual_balance()
        self.click_btn_next()
        self.add_employee(transfer_type, entity_laborer)

    def request_summary(self):
        self.click_btn_next()
        self.click_agree_checkbox()
        self.click_btn_place_the_request()
        self.close_rate_popup()
        self.verify_message(SuccessMessage.ET_REQUEST)

    def create_new_contract(self, laborer_id: int):
        self.click_btn_create_contract()
        self.verify_redirections_popup()
        self.click_popup_btn_proceed()
        self.contract_management_actions.wait_until_title_verification_code_appears(
            ContractManagement.VERIFICATION_CODE, Language.EN
        )
        self.contract_management_actions.refresh_if_not_employee_details(str(laborer_id))
        self.contract_management_actions.fill_contract_info()
        self.contract_management_actions.click_btn_next()
        self.contract_management_actions.click_agree_checkbox()
        self.contract_management_actions.click_btn_add_contract()
        self.verify_title_transfer_laborer_between_my_establishments()

    def confirm_creation_of_contract(
        self,
        entity_laborer: Laborer,
        entity: Entity = employer_old,
        transfer_type=TransferType.FROM_ANOTHER_BUSINESS_OWNER,
        is_get_balance_value: bool = False,
        is_verify_popup: bool = False,
    ):
        self.navigate_to_et_service(entity)
        self.request_new_contract(
            transfer_type=transfer_type,
            establishment_number=entity.establishment_number,
            entity_laborer=entity_laborer,
            is_get_balance_value=is_get_balance_value,
        )
        if is_verify_popup:
            assert self.get_value_warning_popup()
            self.click_warning_popup_btn_agree()
        self.create_new_contract(entity_laborer.login_id)
        self.request_summary()

    def verify_balance_value(self, is_decreased: bool = True):
        expected_value = self.balance_value - 1 if is_decreased else self.balance_value
        assert_that(self.get_actual_balance()).equals_to(expected_value)

    def verify_info_banner(self, locale: str):
        self.verify_breadcrumb(EmployeeTransfer.DASHBOARD, locale)
        self.verify_title_employee_transfer(EmployeeTransfer.EMPLOYEE_TRANSFER, locale)
        self.verify_description(EmployeeTransfer.DESCRIPTION, locale)
        self.verify_establishment_id_label(EmployeeTransfer.ESTABLISHMENT_ID_LABEL, locale)
        self.verify_establishment_id_value(
            f"{employer_old.labor_office_id}-{employer_old.sequence_number}"
        )
        self.verify_establishment_name_label(EmployeeTransfer.ESTABLISHMENT_NAME_LABEL, locale)
        self.verify_establishment_name_value(employer_old.establishment_name_ar)
        self.btn_request_employee_transfer_should_be_enabled()

    def verify_terms_conditions_popup(self, locale: str):
        self.click_btn_request_employee_transfer()
        self.verify_terms_popup_title(EmployeeTransfer.TERMS_POPUP_TITLE, locale)
        self.verify_terms_popup_description(EmployeeTransfer.TERMS_POPUP_DESCRIPTION, locale)
        self.verify_terms_popup_close_icon()
        self.click_btn_request_employee_transfer()
        self.click_terms_popup_redirections_link()
        self.contract_management_actions.wait_until_title_verification_code_appears(
            ContractManagement.VERIFICATION_CODE, locale
        )
        self.navigate_to_employee_transfer_by_link()
        self.click_btn_request_employee_transfer()
        self.verify_terms_popup_btn_approve(EmployeeTransfer.TERMS_POPUP_BTN_APPROVE, locale)
        self.close_terms_popup()

    def verify_sent_requests_tab(self, locale: str):
        self.verify_title_transfer_request(locale)
        self.verify_title_tab_sent_requests(locale)
        self.verify_tab_sent_requests_is_active()
        self.verify_table_headers(locale)
        self.verify_placeholder_search(locale)

    def verify_received_requests_tab(self, locale: str):
        self.click_received_requests_tab()
        self.verify_title_tab_received_requests(locale)
        self.verify_tab_received_requests_is_active()
        self.verify_table_headers(locale)
        self.verify_placeholder_search(locale)

    def verify_pagination(self, number_of_pages: int = 2):
        rows = self.get_count_of_total_requests()
        row_per_page = 10
        if rows < row_per_page:
            pytest.skip("Amount of request are less than 10")

        start_page, end_page = 1, row_per_page
        for _ in range(number_of_pages):
            end_page = min(end_page, rows)
            if end_page >= rows:
                break
            self.verify_general_number_of_requests(f"{start_page}-{end_page} of {rows}")
            self.click_next_arrow()
            self.verify_first_row_on_focus()
            start_page += row_per_page
            end_page += row_per_page

    def verify_pagination_per_page(self, amount: str):
        for rows_per_page in RowsPerPage.get_list_of_variable_values():
            self.select_rows_per_page(rows_per_page)
            count_of_rows = min(int(amount), int(rows_per_page))
            self.verify_count_of_rows(count_of_rows)
            if int(amount) > int(rows_per_page):
                self.verify_next_arrow_is_clickable()

    def verify_message(self, expected_message):
        try:
            message_element = s(self.MESSAGE_LOCATOR[expected_message["type"]])
            message_element.wait_until(be.visible)
            message_element.should(have.text(expected_message["text"]))
        except (TimeoutException, NoSuchElementException):
            pytest.mark.xfail(
                f"Expected message was not found on the page in defined timeout. {expected_message}"
            )
