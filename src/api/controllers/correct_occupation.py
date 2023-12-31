import random
from datetime import date

import allure
from requests import Response

from data.shareable.correct_occupation import RequestStatus
from src.api.clients.correct_occupation import CorrectOccupationApi
from src.api.http_client import HTTPClient
from src.api.models.qiwa.correct_occupation import (
    CorrectOccupationsData,
    LaborersData,
    RequestsData,
    SubmitRequestData,
)
from src.api.models.qiwa.raw.correct_occupation.correct_occupations import (
    CorrectOccupationAttributes,
)
from src.api.models.qiwa.raw.correct_occupation.laborers import LaborerAttributes
from src.api.models.qiwa.raw.correct_occupation.requests import (
    OccupationCorrectionRequestAttributes,
)


class CorrectOccupationController:
    def __init__(self, client: HTTPClient):
        self.api = CorrectOccupationApi(client)

    @allure.step
    def get_laborers(
        self,
        page: int = 1,
        per: int = 100,
        laborer_name: str = None,
        laborer_id: str = None,
        occupation_id: int = None,
        nationality_id: int = None,
    ) -> LaborersData:
        response = self.api.get_laborers(
            page, per, laborer_name, laborer_id, occupation_id, nationality_id
        )
        assert response.status_code == 200
        return LaborersData.parse_obj(response.json())

    @allure.step
    def get_requests(
        self,
        page: int = 1,
        per: int = 10,
        laborer_name: str = None,
        laborer_id: str = None,
        request_status: RequestStatus = None,
        date_range: tuple[date, date] = None,
    ) -> RequestsData:
        status = int(request_status.value) if request_status else request_status
        response = self.api.get_requests(page, per, laborer_name, laborer_id, status, date_range)
        assert response.status_code == 200
        return RequestsData.parse_obj(response.json())

    @allure.step
    def create_request(
        self, laborer: LaborerAttributes, new_occupation_id: str
    ) -> SubmitRequestData:
        response = self.api.create_request(
            laborer.laborer_id, laborer.laborer_name, laborer.occupation_id, new_occupation_id
        )
        assert response.status_code == 200
        return SubmitRequestData.parse_obj(response.json())

    @allure.step
    def get_occupations(
        self,
        occupation_id: str,
        page: int = 1,
        per: int = 10,
    ) -> CorrectOccupationsData:
        response = self.api.get_correct_occupations(occupation_id, page, per)
        assert response.status_code == 200
        return CorrectOccupationsData.parse_obj(response.json())

    @allure.step
    def get_any_laborer(self) -> LaborerAttributes:
        laborers = self.get_laborers(per=100)
        return random.choice(laborers.data).attributes

    @allure.step
    def get_any_request(self) -> OccupationCorrectionRequestAttributes:
        requests = self.get_requests(per=100)
        return random.choice(requests.data).attributes

    @allure.step
    def get_any_occupation(self, occupation_id: str) -> CorrectOccupationAttributes:
        occupations = self.get_occupations(occupation_id, per=100)
        return random.choice(occupations.data).attributes

    @allure.step
    def delete_request_in_ibm(self, laborer_id: str) -> Response:
        payload = {"laborer-id": laborer_id}
        response = self.api.http.delete(
            "http://192.168.168.29:5000/occupationCorrectionRequest", json=payload
        )
        return response
