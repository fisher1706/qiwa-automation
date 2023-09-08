import allure

import config
from src.api.assertions.response_validator import ResponseValidator
from src.api.requests.services import Services


class ServicesApi:
    url = config.qiwa_urls.api

    def __init__(self, api):
        self.api = api

        self.services = None
        self.services_id = []
        self.last_service_id = None
        self.last_service = None
        self.service_status = None
        self.last_sub_service_id = None
        self.last_sub_service = None
        self.sub_service_status = None

    @allure.step("Get all services")
    def get_services(self, expect_code=200, pagination=None, expect_schema="get_services.json"):
        params = f"?page={pagination}&per=10" if pagination else ""
        response = self.api.get(url=self.url, endpoint=f"/labor-offices/services{params}")
        validator = ResponseValidator(response)
        validator.check_status_code(name="GET /labor-offices/services", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)
        return response.json()

    @allure.step("Get last created service")
    def get_last_service_id(self):
        get_services_all = self.get_services()
        get_services_paginated = self.get_services(
            pagination=get_services_all["meta"]["total-pages"]
        )
        for service in get_services_paginated["data"]:
            self.services_id.append(service["id"])
        return self.services_id[-1]

    @allure.step("Get service")
    def get_last_service(self, last_service_id):
        get_services_all = self.get_services()
        get_services_paginated = self.get_services(
            pagination=get_services_all["meta"]["total-pages"]
        )
        for service in get_services_paginated["data"]:
            if service["id"] == last_service_id:
                self.last_service = service
                self.last_sub_service_id = service["relationships"]["sub-services"]["data"][0][
                    "id"
                ]
        for sub_service in get_services_paginated["included"]:
            if sub_service["id"] == self.last_sub_service_id:
                self.last_sub_service = sub_service
        self.service_status = self.last_service["attributes"]["is-active"]
        self.sub_service_status = self.last_sub_service["attributes"]["is-active"]
        return self.service_status, self.sub_service_status

    @allure.step("Create service")
    def post_service(
        self,
        requester_type_id,
        name_en,
        name_ar,
        expect_code=201,
        expect_schema="services_response.json",
    ):
        json_body = Services.service_multi_body(requester_type_id, "lo-service", name_en, name_ar)
        response = self.api.post(url=self.url, endpoint="/labor-offices/services", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="POST /labor-offices/services", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)
        return self

    @allure.step("Create sub service")
    def post_sub_service(
        self,
        requester_type_id,
        name_en,
        name_ar,
        service_id,
        expect_code=201,
        expect_schema="services_response.json",
    ):
        json_body = Services.service_multi_body(
            requester_type_id, "lo-sub-service", name_en, name_ar
        )
        response = self.api.post(
            url=self.url,
            endpoint=f"/labor-offices/services/{service_id}/sub-services",
            json=json_body,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="POST /labor-offices/services/{service_id}/sub-services", expect_code=expect_code
        )
        validator.check_response_schema(schema_name=expect_schema)
        return self

    @allure.step("Edit service")
    def put_edit_service(
        self,
        requester_type_id,
        name_en,
        name_ar,
        service_id,
        expect_code=200,
        expect_schema="services_response.json",
    ):
        json_body = Services.service_multi_body(
            requester_type_id, "lo-service", name_en, name_ar, service_id
        )
        response = self.api.put(url=self.url, endpoint="/labor-offices/services", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="PUT /labor-offices/services", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)
        return self

    @allure.step("Edit sub service")
    def put_edit_sub_service(
        self,
        requester_type_id,
        name_en,
        name_ar,
        service_id,
        sub_service_id,
        service_status=False,
        expect_code=200,
        expect_schema="services_response.json",
    ):
        json_body = Services.service_multi_body(
            requester_type_id, "lo-sub-service", name_en, name_ar, sub_service_id, service_status
        )
        response = self.api.put(
            url=self.url,
            endpoint=f"/labor-offices/services/{service_id}/sub-services",
            json=json_body,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="PUT /labor-offices/services/{service_id}/sub-services", expect_code=expect_code
        )
        validator.check_response_schema(schema_name=expect_schema)
        return self

    @allure.step("Change service status")
    def put_service_status(
        self,
        requester_type_id,
        name_en,
        name_ar,
        service_id,
        service_status,
        expect_code=200,
        expect_schema="services_response.json",
    ):
        json_body = Services.service_multi_body(
            requester_type_id, "lo-service", name_en, name_ar, service_id, service_status
        )
        response = self.api.put(url=self.url, endpoint="/labor-offices/services", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="PUT /labor-offices/services", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)
        return self
