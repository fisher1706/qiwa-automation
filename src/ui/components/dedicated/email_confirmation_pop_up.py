from __future__ import annotations

import time

from selene import be
from selene.support.shared.jquery_style import s


class EmailConfirmationPopup:
    otp_first_cell = s("(//input[@type='tel'])[1]")
    otp_second_cell = s("(//input[@type='tel'])[2]")
    otp_third_cell = s("(//input[@type='tel'])[3]")
    otp_fourth_cell = s("(//input[@type='tel'])[4]")
    confirm_button = s("//button[normalize-space()='Confirm']")
    confirm_and_proceed_button = s("//button[normalize-space()='Confirm and proceed to summary']")

    def proceed_otp_code(self, number: str = "0000") -> EmailConfirmationPopup:
        self.otp_first_cell.type(number)
        self.otp_second_cell.type(number)
        self.otp_third_cell.type(number)
        self.otp_fourth_cell.type(number)
        return self

    def click_on_confirm_btn(self) -> EmailConfirmationPopup:
        self.confirm_button.click()
        return self

    def click_on_confirm_and_proceed(self) -> EmailConfirmationPopup:
        self.confirm_and_proceed_button.should(be.visible).click()
        time.sleep(30)
        return self
