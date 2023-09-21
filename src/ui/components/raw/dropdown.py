from __future__ import annotations

from selene import have
from selene.core.entity import Collection, Element


class Dropdown:
    """
    Object to wrap SELECT tag.
    :Args:
        - element - SELECT element to wrap
    Use it like
    `Select(s('foo')).select_by_value('m')`
    or
    `Select(browser.element('foo')).select_by_value('m')`
    """

    def __init__(self, element: Element, option_element_locator: str = None):
        self.element = element
        self.option_element_locator = option_element_locator

    @property
    def options(self) -> Collection:
        if self.option_element_locator:
            return self.element.all(self.option_element_locator)
        return self.element.all("option")

    def select_by_value(self, value: str) -> Dropdown:
        self.element.click()
        self.options.element_by(have.value(value)).click()
        return self

    def select_by_text(self, value: str) -> Dropdown:
        self.element.click()
        self.options.element_by(have.text(value)).click()
        return self

    def select_by_index(self, index: int) -> Dropdown:
        self.element.click()
        self.options[index].click()
        return self
