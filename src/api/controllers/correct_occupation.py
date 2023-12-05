import random

import allure

from src.api.clients.correct_occupation import CorrectOccupationApi
from src.api.http_client import HTTPClient
from src.api.models.qiwa.correct_occupation import LaborersData
from src.api.models.qiwa.raw.correct_occupation.laborers import LaborerAttributes


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
    def get_any_laborer(self) -> LaborerAttributes:
        laborers = self.get_laborers(per=100)
        return random.choice(laborers.data).attributes
