from __future__ import annotations

import allure
from requests import Response

import config
from src.api.assertions.response_validator import ResponseValidator
from src.api.http_client import HTTPClient


class WorkspacesApi:
    url = config.qiwa_urls.api

    def __init__(self, api=HTTPClient()):
        self.api = api
        self.error_msg = None

    @allure.step
    def get_workspaces(self) -> Response:
        response = self.api.get(url=self.url, endpoint="/context/workspaces")
        validator = ResponseValidator(response)
        validator.check_status_code(name="Workspaces list", expect_code=200)
        return response

    @allure.step
    def select_company_by_id(self, company_id, status_code=200):
        response = self.api.patch(url=self.url, endpoint=f"/context/company/{company_id}")
        ResponseValidator(response).check_status_code(
            name="Select Company by id", expect_code=status_code
        )
        if status_code == 403:
            self.error_msg = response.json()["title"]
