from __future__ import annotations

import allure

import config
from src.api.http_client import HTTPClient
from src.api.payloads.sso.nafath_payloads import init_nafath_logit, nafath_callback
from utils.assertion import assert_status_code


class NafathApiSSO:
    url = config.qiwa_urls.sso_api

    def __init__(self, client=HTTPClient()):
        self.client = client

    @allure.step
    def init_nafath_login(
        self,
        personal_number: str,
        expected_code: int = 200,
    ) -> NafathApiSSO:
        payload = init_nafath_logit(personal_number)
        response = self.client.post(url=self.url, endpoint="/nafath/init-login", json=payload)
        assert_status_code(response.status_code).equals_to(expected_code)
        transaction_id = response.json()["data"]["attributes"]["transaction-id"]
        return transaction_id

    def nafath_callback(self, trans_id: str, status: str = "COMPLETED", expected_code: int = 200):
        payload = nafath_callback(trans_id=trans_id, status=status)
        response = self.client.post(url=self.url, endpoint="/nafath/callback", json=payload)
        assert_status_code(response.status_code).equals_to(expected_code)

    def nafath_authorize_login(self, expected_code: int = 200):
        response = self.client.post(url=self.url, endpoint="/nafath/authorize-login")
        assert_status_code(response.status_code).equals_to(expected_code)
