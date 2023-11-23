from requests import Response

import config
from src.api.http_client import HTTPClient


class OttServiceApi:
    url = config.qiwa_urls.qiwa_ott_service
    route = "/ott-service"

    def __init__(self):
        self.client = HTTPClient()

    def generate_token(
        self, sequence_number: int | str, labor_office_id: int | str = None
    ) -> Response:
        payload = {"sequence-number": sequence_number}
        if labor_office_id:
            payload["labor-office-id"] = labor_office_id
        return self.client.post(self.url, f"{self.route}/generate", json=payload)

    def validate_token(self, token: int | str) -> Response:
        return self.client.post(self.url, f"{self.route}/validate", json={"ott": token})
