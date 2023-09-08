from typing import Dict

from data.lo.models import Booking


class Converter:
    @staticmethod
    def json_to_booking(response_json: Dict):
        data = Booking()
        data.appointment_id = response_json["data"]["attributes"]["id"]
        data.personal_number = response_json["data"]["attributes"]["requester-personal-number"]
        data.requester_name = response_json["data"]["attributes"]["requester-name"]
        data.requester_id = response_json["data"]["attributes"]["requester-id"]
        data.appointment_creation_date = response_json["data"]["attributes"]["creation-date"]

        data.appointment_office_id = response_json["data"]["attributes"]["office-id"]
        data.appointment_service_id = response_json["data"]["attributes"]["service-id"]
        data.appointment_time = response_json["data"]["attributes"]["time"]
        data.appointment_date = response_json["data"]["attributes"]["date"]
        data.appointment_region_id = response_json["data"]["attributes"]["region-id"]
        data.appointment_labor_office_id = response_json["data"]["attributes"]["labor-office-id"]
        data.appointment_sequence_number = response_json["data"]["attributes"]["sequence-number"]
        data.appointment_status = response_json["data"]["attributes"]["status-name-localized"]
        data.appointment_request_type = response_json["data"]["attributes"]["requester-type-id"]

        data.appointment_establishment_name = response_json["data"]["attributes"][
            "establishment-name"
        ]
        data.appointment_region_front_en = response_json["data"]["attributes"]["region-name-en"]
        data.appointment_region_front_ar = response_json["data"]["attributes"]["region-name-ar"]

        data.appointment_office_front = response_json["data"]["attributes"]["office-name"]
        data.appointment_status_en = response_json["data"]["attributes"]["status-name-en"]
        data.appointment_status_ar = response_json["data"]["attributes"]["status-name-ar"]
        data.appointment_status_id = response_json["data"]["attributes"]["status-id"]

        data.appointment_service_front_en = response_json["data"]["attributes"]["service-name-en"]
        data.appointment_service_front_ar = response_json["data"]["attributes"]["service-name-ar"]
        return data
