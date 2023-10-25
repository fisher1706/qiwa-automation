from http import HTTPStatus
from urllib import parse

import allure

from src.api.clients.change_occupation import ChangeOccupationApi
from src.api.http_client import HTTPClient
from src.api.models.qiwa.change_occupation import requests_laborers_data
from src.api.models.qiwa.raw.token import AuthorizationToken
from utils.assertion import assert_status_code
from utils.crypto_manager import decode_authorization_token


class ChangeOccupationController:
    def __init__(self, client: HTTPClient):
        self.api = ChangeOccupationApi(client)

    @allure.step
    def pass_ott_authorization(self) -> None:
        cookie = self.api.client.session.cookies.get("qiwa.authorization")
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
    def get_requests_laborers_data(self, page: int = 1, per: int = 10) -> requests_laborers_data:
        response = self.api.get_requests_laborers(page=page, per=per)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return requests_laborers_data.parse_obj(response.json())
