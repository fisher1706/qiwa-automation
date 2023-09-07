import allure
from requests import Response

import config
from src.api.assertions.response_validator import ResponseValidator
from src.api.clients.e_service.groups import GroupsApi
from src.api.http_client import HTTPClient
from src.api.requests.e_service import EService


class EServiceApi:
    url = config.qiwa_urls.api

    def __init__(self, client: HTTPClient):
        self.client = client
        self.groups = GroupsApi(client)
        self.e_service_id = ""
        self.e_service_english_title = ""
        self.tag_id = ""
        self.tag_english_name = ""
        self.route = ""

    @property
    def as_admin(self):
        self.route = "/admin"
        return self

    @allure.step
    def get_e_services(self, is_admin=False, expect_code=200) -> Response:
        if is_admin:
            response = self.client.get(url=self.url, endpoint="/admin/e-services")
        else:
            response = self.client.get(url=self.url, endpoint=f"{self.route}/e-services")
        if expect_code == 200:
            ResponseValidator(response).check_status_code(
                name="Get e-service data", expect_code=expect_code
            )
        return response

    @allure.step
    def create_e_services(
        self, body: bool = True, permission: bool = False, expect_code: int = 201
    ) -> None:
        json_body = EService.create_e_service_body(permission) if body else {}
        response = self.client.post(url=self.url, endpoint="/admin/e-services", json=json_body)
        ResponseValidator(response).check_status_code(
            name="Create e-services", expect_code=expect_code
        )
        json = response.json()
        if expect_code in (200, 201):
            self.e_service_id = json["data"]["id"]
            self.e_service_english_title = json["data"]["attributes"]["title"]

    @allure.step
    def find_e_service_by_id(self, expected_code=200):
        response = self.client.get(url=self.url, endpoint=f"/admin/e-services/{self.e_service_id}")
        ResponseValidator(response).check_status_code(
            name="Find e-service by id", expect_code=expected_code
        )

    @allure.step
    def update_e_service(self) -> Response:
        update_data = EService.update_e_service_body(self.e_service_id)
        return self.client.put(
            url=self.url,
            endpoint=f"/admin/e-services/{self.e_service_id}",
            json=update_data,
        )

    @allure.step
    def delete_e_service(self) -> Response:
        return self.client.delete(url=self.url, endpoint=f"/admin/e-services/{self.e_service_id}")

    @allure.step
    def get_admin_tags(self, expect_code=200):
        response = self.client.get(url=self.url, endpoint="/admin/tags")
        ResponseValidator(response).check_status_code(
            name="Get e-service data", expect_code=expect_code
        )
        return response

    @allure.step
    def create_tag(self, body=True):
        json_body = EService.create_tag_body()
        if body:
            response = self.client.post(url=self.url, endpoint="/admin/tags", json=json_body)
            ResponseValidator(response).check_status_code(name="Create tag", expect_code=201)
            json = response.json()
            self.tag_id = json["data"]["id"]
            self.tag_english_name = json["data"]["attributes"]["name"]
        else:
            response = self.client.post(url=self.url, endpoint="/admin/tags", json={})
            ResponseValidator(response).check_status_code(
                name="Create e-services", expect_code=422
            )

    @allure.step
    def update_tag(self):
        json_body = EService.update_tag_body(self.tag_id)
        response = self.client.put(
            url=self.url, endpoint=f"/admin/tags/{self.tag_id}", json=json_body
        )
        validator = ResponseValidator(response)
        if self.tag_id:
            validator.check_status_code(name="Update tag", expect_code=200)
        else:
            validator.check_status_code(name="Update tag", expect_code=404)

    @allure.step
    def delete_tag(self, tag_id: str = None):
        tag = tag_id if tag_id else self.tag_id
        response = self.client.delete(url=self.url, endpoint=f"/admin/tags/{tag}")
        validator = ResponseValidator(response)
        if tag:
            validator.check_status_code(name="Delete tag", expect_code=200)
        else:
            validator.check_status_code(name="Delete tag", expect_code=404)
