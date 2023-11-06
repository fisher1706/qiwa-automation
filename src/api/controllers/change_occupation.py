import random
from http import HTTPStatus
from urllib import parse

import allure

from src.api.clients.change_occupation import ChangeOccupationApi
from src.api.http_client import HTTPClient
from src.api.models.qiwa.change_occupation import (
    CreatedRequestsData,
    request_by_id_data,
    requests_data,
    requests_laborers_data,
    users_data,
    OccupationsData,
)
from src.api.models.qiwa.raw.change_occupations.requests import Laborer, Request
from src.api.models.qiwa.raw.change_occupations.requests_laborers import RequestLaborer
from src.api.models.qiwa.raw.change_occupations.users import User
from src.api.payloads.raw.change_occupation import Laborer as LaborerToRequest
from utils.assertion import assert_status_code
from utils.json_search import search_by_data


class ChangeOccupationController:
    def __init__(self, client: HTTPClient):
        self.api = ChangeOccupationApi(client)

    @classmethod
    @allure.step
    def pass_ott_authorization(
        cls, labor_office_id: str, sequence_number: str, personal_number: str
    ) -> 'ChangeOccupationController':
        client = HTTPClient()
        controller = cls(client)
        response = controller.api.get_ott_token(
            labor_office_id,
            sequence_number,
            personal_number,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        redirect_url = response.json()["redirect_url"]
        parsed_url = parse.parse_qs(parse.urlparse(redirect_url).query)
        ott_token = parsed_url.get("ott-token")[0]
        response = controller.api.get_session(ott_token)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return controller

    @allure.step
    def get_requests_laborers(
        self, page: int = 1, per: int = 10, laborer_name: str = None, laborer_id: int = None
    ) -> requests_laborers_data:
        response = self.api.get_requests_laborers(page, per, laborer_name, laborer_id)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return requests_laborers_data.parse_obj(response.json())

    @allure.step
    def get_requests(self, page: int = 1, per: int = 10) -> requests_data:
        response = self.api.get_requests(page=page, per=per)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return requests_data.parse_obj(response.json())

    @allure.step
    def get_request(self, request_id: int) -> request_by_id_data:
        response = self.api.get_request(request_id)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return request_by_id_data.parse_obj(response.json())

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
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return CreatedRequestsData.parse_obj(response.json())

    @allure.step
    def get_users(self, page: int = 1, per: int = 10) -> users_data:
        response = self.api.get_users(page=page, per=per)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return users_data.parse_obj(response.json())

    @allure.step
    def get_occupations(self, page: int = 1, per: int = 10) -> OccupationsData:
        response = self.api.get_occupations(page, per)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return OccupationsData.parse_obj(response.json())

    @allure.step
    def get_random_request(self) -> Request:
        requests = self.get_requests(per=1000)
        return random.choice(requests.data).attributes

    @allure.step
    def get_random_laborer(self) -> RequestLaborer:
        requests = self.get_requests_laborers(per=1000)
        return random.choice(requests.data).attributes

    @allure.step
    def get_random_user(self) -> User:
        users = self.get_users(per=1000)
        return random.choice(users.data).attributes
