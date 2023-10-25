from http import HTTPStatus

from requests import Response

import config
from src.api.http_client import HTTPClient
from src.api.payloads.raw.user_management.payment import Payment
from utils.assertion import assert_status_code


class PaymentApi:
    url = config.qiwa_urls.payment

    def __init__(self, client: HTTPClient):
        self.client = client

    def post_create_payment(self, payment_id) -> Response:
        token = self.client.session.cookies.get("qiwa.authorization")
        headers = {"Authorization": token}
        response = self.client.post(
            url=self.url,
            endpoint="/api/dynamic-gateway/v1/payment/payment-method",
            headers=headers,
            json=Payment(transactionId=payment_id).dict(),
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response

    def post_confirm_payment(self, token, transaction_id):
        # TODO: change confirm payment to IBM endpoint
        headers = {"Authorization": token}
        response = self.client.post(
            url=self.url,
            endpoint=f"/api/dynamic-gateway/v1/transaction/sadad/{transaction_id}/paid",
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response
