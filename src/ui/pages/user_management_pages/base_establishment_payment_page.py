from __future__ import annotations

import allure
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium.webdriver.common.keys import Keys

import config
from data.dedicated.models.user import User
from data.user_management.user_management_data import SUBSCRIPTION_TIME
from data.user_management.user_management_datasets import SubscriptionStatuses
from src.database.sql_requests.user_management.user_management_requests import (
    UserManagementRequests,
)
from utils.assertion import assert_that


class BaseEstablishmentPayment:
    checkbox_read_accept = s("[data-component='Checkbox'] input")

    def open_establishment_account_page(self) -> BaseEstablishmentPayment:
        browser.open(f"{config.qiwa_urls.workspaces}/establishment-accounts?sort_by=1")
        return self

    def open_expired_page(self) -> BaseEstablishmentPayment:
        browser.open(f"{config.qiwa_urls.ui_user_management}/renew-subscription/expired")
        return self

    def check_db_data(self, user: User):
        status, time_delta = UserManagementRequests().get_subscription_data(
            user.personal_number, user.unified_number_id
        )
        assert_that(status).equals_to(SubscriptionStatuses.active)
        assert_that(time_delta).equals_to(SUBSCRIPTION_TIME)
        return self

    @allure.step
    def check_checkbox_read_accept(self) -> BaseEstablishmentPayment:
        self.checkbox_read_accept.press(Keys.SPACE)
        return self
