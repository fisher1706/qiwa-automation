from __future__ import annotations

import allure
from selene import be, browser, have
from selene.support.shared.jquery_style import s, ss

import config
from data.user_management.user_management_datasets import RenewPageData
from src.ui.pages.user_management_pages.base_establishment_payment_page import (
    BaseEstablishmentPayment,
)


class RenewSubscription(BaseEstablishmentPayment):
    main_text = s("//p[contains(text(), 'Renew your expired subscription')]")
    page_title_renew_subscription = s("[data-testid='layout-with-instruction'] > p")
    btn_go_to_payment = s("//button//p[contains(text(), 'Go to payment')]")

    group_manager_text = s("//p[contains(text(), 'Group Manager')]")
    establishment_group_details_text = s("//p[contains(text(), 'Establishment Group Details')]")
    establishments_subscription_text = s(
        "//p[contains(text(), 'Establishments that will be included in the annual subscription')]"
    )
    summary_text = s("//p[contains(text(), 'Summary')]")

    group_manager_content = ss(
        "//p[contains(text(), 'Group Manager')]/../..//*[@data-component='Box']/div/p"
    )
    establishment_group_details_content = ss(
        "//p[contains(text(), 'Establishment Group Details')]/../..//*[@data-component='Box']/div/p"
    )
    establishments_subscription_content = ss("//*[@data-component='Table']//tr")
    summary_content = ss("//*[@data-component='SimpleTable']//td")

    total_value = s("//*[@id='root']//table/tbody/tr[6]//div[1]/span")

    @allure.step
    def click_btn_go_to_payment(self) -> RenewSubscription:
        self.btn_go_to_payment.should(be.visible).click()
        return self

    @allure.step
    def check_group_manager_block(self) -> RenewSubscription:
        self.group_manager_text.should(be.visible)
        self.group_manager_content.should(be.visible.each).should(
            have.size(RenewPageData.COUNT_GROUP_MANAGER_CONTENT)
        )
        return self

    @allure.step
    def check_establishment_group_details_block(self) -> RenewSubscription:
        self.establishment_group_details_text.should(be.visible)
        self.establishment_group_details_content.should(be.visible.each).should(
            have.size(RenewPageData.COUNT_ESTABLISHMENT_GROUP_DETAILS_CONTENT)
        )
        return self

    @allure.step
    def check_establishment_subscription_block(self, user_type: str) -> RenewSubscription:
        self.establishments_subscription_text.should(be.visible)
        if user_type == "without":
            self.establishments_subscription_content.should(be.visible.each).should(
                have.size(RenewPageData.COUNT_ESTABLISHMENT_SUBSCRIPTION_CONTENT_NEW)
            )
        else:
            self.establishments_subscription_content.should(be.visible.each).should(
                have.size(RenewPageData.COUNT_ESTABLISHMENT_SUBSCRIPTION_CONTENT_EXPIRED)
            )
        return self

    @allure.step
    def check_summary_block(self) -> RenewSubscription:
        self.summary_text.should(be.visible)
        self.summary_content.should(be.visible.each).should(
            have.size(RenewPageData.COUNT_SUMMARY_CONTENT)
        )
        return self

    @allure.step
    def check_total_value(self) -> RenewSubscription:
        self.total_value.should(be.visible)
        return self

    @allure.step
    def check_self_renew_expired_page_is_opened(
        self, office_id: str, sequence_number: str
    ) -> RenewSubscription:
        self.page_title_renew_subscription.should(be.visible)
        browser.should(
            have.url(
                f"{config.qiwa_urls.ui_user_management}/renew-subscription/expired?laborOfficeId={office_id}"
                f"&sequenceNumber={sequence_number}"
            )
        )
        self.btn_go_to_payment.should(be.visible)
        return self
