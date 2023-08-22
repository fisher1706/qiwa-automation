from __future__ import annotations

from http import HTTPStatus

import allure
from requests import Response

import config
from data.account import Account
from src.api.assertions.response_validator import ResponseValidator
from src.api.http_client import HTTPClient
from src.api.requests.account_laborer_sso import LaborerSSOAccount
from src.api.requests.hsm_laborer_sso import LaborerSSOHsm


class AuthApiSSO:
    url = config.settings.laborer_sso_api_url

    def __init__(self, api=HTTPClient()):
        self.api = api

    def authorize(self, state: str, code: str) -> Response:
        query = {
            "client_id": "qiwa",
            "redirect_uri": f"{config.settings.env_url}/oauth/callback",
            "response_type": "code",
            "scope": "openid email phone profile",
            "code_challenge_method": "S256",
            "state": state,
            "code_challenge": code,
        }
        response = self.api.post(self.url, "/authorize", params=query)
        assert response.status_code == HTTPStatus.FOUND
        return response

    @allure.step
    def init_laborer_sso_hsm(
        self,
        personal_number: str,
        year: int | str = 1430,
        month: str = "01",
        day: str = "01",
        expected_code: int = 200,
        requests_number: int = None,
        expect_schema="laborer-sso-init.json",
    ) -> AuthApiSSO:
        json_body = LaborerSSOHsm.create_init_body(personal_number, year, month, day)
        response: Response = ...
        if requests_number is not None:
            for _ in range(requests_number):
                response = self.api.post(
                    url=self.url,
                    endpoint="/session/high-security-mode/init/with-birthday",
                    json=json_body,
                )
        else:
            response = self.api.post(
                url=self.url,
                endpoint="/session/high-security-mode/init/with-birthday",
                json=json_body,
            )
        ResponseValidator(response).check_status_code(
            name="Init HSM", expect_code=expected_code
        ).check_response_schema(schema_name=expect_schema)
        return self

    @allure.step
    def active_hsm(
        self,
        expected_code: int = 200,
        sms_code: str = "000000",
        expected_schema="laborer-sso-init.json",
    ) -> AuthApiSSO:
        json_body = LaborerSSOHsm.create_activate_body(sms_code)
        response = self.api.post(
            url=self.url, endpoint="/session/high-security-mode", json=json_body
        )
        validator = ResponseValidator(response)
        validator.check_status_code(name="Activate HSM", expect_code=expected_code)
        if expected_code == 200:
            validator.check_response_schema(schema_name=expected_schema)
        return self

    @allure.step("GET /users/precheck :: pre-check user")
    def pre_check_user(self, expected_code=200, expected_schema="laborer-sso-error.json"):
        response = self.api.get(url=self.url, endpoint="/users/precheck")
        validator = ResponseValidator(response)
        validator.check_status_code(name="Pre-check user", expect_code=expected_code)
        if expected_code != 200:
            validator.check_response_schema(schema_name=expected_schema)
        return self

    @allure.step
    def phone_verification(self, phone_number="966746055769", expected_code=200):
        json_body = LaborerSSOHsm.phone_verification(phone_number)
        response = self.api.post(
            url=self.url, endpoint="/phones/init-verification", json=json_body
        )
        ResponseValidator(response).check_status_code(
            name="Phone verification", expect_code=expected_code
        )
        return self

    @allure.step
    def pre_check_user_email(self, user_email, expected_code=200) -> AuthApiSSO:
        json_body = LaborerSSOHsm.email_pre_check(user_email)
        response = self.api.post(url=self.url, endpoint="/emails/precheck", json=json_body)
        ResponseValidator(response).check_status_code(
            name="Email pre-check", expect_code=expected_code
        )
        return self

    @allure.step
    def verify_email_with_otp_code(self, expected_code: int = 200) -> AuthApiSSO:
        response = self.api.get(url=self.url, endpoint="/emails/verify")
        ResponseValidator(response).check_status_code(
            name="Email verify", expect_code=expected_code
        )
        return self

    @allure.step
    def confirm_verify_email_with_otp_code(self, expected_code: int = 200) -> AuthApiSSO:
        json_body = LaborerSSOAccount.check_otp_code(otp_type="password")
        response = self.api.post(
            url=self.url, endpoint="/emails/confirm-verification", json=json_body
        )
        ResponseValidator(response).check_status_code(
            name="Email confirm verify", expect_code=expected_code
        )
        return self

    @allure.step
    def answer_security_question(self, expected_code: int = 200) -> AuthApiSSO:
        json_body = {
            "data": {
                "type": "account",
                "attributes": {"mother-dob": "1-1-2011", "mother-name": "Some name"},
            }
        }
        response = self.api.post(url=self.url, endpoint="/security-questions", json=json_body)
        ResponseValidator(response).check_status_code(
            name="Email confirm verify", expect_code=expected_code
        )
        return self

    @allure.step
    def register_user(
        self,
        account: Account,
        requests_number: int = None,
        expected_code: int = 200,
        expected_schema: str = "laborer-sso-error.json",
    ) -> AuthApiSSO:
        json_body = LaborerSSOAccount.register_account(account)
        response: Response = ...
        if requests_number is not None:
            for _ in range(requests_number):
                response = self.api.post(url=self.url, endpoint="/accounts", json=json_body)
        else:
            response = self.api.post(url=self.url, endpoint="/accounts", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="Register user", expect_code=expected_code)
        if expected_code != 200:
            validator.check_response_schema(schema_name=expected_schema)
        return self

    @allure.step("GET /session :: get session")
    def get_session(self, expected_code=200):
        response = self.api.get(url=self.url, endpoint="/session")
        ResponseValidator(response).check_status_code(
            name="Get session", expect_code=expected_code
        )

    @allure.step
    def login(self, login, password, expected_code=200):
        login_body = LaborerSSOAccount.login_user(login, password)
        response = self.api.post(url=self.url, endpoint="/session/login", json=login_body)
        ResponseValidator(response).check_status_code(name="Login", expect_code=expected_code)

    @allure.step
    def login_with_otp(self, otp_code="0000", expected_code=200):
        check_otp_code_body = LaborerSSOAccount.check_otp_code(otp_code)
        response = self.api.post(
            url=self.url,
            endpoint="/session/login-with-otp",
            json=check_otp_code_body,
        )
        ResponseValidator(response).check_status_code(
            name="Login with OTP", expect_code=expected_code
        )

    @allure.step("POST /session/logout :: logout user")
    def logout_user(self, expected_code=200):
        response = self.api.post(url=self.url, endpoint="/session/logout")
        ResponseValidator(response).check_status_code(name="Logout", expect_code=expected_code)
