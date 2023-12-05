from __future__ import annotations

import allure
from selene import be
from selene.support.conditions import have
from selene.support.shared.jquery_style import s, ss


class ThankYouPage:
    main_text = s("//p[contains(text(), 'Thank you!')]")
    payment = s("//*[@id='root']//strong")
    payment_data = ss("//*[@data-component='SimpleTable']//td")
    base_count = 12

    @allure.step
    def check_data_thank_you_page(self) -> ThankYouPage:
        self.payment.should(be.visible)
        self.payment_data.should(be.visible.each).should(have.size(self.base_count))
        return self
