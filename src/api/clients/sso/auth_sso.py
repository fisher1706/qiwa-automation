from __future__ import annotations

import time
from http import HTTPStatus
from urllib.parse import parse_qs, urlparse

import allure
from requests import Response

import config
from data.account import Account
from src.api.http_client import HTTPClient
from src.api.payloads.raw.sso_oauth import Authorize
from src.api.payloads.sso_oauth_payloads import (
    activate_sso_hsm_payload,
    email_verification_payload,
    hsm_payload,
    init_hsm_for_reset_password,
    init_sso_hsm_payload,
    login_payload,
    logout_payload,
    otp_code_payload,
    phone_verification_on_login_payload,
    phone_verification_on_registration_payload,
    registration_account_payload,
    request_with_otp_payload,
    reset_password,
    security_question_payload,
    unlock_through_email_payload,
)
from utils.assertion import assert_status_code


class AuthApiSSO:
    url = config.qiwa_urls.sso_api

    def __init__(self, client=HTTPClient()):
        self.client = client

    def authorize(self, state: str, code: str) -> dict:
        query = Authorize(state=state, code_challenge=code)
        response = self.client.post(self.url, "/authorize", params=query.dict())
        assert_status_code(response.status_code).equals_to(HTTPStatus.FOUND)
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
                response = self.client.post(
                    url=self.url,
                    endpoint="/session/high-security-mode/init/with-birthday",
                    json=payload,
                )
        else:
            response = self.client.post(
                url=self.url,
                endpoint="/session/high-security-mode/init/with-birthday",
                json=payload,
            )
        assert_status_code(response.status_code).equals_to(expected_code)
        return self

    @allure.step
    def init_hsm_with_out_birthday(
        self, personal_number: str, expected_code: int = HTTPStatus.OK
    ) -> AuthApiSSO:
        payload = init_sso_hsm_payload(personal_number)
        response = self.client.post(
            url=self.url,
            endpoint="/session/high-security-mode/init",
            json=payload,
        )
        assert_status_code(response.status_code).equals_to(expected_code)
        return self

    @allure.step
    def init_unlock_account_through_email(self) -> AuthApiSSO:
        response = self.client.post(url=self.url, endpoint="/accounts/init-unlock")
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return self

    @allure.step
    def unlock_account_through_email(self, unlock_key: str) -> AuthApiSSO:
        payload = unlock_through_email_payload(lockout_key=unlock_key)
        response = self.client.post(
            url=self.url, endpoint="/accounts/unlock-via-email", json=payload
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return self

    @allure.step
    def unlock_account_with_otp(self) -> None:
        payload = request_with_otp_payload(otp="0000")
        response = self.client.post(
            url=self.url, endpoint="/accounts/unlock-with-otp", json=payload
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    @allure.step
    def resend_absher_code_on_unlock_account_flow(self):
        response = self.client.post(
            url=self.url, endpoint="/session/high-security-mode/init/resend"
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    @allure.step
    def resend_absher_code_on_reset_password_flow(self, expected_code: int = 200):
        # sleep is needed in the matter of the delay on the endpoint for resending the Absher code
        time.sleep(30)
        response = self.client.post(
            url=self.url, endpoint="/reset-password/high-security-mode/resend"
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def resend_otp_on_secure_otp_flow(self):
        response = self.client.post(url=self.url, endpoint="/emails/init-verification/resend")
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()["data"]["attributes"]

    @allure.step
    def active_sso_hsm(
        self, expected_code: int = 200, absher: str = "000000"
    ) -> tuple[Response, AuthApiSSO]:
        response = self.client.post(
            url=self.url,
            endpoint="/session/high-security-mode",
            json=activate_sso_hsm_payload(absher_code=absher),
        )
        assert_status_code(response.status_code).equals_to(expected_code)
        return response.json()

    @allure.step
    def phone_verification(self, phone_number: str, expected_code: int = 200) -> AuthApiSSO:
        response = self.client.post(
            url=self.url,
            endpoint="/phones/init-verification",
            json=phone_verification_on_registration_payload(phone_number),
        )
        assert_status_code(response.status_code).equals_to(expected_code)
        return self

    @allure.step
    def pre_check_user_email(self, email: str, expected_code=200) -> AuthApiSSO:
        response = self.client.post(
            url=self.url, endpoint="/emails/precheck", json=email_verification_payload(email)
        )
        assert_status_code(response.status_code).equals_to(expected_code)
        return self

    @allure.step
    def verify_email_with_otp_code(self, expected_code: int = 200) -> AuthApiSSO:
        response = self.client.get(url=self.url, endpoint="/emails/verify")
        assert_status_code(response.status_code).equals_to(expected_code)
        return self

    @allure.step
    def confirm_verify_email_with_otp_code(
        self, otp_code: str = "0000", expected_code: int = 200
    ) -> AuthApiSSO:
        response = self.client.post(
            url=self.url,
            endpoint="/emails/confirm-verification",
            json=otp_code_payload(otp_code),
        )
        assert_status_code(response.status_code).equals_to(expected_code)
        return self

    @allure.step
    def answer_security_question(
        self,
        first_answer: str = "1-1-2011",
        second_answer: str = "Test name",
        expected_code: int = 200,
    ) -> AuthApiSSO:
        payload = security_question_payload(first_answer, second_answer)
        response = self.client.post(url=self.url, endpoint="/security-questions", json=payload)
        assert_status_code(response.status_code).equals_to(expected_code)
        return self

    @allure.step
    def same_answer(self, expected_code: int = 422):
        # disable pylint because needed to check same question for the API
        payload = {
            "data": {
                "attributes": {  # pylint: disable = duplicate-key
                    "mother-dob": "1-1-2011",
                    "mother-dob": "1-1-2011",
                },
                "type": "account",
            }
        }
        response = self.client.post(url=self.url, endpoint="/security-questions", json=payload)
        assert_status_code(response.status_code).equals_to(expected_code)
        return self

    @allure.step
    def register_user(
        self, account: Account, requests_number: int = None, expected_code: int = 200
    ) -> AuthApiSSO:
        response: Response = ...
        if requests_number is not None:
            for _ in range(requests_number):
                response = self.client.post(
                    url=self.url,
                    endpoint="/accounts",
                    json=registration_account_payload(account),
                )
        else:
            response = self.client.post(
                url=self.url, endpoint="/accounts", json=registration_account_payload(account)
            )
        assert_status_code(response.status_code).equals_to(expected_code)
        return self

    @allure.step("GET /session :: get session")
    def get_session(self, expected_code=200):
        response = self.client.get(url=self.url, endpoint="/session")
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def login(self, login: str, password: str, expected_code: int = 200) -> None:
        response = self.client.post(
            url=self.url,
            endpoint="/session/login",
            json=login_payload(login=login, account_pwd=password),
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def enter_incorrect_password_numerous_times(self, login: str, password: str, times: int = 8):
        for _ in range(times):
            response = self.client.post(
                url=self.url,
                endpoint="/session/login",
                json=login_payload(login=login, account_pwd=password),
            )
            assert_status_code(response.status_code).equals_to(HTTPStatus.UNPROCESSABLE_ENTITY)

    @allure.step
    def login_with_otp(self, otp_code="0000", expected_code=200):
        response = self.client.post(
            url=self.url,
            endpoint="/session/login-with-otp",
            json=request_with_otp_payload(otp=otp_code),
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def logout_user(self, logout_token: str):
        response = self.client.post(
            url=self.url, endpoint="/logout/remote", json=logout_payload(logout_token=logout_token)
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    @allure.step
    def unlock_account(self):
        response = self.client.post(url=self.url, endpoint="/accounts/unlock")
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    @allure.step
    def check_acceptance_criteria(self):
        response = self.client.get(url=self.url, endpoint="/acceptance-criteria")
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()

    @allure.step
    def init_reset_password(self, personal_number: str, expected_code: int = 200):
        payload = init_sso_hsm_payload(personal_number)
        response = self.client.post(url=self.url, endpoint="/reset-password/init", json=payload)
        assert_status_code(response.status_code).equals_to(expected_code)
        if expected_code == 200:
            url_to_parse = urlparse(response.json()["url"])
            token = parse_qs(url_to_parse.query)["token"][0]
            return token
        return response.json()

    @allure.step
    def hsm_on_reset_password(
        self, absher_code: str = "000000", expected_code: int = 200
    ) -> AuthApiSSO:
        payload = hsm_payload(absher_code)
        response = self.client.post(
            url=self.url, endpoint="/reset-password/high-security-mode", json=payload
        )
        assert_status_code(response.status_code).equals_to(expected_code)
        return self

    @allure.step
    def reset_password(
        self, new_password: str, confirm_password: str, token: str, expected_code: int = 200
    ):
        payload = reset_password(
            new_password=new_password, confirm_password=confirm_password, token=token
        )
        response = self.client.post(url=self.url, endpoint="/reset-password", json=payload)
        assert_status_code(response.status_code).equals_to(expected_code)
        return response.json()

    @allure.step
    def init_hsm_for_reset_password(self, token: str, expected_code: int = 200):
        payload = init_hsm_for_reset_password(token=token)
        response = self.client.post(
            url=self.url, endpoint="/reset-password/high-security-mode/init", json=payload
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def init_hsm_for_change_phone_on_login(
        self, personal_number: str, birth_date: str, expected_code: int = 200
    ):
        payload = init_sso_hsm_payload(personal_number=personal_number, birth_date=birth_date)
        response = self.client.post(
            url=self.url,
            endpoint="/change-phone-on-login/high-security-mode/init/with-birthday",
            json=payload,
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def activate_hsm_for_change_phone_on_login(
        self, absher_code: str = "000000", expected_code: int = 200
    ):
        payload = hsm_payload(absher_code=absher_code)
        response = self.client.post(
            url=self.url, endpoint="/change-phone-on-login/high-security-mode", json=payload
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def phone_verification_for_change_phone_on_login(
        self, phone_number: str, expected_code: int = 200
    ) -> AuthApiSSO:
        response = self.client.post(
            url=self.url,
            endpoint="/change-phone-on-login/init-verification",
            json=phone_verification_on_login_payload(phone_number),
        )
        assert_status_code(response.status_code).equals_to(expected_code)
        return response.json()

    @allure.step
    def confirm_phone_verification_for_change_on_login(
        self, otp_code: str = "0000", expected_code: int = 200
    ):
        response = self.client.post(
            url=self.url,
            endpoint="/change-phone-on-login/confirm-verification",
            json=otp_code_payload(otp_code),
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def resend_init_hsm_for_change_phone_on_login(self, expected_code: int = 200):
        response = self.client.post(
            url=self.url, endpoint="/change-phone-on-login/high-security-mode/init/resend"
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def resend_phone_init_for_change_phone_on_login(
        self, phone_number: str, expected_code: int = 200
    ):
        response = self.client.post(
            url=self.url,
            endpoint="/change-phone-on-login/init-verification/resend",
            json=phone_verification_on_login_payload(phone_number),
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def init_hsm_for_change_phone_on_reset_password(
        self, personal_number: str, birth_date: str, expected_code: int = 200
    ):
        payload = init_sso_hsm_payload(personal_number=personal_number, birth_date=birth_date)
        response = self.client.post(
            url=self.url,
            endpoint="/change-phone-on-reset-password/high-security-mode/init/with-birthday",
            json=payload,
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def activate_hsm_for_change_phone_on_reset_password(
        self, absher_code: str, expected_code: int = 200
    ):
        payload = hsm_payload(absher_code=absher_code)
        response = self.client.post(
            url=self.url,
            endpoint="/change-phone-on-reset-password/high-security-mode/init",
            json=payload,
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def get_security_question_for_change_phone_on_reset_password(self, expected_code: int = 200):
        response = self.client.get(
            url=self.url, endpoint="/change-phone-on-reset-password/security-questions"
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def validate_security_answer_for_chane_phone_on_reset_password(self, expected_code: int = 200):
        payload = security_question_payload(
            first_answer="firs_answer", second_answer="second_answer"
        )
        response = self.client.post(
            url=self.url,
            endpoint="/change-phone-on-reset-password/security-questions/validate",
            json=payload,
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def verify_phone_number_on_reset_password(self, new_phone, expected_code: int = 200):
        payload = phone_verification_on_login_payload(new_phone)
        response = self.client.post(
            url=self.url,
            endpoint="/change-phone-on-reset-password/init-verification",
            json=payload,
        )
        assert_status_code(response.status_code).equals_to(expected_code)

    @allure.step
    def confirm_new_phone_verification_on_reset_password(
        self, otp_code: str = "0000", expected_code: int = 200
    ):
        payload = otp_code_payload(otp_code)
        response = self.client.post(
            url=self.url,
            endpoint="/change-phone-on-reset-password/confirm-verification",
            json=payload,
        )
        assert_status_code(response.status_code).equals_to(expected_code)
