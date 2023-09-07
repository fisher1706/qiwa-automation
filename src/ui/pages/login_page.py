from __future__ import annotations

import allure
from selene import be, browser, command
from selene.support.shared.jquery_style import s

import config


class LoginPage:
    login_field = s('input[data-test-id="userId"]')
    password_field = s('input[data-test-id="password"]')
    continue_button = s('[data-test-id="login"]')
    two_fa_field = s('input[data-test-id="otpConfirmValue"]')
    sign_in_button = s('[data-test-id="otpConfirm"]')

    @allure.step
    def open_login_page(self) -> LoginPage:
        browser.open(f"{config.qiwa_urls.laborer_sso_auth}/en/sign-in")
        return self

    @allure.step
    def enter_login(self, login: str) -> LoginPage:
        element = self.login_field
        element.wait_until(be.empty)
        element.perform(command.js.set_value("")).type(login)
        return self

    @allure.step
    def visit(self) -> LoginPage:
        browser.open(config.qiwa_urls.auth + "/en/sign-in")
        return self

    @allure.step
    def enter_password(self, pwd: str) -> LoginPage:
        self.password_field.perform(command.js.set_value("")).type(pwd)
        return self

    @allure.step
    def click_continue_button(self) -> LoginPage:
        self.continue_button.click()
        return self

    @allure.step
    def enter_2fa_code(self, code: str = "0000") -> LoginPage:
        element = self.two_fa_field
        element.wait_until(be.visible)
        element.should(be.blank).type(code).press_tab()
        return self

    @allure.step
    def wait_page_to_load(self) -> LoginPage:
        self.password_field.wait_until(be.visible)
        return self

    @allure.step
    def wait_login_page_to_appear(self) -> LoginPage:
        self.login_field.wait_until(be.visible)
        return self

    @allure.step
    def click_sign_in_button(self) -> LoginPage:
        self.sign_in_button.click()
        return self
