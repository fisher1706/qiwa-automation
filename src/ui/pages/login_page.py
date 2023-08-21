from __future__ import annotations

import allure
from selene import be, browser, command
from selene.support.shared.jquery_style import s

import config
from utils.logger import yaml_logger

logger = yaml_logger.setup_logging(__name__)


class LoginPage:
    sign_in_block = s(".main")
    login_field = s('input[data-test-id="userId"]')
    password_field = s('input[data-test-id="password"]')
    continue_button = s('[data-test-id="login"]')
    two_fa_field = s('input[data-test-id="otpConfirmValue"]')
    sign_in_button = s('[data-test-id="otpConfirm"]')

    @allure.step
    def open_login_page(self) -> LoginPage:
        browser.open(f"{config.settings.laborer_sso_ui_url}/en/sign-in")
        self.sign_in_block.wait_until(be.visible)
        return self

    @allure.step
    def enter_login(self, login: str) -> LoginPage:
        element = self.login_field
        element.wait_until(be.empty)
        element.perform(command.js.set_value("")).type(login)
        return self

    @allure.step
    def visit(self) -> LoginPage:
        browser.open(config.settings.env_url + "/en/sign-in")
        return self

    @allure.step
    def enter_password(self, pwd: str) -> LoginPage:
        self.password_field.perform(command.js.set_value("")).type(pwd)
        return self

    @allure.step
    def click_continue_button(self, click_button: bool = True) -> LoginPage:
        element = self.continue_button
        if click_button:
            element.should(be.clickable).click()
        else:
            element.should(be.disabled)
        return self

    @allure.step
    def enter_2fa_code(self, code: str = "0000") -> LoginPage:
        logger.info(f"Enter otp code: {code}")
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
    def click_sign_in_button(self, click_button: bool = True) -> LoginPage:
        button = self.sign_in_button
        if click_button:
            button.wait_until(be.clickable)
            button.should(be.clickable).click()
        else:
            button.should(be.disabled)
            logger.debug('Skip click on "Sign in" button. Not clickable')
        return self
