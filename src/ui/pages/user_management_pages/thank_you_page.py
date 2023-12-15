from __future__ import annotations

import allure
from selene import be
from selene.support.conditions import have
from selene.support.shared.jquery_style import s, ss

from data.user_management.user_management_datasets import ThankYouPageData


class ThankYouPage:
    main_text = s("//p[contains(text(), 'Thank you!')]")
    payment = s("//*[@id='root']//strong")
    payment_data = ss("//*[@data-component='SimpleTable']//td")

    @allure.step
    def check_data_thank_you_page(self, user_type: str) -> ThankYouPage:
        self.payment.should(be.visible)
        if user_type in ["expired", "owner_flow"]:
            self.payment_data.should(be.visible.each).should(
                have.size(ThankYouPageData.COUNT_EXPIRED_SUBSCRIPTION)
            )
        else:
            self.payment_data.should(be.visible.each).should(
                have.size(ThankYouPageData.COUNT_NEW_SUBSCRIPTION)
            )
        return self
