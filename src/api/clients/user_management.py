from http import HTTPStatus
from urllib import parse

from requests import Response

import config
from src.api.http_client import HTTPClient
from src.api.payloads.raw.user_management.self_flows import SelfSubscription
from utils.assertion import assert_status_code
from utils.crypto_manager import code_um_cookie


class UserManagementApi:  # pylint: disable=duplicate-code
    url = config.qiwa_urls.api_user_management

    def __init__(self, client: HTTPClient):
        self.client = client

    def get_self_subscription_price(self, cookie, labor_office_id, sequence_number) -> str:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.get(
            url=self.url,
            endpoint=f"/api/bff/subscriptions/self/price?laborOfficeId={labor_office_id}"
            f"&sequenceNumber={sequence_number}",
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        self_subsc_price = str(response.json()["totalFeeAmount"])
        return self_subsc_price

    def get_thank_you_page(self, cookie, transaction_id) -> Response:
        coded_cookie = code_um_cookie(cookie)
        headers = {"Cookie": f"qiwa.authorization={coded_cookie}"}
        return self.client.get(
            url=self.url,
            endpoint=f"/api/bff/subscriptions/payments/{transaction_id}/thank-you-page",
            headers=headers,
        )

    def post_self_flow(
        self, cookie, labor_office_id, sequence_number, subscription_price, subscr_type
    ) -> bytes:
        headers = {"Cookie": f"qiwa.authorization={code_um_cookie(cookie)}"}
        response = self.client.post(
            url=self.url,
            endpoint=f"/api/bff/subscriptions/self/{subscr_type}?laborOfficeId={labor_office_id}"
            f"&sequenceNumber={sequence_number}",
            headers=headers,
            json=SelfSubscription(totalFeeAmount=subscription_price).dict(),
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        payment_url = response.json()["paymentUrl"]
        parsed_url = parse.urlparse(payment_url).path
        payment_id = parsed_url.strip("/").split("/")[0]
        return payment_id
