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

    btn_proceed_to_contract_management = s("//button[.='Proceed to Contract Management']")

    tables = ss('table')
    sent_requests_table = Table(tables.first)
    received_requests_table = Table(tables.second)

    items = ss('[data-component="Table"] + div > div > p')
    sent_requests = items.first
    received_requests = items.second

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

    def click_btn_proceed_to_contract_management(self) -> EmployeeTransferV2Page:
        self.btn_proceed_to_contract_management.click()
        return self

    def check_count_of_sent_request_rows(self):
        requests = EmployeeTransferV2Page._get_count_of_requests(self.sent_requests)
        rows = requests if requests < 10 else 10
        self.sent_requests_table.rows.should(have.size(rows))

    def check_count_of_received_request_rows(self):
        requests = EmployeeTransferV2Page._get_count_of_requests(self.received_requests)
        rows = requests if requests < 10 else 10
        self.received_requests_table.rows.should(have.size(rows))
