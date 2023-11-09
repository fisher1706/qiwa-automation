import math
from datetime import datetime, timedelta
from typing import Dict

import allure
import jmespath

import config
from data.lo.models import Booking
from src.api.assertions.response_validator import ResponseValidator
from src.api.requests.booking import Converter
from src.api.requests.visit import Visit


class VisitsApi:
    # pylint: disable=too-many-instance-attributes
    url = config.qiwa_urls.api

    def __init__(self, api):
        self.api = api
        self.appointment_id = None
        self.appointment = {}
        self.valid_date = None
        self.edited_date = None
        self.valid_time = None
        self.current_day = None
        self.edited_time = None
        self.active_appointment_id = None

        self.establishment_name = None
        self.employee_name = None
        self.source_sequence_number = None
        self.nationality_code = None
        self.dest_establishment_name = None
        self.date_of_expire = None
        self.nationality_name_ar = None
        self.nationality_name_en = None
        self.establishment_id = None
        self.source_establishment_name = None
        self.source_labor_office_id = None
        self.request_number = None

    def get_valid_date(self, time_delta=None):
        date_format = "%Y-%m-%d"
        time_format = "%H:%M"
        valid_date = datetime.now() + timedelta(days=time_delta) if time_delta else datetime.now()
        current_day = valid_date.strftime("%a")
        if current_day in {"Fri", "Sat"}:
            valid_date = valid_date + timedelta(days=5) + timedelta(hours=2)
        self.valid_date = valid_date.strftime(date_format)
        self.current_day = valid_date.strftime("%A")
        hours, minutes = divmod(math.ceil(valid_date.minute / 30) * 60, 60)
        self.valid_time = (
            (valid_date + timedelta(hours=hours)).replace(minute=minutes).strftime(time_format)
        )
        self.edited_date = (
            datetime.strptime(self.valid_date, date_format) + timedelta(days=1)
        ).strftime(date_format)
        self.edited_time = (
            datetime.strptime(self.valid_time, time_format) + timedelta(hours=1)
        ).strftime(time_format)

    @allure.step("Get the ID of the last created appointment")
    def get_active_appointment_id(self, user_id, cookies=None):
        response = self.api.get(
            url=self.url, endpoint="/labor-offices/appointment?q[status-id][eq]=1", cookies=cookies
        )
        active_appointment_id = jmespath.search(
            f"data[?attributes.\"status-name-en\"=='Active' && "
            f"attributes.\"requester-personal-number\"=='{user_id}'].id",
            response.json(),
        )
        if active_appointment_id:
            self.active_appointment_id = active_appointment_id[0]

    @allure.step("Get all info for particular appointment")
    def get_appointment_info(
        self, appointment_id, expect_code=200, expect_schema="get_appointment.json"
    ) -> Booking:
        response = self.api.get(
            url=self.url, endpoint=f"/labor-offices/appointment/{appointment_id}"
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="GET /labor-offices/appointment/{appointment_id}", expect_code=expect_code
        )
        validator.check_response_schema(schema_name=expect_schema)
        self.appointment = response.json()
        booking_options = Converter.json_to_booking(self.appointment)
        return booking_options

    @allure.step("Create appointment")
    def post_visit(
        self,
        office_id,
        service_id,
        time,
        date,
        region_id,
        labor_office_id,
        sequence_number,
        sub_service_id,
        requester_type_id,
        visit_reason_id,
        expect_code=201,
        expect_schema="appointment_response.json",
    ):
        # pylint: disable=duplicate-code
        json_body = Visit.visit_body(
            office_id=office_id,
            service_id=service_id,
            time=time,
            date=date,
            region_id=region_id,
            labor_office_id=labor_office_id,
            sequence_number=sequence_number,
            sub_service_id=sub_service_id,
            requester_type_id=requester_type_id,
            visit_reason_id=visit_reason_id,
        )
        response = self.api.post(
            url=self.url, endpoint="/labor-offices/appointment", json=json_body
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="POST /labor-offices/appointment", expect_code=expect_code
        )
        validator.check_response_schema(schema_name=expect_schema)
        self.appointment_id = response.json()["data"]["id"]
        return self

    @allure.step("Edit appointment")
    def put_edit_visit(
        self,
        office_id,
        service_id,
        time,
        date,
        region_id,
        labor_office_id,
        sequence_number,
        sub_service_id,
        requester_type_id,
        appointment_id,
        expect_code=200,
        expect_schema="appointment_response.json",
    ):
        # pylint: disable=duplicate-code
        json_body = Visit.visit_body_edit(
            office_id=office_id,
            service_id=service_id,
            time=time,
            date=date,
            region_id=region_id,
            labor_office_id=labor_office_id,
            sequence_number=sequence_number,
            sub_service_id=sub_service_id,
            requester_type_id=requester_type_id,
            appointment_id=appointment_id,
        )
        response = self.api.put(
            url=self.url, endpoint="/labor-offices/appointment", json=json_body
        )
        validator = ResponseValidator(response)
        validator.check_status_code(name="PUT /labor-offices/appointment", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)
        return self

    @allure.step("Cancel appointment")
    def delete_visit(
        self,
        appointment_id,
        cookies=None,
        expect_code=200,
        expect_schema="appointment_response.json",
    ):
        json_body = Visit.delete_visit_body(appointment_id)
        response = self.api.delete(
            url=self.url, endpoint="/labor-offices/appointment", cookies=cookies, json=json_body
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="DELETE /labor-offices/appointment", expect_code=expect_code
        )
        validator.check_response_schema(schema_name=expect_schema)
        return self
