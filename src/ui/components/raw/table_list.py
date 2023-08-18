from __future__ import annotations

import allure
from selene import Element, be, have

from src.ui.components.raw.pagination import Pagination
from src.ui.components.raw.table import Table


class TableList:
    def __init__(self, web_element: Element):
        self.web_element = web_element
        self.table = Table(web_element.element(".table"))
        self.pagination = Pagination()

    @allure.step
    def to_next_page(self) -> TableList:
        self.pagination.click_next()
        return self

    @allure.step
    def to_previous_page(self) -> TableList:
        self.pagination.click_previous()
        return self

    @allure.step
    def clear_filters(self) -> TableList:
        self.table.header.element("button").click()
        return self

    # ASSERTIONS

    @allure.step
    def should_be_loaded(self) -> TableList:
        self.web_element.element(".q-page-box__table").should(have.css_class("is-loading")).should(
            have.no.css_class("is-loading")
        )
        return self

    @allure.step
    def should_be_loading(
        self,
    ) -> TableList:  # Depends on table UI, so this case relevant only for debts table
        self.web_element.element(".q-spinner").should(be.visible)
        return self

    @allure.step
    def should_be_empty(self) -> TableList:
        self.table.rows.should(have.size(1))
        self.table.rows.first.should(have.css_class("is-empty")).should(
            have.exact_text("Nothing was found")
        )
        return self
