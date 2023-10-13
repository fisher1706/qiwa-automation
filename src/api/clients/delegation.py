from http import HTTPStatus

import config
from data.delegation.delegation_data import AllDelegations, DelegationDetails
from src.api.http_client import HTTPClient
from src.api.payloads.delegation import (
    filter_delegations_by_status_request,
    get_all_delegations_request,
)
from utils.assertion import assert_status_code


class DelegationAPI:
    url = config.qiwa_urls.delegation_service_api

    def __init__(self, client: HTTPClient):
        self.client = client

    def set_headers(self) -> dict:
        token = self.client.session.cookies.get("qiwa.authorization")
        headers = {"Cookie": f"qiwa.authorization={token}", "X-Service-Id": "delegation"}
        return headers

    def get_delegations(self, headers: dict) -> AllDelegations:
        response = self.client.post(
            url=self.url,
            endpoint="/proxy/delegations/find/all",
            json=get_all_delegations_request(),
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return AllDelegations(response.json())

    def get_delegations_by_status(self, headers: dict, status_en: str) -> AllDelegations:
        response = self.client.post(
            url=self.url,
            endpoint="/proxy/delegations/find/all",
            json=filter_delegations_by_status_request(status_en),
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return AllDelegations(response.json())

    def get_delegation_by_id(self, headers: dict, delegation_id: int) -> DelegationDetails:
        response = self.client.get(
            url=self.url, endpoint=f"/proxy/delegations/{delegation_id}", headers=headers
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return DelegationDetails(response.json())

    def get_entity_type(self, headers: dict) -> list:
        response = self.client.get(url=self.url, endpoint="/proxy/entity-type", headers=headers)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()

    def get_entity_name(self, headers: dict) -> str:
        response = self.client.get(
            url=self.url, endpoint="/proxy/entity?type-id=GOVERNMENT", headers=headers
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()[0]["nameEn"]

    def get_entity_permission(self, headers: dict) -> str:
        response = self.client.get(
            url=self.url, endpoint="/proxy/entity-permission/NAFITH", headers=headers
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()[0]["nameEn"]

    def get_max_months(self, headers: dict) -> int:
        response = self.client.get(
            url=self.url, endpoint="/proxy/delegations/duration/months", headers=headers
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()["maxMonths"]

    def get_employees_list(self, headers: dict) -> list:
        response = self.client.get(
            url=self.url,
            endpoint="/proxy/employee?sort=name&direction=ASC&size=10000",
            headers=headers,
        )
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()

    def get_partners(self, headers: dict) -> list:
        response = self.client.get(url=self.url, endpoint="/proxy/partners", headers=headers)
        assert_status_code(response.status_code).equals_to(HTTPStatus.OK)
        return response.json()
