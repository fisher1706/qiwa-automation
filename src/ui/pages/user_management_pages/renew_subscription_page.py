from __future__ import annotations

import allure
from selene import be, have
from selene.support.shared.jquery_style import s, ss

from src.ui.pages.user_management_pages.base_establishment_payment_page import (
    BaseEstablishmentPayment,
)


class RenewSubscription(BaseEstablishmentPayment):
    main_text = s("//p[contains(text(), 'Renew your expired subscription')]")
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

    count_group_manager_content = 4
    count_establishment_group_details_content = 2
    count_establishment_subscription_content_new = 5
    count_establishment_subscription_content_expired = 5
    count_summary_content = 6

    total_value = s("//*[@id='root']//table/tbody/tr[6]//div[1]/span")

    @allure.step
    def click_btn_go_to_payment(self) -> RenewSubscription:
        self.btn_go_to_payment.should(be.visible).click()
        return self

    @allure.step
    def check_group_manager_block(self) -> RenewSubscription:
        self.group_manager_text.should(be.visible)
        self.group_manager_content.should(be.visible.each).should(
            have.size(self.count_group_manager_content)
        )
        return self

    @allure.step
    def check_establishment_group_details_block(self) -> RenewSubscription:
        self.establishment_group_details_text.should(be.visible)
        self.establishment_group_details_content.should(be.visible.each).should(
            have.size(self.count_establishment_group_details_content)
        )
        return self

    @allure.step
    def check_establishment_subscription_block(self, user_type: str) -> RenewSubscription:
        self.establishments_subscription_text.should(be.visible)
        if user_type == "without":
            self.establishments_subscription_content.should(be.visible.each).should(
                have.size(self.count_establishment_subscription_content_new)
            )
        else:
            self.establishments_subscription_content.should(be.visible.each).should(
                have.size(self.count_establishment_subscription_content_expired)
            )
        return self

    @allure.step
    def check_summary_block(self) -> RenewSubscription:
        self.summary_text.should(be.visible)
        self.summary_content.should(be.visible.each).should(have.size(self.count_summary_content))
        return self

    @allure.step
    def check_total_value(self) -> RenewSubscription:
        self.total_value.should(be.visible)
        return self
