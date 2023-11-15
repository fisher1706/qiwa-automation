from __future__ import annotations

from selene import have, query
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


class EmployeeTransferV2Page(
    TransferBetweenMyEstablishmentsPage, TransferFromExternalCompanyPage, SummaryPage
):
    btn_transfer_employee = s("//button[.='Transfer employee']")

    tiles = ss('[data-testid="tile-desktop"] button')
    own_establishment = tiles.first
    another_establishment = tiles.second

    recruitment_quota = ss('[data-testid="desktop_wrapper"] p').second

    btn_proceed_to_contract_management = s("//button[.='Proceed to Contract Management']")

    sent_requests_section = s("#requests-sent-by-you + div + div")
    received_requests_section = s("#received-requests + div + div")

    sent_requests_table = Table(sent_requests_section.s("table"))
    received_requests_table = Table(received_requests_section.s("table"))

    field_rejection_reason = s("#rejectReason")

    pagination_info = '[data-component="Table"] + div > div > p'
    sent_requests_pagination_info = sent_requests_section.s(pagination_info)
    received_requests_pagination_info = received_requests_section.s(pagination_info)

    search_sent_requests = sent_requests_section.s("#sent")
    search_received_requests = received_requests_section.s("#received")

    btn_accept_request = s("//button[.='Accept request']")
    btn_reject_request = s("//button[.='Reject request']")

    @staticmethod
    def _get_count_of_requests(web_element: Element) -> int:
        return int(web_element.get(query.text).split()[2])

    def click_btn_transfer_employee(self) -> EmployeeTransferV2Page:
        self.btn_transfer_employee.click()
        return self

    def select_own_establishment(self) -> EmployeeTransferV2Page:
        self.own_establishment.click()
        return self

    def select_another_establishment(self) -> EmployeeTransferV2Page:
        self.another_establishment.click()
        return self

    def get_recruitment_quota(self) -> int:
        return int(self.recruitment_quota.get(query.text))

    def click_btn_proceed_to_contract_management(self) -> EmployeeTransferV2Page:
        self.btn_proceed_to_contract_management.click()
        return self

    def check_count_of_sent_request_rows(self) -> None:
        requests = EmployeeTransferV2Page._get_count_of_requests(
            self.sent_requests_pagination_info
        )
        rows = requests if requests < 10 else 10
        self.sent_requests_table.rows.should(have.size(rows))

    def check_count_of_received_request_rows(self) -> None:
        requests = EmployeeTransferV2Page._get_count_of_requests(
            self.received_requests_pagination_info
        )
        rows = requests if requests < 10 else 10
        self.received_requests_table.rows.should(have.size(rows))

    def search_sent_request(self, iqama_number: str) -> EmployeeTransferV2Page:
        self.search_sent_requests.type(iqama_number)
        return self

    def search_received_request(self, iqama_number: str) -> EmployeeTransferV2Page:
        self.search_received_requests.type(iqama_number)
        return self

    def click_btn_approve(self) -> EmployeeTransferV2Page:
        self.received_requests_table.cell(row=1, column=5).all("button").first.click()
        return self

    def click_btn_reject(self) -> EmployeeTransferV2Page:
        self.received_requests_table.cell(row=1, column=5).all("button").second.click()
        return self

    def fill_rejection_reason(self) -> EmployeeTransferV2Page:
        self.field_rejection_reason.type("Rejection reason")
        return self

    def click_btn_accept_request(self) -> EmployeeTransferV2Page:
        self.btn_accept_request.click()
        return self

    def click_btn_reject_request(self) -> EmployeeTransferV2Page:
        self.btn_reject_request.click()
        return self

    def check_sponsor_request_status(self, status: str) -> EmployeeTransferV2Page:
        self.received_requests_table.cell(row=1, column=5).should(have.exact_text(status))
        return self
