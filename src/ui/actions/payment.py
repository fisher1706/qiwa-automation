from __future__ import annotations

import allure
from selene import be, browser, have


class PaymentByCard:
    # alrajhibank payment page, used for work permits payment by card feature
    def __init__(self):
        browser.should(have.tabs_number_greater_than(1))
        browser.switch_to_next_tab()

    @allure.step
    def fill_payment_details(self) -> PaymentByCard:
        browser.element("#creditCardholderFirstName").type("John")
        browser.element("#creditCardholderLastName").type("Smith")
        browser.element("#creditCardNumber").type("4111 1111 1111 1111")
        browser.element("#creditMonth").type("11")
        browser.element("#creditYear").type("30")
        browser.element("#cardCvv").type("123")
        return self

    @allure.step
    def cancel_payment(self):
        browser.element("#cancel").click()

    @allure.step
    def confirm_payment(self) -> PaymentByCard:
        browser.element("#proceed").click()
        return self

    @allure.step
    def enter_purchase_auth_code(self):
        browser.switch_to.frame(browser.element("iframe#Cardinal-CCA-IFrame").should(be.visible)())
        browser.element(".input-field").type("1234")
        browser.element(".button.primary").click()

    # ASSERTIONS

    @allure.step
    def should_have_payment_amount(self, amount: str) -> PaymentByCard:
        browser.element("#mrchinfo").all(".mx-2").element(1).should(
            have.exact_text(f"SAR {amount}")
        )
        return self
