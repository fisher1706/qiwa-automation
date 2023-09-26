from selene import be, have
from selene.support.shared.jquery_style import s, ss

from data.constants import Language
from src.ui.components.raw.table import Table


class IndividualLocators:  # pylint: disable=too-few-public-methods, no-member
    SERVICE_CARD = ".service-card__title"
    FIELD_CONFIRMATION_CODE = 'input[name="code"]'
    ACTIONS_VIEW = 'button[title="View"]'
    CHECKBOX_AGREE = ".check"
    BTN_ACCEPT_THE_REQUEST = 'button[title="Accept the request"]'
    BTN_REJECT_THE_REQUEST = 'button[title="Reject the request"] span'
    BTN_MODAL_ACCEPT_THE_REQUEST = (
        '.employee-transfer-action-modal__buttons button[title="Accept the request"]'
    )
    BTN_MODAL_REJECT_THE_REQUEST = (
        '.employee-transfer-action-modal__buttons button[title="Reject the request"]'
    )
    DROPDOWN_MODAL_REJECT_REASON = "#reject-reason"
    LOCALE = "#language-select"
    MODAL = ".basic-modal__header"


class IndividualPage(IndividualLocators):
    individual_table = Table(s(".table"))

    def select_service(self, text: str):
        ss(self.SERVICE_CARD).element_by(have.exact_text(text)).click()

    def proceed_2fa(self, code: str = "0000"):
        s(self.FIELD_CONFIRMATION_CODE).type(code).press_enter()

    def select_first_view_request(self):
        self.individual_table.cell(row=1, column="Action").click()  # pylint: disable=no-member

    def click_agree_checkbox(self):
        s(self.CHECKBOX_AGREE).click()

    def click_btn_accept_the_request(self):
        s(self.BTN_ACCEPT_THE_REQUEST).should(be.clickable).click()

    def click_btn_reject_the_request(self):
        s(self.BTN_REJECT_THE_REQUEST).should(be.clickable).click()

    def click_btn_modal_accept_the_request(self):
        s(self.BTN_MODAL_ACCEPT_THE_REQUEST).should(be.clickable).click()

    def click_btn_modal_reject_the_request(self):
        s(self.BTN_MODAL_REJECT_THE_REQUEST).should(be.clickable).click()

    def verify_expected_status(self, status: dict, locale: str):
        cell_name = "Status" if locale == Language.EN else "الحالة"
        self.individual_table.cell(row=1, column=cell_name).should(have.exact_text(status[locale]))

    def select_rejection_reason(self, reason: str):
        s(self.DROPDOWN_MODAL_REJECT_REASON).should(be.visible).all("option").element_by(
            have.text(reason)
        ).click()

    def change_locale(self, locale: str = Language.AR):
        s(self.LOCALE).should(be.visible).all("option").element_by(have.value(locale)).click()

    def wait_until_popup_disappears(self):
        s(self.MODAL).wait_until(be.not_.visible)
