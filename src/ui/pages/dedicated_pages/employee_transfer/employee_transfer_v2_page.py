from __future__ import annotations

from selene.support.shared.jquery_style import s, ss

from src.ui.pages.dedicated_pages.employee_transfer.transfer_between_my_establishments import \
    TransferBetweenMyEstablishmentsPage
from src.ui.pages.dedicated_pages.employee_transfer.transfer_from_external_company_page import \
    TransferFromExternalCompanyPage


class EmployeeTransferV2Page(TransferBetweenMyEstablishmentsPage, TransferFromExternalCompanyPage):
    btn_transfer_employee = s("//button[.='Transfer employee']")

    tiles = ss('[data-testid="tile-desktop"] button')
    own_establishment = tiles.first
    another_establishment = tiles.second

    btn_proceed_to_contract_management = s("//button[.='Proceed to Contract Management']")

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
