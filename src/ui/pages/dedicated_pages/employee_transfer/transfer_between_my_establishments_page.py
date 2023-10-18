from __future__ import annotations

from selene import be, command, have
from selene.support.shared.jquery_style import s
from selenium.webdriver.common.keys import Keys

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

    def select_first_employee(self, number: int) -> TransferBetweenMyEstablishmentsPage:
        self.table.cell(row=1, column=3).should(have.exact_text(str(number)))
        self.table.cell(row=1, column=1).click()
        return self

    def select_terms_checkbox(self) -> TransferBetweenMyEstablishmentsPage:
        self.terms_checkbox.press(Keys.SPACE)
        return self

    def click_btn_submit_request(self) -> TransferBetweenMyEstablishmentsPage:
        self.btn_submit_request.click()
        return self

    def click_btn_submit(self) -> TransferBetweenMyEstablishmentsPage:
        self.btn_submit.should(be.visible).hover().click()
        return self

    def click_link_create_contract(self) -> TransferBetweenMyEstablishmentsPage:
        self.table.cell(row=1, column=5).ss("a").element_by(have.text("Create contract")).click()
        return self

    def check_existence_of_a_contract(self) -> TransferBetweenMyEstablishmentsPage:
        self.table.cell(row=1, column=4).should(have.exact_text("Yes"))
        return self
