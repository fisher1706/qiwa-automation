from __future__ import annotations

import allure
from selene import be
from selene.support.shared.jquery_style import s

from src.ui.pages.user_management_pages.base_establishment_payment_page import (
    BaseEstablishmentPayment,
)


class AnnualSubscription(BaseEstablishmentPayment):
    main_text = s("//p[contains(text(), 'Annual Subscription')]")
    btn_go_to_payment = s("//button//p[contains(text(), 'Go to payment')]")

    @allure.step
    def click_button_go_to_payment(self) -> AnnualSubscription:
        self.btn_go_to_payment.should(be.visible).click()
        return self
