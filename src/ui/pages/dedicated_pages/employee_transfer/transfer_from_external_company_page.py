from __future__ import annotations

from selene import command, have
from selene.support.shared.jquery_style import s

from src.ui.components.raw.table import Table
from utils.allure import allure_steps


@allure_steps
class TransferFromExternalCompanyPage:
    table = Table()
    btn_next_step = s("//button[.='Next step']")
    employee_iqama_number = s("#borderNumber")
    date_of_birth = s("[data-component='NumericField'] input")
    btn_find_employee = s("//button[.='Find employee']")
    btn_add_employee_to_transfer_request = s("//button[.='Add employee to transfer request']")

    def click_btn_next_step(self) -> TransferFromExternalCompanyPage:
        self.btn_next_step.click()
        return self

    def fill_employee_iqama_number(self, number: str) -> TransferFromExternalCompanyPage:
        self.employee_iqama_number.perform(command.js.set_value("")).type(number)
        return self

    def fill_date_of_birth(self, date: str) -> TransferFromExternalCompanyPage:
        self.date_of_birth.perform(command.js.set_value("")).type(date)
        return self

    def click_btn_find_employee(self) -> TransferFromExternalCompanyPage:
        self.btn_find_employee.click()
        return self

    def click_btn_add_employee_to_transfer_request(self) -> TransferFromExternalCompanyPage:
        self.btn_add_employee_to_transfer_request.click()
        return self

    def click_link_create_contract_another_establishment(self) -> TransferFromExternalCompanyPage:
        self.table.headers.wait_until(have.size(6))
        self.table.cell(row=1, column=6).should(have.text("Create contract")).click()
        return self
