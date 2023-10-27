from __future__ import annotations

from http import HTTPStatus
from urllib import parse

import config
from src.api.http_client import HTTPClient
from src.api.payloads.raw.user_management.edit_privileges import Privileges
from src.api.payloads.raw.user_management.self_flows import SelfSubscription
from src.api.payloads.user_management import owner_subscription_payload
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
        subscription_price: str,
        subscription_type: str,
    ) -> str:
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
        subscription_price: str,
        subscribed_user_personal_number: str,
        labor_office_id: str,
        sequence_number: str,
        privilege_ids: list,
    ) -> str:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.post(
            url=self.url,
            endpoint=f"/api/bff/subscriptions/owner/{subscription_type}",
            headers=headers,
            json=owner_subscription_payload(
                subscription_price,
                subscribed_user_personal_number,
                labor_office_id,
                sequence_number,
                privilege_ids,
            ),
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        payment_url = response.json()["paymentUrl"]
        parsed_url = parse.urlparse(payment_url).path
        payment_id = parsed_url.strip("/").split("/")[0]
        return payment_id

    def get_user_privileges(self, cookie: dict, users_personal_number: str) -> list:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.get(
            url=self.url,
            endpoint=f"/api/bff/users/{users_personal_number}/establishments/privileges",
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        list_of_privileges = response.json()[0]["privilegeIds"]
        return list_of_privileges

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
