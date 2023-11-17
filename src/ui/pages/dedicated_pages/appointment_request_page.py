from __future__ import annotations

import allure
from selene import browser
from selene.support.shared.jquery_style import s, ss

import config
from data.dedicated.enums import SearchingType
from utils.allure import allure_steps


@allure_steps
class AppointmentRequestPage:
    input_otp_code = s(".otp-input")
    input_otp_code_modal = s("#singleOtpInput input")
    input_search_by = s('[name="id"]')
    input_search_by_lo_id = s('[name="lo"]')
    input_search_by_sequence_number = s('[name="sequence"]')

    button_search = s('//button[@type="submit"]')
    button_proceed = s('//button[@class="btn btn--primary with-preloader"]')
    button_proceed_modal = s(".o-modal__otp-actions--single-action button")
    button_next = s('//button[@class="btn btn--primary"]')

    def visit(self) -> AppointmentRequestPage:
        browser.open(config.qiwa_urls.agent_sys_url)
        return self

    def set_search_by(
        self, searching_type: SearchingType, searching_id: int, sequence_number: str = None
    ) -> AppointmentRequestPage:
        if searching_type != SearchingType.ESTABLISHMENT_NUMBER:
            self.input_search_by.type(searching_id)
        else:
            self.input_search_by_lo_id.type(searching_id)
            self.input_search_by_sequence_number.type(sequence_number)
        return self

    def search_visit(self) -> AppointmentRequestPage:
        self.button_search.click()
        return self

    def proceed(self) -> AppointmentRequestPage:
        self.button_proceed.click()
        return self

    def proceed_modal(self) -> AppointmentRequestPage:
        self.button_proceed_modal.click()
        return self

    def set_and_confirm_otp(self, otp_code: str = "0000") -> AppointmentRequestPage:
        self.input_otp_code.type(otp_code)
        self.proceed()
        return self

    def set_and_confirm_otp_modal(self, otp_code: str = "0000") -> AppointmentRequestPage:
        self.input_otp_code_modal.type(otp_code)
        self.proceed_modal()
        return self

    # TODO(dp): Remove after fix
    # pylint: disable=no-member
    def set_and_confirm_otp_temp(self, otp_code: str = "0000") -> AppointmentRequestPage:
        ss(".c-otp-input input")[4].type(otp_code)
        ss(".o-modal__otp-actions--single-action button")[1].click()
        return self
