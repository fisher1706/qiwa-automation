from typing import Optional

import allure
from requests import Response

import config
from src.api.constants.work_permit import WorkPermitStatus
from src.api.http_client import HTTPClient


class WorkPermitApi:
    def __init__(self, api: HTTPClient):
        self.api = api
        self.url = config.qiwa_urls.api + "/working-permit-request"

    @allure.step("GET /working-permit-request/work-permit-transactions")
    def get_wp_transactions(
        self,
        page: int = 1,
        per_page: int = 100,
        status: Optional[WorkPermitStatus] = None,
    ) -> Response:
        payload = {"page": page, "per": per_page}
        if status:
            payload["q[status][eq]"] = status.value

        response = self.api.get(self.url, endpoint="/work-permit-transactions", params=payload)
        return response

    def get_employees(self, page=1, per_page=10) -> Response:
        return self.api.get(
            self.url,
            endpoint=f"/employees?page={page}&per={per_page}",
        )

    def get_employee_by_personal_number(self, personal_number) -> Response:
        return self.api.get(
            self.url,
            endpoint=f"/employees?page=1&per=10&q[personal-number][eq]={personal_number}",
        )

    def validate_expat(self, expat_number: str, regular: bool) -> Response:
        payload = {"validate_user_params": {"expat_number": expat_number, "regular": regular}}
        return self.api.post(self.url, "/validate-expat", json=payload)

    def cancel_sadad_number(self, sadad_number: str | int) -> Response:
        payload = {"sadad-number": sadad_number}
        response = self.api.post(self.url, "/cancel-sadad-number", json=payload)
        response.encoding = "utf-8"
        return response
