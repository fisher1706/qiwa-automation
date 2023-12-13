from __future__ import annotations

import allure
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium.webdriver.common.keys import Keys

import config
from data.dedicated.models.user import User
from src.database.sql_requests.user_management.user_management_requests import (
    UserManagementRequests,
)
from utils.assertion import assert_that


class BaseEstablishmentPayment:
    checkbox_read_accept = s("[data-component='Checkbox'] input")
    subscription_status = 1
    subscription_time = 1

    def open_establishment_account_page(self) -> BaseEstablishmentPayment:
        browser.open(f"{config.qiwa_urls.workspaces}/establishment-accounts?sort_by=1")
        return self

    def switch_to_page(self) -> BaseEstablishmentPayment:
        browser.open(f"{config.qiwa_urls.ui_user_management}/renew-subscription/expired")
        return self

    def check_db_data(self, user: User):
        status, time_delta = UserManagementRequests().get_subscription_data(
            user.personal_number, user.unified_number_id
        )
        assert_that(status).equals_to(self.subscription_status)
        assert_that(time_delta).equals_to(self.subscription_time)
        return self

    @allure.step
    def check_checkbox_read_accept(self) -> BaseEstablishmentPayment:
        self.checkbox_read_accept.press(Keys.SPACE)
        return self
