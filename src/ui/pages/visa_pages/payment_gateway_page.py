from selene import have
from selene.api import be, s
from selene.support.shared import browser

import config
from data.visa.constants import TRANSACTIONID, PayCardSuccess
from utils.helpers import get_url_param


class PaymentGateWay:
    pay_by_card_option = s('//*[@id="card"]//following-sibling::span')
    cardholder_input_field = s('//*[@id="cardHolder-test"]')
    card_number_input_field = s('//*[@id="cardNumber-test"]')
    card_month_input_field = s('//*[@id="date-test-0"]')
    card_year_input_field = s('//*[@id="date-test-1"]')
    card_cvv_input_field = s('//*[@id="cvv-test"]')
    agree_payment_checkbox = s(
        '//*[@id="terms-checkbox"]//parent::label//following-sibling::span/span'
    )
    submit_payment = s('//*[@data-testid="submit-button"]')
    payment_summary = s('//*[@data-testid="summary-section-id"]')
    payment_iframe = s("#challengeFrame")
    payment_iframe_submit_button = s("#acssubmit")
    payment_submit_button = s('//input[@id="acssubmit"]')
    payment_gateway_redirect_page = s("#threedsChallengeRedirect")
    go_to_request_details_button = s('//button/p[contains(text(), "Go to request details")]')
    iframe = "#challengeFrame"

    def pay_successfully(self, visa_db):
        self.payment_summary.should(be.visible)
        visa_db.payment_id = get_url_param()
        self.pay_by_card_option.click()
        self.cardholder_input_field.type(PayCardSuccess.HOLDER)
        self.card_number_input_field.type(PayCardSuccess.NUMBER)
        self.card_month_input_field.type(PayCardSuccess.MONTH)
        self.card_year_input_field.type(PayCardSuccess.YEAR)
        self.card_cvv_input_field.type(PayCardSuccess.CVV2)
        self.agree_payment_checkbox.click()
        self.submit_payment.click()
        browser.switch_to.frame(browser.element(self.iframe).should(be.visible)())
        self.payment_submit_button.click()
        browser.switch_to.default_content()
        self.go_to_request_details_button.click()
        browser.should(have.url_containing(config.qiwa_urls.visa_web_url))
        if get_url_param(TRANSACTIONID) == visa_db.payment_id:
            visa_db.payment_id = None
