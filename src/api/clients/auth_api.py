from __future__ import annotations

import asyncio
from urllib.parse import parse_qs, urlparse

import aiohttp
import allure
from requests import Response

import config
from src.api.assertions.response_validator import ResponseValidator
from src.api.http_client import HTTPClient
from src.api.models.account import Account
from src.api.payloads import Data, Root
from src.api.payloads.raw.auth import (
    Auth,
    ConfirmationToken,
    CreateAccount,
    Hsm,
    RestorePassword,
    VerifyPhone,
)


class AuthApi:
    url = config.settings.api_url

    def __init__(self, api=HTTPClient()):
        self.api = api
        self.restore_password_route = "/985c-4905db0216da/67661da2-6f1f"
        self.error_msg = None
        self.account_id = None
        self.nafath_transaction_id = None
        self.nafath_random_number = None

    @allure.step
    def login(
        self,
        login: str,
        password: str = None,
        expect_code: int = 200,
        expect_schema: str = "context-login.json",
    ) -> AuthApi:
        auth_payload = Root(
            data=Data(type="login", attributes=Auth(login=login, password=password))
        )
        response = self.api.post(
            url=self.url, endpoint="/context", json=auth_payload.dict(exclude_none=True)
        )
        validator = ResponseValidator(response)
        validator.check_status_code(name="Login", expect_code=expect_code)
        if expect_code == 200:
            validator.check_response_schema(schema_name=expect_schema)
        return self

    @allure.step
    def two_factor_auth(
        self,
        login: str,
        password: str = None,
        otp_code: str | int = "0000",
        expect_code: int = 201,
        expect_schema: str = "identities.json",
    ) -> AuthApi:
        auth_payload = Root(
            data=Data(
                type="login", attributes=Auth(login=login, password=password, otp_code=otp_code)
            )
        )
        response = self.api.post(url=self.url, endpoint="/context", json=auth_payload.dict())
        validator = ResponseValidator(response)
        validator.check_status_code(name="Two factor auth", expect_code=expect_code)
        if expect_code == 201:
            self.account_id = response.json()["data"]["id"]
        validator.check_response_schema(schema_name=expect_schema)
        return self

    @allure.step
    def logout_user(self, expect_code: int = 200) -> AuthApi:
        response = self.api.delete(url=self.url, endpoint="/context")
        ResponseValidator(response).check_status_code(name="Logout", expect_code=expect_code)
        return self

    @allure.step
    def get_context(self, expect_code: int = 200) -> ResponseValidator:
        response = self.api.get(url=self.url, endpoint="/context")
        ResponseValidator(response).check_status_code(name="GET context", expect_code=expect_code)
        return response.json()

    @allure.step
    def init_hsm_with_birthday(
        self,
        personal_number: str,
        year: str = "1421",
        month: str = "01",
        day: str = "01",
        expect_code: int = 200,
    ) -> AuthApi:
        init_hsm_payload = Root(
            data=Data(
                type="hsm",
                attributes=Hsm(personal_number=personal_number, year=year, month=month, day=day),
            )
        )
        if personal_number.startswith("1"):
            response = self.api.post(
                url=self.url,
                endpoint="/session/high-security-mode/init/with-birthday",
                json=init_hsm_payload.dict(by_alias=True, exclude_none=True),
            )
        else:
            response = self.api.post(
                url=self.url,
                endpoint="/session/high-security-mode/init",
                json=init_hsm_payload.dict(by_alias=True),
            )
        ResponseValidator(response).check_status_code(name="Init HSM", expect_code=expect_code)
        return self

    @allure.step
    async def async_init_hsm(self, personal_number: str, token: str) -> None:
        init_hsm_payload = Root(
            data=Data(type="hsm", attributes=Hsm(personal_number=personal_number))
        )
        headers = {"HTTP_AUTHORIZATION": token}
        cookies = {"qiwa.authorization": f"{token}"}
        async with aiohttp.ClientSession(headers=headers, cookies=cookies) as session:
            response = await session.post(
                url=f"{self.url}/session/high-security-mode/init",
                json=init_hsm_payload.dict(by_alias=True, exclude_none=True),
            )
        for headers, (key, value) in enumerate(response.raw_headers):
            if str(key).strip("b'") == "HTTP_AUTHORIZATION":
                assert str(value).strip("b'") == token
        assert response.status in (200, 422)

    async def run_parallel_to_init_hsm(self, request_data: list) -> asyncio:
        tasks = []
        for data in request_data:
            for personal_id, auth_token in data.items():
                tasks.append(self.async_init_hsm(personal_number=personal_id, token=auth_token))
        return await asyncio.gather(*tasks, return_exceptions=True)

    @allure.step
    def phone_verification(
        self, phone: str, locale: str = "en", personal_number: str = None, expect_code=200
    ):
        verify_phone_payload = VerifyPhone(
            phone_number="966" + phone, locale=locale, personal_number=personal_number
        )
        response = self.api.post(
            url=self.url,
            endpoint="/session/phone/verification",
            json=verify_phone_payload.dict(by_alias=True, exclude_none=True),
        )
        ResponseValidator(response).check_status_code(
            name="Phone verification", expect_code=expect_code
        )
        return self

    @allure.step
    def enable_hsm(
        self,
        personal_number: str,
        expect_code: int = 200,
        sms_code: str = "000000",
        expect_schema: str = "hsm-enable.json",
    ) -> AuthApi:
        enable_hsm_payload = Root(
            data=Data(
                type="hsm", attributes=Hsm(sms_code=sms_code, personal_number=personal_number)
            )
        )
        response = self.api.post(
            url=self.url,
            endpoint="/session/high-security-mode",
            json=enable_hsm_payload.dict(by_alias=True, exclude_none=True),
        )
        (
            ResponseValidator(response)
            .check_status_code(name="Enable HSM", expect_code=expect_code)
            .check_response_schema(schema_name=expect_schema)
        )
        return self

    @allure.step
    def disable_hsm_session(self, expect_code: int = 200) -> AuthApi:
        response = self.api.delete(url=self.url, endpoint="/session/high-security-mode/disable")
        ResponseValidator(response).check_status_code(name="Disable HSM", expect_code=expect_code)
        return self

    @allure.step
    def create_account(
        self, account: Account, expect_code: int = 201, expect_schema: str = "identities.json"
    ) -> AuthApi:
        create_account_payload = Root(
            data=Data(
                type="user-account",
                attributes=CreateAccount(
                    personal_number=account.personal_number,
                    email=account.email,
                    password=account.password,
                    confirmation_code=account.confirmation_code,
                    password_confirmation=account.password,
                    phone_number=account.phone_number,
                ),
            )
        )
        response = self.api.post(
            url=self.url,
            endpoint="/identities",
            json=create_account_payload.dict(by_alias=True),
        )
        ResponseValidator(response).check_status_code(
            name=f"Create Account {account.personal_number}", expect_code=expect_code
        ).check_response_schema(schema_name=expect_schema)
        return self

    @allure.step
    def get_workspaces(self) -> Response:
        response = self.api.get(url=self.url, endpoint="/context/workspaces")
        validator = ResponseValidator(response)
        validator.check_status_code(name="Workspaces list", expect_code=200)
        return response

    @allure.step
    def get_list_of_companies_status(self, company_list: list[dict], status: str) -> list:
        status_list: list[str] = []
        for company in company_list:
            if company["attributes"]["status"] == status and company["attributes"][
                "space-type"
            ] in ("pending-for-approval-company", "company"):
                status_list.append(company["attributes"]["status"])
        return status_list

    @allure.step
    def compare_company_status(
        self, status_for_comparison: list, company_list: list[dict]
    ) -> None:
        status_list = []
        for company in company_list:
            status_list.append(company["attributes"]["status"])
        assert set(status_for_comparison) == set(status_list), (
            f"Companies status {set(status_for_comparison)}" f" is not equal to {set(status_list)}"
        )

    @allure.step
    def select_company_by_id(self, company_id, status_code=200):
        response = self.api.patch(url=self.url, endpoint=f"/context/company/{company_id}")
        ResponseValidator(response).check_status_code(
            name="Select Company by id", expect_code=status_code
        )
        if status_code == 403:
            self.error_msg = response.json()["title"]

    @allure.step
    def post_confirm_email(self, email_token: str, expected_code=None) -> AuthApi:
        email_confirm_payload = Root(
            data=Data(type="email", attributes=ConfirmationToken(confirmation_token=email_token))
        )
        response = self.api.post(
            url=self.url,
            endpoint="/context/user/emails/confirm",
            json=email_confirm_payload.dict(),
        )
        if expected_code:
            ResponseValidator(response).check_status_code(
                name="Confirm email", expect_code=expected_code
            )
        return self

    @allure.step
    def unlock_through_absher(self):
        response = self.api.post(url=self.url, endpoint="/identity/hsm-unlock")
        ResponseValidator(response).check_status_code(
            name="Unlock through absher", expect_code=200
        )

    @allure.step
    def init_restore_password(self, personal_number: str | int, expect_code: int = 200) -> str:
        init_restore_payload = Root(
            data=Data(
                type="restore-password",
                attributes=RestorePassword(personal_number=personal_number),
            )
        )
        response = self.api.post(
            url=self.url,
            endpoint=f"{self.restore_password_route}/00eb7e42-ae56-4897-b801",
            json=init_restore_payload.dict(by_alias=True, exclude_none=True),
        )
        ResponseValidator(response).check_status_code(
            name="Init restore password request", expect_code=expect_code
        )
        parsed_url = urlparse(response.json()["url"])
        return parse_qs(parsed_url.query)["token"][0]

    @allure.step
    def init_restore_password_token(self, token: str, expect_code: int = 200) -> str | None:
        init_restore_token_payload = Root(
            data=Data(type="restore-password", attributes=RestorePassword(token=token))
        )
        response = self.api.post(
            url=self.url,
            endpoint=f"{self.restore_password_route}/40d59a13-accb-4d37-914d",
            json=init_restore_token_payload.dict(by_alias=True, exclude_none=True),
        )
        ResponseValidator(response).check_status_code(
            name="Init restore password token", expect_code=expect_code
        )
        if expect_code == 200:
            return response.json()["personal-number"]
        return None

    @allure.step
    def init_hsm_for_restore_password(
        self, personal_number: str | int, expect_code: int = 200
    ) -> None:
        init_hsm = Root(data=Data(type="hsm", attributes=Hsm(personal_number=personal_number)))
        response = self.api.post(
            url=self.url,
            endpoint=f"{self.restore_password_route}/87e44873-8efa-44e7-94cd",
            json=init_hsm.dict(by_alias=True, exclude_none=True),
        )
        ResponseValidator(response).check_status_code(
            name="Init hsm for restore password", expect_code=expect_code
        )

    @allure.step
    def verify_absher_for_restore_password(
        self, absher_code: str | int = "000000", expect_code: int = 200
    ) -> None:
        verify_absher = Root(data=Data(type="hsm", attributes=Hsm(sms_code=absher_code)))
        response = self.api.post(
            url=self.url,
            endpoint=f"{self.restore_password_route}/d9ce666c-305b-4194-8509",
            json=verify_absher.dict(by_alias=True, exclude_none=True),
        )
        ResponseValidator(response).check_status_code(
            name="Verify absher", expect_code=expect_code
        )

    @allure.step
    def restore_password(self, new_password: str, expect_code: int = 200) -> None:
        restore_pass_payload = Root(
            data=Data(
                type="passwords",
                attributes=RestorePassword(
                    new_password=new_password, new_password_confirmation=new_password
                ),
            )
        )
        response = self.api.post(
            url=self.url,
            endpoint=f"{self.restore_password_route}/11d107bb-da14-422a-8e9f",
            json=restore_pass_payload.dict(by_alias=True, exclude_none=True),
        )
        ResponseValidator(response).check_status_code(
            name="Restore password init", expect_code=expect_code
        )

    @allure.step
    def sms_confirm(self, sms_code, expect_code=200):
        response = self.api.patch(url=self.url, endpoint=f"/identity/unlock/{sms_code}")
        ResponseValidator(response).check_status_code(
            name="Unlock account", expect_code=expect_code
        )

    @allure.step
    def unlock_account_via_email(self, unlock_token: str, expect_code: int = 200) -> None:
        response = self.api.post(url=self.url, endpoint=f"/identity/unlock/{unlock_token}")
        ResponseValidator(response).check_status_code(
            name="Unlock account", expect_code=expect_code
        )

    @allure.step
    def change_locale(
        self, locale: str, expect_code: int = 200, expect_schema: int = "identities.json"
    ) -> None:
        response = self.api.post(url=self.url, endpoint=f"/session/language/{locale}")
        validator = ResponseValidator(response)
        validator.check_status_code(name="Change locale", expect_code=expect_code)
        if expect_code == 200:
            validator.check_response_schema(schema_name=expect_schema)

    @allure.step
    def nafath_init(self, personal_number: str | int, expect_code: int = 200) -> None:
        nafath_init = Root(
            data=Data(type="login", attributes=Hsm(personal_number=personal_number))
        )
        response = self.api.post(
            url=self.url,
            endpoint="/context/nafath-init",
            json=nafath_init.dict(by_alias=True, exclude_none=True),
        )
        ResponseValidator(response).check_status_code(name="Login", expect_code=expect_code)
        json = response.json()
        if expect_code == 200:
            self.nafath_transaction_id = json["data"]["attributes"]["transaction-id"]
            self.nafath_random_number = json["data"]["attributes"]["random"]

    @allure.step
    def nafath_authorize(self, expect_code: int = 200) -> None:
        response = self.api.post(url=self.url, endpoint="/context/nafath-authorize")
        ResponseValidator(response).check_status_code(name="Login", expect_code=expect_code)
