import json
from pathlib import Path


class DataPortalBody:
    @staticmethod
    def parse_json(filename):
        base_dir = Path(__file__).parent.parent.joinpath("requests").joinpath(filename)
        with open(base_dir, encoding="utf-8") as schema_file:
            return json.loads(schema_file.read())

    @classmethod
    def get_bearer_token_body(cls):
        bearer_token_body = cls.parse_json("get_bearer_token.json")
        bearer_token_body["client_id"] = "e2ed0f7d738fdeb35237112270825d7d"
        bearer_token_body["client_secret"] = "d58fbd8cf848a5dd13270d211f36b796"
        body = json.dumps(bearer_token_body)
        return json.loads(body)

    @classmethod
    def get_work_force_statistics_body(cls, endpoint_id, filtered_data):
        work_force_statistics_body = cls.parse_json("get_work_force_statistics_rq.json")
        work_force_statistics_body["WFSRequest"]["request"]["dim"]["id"] = endpoint_id
        work_force_statistics_body["WFSRequest"]["request"]["dim"]["params"]["filters"][
            "filter"
        ] = filtered_data
        json_body = json.dumps(work_force_statistics_body)
        return json_body

    @classmethod
    def get_max_date_body(cls):
        max_date_body = cls.parse_json("get_max_date_rq.json")
        json_body = json.dumps(max_date_body)
        return json_body
