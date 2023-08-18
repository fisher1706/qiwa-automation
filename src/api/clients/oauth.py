from requests import Response

import config
from src.api.http_client import HTTPClient


class OAuthApi:
    url = config.settings.api_url
    route = "/oauth"

    def __init__(self, client: HTTPClient):
        self.client = client

    def init(self) -> Response:
        payload = {"data": {"type": "oauth-init", "attributes": {"state": {}}}}
        return self.client.post(self.url, f"{self.route}/init", json=payload)

    def callback(self, state: str, auth_code: str) -> Response:
        payload = {
            "data": {"type": "oauth-callback", "attributes": {"state": state, "code": auth_code}}
        }
        return self.client.post(self.url, f"{self.route}/callback", json=payload)
