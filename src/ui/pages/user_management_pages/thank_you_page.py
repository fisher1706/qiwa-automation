from __future__ import annotations

import allure
from selene import be
from selene.support.conditions import have
from selene.support.shared.jquery_style import s, ss


class ThankYouPage:
    main_text = s("//p[contains(text(), 'Thank you!')]")
    payment = s("//*[@id='root']//strong")
    payment_data = ss("//*[@data-component='SimpleTable']//td")
    count_expired_subscription = 11
    count_new_subscription = 12

    @allure.step
    def check_data_thank_you_page(self, user_type: str) -> ThankYouPage:
        self.payment.should(be.visible)
        if user_type == "expired":
            self.payment_data.should(be.visible.each).should(
                have.size(self.count_expired_subscription)
            )
        else:
            self.payment_data.should(be.visible.each).should(
                have.size(self.count_new_subscription)
            )
        return self
