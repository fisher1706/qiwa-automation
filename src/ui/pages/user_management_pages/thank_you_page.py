from __future__ import annotations

import allure
from selene import be
from selene.support.shared.jquery_style import s, ss
from src.ui.pages.user_management_pages.base_establishment_payment_page import (
    BaseEstablishmentPayment,
)


class ThankYouPage(BaseEstablishmentPayment):
    main_text = s("//p[contains(text(), 'Thank you!')]")
    request_details = ss("//p[contains(text(), 'Request details!')]")

    '[data-component="SimpleTable"]'
    '//*[@data-component="SimpleTable"]'

    '//*[text()="Request details"]/..'

    '//*[text()="Request details"]'
