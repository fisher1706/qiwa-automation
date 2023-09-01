from requests import Response

import config
from src.api.http_client import HTTPClient


class OttServiceApi:
    url = config.qiwa_urls.qiwa_ott_service
    route = "/ott-service"

    def __init__(self):
        self.client = HTTPClient()

    def generate_token(self, data: dict) -> Response:
        return self.client.post(self.url, f"{self.route}/generate", json=data)

    def validate_token(self, token: dict) -> Response:
        return self.client.post(self.url, f"{self.route}/validate", json=token)
