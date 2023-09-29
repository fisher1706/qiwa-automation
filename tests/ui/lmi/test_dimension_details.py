import allure
import pytest

from data.lmi.constants import DimensionsInfo
from data.lmi.data_set import SurveyDataSet
from src.ui.lmi import lmi
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check attach question')
@case_id(12007, 12008)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_attach_question(login_lmi_user, survey_id):
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT,
                                                       lmi.cookie)
    lmi.open_dimension_survey_tab(survey_id)
    lmi.dimension_details.attach_question_to_dimension()


@allure.title('Check detach question')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_detach_question(login_lmi_user, survey_id):
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT,
                                                       lmi.cookie)
    lmi.qiwa_api.dimensions_api_actions.attach_questions(survey_id, lmi.cookie)
    lmi.open_dimension_survey_tab(survey_id)
    lmi.dimension_details.detach_question_from_dimension()


@allure.title('Check already attached question')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_attach_already_attached_question(login_lmi_user, survey_id):
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT,
                                                       lmi.cookie)
    lmi.qiwa_api.dimensions_api_actions.attach_questions(survey_id, lmi.cookie)
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE_EDIT,
                                                       DimensionsInfo.NAME_AR_TEXT_EDIT, lmi.cookie)
    lmi.open_dimension_survey_tab(survey_id)
    lmi.dimension_details.attach_already_attached_question()


@allure.title('Check cancel attach already attached question')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_cancel_attach_already_attached_question(login_lmi_user, survey_id):
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT,
                                                       lmi.cookie)
    lmi.qiwa_api.dimensions_api_actions.attach_questions(survey_id, lmi.cookie)
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE_EDIT,
                                                       DimensionsInfo.NAME_AR_TEXT_EDIT, lmi.cookie)
    lmi.open_dimension_survey_tab(survey_id)
    lmi.dimension_details.cancel_attach_already_attached_question()


@allure.title('Check cancel detach question')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_cancel_detach_question(login_lmi_user, survey_id):
    lmi.qiwa_api.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT,
                                                       lmi.cookie)
    lmi.qiwa_api.dimensions_api_actions.attach_questions(survey_id, lmi.cookie)
    lmi.open_dimension_survey_tab(survey_id)
    lmi.dimension_details.cancel_detach_question_from_dimension()
