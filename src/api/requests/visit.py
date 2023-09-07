from utils.schema_parser import load_json_schema


class Visit:
    @classmethod
    def delete_visit_body(cls, appointment_id):
        delete_visit_body = load_json_schema("appointment_delete.json")
        delete_visit_body["data"]["id"] = appointment_id
        delete_visit_body["data"]["attributes"]["id"] = appointment_id
        return delete_visit_body
