from __future__ import annotations

from selene.support.shared.jquery_style import s


class EmailConfirmationPopup:
    otp_code_first_cell = s("(//input[@type='tel'])[1]")
    otp_code_second_cell = s("(//input[@type='tel'])[2]")
    otp_code_third_cell = s("(//input[@type='tel'])[3]")
    otp_code_fourth_cell = s("(//input[@type='tel'])[4]")
    confirm_button = s("//button[normalize-space()='Confirm']")

    def proceed_otp_code(self, number: str) -> EmailConfirmationPopup:
        self.otp_code_first_cell.type(number)
        self.otp_code_second_cell.type(number)
        self.otp_code_third_cell.type(number)
        self.otp_code_fourth_cell.type(number)
        # self.confirm_button.click()
        return self
