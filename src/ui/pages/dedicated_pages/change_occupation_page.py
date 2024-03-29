from __future__ import annotations

from selene import have
from selene.support.shared.jquery_style import s, ss

from data.constants import Titles
from data.dedicated.change_occupation.change_occupation_constants import Label
from data.dedicated.enums import ChangeOccupationWarning
from src.ui.components.raw.table import Table
from utils.allure import allure_steps


@allure_steps
class ChangeOccupationPage:
    title = s(".c-service-heading__text")
    field_search = s(".c-search-input-group__input")
    tables = ss(".table")
    table_employee_list = Table(tables[0])
    change_occupation_requests = Table(tables[1])
    occupation_list = ss(".c-occupation-list__data li")
    create_change_occupation = s(".o-modal__footer button")
    agree_checkbox = s(".c-pending-requests__notice-checkbox")
    btn_send_change_occupation_request = s(".c-pending-requests__cta button")
    field_search_occupation = s(".c-occupation-list__search")
    warning = s(".o-modal__footer-text")

    def check_change_occupation_title(self) -> ChangeOccupationPage:
        self.title.should(have.exact_text(Titles.CHANGE_OCCUPATION))
        return self

    def find_expected_employee(self, personal_number: str) -> ChangeOccupationPage:
        self.field_search.clear().type(personal_number)
        self.table_employee_list.cell(row=1, column=Label.IQAMA_NUMBER).wait_until(
            have.text(personal_number)
        )
        return self

    def check_employee_eligibility(self, eligible: str) -> ChangeOccupationPage:
        self.table_employee_list.cell(row=1, column=Label.ELIGIBILITY).should(
            have.exact_text(eligible)
        )
        return self

    def click_btn_change_occupation(self) -> ChangeOccupationPage:
        self.table_employee_list.cell(row=1, column=Label.ACTIONS).s("button").click()
        return self

    def search_occupation(self, occupation: str) -> ChangeOccupationPage:
        self.field_search_occupation.type(occupation)
        return self

    def select_occupation(self, occupation: str) -> ChangeOccupationPage:
        self.occupation_list.element_by(have.exact_text(occupation)).s(".c-radio__mark").click()
        return self

    def click_create_change_occupation(self) -> ChangeOccupationPage:
        self.create_change_occupation.click()
        return self

    def check_blank_occupation_list(self) -> ChangeOccupationPage:
        self.occupation_list.should(have.size(0))
        return self

    def check_warning_msg(self) -> ChangeOccupationPage:
        self.warning.should(have.exact_text(ChangeOccupationWarning.NOT_ALLOWED.value))
        return self

    def check_request_is_exist(self, personal_number: str) -> ChangeOccupationPage:
        self.change_occupation_requests.cell(row=1, column=Label.IQAMA_NUMBER).should(
            have.exact_text(personal_number)
        )
        return self

    def click_agree_checkbox(self) -> ChangeOccupationPage:
        self.agree_checkbox.click()
        return self

    def click_btn_send_change_occupation_request(self) -> ChangeOccupationPage:
        self.btn_send_change_occupation_request.click()
        return self
