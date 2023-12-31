from __future__ import annotations

import allure
from selene import be, browser, have
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver import Keys

import config
from data.user_management import user_management_data
from data.user_management.user_management_datasets import Texts


class OwnerFLowPage:
    owner_subscription_title = s("[data-testid='layout-with-instruction'] > p")
    next_step_btn = s("[data-testid='next-step']")
    upload_user_data_btn = s("[data-testid='user-actions-load-btn']")
    go_to_payment_btn = s("[data-testid='button-pay']")
    establishment_list = ss("[data-testid='est-and-perm-summary'] > div > div")
    terms_and_conditions_checkbox = s("[data-testid='checkbox-btn']")

    @allure.step
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
    def check_extend_subscription_page_is_opened(self, personal_number: str) -> OwnerFLowPage:
        self.owner_subscription_title.should(have.text(user_management_data.EXTEND_SUBSCRIPTION))
        browser.should(
            have.url(
                f"{config.qiwa_urls.ui_user_management}/extend-subscription/{personal_number}"
            )
        )
        self.go_to_payment_btn.should(be.visible)
        return self

    @allure.step
    def check_subscribe_user_page_is_opened(self) -> OwnerFLowPage:
        self.owner_subscription_title.should(have.text(Texts.add_new_workspace_user))
        browser.should(have.url(f"{config.qiwa_urls.ui_user_management}/subscribe-user"))
        self.upload_user_data_btn.should(be.visible)
        return self

    @allure.step
    def check_establishment_list_is_displayed_on_owner_subscription_page(
        self, establishment_list: list
    ) -> OwnerFLowPage:
        self.establishment_list.should(have.texts(establishment_list))
        return self

    @allure.step
    def check_establishment_is_hidden_on_owner_subscription_page(
        self, establishment: str
    ) -> OwnerFLowPage:
        self.establishment_list.element_by(have.text(establishment)).should(be.not_.visible)
        return self

    @allure.step
    def select_terms_and_conditions_checkbox_on_owner_subscription_page(self) -> OwnerFLowPage:
        self.terms_and_conditions_checkbox.press(Keys.SPACE)
        return self

    @allure.step
    def click_go_to_payment_btn(self) -> OwnerFLowPage:
        self.go_to_payment_btn.click()
        return self
