from http import HTTPStatus
from typing import Optional

import allure
from requests import Response

import config
from src.api.assertions.response_validator import ResponseValidator
from src.api.constants.work_permit import WorkPermitStatus
from src.api.http_client import HTTPClient


class WorkPermitApi:
    def __init__(self, api: HTTPClient):
        self.api = api
        self.url = config.settings.api_url + "/working-permit-request"

    @allure.step("GET /working-permit-request/work-permit-transactions")
    def get_wp_transactions(
        self,
        page: int = 1,
        per_page: int = 100,
        status: Optional[WorkPermitStatus] = None,
        expect_code: HTTPStatus = HTTPStatus.OK,
    ) -> Response:
        payload = {"page": page, "per": per_page}
        if status:
            payload["q[status][eq]"] = status.value

        response = self.api.get(self.url, endpoint="/work-permit-transactions", params=payload)
        ResponseValidator(response).check_status_code(
            name="GET /working-permit-request/work-permit-transactions", expect_code=expect_code
        )
        return response

    @allure.step("GET /working-permit-request/employees")
    def get_employees(self, page=1, per_page=10, expect_code=200) -> Response:
        response = self.api.get(
            self.url,
            endpoint=f"/employees?page={page}&per={per_page}",
        )
        ResponseValidator(response).check_status_code(
            name="GET /working-permit-request/employees", expect_code=expect_code
        ).check_response_schema("wp_employees.json")
        return response

    @allure.step("GET /working-permit-request/employees")
    def get_employee_by_personal_number(self, personal_number, expect_code=200) -> Response:
        response = self.api.get(
            self.url,
            endpoint=f"/employees?page=1&per=10&q[personal-number][eq]={personal_number}",
        )
        ResponseValidator(response).check_status_code(
            name="GET /working-permit-request/employees", expect_code=expect_code
        ).check_response_schema("wp_employees.json")
        return response

    def validate_expat(self, expat_number: str, regular: bool) -> Response:
        payload = {"validate_user_params": {"expat_number": expat_number, "regular": regular}}
        return self.api.post(self.url, "/validate-expat", json=payload)

    def cancel_sadad_number(self, sadad_number: str | int) -> Response:
        payload = {"sadad-number": sadad_number}
        response = self.api.post(self.url, "/cancel-sadad-number", json=payload)
        response.encoding = "utf-8"
        return response
