from requests import Response

import config
from src.api.http_client import HTTPClient


class ChangeOccupationApi:
    url = f"{config.qiwa_urls.qiwa_change_occupation}/change-occupation"

    def __init__(self, client: HTTPClient):
        self.client = client

    def get_ott_token(self, payload) -> Response:
        return self.client.post(f"{self.url}/ott-token", json=payload)

    def get_session(self, token: str) -> Response:
        return self.client.post(f"{self.url}/session", params={"ott-token": token})

    def get_requests_laborers(self, page: int = 1, per: int = 10) -> Response:
        return self.client.get(f"{self.url}/requests-laborers", params={"page": page, "per": per})

    def get_requests(self, page: int = 1, per: int = 10) -> Response:
        return self.client.get(f"{self.url}/requests", params={"page": page, "per": per})

    def get_count(self) -> Response:
        return self.client.get(f"{self.url}/count")
