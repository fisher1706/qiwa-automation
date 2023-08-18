from selene import have
from selene.core.entity import Element


class Table:
    def __init__(self, web_element: Element):
        self.web_element = web_element
        self.header = self.web_element.element("thead")
        self.body = self.web_element.element("tbody")
        self.headers = self.header.all("th")
        self.rows = self.body.all("tr")

    def row(self, number: int) -> "Row":
        return Row(self.rows.element(number - 1))


class Row:
    def __init__(self, web_element: Element):
        self.web_element = web_element
        self.cells = self.web_element.all("td")

    def cell(self, label: str) -> Element:
        return self.cells.element_by(have.attribute("data-label", label))
