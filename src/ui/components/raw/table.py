from selene import be, browser, have
from selene.core.condition import Condition
from selene.core.entity import Collection, Element

from utils.selene import index_of_element_by


class Table:
    def __init__(self, web_element: Element | str = "table"):
        self.web_element = (
            browser.element(web_element) if isinstance(web_element, str) else web_element
        )
        self.header = self.web_element.element("thead")
        self.body = self.web_element.element("tbody")
        self.headers = self.header.all("th")
        self.rows = self.body.all("tr")

    def row(self, number: int) -> Element:
        return self.rows.element(number - 1)

    def cells(self, *, row: int | Condition[Element]) -> Collection:
        _row = self.row(row) if isinstance(row, int) else self.rows.element_by(row)
        return _row.all("td").by(be.visible)

    def cell(self, *, row: int | Condition[Element], column: int | str) -> Element:
        column_index = (
            column - 1
            if isinstance(column, int)
            else self.headers.get(index_of_element_by(have.text(column)))
        )
        return self.cells(row=row)[column_index]
