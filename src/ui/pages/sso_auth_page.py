from __future__ import annotations

import allure
from selene.support.shared.jquery_style import s


class SSOAuthPage:
    user_id = s("input[id='userId']")
    password = s("input[id='password']")
    login_button = s("button[type='submit']")
    otp_code_first_cell = s("input[id='test-0']")
    otp_code_second_cell = s("input[id='test-1']")
    otp_code_third_cell = s("input[id='test-2']")
    otp_code_fourth_cell = s("input[id='test-3']")
    confirm_otp_button = s("#submit")

    @allure.step
    def enter_user_id(self, user_id: str) -> SSOAuthPage:
        self.user_id.type(user_id)
        return self

    @allure.step
    def enter_password(self, password: str) -> SSOAuthPage:
        self.password.type(password)
        return self

    @allure.step
    def login(self) -> SSOAuthPage:
        self.login_button.click()
        return self

    @allure.step
    def enter_otp_code(self, number: str) -> SSOAuthPage:
        self.otp_code_first_cell.type(number)
        self.otp_code_second_cell.type(number)
        self.otp_code_third_cell.type(number)
        self.otp_code_fourth_cell.type(number)
        return self

    @allure.step
    def confirm_otp_code(self) -> None:
        self.confirm_otp_button.click()
