import allure
import pytest

from data.lmi.data_set import QuestionDataSet, SurveyDataSet
from src.ui.lmi import lmi


@allure.title('Check reset question weight')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_reset_question_weight(login_lmi_user, survey_id):
    lmi.qiwa_api.survey_questions_api_actions.put_question_weight(*QuestionDataSet.setup_action_api_data[1], lmi.cookie)
    lmi.qiwa_api.survey_questions_api_actions.put_question_weight(*QuestionDataSet.setup_action_api_data[0], lmi.cookie)
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.reset_question_weight()


@allure.title('Check setup question weight')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_setup_question_weight(login_lmi_user, survey_id):
    lmi.qiwa_api.survey_questions_api_actions.post_reset_weight(survey_id, lmi.cookie)
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.setup_question_weight()


@allure.title('Check setup answer weight')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_setup_answer_weights(login_lmi_user, survey_id):
    lmi.qiwa_api.survey_questions_api_actions.post_reset_weight(survey_id, lmi.cookie)
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.setup_answer_weights()


@allure.title('Check setup question code')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_setup_question_code(login_lmi_user, survey_id):
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.setup_question_code()


@allure.title('Check calculation max answer score')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_calculation_max_answer_score(login_lmi_user, survey_id):
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.calculation_max_answer_score()


@allure.title('Check setup invalid question values')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
@pytest.mark.parametrize('value', QuestionDataSet.invalid_question_data)
def test_set_invalid_question_value(login_lmi_user, survey_id, value):
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.set_invalid_question_value(value)


@allure.title('Check setup invalid answer score')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
@pytest.mark.parametrize('value', QuestionDataSet.invalid_answer_data)
def test_set_invalid_answer_score(login_lmi_user, survey_id, value):
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.set_invalid_answer_score(value)


@allure.title('Check setup invalid question code')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_set_already_exist_question_code(login_lmi_user, survey_id):
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.set_already_exist_question_code()


@allure.title('Check setup invalid question code')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
@pytest.mark.parametrize('value', QuestionDataSet.invalid_code_data)
def test_set_invalid_question_code(login_lmi_user, survey_id, value):
    lmi.open_question_survey_tab(survey_id)
    lmi.survey_question.set_invalid_question_code(value)
