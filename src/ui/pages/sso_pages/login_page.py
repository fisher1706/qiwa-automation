from __future__ import annotations

import allure
from selene import be, browser, command, have
from selene.support.shared.jquery_style import s, ss

import config
from src.ui.components.code_verification import CodeVerification


class LoginPage:
    identity_number_field = s("#userId")
    password_field = s("#password")
    login_button = s('button[type="submit"]')
    otp_pop_up = CodeVerification(s('[data-testid="modal-root"]'))
    absher_pop_up = CodeVerification(s('[data-testid="absher-popup"]'))
    notification_message_texts = ss('[data-component="VerticalNotification"] p')
    unlock_account_button = s('[data-component="VerticalNotification"] button')
    not_robot_captcha = s('[title="reCAPTCHA"]')

    @allure.step
    def open_login_page(self) -> LoginPage:
        browser.open(f"{config.qiwa_urls.sso}/en/sign-in")
        return self

    @allure.step
    def wait_login_page_to_load(self) -> LoginPage:
        self.identity_number_field.wait_until(be.visible)
        self.password_field.wait_until(be.visible)
        return self

    @allure.step
    def check_login_page_is_displayed(self):
        self.identity_number_field.should(be.visible)
        self.password_field.should(be.visible)
        self.login_button.should(be.visible)

    @allure.step
    def enter_login(self, login: str) -> LoginPage:
        self.identity_number_field.perform(command.js.set_value("")).type(login)
        return self

    @allure.step
    def enter_password(self, pwd: str) -> LoginPage:
        self.password_field.perform(command.js.set_value("")).type(pwd)
        return self

    @allure.step
    def click_login_button(self) -> LoginPage:
        self.login_button.click()
        return self

    @allure.step
    def unlock_account_message_should_have_text(self, message: str) -> LoginPage:
        self.notification_message_texts.element(index=1).should(have.exact_text(message))
        return self

    @allure.step
    def unlock_account_button_should_be_visible(self):
        self.unlock_account_button.should(be.visible)

    @allure.step
    def recaptcha_should_be_visible(self):
        self.not_robot_captcha.should(be.visible)
