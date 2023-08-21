import re
import time

from selene import be, browser, by, command, have, query
from selene.support.shared.jquery_style import s, ss

import config
from data.constants import EmployeeTransfer, Language
from data.enums import RequestStatus, TransferType
from utils.assertion import assert_that
from src.ui.components.raw.table import Table


class EmployeeTransferPage:
    MESSAGE_LOCATOR = {
        "pass validation": by.css('div[name="password"] .validation-message span'),
        "validation": by.css('.validation-message[style=""] span.validation-message__text'),
        "validation sms": by.css(".validation-message--margin-bottom span"),
        "second validation": by.css(
            '.validation-message[style=""]:nth-child(3) span.validation-message__text'
        ),
        "top validation": by.css(".validation-message--margin-bottom span"),
        "error": by.css(".error-message"),
        "error token": by.css('[class="notices is-top"] > div'),
        "success": by.css("p.w-text--big"),
        "subscription_success": by.css(".request-submitted-box__title"),
        "transaction success": by.css(".media-content > div "),
        "edit profile success": by.css(".success.is-top > div"),
        "e service error": by.css(".error-message"),
        "nitaqat error": by.css(".validation-message__text--error"),
        "unconfirmed email error": by.css(".error_sign_in_email_not_confirmed"),
        "invalid credentials error": by.css(".error_sign_in_login_or_password_incorrect"),
        "invalid otp error": by.css(".error_otp_code_wrong"),
        "invalid absher error": by.css(".error_security_code_absher_invalid"),
        "account already exist": by.css(".error_account_already_exist"),
        "new password equals old": by.css(".error_new_password_equal_old_password"),
        "absher many attempts error": by.css(".error_security_code_absher_too_many_attempts"),
        "otp many attempts error": by.css(".error_otp_code_resend"),
        "locked account error": by.css(".error_account_locked span"),
        "e service success": by.css(".request-submitted-box__title"),
        "subscription success": by.css(".p-5"),
        "permissions": by.css(".u-align-center"),
        "certificate validation": by.css("p.is-danger"),
        "certificate error": by.css(".error-block p"),
        "confirmation error": by.css(".confirmation--error"),
        "error message": by.css(".error-message"),
        "valid": by.css(".input-valid span"),
        "valid second": by.css(".subscription__row:nth-child(2) .input-valid span"),
        "e-services pop up email title": by.css(".mt-3"),
        "e-services resend confirmation email": by.css('[role="alert"] div'),
        "confirmation message": ".confirmation-message",
        "et request": "#q-content svg + p",
        "et laborer request": ".is-top div div",
        "et sponsor request": ".Toastify__toast-body div",
    }
    breadcrumb = '[data-testid="router-link"]'

    info_banner = s('[data-testid="section-with-styles"]')
    title_employee_transfer = info_banner.s("h2")
    description = info_banner.ss("p").first
    establishment_id = s('[data-testid="establishment-id"]').ss("p")
    establishment_id_label = establishment_id.first
    establishment_id_value = establishment_id.second
    establishment_name = s('[data-testid="establishment-name"]')
    btn_request_employee_transfer = info_banner.s("button")

    title_transfer_request = ss('[data-testid="box-content"] h2').second
    tabs = s('[role="tablist"]')
    sent_requests = tabs.s("button")
    received_requests = tabs.s("button + button")
    btn_clear_filter = s('//button[.="Clear all filters"]')

    table_body = Table(s(".employee-transfer-MuiTable-root"))
    header_rows = table_body.header.s("tr").all("th")
    dropdown_status = header_rows.element(5).s(".statusSelect__control")
    list_of_statuses = ss(".statusSelect__option")
    all_table_rows = table_body.rows
    spinner = ".employee-transfer-MuiCircularProgress-root"
    rows_per_page = ".employee-transfer-MuiSelect-select"
    pagination_text = ".employee-transfer-MuiTablePagination-displayedRows"
    table_row_status = '[data-testid="row-value-status-id"]'
    row_per_page = s(".employee-transfer-MuiTablePagination-select")
    dropdown_row_per_page = ss(".employee-transfer-MuiList-root li")

    next_arrow = s('[title="Go to next page"]')

    btn_approve = '//div[.="Approve"]'
    btn_cancel = '//div[.="Cancel"]'
    btn_next = '//div[.="Next"]'

    # Rate popup
    rate_popup = '[title="Close"] + div'
    iframe = s('[title="adaaSurvey"]')
    rate_icon_close = ".demo__shutter"

    # Terms popup
    terms_popup = s('[data-testid="modal"]')
    terms_popup_icon_close = terms_popup.ss("button").first
    terms_popup_title = terms_popup.s("h2")
    terms_popup_description = terms_popup.ss("li")
    terms_popup_link = terms_popup.s("a")
    terms_popup_btn_approve = s('[data-testid="dialog-buttonText-btn"]')

    # Popup
    btn_accept = '//div[.="Accept"]'
    btn_accept_request = '//div[.="Accept request"]'
    btn_verify = '//div[.="Verify"]'
    btn_reject = '//div[.="Reject"]'
    btn_reject_request = '//div[.="Reject request"]'
    field_rejection_reason = 'input[name="reason"]'
    field_verification_code = 'input[type="password"]'

    # Transfer type & company
    title_employee_transfer_request_form = s('[data-testid="box-content"] div div')
    from_another_business_owner = s('[data-testid="dependent-section"]')
    between_my_establishments = s('[data-testid="sponsor-section"]')
    check_balance = '//p[.="Check balance"]'
    value_balance = '//span[.="Eligible"]/../../../td/div/button/../div'

    # Add Employee
    filter_iqama_number = ss('[placeholder="Search"]').second
    field_iqama_number = 'input[name="iqama"]'
    field_date_of_birth = 'input[data-testid="calendar-input"]'
    btn_search = '//div[.="Search"]'
    btn_select_to_transfer = '//div[.="Select to transfer"]'
    btn_create_contract = '//div[.="Create contract"]'

    # Warning popup
    warning_popup_description = s('[title="Close"] + div div')
    warning_popup_description_second_p = warning_popup_description.ss("p").second
    warning_popup_btn_agree = s('[data-testid="confirmation-modal-agree-button"]')

    # Redirection Popup
    popup_title = ".sc-gUAEMC.cMylqu h2"
    popup_body = ".sc-fWjsSh.gwVkNi p"
    popup_btn_proceed = '//div[.="Proceed"]'

    checkbox_agree = ".employee-transfer-PrivateSwitchBase-input"
    btn_place_the_request = '//div[.="Place the request"]'

    def __init__(self):
        super().__init__()
        self.et_url = config.settings.employee_transfer

    @staticmethod
    def __extract_number_inside_parentheses(text: str) -> str:
        return str(re.search(r"\((.*?)\)", text).group(1))

    def navigate_to_employee_transfer_by_link(self):
        browser.open(self.et_url)

    def wait_spinner_to_disappear(self):
        s(self.spinner).should(be.not_.visible)

    def verify_expected_status(self, status: dict, locale: str):
        self.table_body.row(1).cells.element_by_its(
            self.table_row_status, have.text(status[locale])
        )

    def verify_breadcrumb(self, text: dict, locale: str):
        s(self.breadcrumb).should(have.exact_text(text[locale]))

    def verify_title_employee_transfer(self, text: dict, locale: str):
        self.title_employee_transfer.should(have.exact_text(text[locale]))

    def verify_description(self, text: dict, locale: str):
        self.description.should(have.exact_text(text[locale]))

    def verify_establishment_id_label(self, text: dict, locale: str):
        self.establishment_id_label.should(have.exact_text(text[locale]))

    def verify_establishment_id_value(self, text: str):
        self.establishment_id_value.should(have.exact_text(text))

    def verify_establishment_name_label(self, text: dict, locale: str):
        self.establishment_name.should(have.text(text[locale]))

    def verify_establishment_name_value(self, text: str):
        self.establishment_name.should(have.text(text))

    def btn_request_employee_transfer_should_be_enabled(self):
        self.btn_request_employee_transfer.should(be.enabled)

    def click_btn_request_employee_transfer(self):
        self.btn_request_employee_transfer.click()
        return self

    # Transfer Requests section on Dashboard page

    def verify_title_transfer_request(self, locale: str):
        self.title_transfer_request.should(
            have.exact_text(EmployeeTransfer.TRANSFER_REQUESTS[locale])
        )

    def verify_title_tab_sent_requests(self, locale: str):
        self.sent_requests.should(have.text(EmployeeTransfer.SENT_REQUESTS[locale]))

    def verify_title_tab_received_requests(self, locale: str):
        self.received_requests.should(have.text(EmployeeTransfer.RECEIVED_REQUESTS[locale]))

    def click_sent_requests_tab(self):
        self.sent_requests.click()

    def click_received_requests_tab(self):
        self.received_requests.click()

    def verify_tab_sent_requests_is_active(self):
        self.sent_requests.should(have.attribute("aria-selected").value("true"))

    def verify_tab_received_requests_is_active(self):
        self.received_requests.should(have.attribute("aria-selected").value("true"))

    def verify_table_headers(self, locale: str):
        for row, header in zip(self.header_rows, EmployeeTransfer.HEADER_TITLES_LIST):
            row.should(have.text(header[locale]))

    def verify_placeholder_search(self, locale: str):
        list_of_search_elements = self.header_rows.all("input")
        for search_field in list_of_search_elements[:-1]:
            search_field.should(
                have.attribute("placeholder").value(EmployeeTransfer.PLACEHOLDER_SEARCH[locale])
            )

    def verify_statuses_in_dropdown(self):
        self.dropdown_status.click()
        self.list_of_statuses.should(have.exact_texts(RequestStatus.get_list_of_variable_values()))

    def select_first_row(self):
        self.table_body.row(1).web_element.s("img").click()

    def verify_expected_dates(self):
        self.table_body.row(2).web_element.ss("li p + p").should(
            have.exact_texts(EmployeeTransfer.EXPECTED_DATE)
        )

    def verify_count_of_rows(self, count: int):
        self.all_table_rows.should(have.size(count))

    def get_count_of_total_requests(self):
        return int(s(self.pagination_text).get(query.text).split()[-1])

    def verify_general_number_of_requests(self, amount: str):
        s(self.pagination_text).should(have.text(amount))

    def get_first_row(self) -> list:
        return [value.get(query.text) for value in self.table_body.row(1).cells]

    def get_rows_per_page(self):
        return int(s(self.rows_per_page).get(query.text))

    def verify_next_arrow_is_clickable(self):
        self.next_arrow.should(be.clickable)

    def click_next_arrow(self):
        self.next_arrow.click()

    def verify_first_row_on_focus(self):
        self.select_first_row()
        self.table_body.row(2).web_element.s("div p").should(
            have.exact_text(EmployeeTransfer.REQUEST_SUBMITTED[Language.EN])
        )

    def select_rows_per_page(self, count: str):
        self.row_per_page.click()
        self.dropdown_row_per_page.element_by(have.attribute("data-value").value(count)).click()

    def verify_filters(self):
        for expected_item, header in zip(self.get_first_row()[:5], self.header_rows):
            header.s("input").perform(command.js.set_value("")).type(expected_item)
            index = None
            for i, item in enumerate(self.header_rows):
                if str(item) == str(header):
                    index = i
                    break
            assert_that(self.get_first_row()[index]).equals_to(expected_item)

    def fill_req_number(self, text: str):
        self.header_rows.element(0).s("input").perform(command.js.set_value("")).type(
            text
        ).press_enter()

    def click_clear_filter_btn(self):
        time.sleep(1)
        self.btn_clear_filter.should(be.clickable).click()

    def verify_disabling_filters_fields(self):
        for element in self.header_rows[:5]:
            assert not element.s("input").get(query.value), (
                f"Element value {element.s('input').get(query.value)} " f"is not empty"
            )

    def get_general_number_of_requests_in_received_requests_tab(self) -> str:
        return self.__extract_number_inside_parentheses(self.received_requests.get(query.text))

    def get_general_number_of_requests_in_sent_requests_tab(self) -> str:
        return self.__extract_number_inside_parentheses(self.sent_requests.get(query.text))

    def click_btn_approve(self):
        s(self.btn_approve).click()

    def click_btn_cancel(self):
        s(self.btn_cancel).click()

    def click_btn_next(self):
        s(self.btn_next).click()

    # Terms popup

    def close_terms_popup(self):
        self.terms_popup_icon_close.click()

    def verify_terms_popup_title(self, text: dict, locale: str):
        self.terms_popup_title.should(have.exact_text(text[locale]))

    def verify_terms_popup_description(self, text: list, locale: str):
        for element, expected_text in zip(self.terms_popup_description, text):
            element.should(have.exact_text(expected_text[locale]))

    def verify_terms_popup_close_icon(self):
        self.close_terms_popup()
        self.terms_popup.should(be.not_.visible)

    def click_terms_popup_redirections_link(self):
        self.terms_popup_link.click()

    def verify_terms_popup_btn_approve(self, text: dict, locale: str):
        self.terms_popup_btn_approve.should(have.exact_text(text[locale]))

    # Employee Transfer Request page
    # Transfer type & company

    def verify_title_from_another_business_owner(self):
        self.title_employee_transfer_request_form.should(
            have.text(EmployeeTransfer.TITLE_FROM_ANOTHER_BUSINESS_OWNER)
        )

    def verify_title_transfer_laborer_between_my_establishments(self):
        self.title_employee_transfer_request_form.should(
            have.text(EmployeeTransfer.TITLE_TRANSFER_LABORER_BETWEEN_MY_ESTABLISHMENTS)
        )

    def select_transfer_type(self, transfer_type: TransferType):
        element = (
            self.from_another_business_owner
            if transfer_type == TransferType.FROM_ANOTHER_BUSINESS_OWNER
            else self.between_my_establishments
        )
        element.click()

    def select_target_company(self, establishment_number: str):
        self.all_table_rows.second.should(be.visible)
        self.all_table_rows.element_by(have.text(establishment_number)).s("input").click()

    def click_check_balance(self):
        s(self.check_balance).click()

    def get_actual_balance(self) -> int:
        return int(s(self.value_balance).get(query.text))

    # Add Employee

    def filter_by_iqama_number(self, number: int):
        self.filter_iqama_number.perform(command.js.set_value("")).type(number)

    def select_employee(self):
        self.table_body.row(1).web_element.s("input").click()

    def fill_field_iqama_number(self, number: int):
        s(self.field_iqama_number).perform(command.js.set_value("")).type(number)

    def select_field_date_of_birth(self, date: str):
        s(self.field_date_of_birth).perform(command.js.set_value("")).type(date)

    def click_btn_search(self):
        s(self.btn_search).click()

    def get_value_warning_popup(self):
        return int(
            self.__extract_number_inside_parentheses(
                self.warning_popup_description_second_p.get(query.text)
            )
        )

    def click_warning_popup_btn_agree(self):
        self.warning_popup_btn_agree.click()

    def click_btn_select_to_transfer(self):
        s(self.btn_select_to_transfer).click()

    def verify_redirections_popup(self):
        s(self.popup_title).should(have.exact_text(EmployeeTransfer.POPUP_REDIRECTION_TITLE))
        s(self.popup_body).should(have.exact_text(EmployeeTransfer.POPUP_REDIRECTION_BODY))

    def click_popup_btn_proceed(self):
        s(self.popup_btn_proceed).click()

    def click_btn_create_contract(self):
        s(self.btn_create_contract).click()

    def click_agree_checkbox(self):
        s(self.checkbox_agree).click()

    def click_btn_place_the_request(self):
        s(self.btn_place_the_request).click()

    def click_btn_accept(self):
        s(self.btn_accept).click()

    def click_btn_accept_request(self):
        s(self.btn_accept_request).click()

    def click_btn_verify(self):
        s(self.btn_verify).click()

    def fill_verification_code(self, code: str = "0000"):
        s(self.field_verification_code).perform(command.js.set_value("")).type(code)

    def click_btn_reject(self):
        s(self.btn_reject).click()

    def fill_field_rejection_reason(self, data: str = "Reject reason"):
        s(self.field_rejection_reason).perform(command.js.set_value("")).type(data)

    def click_btn_reject_request(self):
        s(self.btn_reject_request).click()

    def close_rate_popup(self):
        if s(self.rate_popup).matching(be.visible):
            browser.driver.switch_to.frame(self.iframe())
            s(self.rate_icon_close).click()
            browser.switch_to.default_content()
