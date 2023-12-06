from __future__ import annotations

from selene import have
from selene.support.shared.jquery_style import s

from src.ui.components.raw.table import Table
from utils.allure import allure_steps


@allure_steps
class EmployeeListPage:
    field_search = s("#header-search")
    table = Table(s(".table"))
    see_all_services = s('//a[@href="/services"]')
    go_to_resume_management = s("//p[normalize-space()='Go to Resume Management']")

    def fill_random_search_and_clear(self):
        self.field_search.type("test")
        self.field_search.clear()

    def search(self, by_column: str, text: str) -> None:
        self.field_search.type(text)
        self.table.cell(row=1, column=by_column).should(have.text(text))

    def verify_nothing_was_found_message(self, text: str) -> None:
        self.field_search.type(text)
        self.table.cell(row=1, column=1).should(have.text("Nothing was found"))

    def get_users_ids_from_table(self) -> list:
        return [self.table.cell(row=row, column=2) for row in range(1, len(self.table.rows))]

    def verify_user_ids(self, user_ids: list) -> None:
        for index, user_id in enumerate(user_ids):
            self.table.cell(row=index + 1, column=2).should(have.text(user_id))
