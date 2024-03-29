import random
from datetime import date

import allure

from data.shareable.change_occupation import RequestStatus
from src.api.clients.change_occupation import ChangeOccupationApi
from src.api.clients.ott_service import OttServiceApi
from src.api.http_client import HTTPClient
from src.api.models.qiwa.change_occupation import (
    ChangeOccupationsCountData,
    CreatedRequestsData,
    OccupationsData,
    RequestByIdData,
    RequestsData,
    RequestsLaborersData,
    UsersData,
)
from src.api.models.qiwa.raw.change_occupations.count import (
    ChangeOccupationCountAttributes,
)
from src.api.models.qiwa.raw.change_occupations.occupations import OccupationAttributes
from src.api.models.qiwa.raw.change_occupations.requests import Laborer, Request
from src.api.models.qiwa.raw.change_occupations.requests_laborers import RequestLaborer
from src.api.models.qiwa.raw.change_occupations.users import User
from src.api.payloads.raw.change_occupation import Laborer as LaborerToRequest
from utils.assertion import assert_status_code, assert_that
from utils.json_search import search_by_data


class ChangeOccupationController:
    def __init__(self, client: HTTPClient):
        self.api = ChangeOccupationApi(client)

    @classmethod
    @allure.step
    def pass_ott_authorization(
        cls, office_id: str, sequence_number: str, personal_number: str = None
    ) -> "ChangeOccupationController":
        ott_service = OttServiceApi()
        response = ott_service.generate_token(
            sequence_number=sequence_number,
            labor_office_id=office_id,
            personal_number=personal_number,
        )
        assert_that(response).has(status_code=200)
        ott_token = response.json().get("ott")
        client = HTTPClient()
        controller = cls(client)
        response = controller.api.get_session(ott_token)
        assert_that(response).has(status_code=200)
        return controller

    @allure.step
    def get_requests_laborers(
        self,
        page: int = 1,
        per: int = 10,
        laborer_name: str = None,
        laborer_id: int = None,
        request_status: RequestStatus = None,
        date_range: tuple[date, date] = None,
    ) -> RequestsLaborersData:
        status = request_status.value if request_status else request_status
        response = self.api.get_requests_laborers(
            page, per, laborer_name, laborer_id, status, date_range
        )
        assert_status_code(response.status_code).equals_to(200)
        return RequestsLaborersData.parse_obj(response.json())

    @allure.step
    def get_requests(
        self, page: int = 1, per: int = 10, employee_name: str = None, request_id: str = None
    ) -> RequestsData:
        response = self.api.get_requests(page, per, employee_name, request_id)
        assert_status_code(response.status_code).equals_to(200)
        return RequestsData.parse_obj(response.json())

    @allure.step
    def get_request_by_id(self, request_id: str) -> RequestByIdData:
        response = self.api.get_request_by_id(request_id)
        assert_status_code(response.status_code).equals_to(200)
        return RequestByIdData.parse_obj(response.json())

    @allure.step
    def get_requests_by_laborer(self, personal_number: str):
        requests = self.get_requests(per=100)
        expression = (
            f"data[?attributes.laborers[?\"employee_personal_number\" == '{personal_number}'"
            f' && "status_id" != `9`]]'
            f"[attributes.laborers[? \"employee_personal_number\" == '{personal_number}']][][]"
        )
        return search_by_data(expression, requests.dict(exclude_unset=True))

    @allure.step
    def get_requests_by_request_number(self, number: str) -> list[Laborer]:
        requests = self.get_requests(per=100)
        expression = (
            f"data[?attributes.laborers[?\"request_number\" == '{number}']]"
            f"[attributes.laborers[? \"request_number\" == '{number}']][][]"
        )
        return [
            Laborer.parse_obj(data)
            for data in search_by_data(expression, requests.dict(exclude_unset=True))
        ]

    @allure.step
    def create_request(self, *laborers: LaborerToRequest) -> CreatedRequestsData:
        response = self.api.create_request(*laborers)
        assert_status_code(response.status_code).equals_to(200)
        return CreatedRequestsData.parse_obj(response.json())

    @allure.step
    def get_users(self, page: int = 1, per: int = 10) -> UsersData:
        response = self.api.get_users(page=page, per=per)
        assert_status_code(response.status_code).equals_to(200)
        return UsersData.parse_obj(response.json())

    @allure.step
    def get_occupations(
        self, page: int = 1, per: int = 10, english_name: str = None, arabic_name: str = None
    ) -> OccupationsData:
        response = self.api.get_occupations(page, per, english_name, arabic_name)
        assert_status_code(response.status_code).equals_to(200)
        return OccupationsData.parse_obj(response.json())

    @allure.step
    def get_requests_count(self) -> ChangeOccupationsCountData:
        response = self.api.get_count()
        assert_status_code(response.status_code).equals_to(200)
        return ChangeOccupationsCountData.parse_obj(response.json())

    @allure.step
    def get_requests_count_by_status(
        self, status: RequestStatus
    ) -> ChangeOccupationCountAttributes:
        counts = self.get_requests_count()
        expression = f'data[?attributes."status_id"== `{status.value}`].attributes | [0]'
        return ChangeOccupationCountAttributes.parse_obj(search_by_data(expression, counts.dict()))

    @allure.step
    def get_random_request(self) -> Request:
        requests = self.get_requests(per=1000)
        return random.choice(requests.data).attributes

    @allure.step
    def get_random_laborer(self) -> RequestLaborer:
        laborers = self.get_requests_laborers(per=100)
        laborers_with_name = list(filter(lambda l: bool(l.attributes.laborer_name), laborers.data))
        return random.choice(laborers_with_name).attributes

    @allure.step
    def get_random_user(self, eligible: bool = True) -> User:
        users = self.get_users(per=1000)
        expression = f"data[?attributes.\"eligibility\"== '{int(eligible)}'].attributes"
        return User.parse_obj(random.choice(search_by_data(expression, users.dict())))

    @allure.step
    def get_random_occupation(self) -> OccupationAttributes:
        occupations = self.get_occupations(per=100)
        return random.choice(occupations.data).attributes
