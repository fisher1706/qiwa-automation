from __future__ import annotations

import allure
from selene import be, command
from selene.support.shared.jquery_style import s

from src.api.payloads.raw.user_management.payment import CardDetails
from src.ui.pages.user_management_pages.base_establishment_payment_page import (
    BaseEstablishmentPayment,
)


class PaymentSummary(BaseEstablishmentPayment):
    main_text = s("//p[contains(text(), 'Payment Summary')]")
    btn_submit_pay = s("//button//p[contains(text(), 'Submit and pay')]")
    pay_by_wallet = s("//*[@id='eWallet']/../span")
    pay_by_sadat = s("//*[@id='sadad']/../span")
    pay_by_card = s("//*[@id='card']/../span")
    pay_by_apple_pay = s("//*[@id='applePay']/../span")
    field_cardholder_name = s("//*[@id='cardHolder-test']")
    field_card_number = s("//*[@id='cardNumber-test']")
    field_month = s("//*[@id='date-test-0']")
    field_year = s("//*[@id='date-test-1']")
    field_CVV = s("//*[@id='cvv-test']")
    btn_submit = s("//*[@id='acssubmit']")

    def _fill_card_data(self, card: CardDetails = CardDetails()) -> PaymentSummary:
        self.field_cardholder_name.should(be.visible).perform(command.js.set_value("")).type(
            card.Holder
        )
        self.field_card_number.should(be.visible).perform(command.js.set_value("")).type(
            card.Number
        )
        self.field_month.should(be.visible).perform(command.js.set_value("")).type(
            card.ExpiryMonth
        )
        self.field_year.should(be.visible).perform(command.js.set_value("")).type(card.ExpiryYear)
        self.field_CVV.should(be.visible).perform(command.js.set_value("")).type(card.CVV)
        return self

    # TODO: complete all "_fill" methods after add functionality on stage env
    def _fill_sadat_data(self) -> PaymentSummary:
        pass

    def _fill_wallet_data(self) -> PaymentSummary:
        pass

    def _fill_apple_pay_data(self) -> PaymentSummary:
        pass

    @allure.step
    def choose_and_make_payment(self, payment_type: str = None) -> PaymentSummary:
        if payment_type == "sadat":
            self.pay_by_wallet.should(be.visible).click()
            self._fill_sadat_data()
        elif payment_type == "wallet":
            self.pay_by_wallet.should(be.visible).click()
            self._fill_wallet_data()
        elif payment_type == "apple":
            self.pay_by_apple_pay.should(be.visible).click()
            self._fill_apple_pay_data()
        else:
            self.pay_by_card.should(be.visible).click()
            self._fill_card_data()
        return self

    @allure.step
    def click_btn_submit_pay(self) -> PaymentSummary:
        self.btn_submit_pay.should(be.visible).click()
        return self

    # TODO: complete method after add functionality on stage env
    @allure.step
    def complete_payment(self, payment_type: str = None) -> PaymentSummary:
        if not payment_type:
            # self.btn_submit.should(be.visible).click()
            self.btn_submit.click()
        else:
            pass
        return self
