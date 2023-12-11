from __future__ import annotations

import allure
from selene import be
from selene.support.shared.jquery_style import s

from src.ui.pages.user_management_pages.base_establishment_payment_page import (
    BaseEstablishmentPayment,
)


class RenewSubscription(BaseEstablishmentPayment):
    main_text = s("//p[contains(text(), 'Renew your expired subscription')]")
    btn_go_to_payment = s("//button//p[contains(text(), 'Go to payment')]")

    @allure.step
    def click_btn_go_to_payment(self) -> RenewSubscription:
        self.btn_go_to_payment.should(be.visible).click()
        return self
