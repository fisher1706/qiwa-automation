from http import HTTPStatus
from typing import Literal
from urllib import parse

import allure
from requests import Response

import config
from utils.assertion import assert_status_code
from src.api.http_client import HTTPClient
from src.api.models.qiwa.raw.token import AuthorizationToken


class ChangeOccupationApi:
    url = config.settings.qiwa_change_occupation_url
    route = "/change-occupation"

    def __init__(self, client: HTTPClient, token: AuthorizationToken):
        self.client = client
        self.auth_token = token

    def _get_ott_token(self) -> str:
        payload = {
            "labor-office-id": self.auth_token.company_labor_office_id,
            "sequence-number": self.auth_token.company_sequence_number,
            "personal-number": self.auth_token.user_personal_number,
            "service-code": "change_occupation",
            "platform-id": 1,
            "channel-id": "Qiwa",
            "language": "en",
        }
        response = self.client.post(self.url, f"{self.route}/ott-token", json=payload)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        redirect_url = response.json()["redirect_url"]
        parsed_url = parse.parse_qs(parse.urlparse(redirect_url).query)
        ott_token = parsed_url.get("ott-token")[0]
        return ott_token

    @allure.step
    def pass_ott_authorization(self) -> dict:
        ott_token = self._get_ott_token()
        response = self.client.post(self.url, f"{self.route}/session?ott-token={ott_token}")
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()

    @allure.step
    def get_change_occupation_requests(
        self, page: int = 1, per: int = 10, sort: Literal["DESC", "ESC"] = "DESC", **kwargs
    ) -> Response:
        params = {"page": page, "per": per, "sort": sort, **kwargs}
        return self.client.get(self.url, f"{self.route}/requests", params=params)

    @allure.step
    def get_change_occupation_request_by_id(self, request_id: str) -> Response:
        return self.client.get(self.url, f"{self.route}/requests/{request_id}")

    @allure.step
    def create_change_occupation_request(self, payload) -> Response:
        return self.client.post(self.url, self.route, json=payload)
