import json
from pathlib import Path


class Services:
    @staticmethod
    def parse_json(filename):
        base_dir = Path(__file__).parent.parent.joinpath("schemas").joinpath(filename)
        with open(base_dir, encoding="utf-8") as schema_file:
            return json.loads(schema_file.read())

    @classmethod
    def service_multi_body(
        cls,
        requester_type_id,
        request_type,
        name_en=None,
        name_ar=None,
        service_id=None,
        service_status=True,
    ):
        service_multi_body = cls.parse_json("service_multi.json")
        service_multi_body["data"]["type"] = request_type
        service_multi_body["data"]["id"] = service_id
        service_multi_body["data"]["attributes"]["name-en"] = name_en
        service_multi_body["data"]["attributes"]["name-ar"] = name_ar
        service_multi_body["data"]["attributes"]["id"] = service_id
        service_multi_body["data"]["attributes"]["is-active"] = service_status
        service_multi_body["data"]["attributes"]["requester-type-id"] = requester_type_id
        return service_multi_body
