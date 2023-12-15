from http import HTTPStatus
from urllib.parse import parse_qs, urlparse

from requests import Response
from requests.cookies import RequestsCookieJar

import config
from src.api.http_client import HTTPClient
from src.api.payloads.sso_oauth_payloads import (
    oauth_callback_payload,
    oauth_init_payload,
)
from utils.assertion import assert_status_code


class OAuthApi:
    url = config.qiwa_urls.api
    route = "/oauth"

    def __init__(self, client: HTTPClient):
        self.client = client

    def init(self) -> dict:
        init = self.client.post(self.url, f"{self.route}/init", json=oauth_init_payload())
        assert_status_code(init.status_code).equals_to(HTTPStatus.OK)
        redirect_uri = urlparse(init.json()["data"]["attributes"]["redirect-uri"])
        redirect_uri_query = parse_qs(redirect_uri.query)
        return redirect_uri_query

    def callback(self, state: str, auth_code: str) -> Response:
        response = self.client.post(
            self.url,
            f"{self.route}/callback",
            json=oauth_callback_payload(state=state, code=auth_code),
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response

    def get_context(self) -> RequestsCookieJar:
        response = self.client.get(
            url=self.url,
            endpoint="/context",
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.cookies

    def get_user_data(self) -> tuple:
        response = self.client.get(
            url=self.url,
            endpoint="/context/user",
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        notification_email = response.json()["data"]["attributes"]["notification-email"]
        notification_phone = response.json()["data"]["attributes"]["notification-phone"]
        return notification_email, notification_phone

    def delete_context(self):
        self.client.get(self.url, endpoint="/context")
        delete_context = self.client.delete(
            self.url, endpoint="/context", headers={"Origin": f"{self.url}"}
        )
        assert_status_code(delete_context.status_code).equals_to(HTTPStatus.OK)

    def init_logout(self):
        init = self.client.post(self.url, f"{self.route}/init", json=oauth_init_payload())
        assert_status_code(init.status_code).equals_to(HTTPStatus.OK)
        logout_token = urlparse(init.json()["data"]["attributes"]["redirect-uri"])
        logout_token = parse_qs(logout_token.query)["logout_token"][0]
        return logout_token
