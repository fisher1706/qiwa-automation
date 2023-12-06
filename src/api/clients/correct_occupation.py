from datetime import date

from requests import Response

import config
from src.api.http_client import HTTPClient
from src.api.payloads.data import data


class CorrectOccupationApi:
    url = f"{config.qiwa_urls.api}/correct-occupation-proxy"

    def __init__(self, client: HTTPClient):
        self.http = client

    def create_request(
        self, laborer_id: str, laborer_name: str, current_id: str, new_id: str
    ) -> Response:
        payload = data(
            "correct_occupation",
            {
                "laborer_id": laborer_id,
                "laborer_name": laborer_name,
                "current_occupation_id": current_id,
                "new_occupation_id": new_id,
            },
        )
        return self.http.post(f"{self.url}/correct-occupations", json=payload)

    def get_laborers(
        self,
        page: int = 1,
        per: int = 10,
        laborer_name: str = None,
        laborer_id: str = None,
        occupation_id: int = None,
        nationality_id: int = None,
    ) -> Response:
        params = dict(
            page=page,
            per=per,
        )
        if laborer_name:
            params["q[laborer-name][eq]"] = laborer_name
        if laborer_id:
            params["q[laborer-id][eq]"] = laborer_id
        if occupation_id:
            params["q[current-occupation-id][eq]"] = occupation_id
        if nationality_id:
            params["q[nationality-id][eq]"] = nationality_id
        return self.http.get(f"{self.url}/laborers", params=params)

    def get_requests(
        self,
        page: int,
        per: int,
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
            params["q[employee-name][eq]"] = laborer_name
        if laborer_id:
            params["q[laborer-id][eq]"] = laborer_id
        if request_status is not None:
            params["q[request-status][eq]"] = request_status
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
        return self.http.get(f"{self.url}/correct-occupation-requests", params=params)

    def get_count(self) -> Response:
        return self.http.get(f"{self.url}/count")

    def get_correct_occupations(
        self,
        page: int = 1,
        per: int = 10,
        occupation_id: int = None,
    ) -> Response:
        params = dict(
            page=page,
            per=per,
        )
        if occupation_id:
            params["q[current-occupation-id][eq][]"] = occupation_id
        return self.http.get(f"{self.url}/correct-occupations", params=params)
