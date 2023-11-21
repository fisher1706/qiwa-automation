from __future__ import annotations

from http import HTTPStatus
from urllib import parse

import allure

import config
from src.api.http_client import HTTPClient
from src.api.payloads.raw.user_management.edit_privileges import Privileges
from src.api.payloads.raw.user_management.self_flows import SelfSubscription
from src.api.payloads.user_management import (
    owner_subscription_payload,
    owner_subscription_payload_for_new_subscription_type,
)
from utils.assertion import assert_status_code
from utils.crypto_manager import code_um_cookie


class UserManagementApi:  # pylint: disable=duplicate-code
    url = config.qiwa_urls.api_user_management

    def __init__(self, client: HTTPClient):
        self.client = client

    def get_self_subscription_price(
        self, cookie: dict, labor_office_id: str, sequence_number: str
    ) -> str:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.get(
            url=self.url,
            endpoint="/api/bff/subscriptions/self/price",
            params={"laborOfficeId": labor_office_id, "sequenceNumber": sequence_number},
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        self_subscription_price = str(response.json()["totalFeeAmount"])
        return self_subscription_price

    def get_owner_subscription_price(
        self, cookie: dict, subscribed_user_personal_number: str
    ) -> str:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.get(
            url=self.url,
            endpoint="/api/bff/subscriptions/price",
            params={"idno": subscribed_user_personal_number},
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        owner_subscription_price = str(response.json()["totalFeeAmount"])
        return owner_subscription_price

    def get_subscription_price_number_of_users(self, cookie: dict, id_no: str = 555) -> float:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.get(
            url=self.url,
            endpoint="/api/bff/subscriptions/price",
            params={"idno": id_no},
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json().get("totalFeeAmount")

    def get_thank_you_page(self, cookie: dict, transaction_id: int) -> UserManagementApi:
        coded_cookie = code_um_cookie(cookie)
        headers = {"Cookie": f"qiwa.authorization={coded_cookie}"}
        response = self.client.get(
            url=self.url,
            endpoint=f"/api/bff/subscriptions/payments/{transaction_id}/thank-you-page",
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return self

    def post_self_flow(
        self,
        cookie: dict,
        labor_office_id: str,
        sequence_number: str,
        subscription_price: float,
        subscription_type: str,
    ) -> bytes:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.post(
            url=self.url,
            endpoint=f"/api/bff/subscriptions/self/{subscription_type}",
            params={"laborOfficeId": labor_office_id, "sequenceNumber": sequence_number},
            headers=headers,
            json=SelfSubscription(totalFeeAmount=subscription_price).dict(),
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        payment_url = response.json()["paymentUrl"]
        parsed_url = parse.urlparse(payment_url).path
        payment_id = parsed_url.strip("/").split("/")[0]
        return payment_id

    def post_owner_subscription_flow(
        self,
        cookie: dict,
        subscription_type: str,
        subscription_price: float,
        subscribed_user_personal_number: str,
        labor_office_id: str,
        sequence_number: str,
        privilege_ids: list,
    ) -> bytes:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        if subscription_type == "new":
            json = owner_subscription_payload_for_new_subscription_type(
                subscription_price,
                subscribed_user_personal_number,
                labor_office_id,
                sequence_number,
                privilege_ids,
            )
        else:
            json = owner_subscription_payload(
                subscription_price,
                subscribed_user_personal_number,
                labor_office_id,
                sequence_number,
                privilege_ids,
            )
        response = self.client.post(
            url=self.url,
            endpoint=f"/api/bff/subscriptions/owner/{subscription_type}",
            headers=headers,
            json=json,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        payment_url = response.json()["paymentUrl"]
        parsed_url = parse.urlparse(payment_url).path
        payment_id = parsed_url.strip("/").split("/")[0]
        return payment_id

    @allure.step
    def get_user_privileges(self, cookie: dict, users_personal_number: str) -> dict:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.get(
            url=self.url,
            endpoint=f"/api/bff/users/{users_personal_number}/establishments/privileges",
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()[0]

    def post_update_privileges(
        self,
        cookie: dict,
        users_personal_number: str,
        labor_office_id: str,
        sequence_number: str,
        privileges: list,
    ) -> UserManagementApi:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.post(
            url=self.url,
            endpoint=f"/api/bff/users/{users_personal_number}/establishments/privileges",
            headers=headers,
            json=Privileges(
                laborOfficeId=labor_office_id,
                sequenceNumber=sequence_number,
                privilegeIds=privileges,
            ).dict(),
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return self

    def get_user_subscription_info(self, cookie: dict) -> int:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.get(
            url=self.url,
            endpoint="/api/bff/users/user-subscription-info",
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        expired_date = response.json()["subscription"]["expireAt"]
        return expired_date

    def cron_job_for_expiry_subscription(self) -> UserManagementApi:
        headers = {"Authorization": "Bearer 18353afa-2144-437e-89d5-458d788c6549"}
        self.client.post(
            url=self.url,
            endpoint="/api/private/trigger-expire-job",
            headers=headers,
        )
        return self

    @allure.step
    def post_subscribe_user_to_establishment(
        self,
        cookie: dict,
        users_personal_number: str,
        labor_office_id: str,
        sequence_number: str,
        privileges: list,
    ) -> UserManagementApi:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.post(
            url=self.url,
            endpoint=f"/api/bff/users/{users_personal_number}/establishments",
            headers=headers,
            json=Privileges(
                laborOfficeId=labor_office_id,
                sequenceNumber=sequence_number,
                privilegeIds=privileges,
            ).dict(),
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return self

    @allure.step
    def patch_remove_establishment_from_user(
        self,
        cookie: dict,
        users_personal_number: str,
        labor_office_id: str,
        sequence_number: str,
    ) -> UserManagementApi:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.patch(
            url=self.url,
            endpoint=f"/api/bff/users/{users_personal_number}/establishments",
            headers=headers,
            json=[
                Privileges(
                    laborOfficeId=labor_office_id,
                    sequenceNumber=sequence_number,
                ).dict(exclude={"privilegeIds"})
            ],
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return self

    def get_user_subscribed_establishments(
        self,
        cookie: dict,
        users_personal_number: str,
        subscribed_state: bool,
    ) -> list:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.get(
            url=self.url,
            endpoint=f"/api/bff/users/{users_personal_number}/establishments?active={subscribed_state}",
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()["content"]

    def patch_terminate_subscription(
        self,
        cookie: dict,
        users_personal_number: str,
    ):
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.patch(
            url=self.url,
            endpoint=f"/api/bff/subscriptions/{users_personal_number}",
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
