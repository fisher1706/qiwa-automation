from http import HTTPStatus
from urllib.parse import parse_qs, urlparse

import allure

from data.account import Account
from src.api.clients.auth_sso import AuthApiSSO
from src.api.clients.oauth import OAuthApi


class AuthApiSSOController(AuthApiSSO):
    @property
    def oauth_api(self) -> OAuthApi:
        return OAuthApi(self.api)

    @allure.step("Login {personal_number} via Laborer SSO API")
    def login_user(self, personal_number: str, password: str) -> None:
        init = self.oauth_api.init()
        assert init.status_code == HTTPStatus.OK
        redirect_uri = urlparse(init.json()["data"]["attributes"]["redirect-uri"])
        redirect_uri_query = parse_qs(redirect_uri.query)
        self.login(personal_number, password)
        self.login_with_otp()
        authorize = self.authorize(
            state=redirect_uri_query["state"][0], code=redirect_uri_query["code_challenge"][0]
        )
        url = urlparse(authorize.headers.get("location"))
        url_query = parse_qs(url.query)
        callback = self.oauth_api.callback(
            state=url_query["state"][0], auth_code=url_query["code"][0]
        )
        assert callback.status_code == HTTPStatus.OK

    @allure.step
    def create_account_via_laborer_sso_api(self, account: Account) -> None:
        self.phone_verification(account.phone_number)
        self.pre_check_user_email(account.email)
        self.register_user(account)

    @allure.step
    def register_account_via_sso_api(self, account: Account) -> None:
        self.init_laborer_sso_hsm(account.personal_number)
        self.active_hsm()
        self.create_account_via_laborer_sso_api(account)

    @allure.step
    def pass_account_security(self, personal_number: str, password: str):
        self.login(personal_number, password)
        self.login_with_otp()
        self.verify_email_with_otp_code()
        self.confirm_verify_email_with_otp_code()
        self.answer_security_question()
        self.logout()

    @allure.step("Log out the user from Laborer SSO")
    def logout(self):
        self.get_session()
        self.logout_user()
