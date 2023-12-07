from __future__ import annotations

import allure
from selene import be
from selene.support.shared.jquery_style import s, ss

from src.ui.pages.user_management_pages.base_establishment_payment_page import (
    BaseEstablishmentPayment,
)


class EstablishmentUser(BaseEstablishmentPayment):
    main_text = s("//p[contains(text(), 'Establishment and user details')]")
    btn_proceed_subscription = ss("//button//p[contains(text(), 'Proceed with subscription')]")

    @allure.step
    def click_btn_proceed_subscription(self, number: int = None) -> EstablishmentUser:
        self.btn_proceed_subscription[number].should(
            be.visible
        ).click() if number else self.btn_proceed_subscription[0].should(be.visible).click()
        return self
