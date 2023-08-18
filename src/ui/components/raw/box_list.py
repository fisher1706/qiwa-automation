from __future__ import annotations

from selene import Element, have


class BoxList:
    def __init__(self, element: Element):
        self.element = element
        self.items = self.element.all(".q-page-box__list_item")

    def item(self, title: str) -> BoxListItem:
        return BoxListItem(self.items.element_by_its("dt", have.exact_text(title)))


class BoxListItem:
    def __init__(self, element: Element):
        self.element = element
        self.title = self.element.s("dt")
        self.value = self.element.s("dd")


class ItemsList:
    def __init__(self, web_element: Element):
        self.web_element = web_element
        self.items = self.web_element.all("div")
        self.titles = self.web_element.all("dt")
        self.values = self.web_element.all("dd")

    def item(self, title: str) -> ListItem:
        return ListItem(self.items.element_by_its("dt", have.text(title)))


class ListItem:
    def __init__(self, web_element: Element):
        self.web_element = web_element
        self.title = self.web_element.element("dt")
        self.value = self.web_element.element("dd")

    def should_have_value(self, value: str = "") -> Element:
        return self.value.should(have.exact_text(value) if value else have.text(value))
