import random
from http import HTTPStatus
from urllib import parse

import allure

from src.api.clients.change_occupation import ChangeOccupationApi
from src.api.models.qiwa.change_occupation import (
    requests_data,
    requests_laborers_data,
    users_data,
)
from src.api.models.qiwa.raw.change_occupations.requests import Request
from src.api.models.qiwa.raw.change_occupations.requests_laborers import RequestLaborer
from src.api.models.qiwa.raw.token import AuthorizationToken
from utils.assertion import assert_status_code
from utils.crypto_manager import decode_authorization_token


class ChangeOccupationController(ChangeOccupationApi):
    @allure.step
    def pass_ott_authorization(self) -> None:
        cookie = self.client.session.cookies.get("qiwa.authorization")
        jwt = decode_authorization_token(cookie)
        auth_token = AuthorizationToken.parse_obj(jwt)
        response = self.get_ott_token(
            auth_token.company_labor_office_id,
            auth_token.company_sequence_number,
            auth_token.user_personal_number,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        redirect_url = response.json()["redirect_url"]
        parsed_url = parse.parse_qs(parse.urlparse(redirect_url).query)
        ott_token = parsed_url.get("ott-token")[0]
        response = self.get_session(ott_token)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)

    @allure.step
    def get_requests_laborers_data(self, page: int = 1, per: int = 10) -> requests_laborers_data:
        response = self.get_requests_laborers(page=page, per=per)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return requests_laborers_data.parse_obj(response.json())

    @allure.step
    def get_requests_data(self, page: int = 1, per: int = 10) -> requests_data:
        response = self.get_requests(page=page, per=per)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return requests_data.parse_obj(response.json())

    @allure.step
    def get_users_data(self, page: int = 1, per: int = 10) -> users_data:
        response = self.get_users(page=page, per=per)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return users_data.parse_obj(response.json())

    @allure.step
    def get_random_request(self) -> Request:
        requests = self.get_requests_data(per=1000)
        return random.choice(requests.data).attributes

    @allure.step
    def get_random_laborer(self) -> RequestLaborer:
        requests = self.get_requests_laborers_data(per=1000)
        return random.choice(requests.data).attributes
