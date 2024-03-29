from datetime import date

from requests import Response

import config
from src.api.http_client import HTTPClient
from src.api.payloads.data import change_occupation
from src.api.payloads.raw.change_occupation import Laborer


class ChangeOccupationApi:
    url = f"{config.qiwa_urls.qiwa_change_occupation}/change-occupation"

    def __init__(self, client: HTTPClient):
        self.http = client

    def get_session(self, token: str) -> Response:
        return self.http.post(f"{self.url}/session", params={"ott-token": token})

    def get_requests_laborers(
        self,
        page: int = 1,
        per: int = 10,
        laborer_name: str = None,
        laborer_id: int = None,
        request_status: int = None,
        date_range: tuple[date, date] = None,
    ) -> Response:
        params = dict(
            page=page,
            per=per,
        )
        if laborer_name:
            params["q[laborer-name][eq]"] = laborer_name
        if laborer_id:
            params["q[laborer-id-no][eq]"] = laborer_id
        if request_status:
            params["q[status-list][eq][]"] = request_status
        if date_range:
            from_date, to_date = date_range
            (
                params["q[request-date-from][gte][y]"],
                params["q[request-date-from][gte][m]"],
                params["q[request-date-from][gte][d]"],
            ) = (from_date.year, from_date.month, from_date.day)
            (
                params["q[request-date-to][lte][y]"],
                params["q[request-date-to][lte][m]"],
                params["q[request-date-to][lte][d]"],
            ) = (to_date.year, to_date.month, to_date.day)
        return self.http.get(f"{self.url}/requests-laborers", params=params)

    def get_requests(
        self, page: int = 1, per: int = 10, employee_name: str = None, request_id: str = None
    ) -> Response:
        params = dict(
            page=page,
            per=per,
        )
        if employee_name:
            params["q[employee-name][eq]"] = employee_name
        if request_id:
            params["q[request-id][eq]"] = request_id
        return self.http.get(f"{self.url}/requests", params=params)

    def get_request_by_id(self, request_id: str) -> Response:
        return self.http.get(f"{self.url}/requests/{request_id}")

    def create_request(self, *laborers: Laborer) -> Response:
        payload = change_occupation(
            {
                "laborers": [laborer.dict(by_alias=True) for laborer in laborers],
            }
        )
        return self.http.post(f"{self.url}", json=payload)

    def cancel_request(self, request_number: str) -> Response:
        return self.http.put(f"{self.url}/cancel/{request_number}")

    def get_count(self) -> Response:
        return self.http.get(f"{self.url}/count")

    def get_users(self, page: int, per: int) -> Response:
        return self.http.get(f"{self.url}/users", params={"page": page, "per": per})

    def get_occupations(
        self, page: int, per: int, english_name: str = None, arabic_name: str = None
    ) -> Response:
        params = dict(
            page=page,
            per=per,
        )
        if english_name:
            params["q[english-name][match_phrase]"] = english_name
        if arabic_name:
            params["q[arabic-name][match_phrase]"] = arabic_name
        return self.http.get(f"{self.url}/occupations", params=params)

    def get_context(self) -> Response:
        return self.http.get(f"{self.url}/context")

    def validate_establishment(self) -> Response:
        return self.http.post(f"{self.url}/establishment/validate")

    def validate_laborer(self, personal_number: str | int, occupation_code: str | int) -> Response:
        payload = change_occupation(
            {"personal-number": personal_number, "occupation-code": occupation_code}
        )
        return self.http.post(f"{self.url}/validate", json=payload)
