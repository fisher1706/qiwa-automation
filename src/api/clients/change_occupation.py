from requests import Response

import config
from src.api.http_client import HTTPClient
from src.api.payloads.data import change_occupation
from src.api.payloads.raw.change_occupation import Laborer


class ChangeOccupationApi:
    url = f"{config.qiwa_urls.qiwa_change_occupation}/change-occupation"

    def __init__(self, client: HTTPClient):
        self.http = client

    def get_ott_token(
        self, labor_office_id: str, sequence_number: str, personal_number: str
    ) -> Response:
        payload = {
            "labor-office-id": labor_office_id,
            "sequence-number": sequence_number,
            "personal-number": personal_number,
            "service-code": "change_occupation",
            "platform-id": 1,
            "channel-id": "Qiwa",
            "language": "en",
        }
        return self.http.post(f"{self.url}/ott-token", json=payload)

    def get_session(self, token: str) -> Response:
        return self.http.post(f"{self.url}/session", params={"ott-token": token})

    def get_requests_laborers(
        self, page: int, per: int, laborer_name: str = None, laborer_id: int = None
    ) -> Response:
        params = dict(
            page=page,
            per=per,
        )
        if laborer_name:
            params["q[laborer-name][eq]"] = laborer_name
        if laborer_id:
            params["q[laborer-id-no][eq]"] = laborer_id
        return self.http.get(f"{self.url}/requests-laborers", params=params)

    def get_requests(self, page: int, per: int) -> Response:
        return self.http.get(f"{self.url}/requests", params={"page": page, "per": per})

    def get_request(self, request_id: int) -> Response:
        return self.http.get(f"{self.url}/requests/{request_id}")

    def create_request(
        self, labor_office_id: str, sequence_number: str, *laborers: Laborer
    ) -> Response:
        payload = change_occupation(
            {
                "labor-office-id": labor_office_id,
                "sequence-number": sequence_number,
                "laborers": [laborer.dict(by_alias=True) for laborer in laborers],
            }
        )
        return self.http.post(f"{self.url}", json=payload)

    def cancel_request(self, request_id: int) -> Response:
        return self.http.put(f"{self.url}/cancel/{request_id}")

    def get_count(self) -> Response:
        return self.http.get(f"{self.url}/count")

    def get_users(self, page: int, per: int) -> Response:
        return self.http.get(f"{self.url}/users", params={"page": page, "per": per})

    def get_occupations(self, page: int, per: int) -> Response:
        return self.http.get(f"{self.url}/occupations", params={"page": page, "per": per})

    def get_context(self) -> Response:
        return self.http.get(f"{self.url}/context")

    def validate_establishment(self) -> Response:
        return self.http.get(f"{self.url}/establishment/validate")

    def validate_laborer(self, personal_number: str, occupation_code: str) -> Response:
        payload = change_occupation(
            {"personal-number": personal_number, "occupation-code": occupation_code}
        )
        return self.http.post(f"{self.url}/validate", json=payload)
