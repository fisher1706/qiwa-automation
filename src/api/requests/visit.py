from utils.schema_parser import load_json_schema


class Visit:
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
        visit_body = load_json_schema("appointment.json")
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
        visit_body = load_json_schema("appointment_edit.json")
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
        delete_visit_body = load_json_schema("appointment_delete.json")
        delete_visit_body["data"]["id"] = appointment_id
        delete_visit_body["data"]["attributes"]["id"] = appointment_id
        return delete_visit_body
