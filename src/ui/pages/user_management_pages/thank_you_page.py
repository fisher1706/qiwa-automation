from __future__ import annotations

import allure
from selene import be
from selene.support.shared.jquery_style import s, ss

from utils.assertion import assert_that


class ThankYouPage:
    main_text = s("//p[contains(text(), 'Thank you!')]")
    payment = s("//*[@id='root']//strong")
    payment_data = ss("//*[@data-component='SimpleTable']//td")
    count = 11

    @allure.step
    def check_data_thank_you_page(self) -> ThankYouPage:
        self.payment.should(be.visible)
        elements = [item.should(be.visible) for item in self.payment_data]
        assert_that(len(elements)).equals_to(self.count)
        return self
