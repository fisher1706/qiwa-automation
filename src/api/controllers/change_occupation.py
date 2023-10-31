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
)
from src.api.models.qiwa.raw.change_occupations.requests import Request
from src.api.models.qiwa.raw.change_occupations.requests_laborers import RequestLaborer
from src.api.models.qiwa.raw.change_occupations.users import User
from src.api.models.qiwa.raw.token import AuthorizationToken
from src.api.payloads.raw.change_occupation import Laborer
from utils.assertion import assert_status_code
from utils.crypto_manager import decode_authorization_token
from utils.json_search import search_by_data


class ChangeOccupationController:
    def __init__(self, client: HTTPClient):
        self.api = ChangeOccupationApi(client)

    @allure.step
    def pass_ott_authorization(self) -> None:
        cookie = self.api.http.session.cookies.get("qiwa.authorization")
        jwt = decode_authorization_token(cookie)
        auth_token = AuthorizationToken.parse_obj(jwt)
        response = self.api.get_ott_token(
            auth_token.company_labor_office_id,
            auth_token.company_sequence_number,
            auth_token.user_personal_number,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        redirect_url = response.json()["redirect_url"]
        parsed_url = parse.parse_qs(parse.urlparse(redirect_url).query)
        ott_token = parsed_url.get("ott-token")[0]
        response = self.api.get_session(ott_token)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

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
    def create_request(self, *laborers: Laborer) -> CreatedRequestsData:
        response = self.api.create_request(*laborers)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return CreatedRequestsData.parse_obj(response.json())

    @allure.step
    def get_users(self, page: int = 1, per: int = 10) -> users_data:
        response = self.api.get_users(page=page, per=per)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return users_data.parse_obj(response.json())

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
