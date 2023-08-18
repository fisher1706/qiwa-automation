from __future__ import annotations

from selene import browser


class Pagination:
    web_element = browser.element(".pagination")

    def click_next(self) -> Pagination:
        self.web_element.element(".pagination-next").click()
        return self

    def click_previous(self) -> Pagination:
        self.web_element.element(".pagination-previous").click()
        return self
