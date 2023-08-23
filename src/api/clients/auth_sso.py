from __future__ import annotations

from http import HTTPStatus

import allure
from requests import Response

import config
from data.account import Account
from src.api.assertions.response_validator import ResponseValidator
from src.api.http_client import HTTPClient
from src.api.payloads import Data, Root
from src.api.payloads.sso.sso_auth import (
    Auth,
    Authorize,
    CreateAccount,
    Hsm,
    SecurityQuestion,
    VerifyEmail,
    VerifyPhone,
)


class AuthApiSSO:
    url = config.settings.laborer_sso_api_url

    def __init__(self, api=HTTPClient()):
        self.api = api

    def authorize(self, state: str, code: str) -> Response:
        query = Authorize(state=state, code_challenge=code)
        response = self.api.post(self.url, "/authorize", params=query.dict())
        assert response.status_code == HTTPStatus.FOUND
        return response

    @allure.step
    def init_laborer_sso_hsm(
        self,
        personal_number: str,
        birth_date: str = "1430-01-01",
        expected_code: int = 200,
        requests_number: int = None,
        expect_schema="laborer-sso-init.json",
    ) -> AuthApiSSO:
        payload = Root(
            data=Data(
                type="session",
                attributes=Hsm(personal_number=personal_number, birth_date=birth_date),
            )
        )
        response: Response = ...
        if requests_number is not None:
            for _ in range(requests_number):
                response = self.api.post(
                    url=self.url,
                    endpoint="/session/high-security-mode/init/with-birthday",
                    json=payload.dict(by_alias=True, exclude_unset=True),
                )
        else:
            response = self.api.post(
                url=self.url,
                endpoint="/session/high-security-mode/init/with-birthday",
                json=payload.dict(by_alias=True, exclude_unset=True),
            )
        ResponseValidator(response).check_status_code(
            name="Init HSM", expect_code=expected_code
        ).check_response_schema(schema_name=expect_schema)
        return self

    @allure.step
    def active_hsm(
        self,
        expected_code: int = 200,
        absher: str = "000000",
        expected_schema="laborer-sso-init.json",
    ) -> AuthApiSSO:
        payload = Root(
            data=Data(
                type="registration",
                attributes=Hsm(otp=absher),
            )
        )
        response = self.api.post(
            url=self.url,
            endpoint="/session/high-security-mode",
            json=payload.dict(exclude_unset=True),
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
    def phone_verification(self, phone_number: str, expected_code=200):
        payload = Root(
            data=Data(
                type="registration",
                attributes=VerifyPhone(phone=phone_number),
            )
        )
        response = self.api.post(
            url=self.url, endpoint="/phones/init-verification", json=payload.dict()
        )
        ResponseValidator(response).check_status_code(
            name="Phone verification", expect_code=expected_code
        )
        return self

    @allure.step
    def pre_check_user_email(self, email: str, expected_code=200) -> AuthApiSSO:
        payload = Root(
            data=Data(
                type="user-email",
                attributes=VerifyEmail(email=email),
            )
        )
        response = self.api.post(url=self.url, endpoint="/emails/precheck", json=payload.dict())
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
        payload = Root(data=Data(type="password", attributes=Auth(otp=otp_code)))
        response = self.api.post(
            url=self.url,
            endpoint="/emails/confirm-verification",
            json=payload.dict(exclude_unset=True),
        )
        ResponseValidator(response).check_status_code(
            name="Email confirm verify", expect_code=expected_code
        )
        return self

    @allure.step
    def answer_security_question(self, expected_code: int = 200) -> AuthApiSSO:
        security_payload = Root(data=Data(type="account", attributes=SecurityQuestion()))
        response = self.api.post(
            url=self.url, endpoint="/security-questions", json=security_payload.dict(by_alias=True)
        )
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
        payload = Root(
            data=Data(
                type="account",
                attributes=CreateAccount(
                    otp=account.confirmation_code,
                    birth_date=account.birth_day,
                    email=account.email,
                    password=account.password,
                    password_confirm=account.password,
                ),
            )
        )
        response: Response = ...
        if requests_number is not None:
            for _ in range(requests_number):
                response = self.api.post(
                    url=self.url,
                    endpoint="/accounts",
                    json=payload.dict(by_alias=True),
                )
        else:
            response = self.api.post(url=self.url, endpoint="/accounts", json=payload.dict(by_alias=True))
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
        login_body = Root(data=Data(type="login", attributes=Auth(login=login, password=password)))
        response = self.api.post(
            url=self.url, endpoint="/session/login", json=login_body.dict(exclude_unset=True)
        )
        ResponseValidator(response).check_status_code(name="Login", expect_code=expected_code)

    @allure.step
    def login_with_otp(self, otp_code="0000", expected_code=200):
        check_otp_code_body = Root(data=Data(type="otp", attributes=Auth(otp=otp_code)))
        response = self.api.post(
            url=self.url,
            endpoint="/session/login-with-otp",
            json=check_otp_code_body.dict(exclude_unset=True),
        )
        ResponseValidator(response).check_status_code(
            name="Login with OTP", expect_code=expected_code
        )

    @allure.step("POST /session/logout :: logout user")
    def logout_user(self, expected_code=200):
        response = self.api.post(url=self.url, endpoint="/session/logout")
        ResponseValidator(response).check_status_code(name="Logout", expect_code=expected_code)
