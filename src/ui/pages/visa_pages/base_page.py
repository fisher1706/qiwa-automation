from selene import have
from selene.api import be, s, ss
from selene.support.shared import browser

import config
from data.visa.constants import TRANSACTIONID, Languages, PayCardSuccess
from utils.helpers import get_url_param


class BasePage:
    LANGUAGE_MENU_BUTTON = (
        '//button[contains(@class, "MenuTrigger") or contains(@class, "lang-switcher__trigger")]'
        '//p[contains(text(), "{}") or contains(text(), "{}")]'
    )
    LANGUAGE_MENU = '//button[contains(@class, "MenuTrigger")]//p[contains(text(), "{}")]'
    SWITCH_LANGUAGE_BOX = '//div[@class="tippy-box"]'
    SWITCH_LANGUAGE_BUTTON = './/p[contains(text(), "{}")]'
    current_language_english = s(LANGUAGE_MENU.format(Languages.ENGLISH))
    current_language_arabic = s(LANGUAGE_MENU.format(Languages.ARABIC))
    english_button = s(SWITCH_LANGUAGE_BOX).s(SWITCH_LANGUAGE_BUTTON.format(Languages.ENGLISH))
    arabic_button = s(SWITCH_LANGUAGE_BOX).s(SWITCH_LANGUAGE_BUTTON.format(Languages.ARABIC))
    quiz_popup_close_button = s('//div[contains(@class, "demo__shutter")]')
    quiz_popup_window = s('//div[contains(@class,"animation-content")]')
    quiz_popup = s('[title="iframe"]')
    page_navigation_chain = s("//nav")
    page_title = ss('//div[@data-component="Layout"]/div[@data-component="Box"]//p').first
    pay_by_card_option = s('//*[@id="card"]//following-sibling::span')
    cardholder_input_field = s('//*[@id="cardHolder-test"]')
    card_number_input_field = s('//*[@id="cardNumber-test"]')
    card_month_input_field = s('//*[@id="1"]')
    card_year_input_field = s('//*[@id="2"]')
    card_cvv_input_field = s('//*[@id="cvv-test"]')
    agree_payment_checkbox = s(
        '//*[@id="terms-checkbox"]//parent::label//following-sibling::span/span'
    )
    submit_payment = s('//*[@data-testid="submit-button"]')
    payment_summary = s('//*[@data-testid="summary-section-id"]')
    payment_iframe = s("#challengeFrame")
    payment_iframe_submit_button = s("#acssubmit")
    payment_gateway_redirect_page = s("#threedsChallengeRedirect")
    go_to_request_details_button = s('//button/p[contains(text(), "Go to request details")]')

    def refresh_page(self):
        browser.driver.refresh()
        self.select_language(Languages.ENGLISH)
        return self

    def select_language(self, language):
        s(self.LANGUAGE_MENU_BUTTON.format(Languages.ENGLISH, Languages.ARABIC)).should(be.visible)
        if self.selected_language() == language:
            return
        self.current_language_box().click()
        self.english_button.should(be.visible)
        self.arabic_button.should(be.visible)
        if language == Languages.ENGLISH:
            self.english_button.click()
            return
        self.arabic_button.click()

    def selected_language(self):
        if self.current_language_arabic.with_(timeout=1).wait_until(be.visible):
            return Languages.ARABIC
        return Languages.ENGLISH

    def current_language_box(self):
        return s(self.SWITCH_LANGUAGE_BUTTON.format(self.selected_language()))

    def close_quiz_popup(self):
        if self.quiz_popup.with_(timeout=10).wait_until(be.visible):
            self.quiz_popup.wait_until(be.visible)
            browser.switch_to.frame(self.quiz_popup())
            self.quiz_popup_close_button.click()
            browser.switch_to.default_content()
            self.quiz_popup_window.should(be.hidden)

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
        self.payment_gateway_redirect_page.should(be.visible)
        browser.driver.switch_to.frame(self.payment_iframe())
        self.payment_iframe_submit_button.click()
        browser.switch_to.default_content()
        self.go_to_request_details_button.click()
        browser.should(have.url_containing(config.qiwa_urls.visa_web_url))
        if get_url_param(TRANSACTIONID) == visa_db.payment_id:
            visa_db.payment_id = None
