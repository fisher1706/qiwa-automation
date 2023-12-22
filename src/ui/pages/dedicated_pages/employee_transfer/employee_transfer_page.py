from __future__ import annotations

from selene import be, have, query
from selene.core.entity import Element
from selene.support.shared.jquery_style import s, ss

from src.ui.components.raw.table import Table
from src.ui.pages.dedicated_pages.employee_transfer.summary_page import SummaryPage
from src.ui.pages.dedicated_pages.employee_transfer.transfer_between_my_establishments_page import (
    TransferBetweenMyEstablishmentsPage,
)
from src.ui.pages.dedicated_pages.employee_transfer.transfer_from_external_company_page import (
    TransferFromExternalCompanyPage,
)
from utils.allure import allure_steps
from utils.selene import scroll_into_view_if_needed


@allure_steps
class EmployeeTransferPage(
    TransferBetweenMyEstablishmentsPage, TransferFromExternalCompanyPage, SummaryPage
):
    btn_transfer_employee = s("//button[.='Transfer employee']")

    tiles = ss('[data-testid="tile-desktop"] button')
    own_establishment = tiles.first
    another_establishment = tiles.second

    recruitment_quota = ss('[data-testid="desktop_wrapper"] p').second

    btn_proceed_to_contract_management = s("//button[.='Proceed to Contract Management']")

    sent_requests_section = s("#requests-sent-by-you + div + div")
    received_requests_pending_decision = s("#requests-sent-by-you + div")
    received_requests_section = s("#received-requests + div + div")

    sent_requests_table = Table(sent_requests_section.s("table"))
    received_requests_table = Table(received_requests_section.s("table"))

    field_rejection_reason = s("#rejectReason")
    field_sponsor_rejection_reason = s("#rejectionReason")

    pagination_info = '[data-component="Table"] + div > div > p'
    sent_requests_pagination_info = sent_requests_section.s(pagination_info)
    received_requests_pagination_info = received_requests_section.s(pagination_info)

    search_sent_requests = s("#sent")
    search_received_requests_pending = s("#SearchField-requests_pending")
    search_received_requests = s("#received")

    btn_accept = s("//button[.='Accept']")
    btn_accept_request = s("//button[.='Accept request']")
    btn_yes_accept_transfer = s("//button[.='Yes, accept transfer']")
    btn_reject = s("//button[.='Reject']")
    btn_reject_request = s("//button[.='Reject request']")
    btn_reject_transfer = s("//button[.='Reject transfer']")

    @staticmethod
    def _get_count_of_requests(web_element: Element) -> int:
        return int(web_element.get(query.text).split()[2])

    def click_btn_transfer_employee(self) -> EmployeeTransferPage:
        self.btn_transfer_employee.click()
        return self

    def select_own_establishment(self) -> EmployeeTransferPage:
        self.own_establishment.click()
        return self

    def select_another_establishment(self) -> EmployeeTransferPage:
        self.another_establishment.click()
        return self

    def get_recruitment_quota(self) -> int:
        return int(self.recruitment_quota.get(query.text))

    def click_btn_proceed_to_contract_management(self) -> EmployeeTransferPage:
        self.btn_proceed_to_contract_management.click()
        return self

    def check_count_of_sent_request_rows(self) -> None:
        requests = EmployeeTransferPage._get_count_of_requests(self.sent_requests_pagination_info)
        rows = requests if requests < 10 else 10
        self.sent_requests_table.rows.should(have.size(rows))

    def check_count_of_received_request_rows(self) -> None:
        requests = EmployeeTransferPage._get_count_of_requests(
            self.received_requests_pagination_info
        )
        rows = requests if requests < 10 else 10
        self.received_requests_table.rows.should(have.size(rows))

    def search_sent_request(self, iqama_number: str) -> EmployeeTransferPage:
        self.sent_requests_section.should(be.present)
        scroll_into_view_if_needed(self.sent_requests_section)
        self.search_sent_requests.type(iqama_number)
        return self

    def search_received_requests_pending_decision(self, iqama_number: str) -> EmployeeTransferPage:
        self.received_requests_pending_decision.should(be.present)
        scroll_into_view_if_needed(self.received_requests_pending_decision)
        self.search_received_requests_pending.type(iqama_number)
        return self

    def search_received_request(self, iqama_number: str) -> EmployeeTransferPage:
        self.received_requests_section.should(be.present)
        scroll_into_view_if_needed(self.received_requests_section)
        self.search_received_requests.type(iqama_number)
        return self

    def click_btn_accept(self) -> EmployeeTransferPage:
        self.btn_accept.click()
        return self

    def click_btn_reject(self) -> EmployeeTransferPage:
        self.btn_reject.click()
        return self

    def fill_rejection_reason(self) -> EmployeeTransferPage:
        self.field_rejection_reason.type("Rejection reason")
        return self

    def fill_sponsor_rejection_reason(self) -> EmployeeTransferPage:
        self.field_sponsor_rejection_reason.type("Rejection reason")
        return self

    def click_btn_accept_request(self) -> EmployeeTransferPage:
        self.btn_accept_request.click()
        return self

    def click_btn_yes_accept_transfer(self) -> EmployeeTransferPage:
        self.btn_yes_accept_transfer.click()
        return self

    def click_btn_reject_request(self) -> EmployeeTransferPage:
        self.btn_reject_request.click()
        return self

    def click_btn_reject_transfer(self) -> EmployeeTransferPage:
        self.btn_reject_transfer.click()
        return self

    def check_sponsor_request_status(self, status: str) -> EmployeeTransferPage:
        self.received_requests_table.cell(row=1, column=5).should(have.exact_text(status))
        return self
