from __future__ import annotations

import allure
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium.webdriver.common.keys import Keys

import config


class BaseEstablishmentPayment:
    checkbox_read_accept = s("[data-component='Checkbox'] input")

    def open_establishment_account_page(self) -> BaseEstablishmentPayment:
        browser.open(f"{config.qiwa_urls.workspaces}/establishment-accounts?sort_by=1")
        return self

    @allure.step
    def check_checkbox_read_accept(self) -> BaseEstablishmentPayment:
        self.checkbox_read_accept.press(Keys.SPACE)
        return self
