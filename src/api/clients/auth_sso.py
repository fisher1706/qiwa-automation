from __future__ import annotations

from http import HTTPStatus
from urllib.parse import parse_qs, urlparse

import allure
from requests import Response

import config
from data.account import Account
from src.api.assertions.response_validator import ResponseValidator
from src.api.http_client import HTTPClient
from src.api.payloads.raw.sso_oauth import Authorize
from src.api.payloads.sso_oauth_payloads import (
    activate_sso_hsm_payload,
    email_verification_payload,
    init_sso_hsm_payload,
    login_payload,
    logout_payload,
    otp_code_payload,
    phone_verification_payload,
    registration_account_payload,
    request_with_otp_payload,
    security_question_payload,
    unlock_through_email_payload,
)


class AuthApiSSO:
    url = config.qiwa_urls.sso_api

    def __init__(self, api=HTTPClient()):
        self.api = api

    def authorize(self, state: str, code: str) -> dict:
        query = Authorize(state=state, code_challenge=code)
        response = self.api.post(self.url, "/authorize", params=query.dict())
        assert response.status_code == HTTPStatus.FOUND
        url = urlparse(response.headers.get("location"))
        url_query = parse_qs(url.query)
        return url_query

    @allure.step
    def init_sso_hsm(
        self,
        personal_number: str,
        birth_date: str,
        expected_code: int = 200,
        requests_number: int = None,
    ) -> AuthApiSSO:
        payload = init_sso_hsm_payload(personal_number, birth_date)
        response: Response = ...
        if requests_number is not None:
            for _ in range(requests_number):
                response = self.api.post(
                    url=self.url,
                    endpoint="/session/high-security-mode/init/with-birthday",
                    json=payload,
                )
        else:
            response = self.api.post(
                url=self.url,
                endpoint="/session/high-security-mode/init/with-birthday",
                json=payload,
            )
        assert response.status_code == expected_code
        return self

    @allure.step
    def init_hsm_with_out_birthday(
        self, personal_number: str, expected_code: int = HTTPStatus.OK
    ) -> AuthApiSSO:
        payload = init_sso_hsm_payload(personal_number)
        response = self.api.post(
            url=self.url,
            endpoint="/session/high-security-mode/init",
            json=payload,
        )
        assert response.status_code == expected_code
        return self

    @allure.step
    def init_unlock_account_through_email(self) -> AuthApiSSO:
        response = self.api.post(url=self.url, endpoint="/accounts/init-unlock")
        assert response.status_code == HTTPStatus.OK
        return self

    @allure.step
    def unlock_account_through_email(self, unlock_key: str) -> AuthApiSSO:
        payload = unlock_through_email_payload(lockout_key=unlock_key)
        response = self.api.post(url=self.url, endpoint="/accounts/unlock-via-email", json=payload)
        assert response.status_code == HTTPStatus.OK
        return self

    @allure.step
    def unlock_account_with_otp(self) -> None:
        payload = request_with_otp_payload(otp="0000")
        response = self.api.post(url=self.url, endpoint="/accounts/unlock-with-otp", json=payload)
        assert response.status_code == HTTPStatus.OK

    @allure.step
    def resend_absher_code_on_unlock_account_flow(self):
        response = self.api.post(url=self.url, endpoint="/session/high-security-mode/init/resend")
        assert response.status_code == HTTPStatus.OK

    @allure.step
    def active_sso_hsm(
        self, expected_code: int = 200, absher: str = "000000"
    ) -> tuple[Response, AuthApiSSO]:
        response = self.api.post(
            url=self.url,
            endpoint="/session/high-security-mode",
            json=activate_sso_hsm_payload(absher_code=absher),
        )
        assert response.status_code == expected_code
        return response.json()

    @allure.step
    def phone_verification(self, phone_number: str, expected_code: int = 200) -> AuthApiSSO:
        response = self.api.post(
            url=self.url,
            endpoint="/phones/init-verification",
            json=phone_verification_payload(phone_number),
        )
        ResponseValidator(response).check_status_code(
            name="Phone verification", expect_code=expected_code
        )
        return self

    @allure.step
    def pre_check_user_email(self, email: str, expected_code=200) -> AuthApiSSO:
        response = self.api.post(
            url=self.url, endpoint="/emails/precheck", json=email_verification_payload(email)
        )
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
    def confirm_verify_email_with_otp_code(
        self, otp_code: str = "0000", expected_code: int = 200
    ) -> AuthApiSSO:
        response = self.api.post(
            url=self.url,
            endpoint="/emails/confirm-verification",
            json=otp_code_payload(otp_code),
        )
        ResponseValidator(response).check_status_code(
            name="Email confirm verify", expect_code=expected_code
        )
        return self

    @allure.step
    def answer_security_question(self, expected_code: int = 200) -> AuthApiSSO:
        response = self.api.post(
            url=self.url, endpoint="/security-questions", json=security_question_payload()
        )
        ResponseValidator(response).check_status_code(
            name="Email confirm verify", expect_code=expected_code
        )
        return self

    @allure.step
    def register_user(
        self, account: Account, requests_number: int = None, expected_code: int = 200
    ) -> AuthApiSSO:
        response: Response = ...
        if requests_number is not None:
            for _ in range(requests_number):
                response = self.api.post(
                    url=self.url,
                    endpoint="/accounts",
                    json=registration_account_payload(account),
                )
        else:
            response = self.api.post(
                url=self.url, endpoint="/accounts", json=registration_account_payload(account)
            )
        assert response.status_code == expected_code
        return self

    @allure.step("GET /session :: get session")
    def get_session(self, expected_code=200):
        response = self.api.get(url=self.url, endpoint="/session")
        ResponseValidator(response).check_status_code(
            name="Get session", expect_code=expected_code
        )

    @allure.step
    def login(self, login: str, password: str, expected_code: int = 200) -> None:
        response = self.api.post(
            url=self.url,
            endpoint="/session/login",
            json=login_payload(login=login, account_pwd=password),
        )
        ResponseValidator(response).check_status_code(name="Login", expect_code=expected_code)

    @allure.step
    def enter_incorrect_password_numerous_times(self, login: str, password: str, times: int = 8):
        for _ in range(times):
            response = self.api.post(
                url=self.url,
                endpoint="/session/login",
                json=login_payload(login=login, account_pwd=password),
            )
            assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    @allure.step
    def login_with_otp(self, otp_code="0000", expected_code=200):
        response = self.api.post(
            url=self.url,
            endpoint="/session/login-with-otp",
            json=request_with_otp_payload(otp=otp_code),
        )
        ResponseValidator(response).check_status_code(
            name="Login with OTP", expect_code=expected_code
        )

    @allure.step
    def logout_user(self, logout_token: str):
        response = self.api.post(
            url=self.url, endpoint="/logout/remote", json=logout_payload(logout_token=logout_token)
        )
        assert response.status_code == HTTPStatus.OK

    @allure.step
    def unlock_account(self):
        response = self.api.post(url=self.url, endpoint="/accounts/unlock")
        assert response.status_code == HTTPStatus.OK
