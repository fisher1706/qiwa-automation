from __future__ import annotations

import allure
from selene import be, browser, have
from selene.support.shared.jquery_style import s

import config
from data.user_management import user_management_data
from data.user_management.user_management_datasets import Texts


class OwnerFLowPage:
    owner_subscription_title = s("[data-testid='layout-with-instruction'] > p")
    next_step_btn = s("[data-testid='next-step']")
    upload_user_data_btn = s("[data-testid='user-actions-load-btn']")

    def check_title(self, title) -> OwnerFLowPage:
        self.owner_subscription_title.should(have.text(title))
        return self

    @allure.step
    def check_renew_terminated_page_is_opened(self, personal_number: str) -> OwnerFLowPage:
        self.owner_subscription_title.should(
            have.text(user_management_data.RENEW_TERMINATED_SUBSCRIPTION)
        )
        browser.should(
            have.url(
                f"{config.qiwa_urls.ui_user_management}/renew-subscription/terminated/{personal_number}"
            )
        )
        self.next_step_btn.should(be.visible)
        return self

    @allure.step
    def check_subscribe_user_page_is_opened(self) -> OwnerFLowPage:
        self.owner_subscription_title.should(have.text(Texts.add_new_workspace_user))
        browser.should(have.url(f"{config.qiwa_urls.ui_user_management}/subscribe-user"))
        self.upload_user_data_btn.should(be.visible)
        return self
