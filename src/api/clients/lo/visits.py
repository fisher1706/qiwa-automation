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

    def post_lo_otp_auth(self, otp_code="0000", expect_code=200):
        json_body = Visit.lo_otp_body(otp_code)
        response = self.api.post(url=self.url, endpoint="/session/login-with-otp", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="LO OTP auth", expect_code=expect_code)
        return self

    def post_otp_custom(self, appointment_id, service_type, otp_code="0000", expect_code=200):
        json_body = Visit.otp_custom_body(appointment_id, service_type, otp_code)
        response = self.api.post(url=self.url, endpoint="/context/otp/custom", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="OTP custom", expect_code=expect_code)
        return self

    @allure.step("Get all cities")
    def get_cities(self):
        response = self.api.get(url=self.url, endpoint="/labor-offices/cities")
        cities = response.json()
        selected_id = int(cities["data"][0]["id"])
        selected_name = cities["data"][0]["attributes"]["name-ar"]
        for city in cities["data"]:
            if int(city["id"]) > selected_id:
                selected_id = int(city["id"])
                selected_name = city["attributes"]["name-ar"]
        return selected_id, selected_name

    @allure.step(
        "Get all info for particular appointment by agent from lo-agent-system environment"
    )
    def get_appointment_by_agent(
        self, appointment_id, expect_code=200, expect_schema="get_appointment_by_agent.json"
    ):
        response = self.api.get(
            url=self.url, endpoint=f"/labor-offices/appointment/agent/id/{appointment_id}"
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="GET /labor-offices/appointment/agent/id/{appointment_id}",
            expect_code=expect_code,
        )
        validator.check_response_schema(schema_name=expect_schema)
        self.appointment = response.json()
        return self

    @allure.step("Run appointment process")
    def post_appointment_process(self, appointment_id, expect_code=200):
        response = self.api.post(
            url=self.url, endpoint=f"/labor-offices/appointment/{appointment_id}/process"
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="POST /labor-offices/appointment/{appointment_id}/process",
            expect_code=expect_code,
        )
        return self

    @allure.step("Finish appointment")
    def delete_appointment_process(self, expect_code=200):
        response = self.api.delete(url=self.url, endpoint="/labor-offices/appointment/unprocess")
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="DELETE /labor-offices/appointment/unprocess", expect_code=expect_code
        )
        return self

    @allure.step("Get employee info")
    def get_employee_info(self, personal_number, expect_code=200):
        """request for get variables for Employee Transfer with unified number"""
        response = self.api.get(url=self.url, endpoint="/change-sponsor-requests/employee")
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="PUT /change-sponsor-requests/employee", expect_code=expect_code
        )
        users_info = response.json()
        for user_info in users_info["data"]:
            if user_info["id"] == personal_number:
                self.employee_name = user_info["attributes"]["full-name"]
                self.nationality_code = user_info["attributes"]["nationality-code"]
                self.source_sequence_number = user_info["attributes"]["sequence-number"]
                self.source_labor_office_id = user_info["attributes"]["labor-office-id"]
        return self

    @allure.step("Employee validation")
    def post_employee_info_validate(self, personal_number, birth_date, expect_code=200):
        """request for get variables for Employee Transfer with another business owner"""
        json_body = Visit.employee_info_validate_body(personal_number, birth_date)
        response = self.api.post(
            url=self.url, endpoint="/change-sponsor-requests/employee/validate", body=json_body
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="POST /change-sponsor-requests/employee/validate", expect_code=expect_code
        )
        user_info = response.json()
        self.date_of_expire = user_info["included"][1]["attributes"]["iqama-expiry-date"]
        self.employee_name = user_info["included"][1]["attributes"]["full-name"]
        self.nationality_code = user_info["included"][1]["attributes"]["nationality-code"]
        self.nationality_name_ar = user_info["included"][1]["attributes"]["nationality-name-ar"]
        self.nationality_name_en = user_info["included"][1]["attributes"]["nationality-name-en"]
        self.establishment_id = user_info["included"][2]["attributes"]["id"]
        self.source_establishment_name = user_info["included"][2]["attributes"][
            "establishment-name"
        ]
        return self

    @allure.step(
        "Submit Employee transfer request within unified number through appointment by LO Agent"
    )
    def post_employee_trans_request_unified_number(
        self,
        dest_establishment_name,
        dest_labor_office_id,
        dest_sequence_number,
        personal_number,
        employee_name,
        nationality_code,
        source_labor_office_id,
        source_sequence_number,
        expect_code=201,
    ):
        json_body = Visit.lo_et_request_unified_number_body(
            dest_establishment_name,
            dest_labor_office_id,
            dest_sequence_number,
            personal_number,
            employee_name,
            nationality_code,
            source_labor_office_id,
            source_sequence_number,
        )
        response = self.api.post(url=self.url, endpoint="/change-sponsor-requests", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="POST /change-sponsor-requests", expect_code=expect_code)
        self.request_number = response.json()["data"][0]["attributes"]["request-number"]
        return self

    @allure.step(
        "Submit Employee transfer request from another business owner through appointment by LO Agent"
    )
    def post_employee_trans_request_another_business_owner(
        self,
        dest_establishment_name,
        dest_labor_office_id,
        dest_sequence_number,
        personal_number,
        employee_name,
        nationality_code,
        date_of_expire,
        source_establishment_name,
        nationality_name_ar,
        nationality_name_en,
        establishment_id,
        expect_code=201,
    ):
        json_body = Visit.lo_et_request_another_business_owner_body(
            dest_establishment_name,
            dest_labor_office_id,
            dest_sequence_number,
            personal_number,
            employee_name,
            nationality_code,
            date_of_expire,
            nationality_name_ar,
            nationality_name_en,
            establishment_id,
            source_establishment_name,
        )
        response = self.api.post(url=self.url, endpoint="/change-sponsor-requests", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="POST /change-sponsor-requests", expect_code=expect_code)
        self.request_number = response.json()["data"][0]["attributes"]["request-number"]
        return self

    @allure.step("Create contract for user, this is necessary for performing et requests")
    def post_new_contract(self, personal_number, expect_code=200):
        json_body = Visit.create_new_contract_body(personal_number)
        response = self.api.post(
            url=config.settings.ibm_url,
            endpoint="/takamol/staging/contractmanagement/createnewcontract",
            body=json_body,
            headers=self.api.json_headers_ibm,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(name="POST /createnewcontract", expect_code=expect_code)

    @allure.step("Cancel Employee Transfer request")
    def post_cancel_et_request(self, request_number, expect_code=200):
        response = self.api.post(
            url=self.api.emlp_trans_api, endpoint=f"/requests/{request_number}/cancel"
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="POST / employee transfer request cancel", expect_code=expect_code
        )

    @allure.step("Submit Visa request through appointment by LO Agent")
    def post_lo_visa_request(
        self,
        gender_id,
        occupation_id,
        nationality_id,
        embassy_id,
        religion_id,
        visas_amount,
        establishment_id,
        type_id,
        expect_code=200,
        expect_schema="lo_visa_response.json",
    ):
        # pylint: disable=duplicate-code
        json_body = Visit.lo_visa_request_body(
            gender_id,
            occupation_id,
            nationality_id,
            embassy_id,
            religion_id,
            visas_amount,
            establishment_id,
            type_id,
        )
        response = self.api.post(url=self.url, endpoint="/lo-visa-requests", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="POST /lo-visa-requests", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)
        return self

    @allure.step("Get employee transfer request by personal number")
    def get_employee_transfer_request_by_personal_number(
        self, personal_number: str, expect_code: int = 200
    ) -> [Dict, str]:
        response = self.api.get(
            url=self.url,
            endpoint="/change-sponsor-requests/employee-transfer/sent?page=1&per=1000",
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            "GET /change-sponsor-requests/employee-transfer/sent?page=1&per=1000", expect_code
        )
        transfer_request = response.json()["data"]
        for item in reversed(transfer_request):
            if item["attributes"]["laborer-personal-number"] == personal_number:
                return item
        raise AttributeError("Employee transfer request does not exist")

    @allure.step("Cancel issued visas request")
    def post_lo_cancel_issued_visas(self, border_number, expect_code=200):
        response = self.api.post(
            url=self.url, endpoint=f"lo-visa-requests/visas/{border_number}/cancel"
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="POST /lo-visas/{border_number}/cancel", expect_code=expect_code
        )
        return self

    @allure.step("Submit Policies request through appointment by LO Agent")
    def post_lo_policies_request(
        self,
        company_name,
        city,
        email,
        phone,
        off_day,
        calendar_type,
        expect_code=200,
        expect_schema="lo_policies_response.json",
    ):
        json_body = Visit.lo_policies_request_body(
            company_name, city, email, phone, off_day, calendar_type
        )
        response = self.api.post(url=self.url, endpoint="/lo-policies-requests", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="POST /lo-policies-requests", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)
        return self
