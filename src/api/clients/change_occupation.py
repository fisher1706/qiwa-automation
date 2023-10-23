from requests import Response

import config
from src.api.http_client import HTTPClient
from src.api.payloads.data import change_occupation
from src.api.payloads.raw.change_occupation import Laborer


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

    def get_request(self, request_id: int) -> Response:
        return self.client.get(f"{self.url}/requests/{request_id}")

    def create_request(self, labor_office_id: str, sequence_number: str, *laborers: Laborer) -> Response:
        payload = change_occupation(
            {
                "labor-office-id": labor_office_id,
                "sequence-number": sequence_number,
                "laborers": [*laborers]
            }
        )
        return self.client.post(f"{self.url}", json=payload)

    def cancel_request(self, request_id: int) -> Response:
        return self.client.put(f"{self.url}/cancel/{request_id}")

    def get_count(self) -> Response:
        return self.client.get(f"{self.url}/count")

    def get_users(self, page: int = 1, per: int = 10) -> Response:
        return self.client.get(f"{self.url}/users", params={"page": page, "per": per})

    def get_occupations(self, page: int = 1, per: int = 10) -> Response:
        return self.client.get(f"{self.url}/occupations", params={"page": page, "per": per})

    def get_context(self) -> Response:
        return self.client.get(f"{self.url}/context")

    def validate_establishment(self) -> Response:
        return self.client.get(f"{self.url}/establishment/validate")
