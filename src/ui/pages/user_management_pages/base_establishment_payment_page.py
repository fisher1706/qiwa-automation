from __future__ import annotations

import allure
from selene import be
from selene.core.entity import Element
from selene.support.shared.jquery_style import s
from selenium.webdriver.common.keys import Keys


class BaseEstablishmentPayment:
    checkbox_read_accept = s("[data-component='Checkbox'] input")

    def wait_until_page_load(self, locator: Element) -> BaseEstablishmentPayment:
        locator.wait_until(be.visible)
        return self

    @allure.step
    def check_checkbox_read_accept(self) -> BaseEstablishmentPayment:
        self.checkbox_read_accept.press(Keys.SPACE)
        return self
