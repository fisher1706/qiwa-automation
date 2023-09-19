import json
from pathlib import Path


class Dimensions:
    @staticmethod
    def parse_json(filename):
        base_dir = Path(__file__).parent.parent.joinpath("schemas").joinpath(filename)
        with open(base_dir, encoding="utf-8") as schema_file:
            return json.loads(schema_file.read())

    @classmethod
    def dimension_body(cls, name_en, name_ar):
        dimension_body = cls.parse_json("dimension.json")
        dimension_body["data"]["attributes"]["name"] = name_en
        dimension_body["data"]["attributes"]["ar_name"] = name_ar
        return dimension_body

    @classmethod
    def attach_detach_question_body(cls, survey_question_id):
        attach_detach_question_body = cls.parse_json("attach_detach_question.json")
        attach_detach_question_body["data"]["attributes"][
            "survey_question_id"
        ] = survey_question_id
        return attach_detach_question_body
