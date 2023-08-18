from http import HTTPStatus
from urllib.parse import parse_qs, urlparse

import allure

from src.api.clients.auth_api_laborer_sso import AuthApiLaborerSSO
from src.api.clients.oauth import OAuthApi


class AuthApiLaborerSSOActions(AuthApiLaborerSSO):  # pylint: disable=duplicate-code
    @property
    def oauth_api(self) -> OAuthApi:
        return OAuthApi(self.api)

    @allure.step("Login {personal_number} via Laborer SSO API")
    def login_user(self, personal_number: str, password: str):
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

    @allure.step("Prepare HSM")
    def prepare_hsm(self, account, expected_code=200):
        self.init_laborer_sso_hsm(
            account.personal_number, account.year, account.month, account.day, expected_code
        )
        self.active_hsm(expected_code)

    @allure.step("Create prepared user account via API")
    def create_account_via_laborer_sso_api(self, account):
        self.phone_verification(account.phone_number)
        self.pre_check_user_email(account.email)
        self.register_user(account)

    @allure.step("Complete create user account via laborer SSO API")
    def complete_create_account_via_laborer_sso_api(self, account):
        self.init_laborer_sso_hsm(
            account.personal_number, account.year, account.month, account.day
        )
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
