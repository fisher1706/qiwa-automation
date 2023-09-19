import json
from pathlib import Path


class Surveys:
    @staticmethod
    def parse_json(filename):
        base_dir = Path(__file__).parent.parent.joinpath("schemas").joinpath(filename)
        with open(base_dir, encoding="utf-8") as schema_file:
            return json.loads(schema_file.read())

    @classmethod
    def update_question_weight_body(
        cls, question_choices_id, question_choices_weight, question_id, question_weight
    ):
        question_body = cls.parse_json("question_weight.json")
        question_body["data"]["attributes"]["question_choices"][0]["id"] = question_choices_id
        question_body["data"]["attributes"]["question_choices"][0][
            "weight"
        ] = question_choices_weight
        question_body["data"]["attributes"]["questions"][0]["id"] = question_id
        question_body["data"]["attributes"]["questions"][0]["weight"] = question_weight
        return question_body

    @classmethod
    def setup_target_group_body(cls, target_group):
        target_group_field = cls.parse_json("target_group.json")
        target_group_field["data"]["attributes"]["sector_ids"] = target_group
        return target_group_field

    @classmethod
    def create_sparrow_survey_body(cls, survey_name, environment):
        sparrow_survey_body = cls.parse_json("create_sparrow_survey.json")
        sparrow_survey_body["name"] = survey_name
        sparrow_survey_body["survey_folder_id"] = environment
        return sparrow_survey_body

    @classmethod
    def create_question_pro_survey_body(cls, survey_name, environment):
        question_pro_survey_body = cls.parse_json("create_question_pro_survey.json")
        question_pro_survey_body["name"] = survey_name
        question_pro_survey_body["folderID"] = environment
        return question_pro_survey_body

    @classmethod
    def update_question_code_body(cls, code):
        question_code_body = cls.parse_json("question_code.json")
        question_code_body["code"] = code
        return question_code_body

    @classmethod
    def create_link_body(cls, survey_id, link_name):
        link_body = cls.parse_json("link.json")
        link_body["data"]["attributes"]["name"] = link_name
        link_body["data"]["attributes"]["survey_id"] = survey_id
        return link_body

    @classmethod
    def edit_link_body(cls, link_id, link_name):
        link_body = cls.parse_json("link.json")
        link_body["data"]["attributes"]["name"] = link_name
        link_body["data"]["attributes"]["id"] = link_id
        return link_body

    @classmethod
    def company_name_body(cls, link_hex):
        company_name_body = cls.parse_json("company_name.json")
        company_name_body["data"]["attributes"]["hex"] = link_hex
        return company_name_body

    @classmethod
    def sync_survey_body(cls, survey_type):
        sync_survey_body = cls.parse_json("sync_survey.json")
        sync_survey_body["source"] = survey_type
        return sync_survey_body

    @classmethod
    def individual_displayed_body(cls, bool_value):
        individual_displayed_body = cls.parse_json("individual_displayed.json")
        individual_displayed_body["data"]["attributes"][
            "is_qiwa_individual_displayed"
        ] = bool_value
        return individual_displayed_body

    @classmethod
    def favorite_survey_body(cls, bool_value):
        favorite_survey_body = cls.parse_json("favorite_survey.json")
        favorite_survey_body["data"]["attributes"]["favorite_survey"] = bool_value
        return favorite_survey_body

    @classmethod
    def add_question_to_sparrow_survey_body(cls, survey_id, tag):
        question_survey_body = cls.parse_json("add_question_to_sparrow_survey.json")
        question_survey_body["survey_id"] = survey_id
        question_survey_body["question"]["tags"][0] = tag
        return question_survey_body
