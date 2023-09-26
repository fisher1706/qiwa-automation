import allure

import config
from src.api.assertions.response_validator import ResponseValidator
from src.api.lmi.requests.surveys import Surveys


class SurveyQuestionsApi:
    url = config.qiwa_urls.api

    def __init__(self, api):
        self.api = api
        self.update_code_response = None

    @allure.step("PUT /lmi-admin/surveys/surveys_id/update-weight:: change question weight")
    def put_question_weight(
        self,
        survey_id,
        question_choices_id,
        question_choices_weight,
        question_id,
        question_weight,
        cookies=None,
        expect_code=200,
    ):
        json_body = Surveys.update_question_weight_body(
            question_choices_id, question_choices_weight, question_id, question_weight
        )
        response = self.api.put(
            url=self.url,
            endpoint=f"/lmi-admin/surveys/{survey_id}/update-weight",
            json=json_body,
            cookies=cookies,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="PUT /lmi-admin/surveys/surveys_id/update-weight", expect_code=expect_code
        )
        assert response.text == "success"

    @allure.step("POST /lmi-admin/surveys/survey_id/set-default-weights :: reset weights")
    def post_reset_weight(self, survey_id, cookies=None, expect_code=200):
        response = self.api.post(
            url=self.url,
            endpoint=f"/lmi-admin/surveys/{survey_id}/set-default-weights",
            cookies=cookies,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(
            name="POST /lmi-admin/surveys/survey_id/set-default-weights", expect_code=expect_code
        )
        assert response.text == "success"

    def put_question_code(self, survey_id, question_id, code, cookies=None, expect_code=200):
        json_body = Surveys.update_question_code_body(code)
        response = self.api.put(
            url=self.url,
            endpoint=f"/lmi-admin/surveys/{survey_id}/questions/{question_id}/update-code",
            json=json_body,
            cookies=cookies,
        )
        validator = ResponseValidator(response)
        validator.check_status_code(name="PUT Question code", expect_code=expect_code)
        self.update_code_response = response.json()
