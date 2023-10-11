from __future__ import annotations

from selene import command
from selene.support.shared.jquery_style import s

from src.ui.components.raw.table import Table


class TransferBetweenMyEstablishmentsPage:
    table = Table()
    btn_next_step = s("//button[.='Next step']")
    search = s("#test")
    terms_checkbox = s("#terms + span")
    btn_submit_request = s("//button[.='Submit request']")
    btn_submit = s("//button[.='Submit']")

    def click_btn_next_step(self) -> TransferBetweenMyEstablishmentsPage:
        self.btn_next_step.click()
        return self

    def search_by_iqama_number(self, number: str) -> TransferBetweenMyEstablishmentsPage:
        self.search.perform(command.js.set_value("")).type(number)
        return self

    def select_first_employee(self) -> TransferBetweenMyEstablishmentsPage:
        self.table.cell(row=1, column=1).click()
        return self

    def select_terms_checkbox(self) -> TransferBetweenMyEstablishmentsPage:
        self.terms_checkbox.click()
        return self

    def click_btn_submit_request(self) -> TransferBetweenMyEstablishmentsPage:
        self.btn_submit_request.click()
        return self

    def click_btn_submit(self) -> TransferBetweenMyEstablishmentsPage:
        self.btn_submit.hover().click()
        return self

    def click_link_create_contract_own_establishment(self) -> TransferBetweenMyEstablishmentsPage:
        self.table.cell(row=1, column=5).ss("a").first.click()
        return self
