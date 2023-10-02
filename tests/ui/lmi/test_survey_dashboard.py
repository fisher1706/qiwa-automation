import allure
import pytest

from data.lmi.constants import SurveysInfo, TargetGroups
from data.lmi.data_set import SurveyDataSet
from src.api.lmi.requests.surveys import Surveys
from src.ui.lmi import lmi
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check Synchronization with SurveySparrow')
@case_id(11942, 17287, 17289, 17290, 17323)
def test_sync_with_survey_sparrow_service(login_lmi_user):
    lmi.qiwa_api.dashboard_api_actions.create_sparrow_survey()
    lmi.qiwa_api.dashboard_api_actions.add_question_to_sparrow_survey()
    lmi.dashboard_survey.perform_sync_survey(SurveysInfo.SURVEY_SPARROW_OPTION)
    lmi.dashboard_survey.check_sync_survey_and_question(lmi.qiwa_api.dashboard_api_actions.survey_id)


@allure.title('Check Synchronization with QuestionPro')
@case_id(11942, 17287, 17289, 17290, 17323)
def test_sync_with_question_pro_service(login_lmi_user):
    lmi.qiwa_api.dashboard_api_actions.create_question_pro_survey()
    lmi.dashboard_survey.perform_sync_survey(SurveysInfo.SURVEY_QPRO_OPTION)
    lmi.dashboard_survey.check_sync_survey_and_question(lmi.qiwa_api.dashboard_api_actions.survey_id)


@allure.title('Add survey form Favorite option')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_add_survey_to_favorite_option(login_lmi_user, survey_id):
    lmi.qiwa_api.dashboard_api_actions.put_survey_attribute(survey_id, Surveys.favorite_survey_body(False), lmi.cookie)
    lmi.open_general_survey_tab(survey_id)
    lmi.dashboard_survey.add_survey_to_favorite_option(survey_id)


@allure.title('Remove survey form Favorite option')
@case_id(11909, 11910, 11911, 11912)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_remove_survey_from_favorite_option(login_lmi_user, survey_id):
    lmi.qiwa_api.dashboard_api_actions.put_survey_attribute(survey_id, Surveys.favorite_survey_body(True), lmi.cookie)
    lmi.open_general_survey_tab(survey_id)
    lmi.dashboard_survey.remove_survey_from_favorite_option(survey_id)


@allure.title('Add survey to Target group')
@case_id(17281)
@pytest.mark.skip('Skipped due to absence UI functional')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_add_survey_to_target_group(login_lmi_user, survey_id):
    lmi.qiwa_api.dashboard_api_actions.put_survey_attribute(survey_id,
                                                            Surveys.setup_target_group_body(TargetGroups.RETAIL_MULTI),
                                                            lmi.cookie)
    lmi.open_general_survey_tab(survey_id)
    lmi.dashboard_survey.add_survey_to_target_group(survey_id)


@allure.title('Remove survey from Target group')
@pytest.mark.skip('Skipped due to absence UI functional')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_remove_survey_from_target_group(login_lmi_user, survey_id):
    lmi.qiwa_api.dashboard_api_actions.put_survey_attribute(survey_id,
                                                            Surveys.setup_target_group_body(TargetGroups.ALL),
                                                            lmi.cookie)
    lmi.open_general_survey_tab(survey_id)
    lmi.dashboard_survey.remove_survey_from_target_group(survey_id)


@allure.title('Check Displayed on Individual checkbox')
@pytest.mark.skip('Skipped due to affect for third party QA team')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_setup_to_individual_page(login_lmi_user, survey_id):
    lmi.qiwa_api.dashboard_api_actions.put_survey_attribute(survey_id, Surveys.individual_displayed_body(True),
                                                            lmi.cookie)
    lmi.open_general_survey_tab(survey_id)
    lmi.dashboard_survey.setup_to_individual_page(survey_id)


@allure.title('Check Displayed on Individual checkbox')
@pytest.mark.skip('Skipped due to affect for third party QA team')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_remove_from_individual_page(login_lmi_user, survey_id):
    lmi.qiwa_api.dashboard_api_actions.put_survey_attribute(survey_id, Surveys.individual_displayed_body(False),
                                                            lmi.cookie)
    lmi.open_general_survey_tab(survey_id)
    lmi.dashboard_survey.setup_to_individual_page(survey_id)
