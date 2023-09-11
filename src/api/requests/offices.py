import json
from pathlib import Path


class Offices:
    @staticmethod
    def parse_json(filename):
        base_dir = Path(__file__).parent.parent.joinpath("schemas").joinpath(filename)
        with open(base_dir, encoding="utf-8") as schema_file:
            return json.loads(schema_file.read())

    @classmethod
    def offices_body(
        cls,
        office_name,
        hourly_capacity,
        working_hours_from,
        working_hours_to,
        address,
        region_id,
        latitude,
        longitude,
        service_id,
        office_id=None,
        is_electronic_office=False,
    ):
        office_body = cls.parse_json("office.json")
        office_body["included"][0]["id"] = service_id
        office_body["included"][0]["attributes"]["id"] = service_id
        office_body["data"]["id"] = office_id
        office_body["data"]["attributes"]["id"] = office_id
        office_body["data"]["attributes"]["office-name"] = office_name
        office_body["data"]["attributes"]["hourly-capacity"] = hourly_capacity
        office_body["data"]["attributes"]["working-hours-from"] = working_hours_from
        office_body["data"]["attributes"]["working-hours-to"] = working_hours_to
        office_body["data"]["attributes"]["gmap-address"] = address
        office_body["data"]["attributes"]["region-id"] = region_id
        office_body["data"]["attributes"]["latitude"] = latitude
        office_body["data"]["attributes"]["longitude"] = longitude
        office_body["data"]["attributes"]["is-electronic-office"] = is_electronic_office
        office_body["data"]["relationships"]["appointment-service"]["data"][0]["id"] = service_id
        return office_body

    @classmethod
    def office_status_body(cls, office_id, office_status):
        status_body = cls.parse_json("office_status.json")
        status_body["data"]["id"] = office_id
        status_body["data"]["attributes"]["id"] = office_id
        status_body["data"]["attributes"]["is-active"] = office_status
        return status_body
