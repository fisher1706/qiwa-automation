import random
from datetime import date

import allure

from data.shareable.correct_occupation import RequestStatus
from src.api.clients.correct_occupation import CorrectOccupationApi
from src.api.http_client import HTTPClient
from src.api.models.qiwa.correct_occupation import LaborersData, RequestsData
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
    def get_any_laborer(self) -> LaborerAttributes:
        laborers = self.get_laborers(per=100)
        return random.choice(laborers.data).attributes

    @allure.step
    def get_any_request(self) -> OccupationCorrectionRequestAttributes:
        requests = self.get_requests(per=100)
        return random.choice(requests.data).attributes
