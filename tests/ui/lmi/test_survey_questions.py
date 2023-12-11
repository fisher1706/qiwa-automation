import allure
import pytest

from data.lmi.data_set import QuestionDataSet, SurveyDataSet
from src.ui.lmi import lmi
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check reset question weight')
@case_id(11874, 11875, 11880, 11943, 17336)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_reset_question_weight(login_lmi_user, survey_id):
    lmi.qiwa_api.survey_questions_api_actions.put_question_weight(*QuestionDataSet.setup_action_api_data[1], lmi.cookie)
    lmi.qiwa_api.survey_questions_api_actions.put_question_weight(*QuestionDataSet.setup_action_api_data[0], lmi.cookie)
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.reset_question_weight()
    lmi.survey_question.check_reset_values()


@allure.title('Check setup question weight')
@case_id(11876, 17295, 17335)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_setup_question_weight(login_lmi_user, survey_id):
    lmi.qiwa_api.survey_questions_api_actions.post_reset_weight(survey_id, lmi.cookie)
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.setup_question_weight()


@allure.title('Check setup answer weight')
@case_id(11877)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_setup_answer_weights(login_lmi_user, survey_id):
    lmi.qiwa_api.survey_questions_api_actions.post_reset_weight(survey_id, lmi.cookie)
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.setup_answer_weights()


@allure.title('Check setup question code')
@case_id(12006, 17263, 17264, 17265)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_setup_question_code(login_lmi_user, survey_id):
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.setup_question_code()


@allure.title('Check calculation max answer score')
@case_id(12013)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_calculation_max_answer_score(login_lmi_user, survey_id):
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.calculation_max_answer_score()


@allure.title('Check setup invalid question values')
@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2805')
@case_id(11879, 11941, 11944)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
@pytest.mark.parametrize('value', QuestionDataSet.invalid_question_data)
def test_set_invalid_question_value(login_lmi_user, survey_id, value):
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.set_invalid_question_value(value)


@allure.title('Check setup invalid answer score')
@case_id(11879)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
@pytest.mark.parametrize('value', QuestionDataSet.invalid_answer_data)
def test_set_invalid_answer_score(login_lmi_user, survey_id, value):
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.set_invalid_answer_score(value)


@allure.title('Check setup already_exist question code')
@case_id(17266)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_set_already_exist_question_code(login_lmi_user, survey_id):
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.set_already_exist_question_code()


@allure.title('Check setup invalid question code')
@case_id(17334)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
@pytest.mark.parametrize('value', QuestionDataSet.invalid_code_data)
def test_set_invalid_question_code(login_lmi_user, survey_id, value):
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.set_invalid_question_code(value)
