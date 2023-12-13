import random

import allure
import jmespath

from data.lmi.constants import QuestionActions
from src.api.clients.lmi.dashboard_api import DashboardApi
from src.api.clients.lmi.survey_questions_api import SurveyQuestionsApi


class SurveyQuestionsApiAction(SurveyQuestionsApi):
    def __init__(self, api):
        super().__init__(api)
        self.dashboard_api = DashboardApi(api)

    @allure.step("I change question and option weights by reset and setup new weight")
    def update_question_weight(
        self, survey_id, question_id, question_weight, question_choices_id, question_choices_weight
    ):
        self.put_question_weight(
            survey_id, question_id, question_choices_weight, question_choices_id, question_weight
        )
        self.dashboard_api.get_surveys_detail(survey_id)
        assert (
            float(jmespath.search("*.*.*[0].weight", self.dashboard_api.survey)[0][0][0])
            == question_weight
        )
        assert (
            float(
                jmespath.search("*.*.*[0].question_choices[0].weight", self.dashboard_api.survey)[
                    0
                ][0][0]
            )
            == question_choices_weight
        )

    @allure.step("I reset question weight")
    def reset_questions_weight(self, survey_id):
        self.post_reset_weight(survey_id)
        self.dashboard_api.get_surveys_detail(survey_id)
        assert jmespath.search("*.*.*[0].weight", self.dashboard_api.survey)[0][0][0] == "0.0"
        assert (
            jmespath.search("*.*.*[0].question_choices[0].weight", self.dashboard_api.survey)[0][
                0
            ][0]
            == "1.0"
        )

    @allure.step("I update question code")
    def update_question_code(self, survey_id, question_id, code):
        code = code + random.random()
        self.put_question_code(survey_id, question_id, code)
        setup_dict = {"id": question_id, "question_code": str(code)}
        result_dict = jmespath.search(
            "data.attributes.survey_questions[0].{id:id, question_code: question_code}",
            self.update_code_response,
        )
        assert setup_dict == result_dict, (
            f"Values not matched \n Setup values: {setup_dict}\n " f"Actual values: {result_dict}"
        )

    def define_weight_action(self, action, arg):
        actions_dict = {
            QuestionActions.QUESTION_WEIGHT: self.update_question_weight,
            QuestionActions.RESET_WEIGHT: self.reset_questions_weight,
            QuestionActions.QUESTION_CODE: self.update_question_code,
        }
        arg_selector = {
            QuestionActions.QUESTION_WEIGHT: arg,
            QuestionActions.RESET_WEIGHT: arg[:1],
            QuestionActions.QUESTION_CODE: arg[:3],
        }
        if action in arg_selector:
            arg = arg_selector.get(action)
        if action in actions_dict:
            actions_dict[action](*arg)
