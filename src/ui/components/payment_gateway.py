from __future__ import annotations

import allure
from selene import be, browser, command
from selene.support.shared.jquery_style import s

from data.constants import (
    APPLE,
    CARD,
    SADAD,
    WALLET,
    CardDetails,
    PaymentResult,
    PaymentTypes,
)


class PaymentPage:
    BTN_SUBMIT_PAY = "//button//p[contains(text(), '{}')]"
    main_text = s("//p[contains(text(), 'Payment Summary')]")
    pay_by_wallet = s("//*[@id='eWallet']/../span")
    pay_by_sadat = s("//*[@id='sadad']/../span")
    pay_by_card = s("//*[@id='card']/../span")
    pay_by_apple_pay = s("//*[@id='applePay']/../span")
    field_cardholder_name = s("//*[@id='cardHolder-test']")
    field_card_number = s("//*[@id='cardNumber-test']")
    field_month = s("//*[@id='date-test-0']")
    field_year = s("//*[@id='date-test-1']")
    field_CVV = s("//*[@id='cvv-test']")
    iframe = s("//*[@id='challengeFrame']")
    btn_submit = s("//*[@id='acssubmit']")
    agree_payment_checkbox = s(
        '//*[@id="terms-checkbox"]//parent::label//following-sibling::span/span'
    )
    payment_result_dropdown = s('//*[@id="selectAuthResult"]')
    success_card = s('//*[@data-testid="success-by-card-page"]')
    error_card = s('//*[@data-testid="error-by-card-page"]')
    button_success_return = success_card.s(".//button")
    button_back_to_service = s('//button/p[contains(text(), "Back to Service")]')
    PAYMENT_RESULT_OPTION = "//*[@id='{}']"

    def _fill_card_data(self, card: CardDetails = CardDetails()) -> PaymentPage:
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
    def _fill_sadat_data(self) -> PaymentPage:
        pass

    def _fill_wallet_data(self) -> PaymentPage:
        pass

    def _fill_apple_pay_data(self) -> PaymentPage:
        pass

    @allure.step
    def choose_and_make_payment(self, payment_type: PaymentTypes = None) -> PaymentPage:
        if payment_type == SADAD:
            self.pay_by_wallet.should(be.visible).click()
            self._fill_sadat_data()
        elif payment_type == WALLET:
            self.pay_by_wallet.should(be.visible).click()
            self._fill_wallet_data()
        elif payment_type == APPLE:
            self.pay_by_apple_pay.should(be.visible).click()
            self._fill_apple_pay_data()
        else:  # default is CARD
            self.pay_by_card.should(be.visible).click()
            self._fill_card_data()
        return self

    @allure.step
    def click_btn_submit_pay(self, payment_type: PaymentTypes) -> PaymentPage:
        s(self.BTN_SUBMIT_PAY.format(payment_type.submit_button)).should(be.visible).click()
        return self

    @allure.step
    def complete_payment(self, payment_result: PaymentResult = None) -> PaymentPage:
        browser.switch_to.frame(self.iframe.should(be.visible)())
        if payment_result != PaymentResult().AUTHENTICATED:
            self.payment_result_dropdown.click()
            s(self.PAYMENT_RESULT_OPTION.format(payment_result)).should(be.visible).click()
        self.btn_submit.should(be.visible).click()
        return self

    @allure.step
    def check_checkbox_agreed(self):
        self.agree_payment_checkbox.click()
        return self

    @allure.step
    def return_to_request_page(self, payment_result: PaymentResult) -> PaymentPage:
        if payment_result in PaymentResult().successful_results:
            self.return_from_success_page()
        else:
            self.return_from_error_page()
        return self

    @allure.step
    def return_from_error_page(self) -> None:
        self.error_card.with_(timeout=60).should(be.visible)
        self.button_back_to_service.should(be.visible).click()

    @allure.step
    def return_from_success_page(self) -> PaymentPage:
        self.success_card.should(be.visible)
        self.button_success_return.should(be.visible).click()
        return self

    @allure.step
    def pay_completely_by(
        self,
        payment_type: PaymentTypes = CARD,
        payment_result: PaymentResult = PaymentResult().AUTHENTICATED,
    ) -> PaymentPage:
        self.choose_and_make_payment(payment_type).check_checkbox_agreed().click_btn_submit_pay(
            payment_type
        ).complete_payment(payment_result).return_to_request_page(payment_result)
        return self
