from requests import Response

import config
from src.api.http_client import HTTPClient


class ChangeOccupationApi:
    url = config.qiwa_urls.qiwa_change_occupation
    route = "/change-occupation"

    def __init__(self, client: HTTPClient):
        self.client = client

    def get_ott_token(self, payload) -> Response:
        return self.client.post(f"{self.url}{self.route}/ott-token", json=payload)

    def get_session(self, token: str) -> Response:
        return self.client.post(f"{self.url}{self.route}/session", params={"ott-token": token})

    def get_requests_laborers(self, page: int = 1, per: int = 10) -> Response:
        return self.client.get(
            f"{self.url}{self.route}/requests-laborers", params={"page": page, "per": per}
        )
