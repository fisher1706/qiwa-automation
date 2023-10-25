from __future__ import annotations

from selene import be, have
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.keys import Keys

from data.constants import Language
from src.ui.components.raw.table import Table


class IndividualPage:
    service_card = ss('[data-component="ActionTile"] div')
    field_confirmation_code = ss('[inputmode="numeric"]')
    checkbox_agree = s("#termsOfService")
    btn_accept_the_request = s('//button[.="Accept"]')
    btn_reject_the_request = s('//button[.="Reject"]')
    btn_modal_accept_the_request = s('//button[.="Accept transfer"]')
    btn_modal_reject_the_request = s('//button[.="Reject the request"]')
    dropdown_modal_reject_reason = s("#reject-reason")
    locale = s("#language-select")
    modal = s(".basic-modal__header")
    individual_table = Table(s(".table"))
    status = s('[role="status"]')

    def select_service(self, text: str) -> IndividualPage:
        self.service_card.element_by(have.text(text)).click()
        return self

    def click_agree_checkbox(self) -> IndividualPage:
        self.checkbox_agree.press(Keys.SPACE)
        return self

    def click_btn_accept_the_request(self) -> IndividualPage:
        self.btn_accept_the_request.click()
        return self

    def click_btn_reject_the_request(self) -> IndividualPage:
        self.btn_reject_the_request.click()
        return self

    def click_btn_modal_accept_the_request(self) -> IndividualPage:
        self.btn_modal_accept_the_request.click()
        return self

    def click_btn_modal_reject_the_request(self) -> IndividualPage:
        self.btn_modal_reject_the_request.click()
        return self

    def verify_expected_status(self, text: str) -> IndividualPage:
        self.status.should(have.exact_text(text))
        return self

    def select_rejection_reason(self, reason: str) -> IndividualPage:
        self.dropdown_modal_reject_reason.should(be.visible).all("option").element_by(
            have.text(reason)
        ).click()
        return self

    def change_locale(self, locale: str = Language.AR) -> IndividualPage:
        self.locale.should(be.visible).all("option").element_by(have.value(locale)).click()
        return self

    def wait_until_popup_disappears(self) -> IndividualPage:
        self.modal.wait_until(be.not_.visible)
        return self
