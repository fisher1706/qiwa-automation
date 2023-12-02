from __future__ import annotations

import allure

from data.account import Account
from src.api.clients.sso.auth_sso import AuthApiSSO
from src.api.clients.oauth import OAuthApi


class AuthApiSSOController(AuthApiSSO):
    @property
    def oauth_api(self) -> OAuthApi:
        return OAuthApi(self.client)

    @allure.step("Login {personal_number} via Laborer SSO API")
    def login_user(self, personal_number: str, password: str) -> None:
        init = self.oauth_api.init()
        self.login(personal_number, password)
        self.login_with_otp()
        authorize = self.authorize(state=init["state"][0], code=init["code_challenge"][0])
        self.oauth_api.callback(state=authorize["state"][0], auth_code=authorize["code"][0])

    @allure.step
    def create_account_via_laborer_sso_api(self, account: Account) -> None:
        self.phone_verification(account.phone_number)
        self.pre_check_user_email(account.email)
        self.register_user(account)

    @allure.step
    def register_account_via_sso_api(self, account: Account) -> AuthApiSSOController:
        self.init_sso_hsm(account.personal_number, account.birth_day)
        self.active_sso_hsm()
        self.create_account_via_laborer_sso_api(account)
        return self

    @allure.step
    def pass_account_security(self) -> None:
        self.verify_email_with_otp_code()
        self.confirm_verify_email_with_otp_code()
        self.answer_security_question()
        self.logout()

    @allure.step
    def logout(self) -> None:
        self.oauth_api.delete_context()
        logout_token = self.oauth_api.init_logout()
        self.logout_user(logout_token)
