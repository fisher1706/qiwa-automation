from http import HTTPStatus
from urllib.parse import urlparse, parse_qs

from requests import Response

import config
from src.api.http_client import HTTPClient
from src.api.payloads.sso_oauth_payloads import (
    oauth_callback_payload,
    oauth_init_payload,
)


class OAuthApi:
    url = config.settings.api_url
    route = "/oauth"

    def __init__(self, client: HTTPClient):
        self.client = client

    def init(self) -> dict:
        init = self.client.post(self.url, f"{self.route}/init", json=oauth_init_payload())
        assert init.status_code == HTTPStatus.OK
        redirect_uri = urlparse(init.json()["data"]["attributes"]["redirect-uri"])
        redirect_uri_query = parse_qs(redirect_uri.query)
        return redirect_uri_query

    def callback(self, state: str, auth_code: str) -> Response:
        response = self.client.post(
            self.url,
            f"{self.route}/callback",
            json=oauth_callback_payload(state=state, code=auth_code),
        )
        assert response.status_code == HTTPStatus.OK
        return response
