import random

import allure
import jmespath

import config
from data.lmi.constants import SurveysInfo
from src.api.assertions.response_validator import ResponseValidator
from src.api.lmi.requests.surveys import Surveys


class DashboardApi:
    url = config.qiwa_urls.api

    def __init__(self, api):
        self.api = api
        self.support = ResponseValidator
        self.surveys = None
        self.survey = None
        self.survey_id = None
        self.question_id = None
        self.all_surveys_id = []
        self.tag = random.randint(10, 100)
        """No secure"""
        self.json_headers_sparrow = {
            "Authorization": "Bearer pr2Vtg4jtFIx-Cu8Vw2ryXBnzpjwIikbHTMmAl"
            "85khCXa9VOJ4eDCSFdtxZJjzCG1cIaCz6x_8pM9-9aVIl5yAQw"
        }
        self.json_params_quest_pro = {"apiKey": "c33cc2fa-5cee-463d-8388-8e11c01ee08d"}

    @allure.step("POST /surveys :: post survey to sparrow")
    def create_sparrow_survey(self, expect_code=200):
        json_body = Surveys.create_sparrow_survey_body(
            SurveysInfo.SURVEY_NAME, SurveysInfo.STAGE_ENV_SPARROW
        )
        response = self.api.post(
            url="https://api.surveysparrow.com/v3",
            endpoint="/surveys",
            json=json_body,
            headers=self.json_headers_sparrow,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="POST /surveys :: post survey to sparrow", expect_code=expect_code
        )
        self.survey_id = str(response.json()["data"]["id"])

    @allure.step("GET /lmi-admin/surveys :: get all surveys")
    def get_surveys(self, expect_code=200, expect_schema="surveys.json"):
        response = self.api.get(url=self.url, endpoint="/lmi-admin/surveys")
        validator = ResponseValidator(response)
        validator.check_status_code(name="GET /lmi-admin/surveys", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)
        self.surveys = response.json()
        return self

    @allure.step("POST /lmi-admin/sync-surveys :: surveys synchronization")
    def sync_surveys(self, survey_type, expect_code=200, expect_schema="sync_surveys.json"):
        json_body = Surveys.sync_survey_body(survey_type)
        response = self.api.post(url=self.url, endpoint="/lmi-admin/sync-surveys", json=json_body)
        validator = ResponseValidator(response)
        validator.check_status_code(name="GET /lmi-admin/sync-surveys", expect_code=expect_code)
        validator.check_response_schema(schema_name=expect_schema)
        self.surveys = response.json()

    @allure.step("GET /lmi-admin/surveys/surveys_id/detail :: get surveys details")
    def get_surveys_detail(
        self, surveys_id, cookies=None, expect_code=200, expect_schema="surveys_detail.json"
    ):
        response = self.api.get(
            url=self.url, endpoint=f"/lmi-admin/surveys/{surveys_id}/detail", cookies=cookies
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="GET /lmi-admin/surveys/surveys_id/detail", expect_code=expect_code
        )
        validator.check_response_schema(schema_name=expect_schema)
        self.survey = response.json()
        questions_id = []
        for question in self.survey["data"]["attributes"]["survey_questions"]:
            questions_id.append(question["id"])
        self.question_id = max(questions_id)

    def get_all_surveys_id(self, cookies=None):
        self.get_surveys(cookies)
        for ids in jmespath.search("data.attributes.favorite_surveys[*].id", self.surveys):
            self.all_surveys_id.append(ids)
        for ids in jmespath.search("data.attributes.surveys[*].id", self.surveys):
            self.all_surveys_id.append(ids)

    @allure.step("PUT /lmi-admin/surveys/surveys_id :: define target group")
    def put_target_group(self, surveys_id, target_group, cookies=None, expect_code=200):
        json_body = Surveys.setup_target_group_body(target_group)
        response = self.api.put(
            url=self.url,
            endpoint=f"/lmi-admin/surveys/{surveys_id}",
            cookies=cookies,
            json=json_body,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="PUT /lmi-admin/surveys/surveys_id", expect_code=expect_code
        )
        assert response.text == "success"

    @allure.step("POST /surveys :: post survey to question pro")
    def create_question_pro_survey(self, expect_code=200):
        json_body = Surveys.create_question_pro_survey_body(
            SurveysInfo.SURVEY_NAME, SurveysInfo.STAGE_ENV_QPRO
        )
        response = self.api.post(
            url="https://api.questionpro.com/a/api/v2",
            endpoint=f"/users/{SurveysInfo.USER_ID_QPRO}/surveys",
            json=json_body,
            params=self.json_params_quest_pro,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="POST /surveys :: post survey to question pro", expect_code=expect_code
        )
        self.survey_id = str(response.json()["response"]["surveyID"])

    @allure.step("PUT /lmi-admin/surveys/surveys_id :: setup survey attributes")
    def put_survey_attribute(self, surveys_id, json_body, cookies=None, expect_code=200):
        response = self.api.put(
            url=self.url,
            endpoint=f"/lmi-admin/surveys/{surveys_id}",
            cookies=cookies,
            json=json_body,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="PUT /lmi-admin/surveys/surveys_idd", expect_code=expect_code
        )
        assert response.text == "success"

    @allure.step("POST /surveys :: post add question to sparrow survey")
    def add_question_to_sparrow_survey(self, expect_code=200):
        tag = f"s{self.tag}"
        json_body = Surveys.add_question_to_sparrow_survey_body(self.survey_id, tag)
        response = self.api.post(
            url="https://api.surveysparrow.com/v3",
            endpoint="/questions",
            json=json_body,
            headers=self.json_headers_sparrow,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="POST /surveys :: post add question to sparrow survey", expect_code=expect_code
        )
