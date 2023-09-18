import allure

import config
from src.api.assertions.response_validator import ResponseValidator
from src.api.requests.offices import Offices


class OfficesApi:
    url = config.qiwa_urls.api

    def __init__(self, api):
        self.api = api
        self.support = ResponseValidator
        self.offices_id = []
        self.offices = None
        self.office = None
        self.office_id = None
        self.last_office_id = None
        self.office_status = None

    @allure.step("Get labor office")
    def get_office(self, offices_id, expect_code=200):
        response = self.api.get(url=self.url, endpoint=f"/labor-offices/{offices_id}")
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="GET /labor-offices/{offices_id}", expect_code=expect_code
        )
        self.office = response.json()
        self.office_status = self.office["data"]["attributes"]["is-active"]
        return self

    @allure.step("Get all labor offices")
    def get_offices(self, expect_code=200, expect_schema="get_offices.json"):
        response = self.api.get(url=self.url, endpoint="/labor-offices/offices")
        validator = ResponseValidator(response)
        validator.check_status_code(name="GET /labor-offices/offices", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)
        self.offices = response.json()
        for offices in self.offices["data"]:
            self.offices_id.append(offices["id"])
        self.last_office_id = max(self.offices_id)
        return response.json()

    def get_last_office_id(self, response=None):
        if not response:
            response = self.get_offices()
        return max(x["id"] for x in response["data"])

    @allure.step("Create labor office")
    def post_office(
        self,
        office_name,
        hourly_capacity,
        working_hours_from,
        working_hours_to,
        address,
        region_id,
        latitude,
        longitude,
        service_id,
        is_electronic_office=False,
        expect_code=201,
        expect_schema="offices_response.json",
    ):
        # pylint: disable=duplicate-code
        json_body = Offices.offices_body(
            office_name=office_name,
            hourly_capacity=hourly_capacity,
            working_hours_from=working_hours_from,
            working_hours_to=working_hours_to,
            address=address,
            region_id=region_id,
            latitude=latitude,
            longitude=longitude,
            service_id=service_id,
            is_electronic_office=is_electronic_office,
        )
        response = self.api.post(url=self.url, endpoint="/labor-offices", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="POST /labor-offices", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)
        return response.json()["data"]["id"]

    @allure.step("Edit labor office")
    def put_edit_office(
        self,
        office_name,
        hourly_capacity,
        working_hours_from,
        working_hours_to,
        address,
        region_id,
        latitude,
        longitude,
        service_id,
        office_id,
        expect_code=200,
        expect_schema="offices_response.json",
    ):
        json_body = Offices.offices_body(
            office_name,
            hourly_capacity,
            working_hours_from,
            working_hours_to,
            address,
            region_id,
            latitude,
            longitude,
            int(service_id) - 1,
            office_id,
        )
        response = self.api.put(url=self.url, endpoint="/labor-offices", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="PUT /labor-offices", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)

    @allure.step("Change office status")
    def patch_office_status(
        self, office_id, office_status, expect_code=200, expect_schema="offices_response.json"
    ):
        json_body = Offices.office_status_body(office_id, office_status)
        response = self.api.patch(url=self.url, endpoint="/labor-offices/status", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="PATCH /labor-offices/status", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)
        return self
