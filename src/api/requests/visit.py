import json
from pathlib import Path


class Visit:
    @staticmethod
    def parse_json(filename):
        base_dir = Path(__file__).parent.parent.joinpath("schemas").joinpath(filename)
        with open(base_dir, encoding="utf-8") as schema_file:
            return json.loads(schema_file.read())

    @classmethod
    def lo_otp_body(cls, code):
        lo_otp_body = cls.parse_json("context_lo_otp.json")
        lo_otp_body["data"]["attributes"]["sms-code"] = code
        return lo_otp_body

    @classmethod
    def otp_custom_body(cls, visit_id, service_type, code):
        otp_custom_body = cls.parse_json("otp_custom.json")
        otp_custom_body["data"]["attributes"]["sms-code"] = code
        otp_custom_body["data"]["attributes"]["name"] = f"app-{visit_id}-{service_type}"
        return otp_custom_body

    @classmethod
    def visit_body(
        cls,
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
        appointment_id=None,
    ):
        visit_body = cls.parse_json("appointment.json")
        visit_body["data"]["attributes"]["date"] = date
        visit_body["data"]["attributes"]["time"] = time
        visit_body["data"]["attributes"]["id"] = appointment_id
        visit_body["data"]["attributes"]["labor-office-id"] = labor_office_id
        visit_body["data"]["attributes"]["office-id"] = office_id
        visit_body["data"]["attributes"]["region-id"] = region_id
        visit_body["data"]["attributes"]["requester-type-id"] = requester_type_id
        visit_body["data"]["attributes"]["sequence-number"] = sequence_number
        visit_body["data"]["attributes"]["service-id"] = service_id
        visit_body["data"]["attributes"]["sub-service-id"] = sub_service_id
        visit_body["data"]["attributes"]["visit-reason-id"] = visit_reason_id
        return visit_body

    @classmethod
    def visit_body_edit(
        cls,
        office_id,
        service_id,
        time,
        date,
        region_id,
        labor_office_id,
        sequence_number,
        sub_service_id,
        requester_type_id,
        appointment_id=None,
    ):
        visit_body = cls.parse_json("appointment_edit.json")
        visit_body["data"]["attributes"]["date"] = date
        visit_body["data"]["attributes"]["time"] = time
        visit_body["data"]["attributes"]["id"] = appointment_id
        visit_body["data"]["attributes"]["labor-office-id"] = labor_office_id
        visit_body["data"]["attributes"]["office-id"] = office_id
        visit_body["data"]["attributes"]["region-id"] = region_id
        visit_body["data"]["attributes"]["requester-type-id"] = requester_type_id
        visit_body["data"]["attributes"]["sequence-number"] = sequence_number
        visit_body["data"]["attributes"]["service-id"] = service_id
        visit_body["data"]["attributes"]["sub-service-id"] = sub_service_id
        return visit_body

    @classmethod
    def delete_visit_body(cls, appointment_id):
        delete_visit_body = cls.parse_json("appointment_delete.json")
        delete_visit_body["data"]["id"] = appointment_id
        delete_visit_body["data"]["attributes"]["id"] = appointment_id
        return delete_visit_body

    @classmethod
    def lo_policies_request_body(cls, company_name, city, email, phone, off_day, calendar_type):
        lo_policies_request_body = cls.parse_json("lo_policies_request.json")
        lo_policies_request_body["data"]["attributes"]["company-name"] = company_name
        lo_policies_request_body["data"]["attributes"]["city-id"] = city
        lo_policies_request_body["data"]["attributes"]["email"] = email
        lo_policies_request_body["data"]["attributes"]["phone"] = phone
        lo_policies_request_body["data"]["attributes"]["off-days"][0] = off_day
        lo_policies_request_body["data"]["attributes"]["calendar-type"] = calendar_type
        return lo_policies_request_body

    @classmethod
    def lo_et_request_unified_number_body(
        cls,
        dest_establishment_name,
        dest_labor_office_id,
        dest_sequence_number,
        personal_number,
        employee_name,
        nationality_code,
        source_labor_office_id,
        source_sequence_number,
    ):
        lo_et_request_body = cls.parse_json("lo_employee_trans_request_unif_numb.json")
        lo_et_request_body["data"]["attributes"][
            "destination-establishment-name"
        ] = dest_establishment_name
        lo_et_request_body["data"]["attributes"][
            "destination-labor-office-id"
        ] = dest_labor_office_id
        lo_et_request_body["data"]["attributes"][
            "destination-sequence-number"
        ] = dest_sequence_number
        lo_et_request_body["data"]["attributes"]["employee-name"] = employee_name
        lo_et_request_body["data"]["attributes"]["employee-nationality-code"] = nationality_code
        lo_et_request_body["data"]["attributes"]["employee-personal-number"] = personal_number
        lo_et_request_body["data"]["attributes"]["source-labor-office-id"] = source_labor_office_id
        lo_et_request_body["data"]["attributes"]["source-sequence-number"] = source_sequence_number
        return lo_et_request_body

    @classmethod
    def lo_et_request_another_business_owner_body(
        cls,
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
    ):
        lo_et_request_body = cls.parse_json("lo_employee_trans_request_owner.json")
        lo_et_request_body["data"]["attributes"][
            "destination-establishment-name"
        ] = dest_establishment_name
        lo_et_request_body["data"]["attributes"][
            "destination-labor-office-id"
        ] = dest_labor_office_id
        lo_et_request_body["data"]["attributes"][
            "destination-sequence-number"
        ] = dest_sequence_number
        lo_et_request_body["data"]["attributes"]["employee-iqama-expiry-date"] = date_of_expire
        lo_et_request_body["data"]["attributes"]["employee-name"] = employee_name
        lo_et_request_body["data"]["attributes"]["employee-nationality-code"] = nationality_code
        lo_et_request_body["data"]["attributes"][
            "employee-nationality-name-ar"
        ] = nationality_name_ar
        lo_et_request_body["data"]["attributes"][
            "employee-nationality-name-en"
        ] = nationality_name_en
        lo_et_request_body["data"]["attributes"]["employee-personal-number"] = personal_number
        lo_et_request_body["data"]["attributes"]["source-establishment-id"] = establishment_id
        lo_et_request_body["data"]["attributes"][
            "source-establishment-name"
        ] = source_establishment_name
        return lo_et_request_body

    @classmethod
    def create_new_contract_body(cls, personal_number):
        create_new_contract_body = cls.parse_json("new_contract_body.json")
        create_new_contract_body["CreateNewContractRq"]["Body"]["LaborerDetails"][
            "LaborerIdNo"
        ] = personal_number
        return create_new_contract_body

    @classmethod
    def employee_info_validate_body(cls, personal_number, birth_date):
        employee_info_validate_body = cls.parse_json("employee_info_validate.json")
        employee_info_validate_body["data"]["attributes"][
            "employee-personal-number"
        ] = personal_number
        employee_info_validate_body["data"]["attributes"]["employee-birth-date"] = birth_date
        return employee_info_validate_body

    @classmethod
    def lo_visa_request_body(
        cls,
        gender_id,
        occupation_id,
        nationality_id,
        embassy_id,
        religion_id,
        visas_amount,
        establishment_id,
        type_id,
    ):
        lo_visa_request_body = cls.parse_json("lo_visa_request.json")
        lo_visa_request_body["data"]["attributes"]["gender-id"] = gender_id
        lo_visa_request_body["data"]["attributes"]["occupation-id"] = occupation_id
        lo_visa_request_body["data"]["attributes"]["nationality-id"] = nationality_id
        lo_visa_request_body["data"]["attributes"]["embassy-id"] = embassy_id
        lo_visa_request_body["data"]["attributes"]["religion-id"] = religion_id
        lo_visa_request_body["data"]["attributes"]["visas-amount"] = visas_amount
        lo_visa_request_body["data"]["attributes"]["establishment-id"] = establishment_id
        lo_visa_request_body["data"]["attributes"]["establishment-condition-type-id"] = type_id
        return lo_visa_request_body
