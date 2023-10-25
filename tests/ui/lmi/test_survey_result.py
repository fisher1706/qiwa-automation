import allure
import pytest

from data.lmi.constants import DimensionsInfo
from data.lmi.data_set import SurveyDataSet
from src.ui.lmi import lmi
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check download xlsx result')
@pytest.mark.skip("Skipped due to https://employeesgate.atlassian.net/browse/LR-2622")
@case_id(17305, 17305, 17306, 17307, 17308, 17309, 17310, 17325, 17326)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_download_xlsx_result(login_lmi_user, survey_id):
    lmi.open_result_survey_tab(survey_id)
    lmi.result_detail_survey.download_result_xlsx()


@allure.title('Check create link')
@case_id(11933, 17294)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_create_link(login_lmi_user, survey_id):
    lmi.qiwa_api.survey_result_api_actions.delete_all_links(survey_id, lmi.cookie)
    lmi.open_result_survey_tab(survey_id)
    lmi.result_detail_survey.create_new_link()


@allure.title('Check edit link')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_edit_link(login_lmi_user, survey_id):
    lmi.qiwa_api.survey_result_api_actions.delete_all_links(survey_id, lmi.cookie)
    lmi.qiwa_api.survey_result_api_actions.post_link(survey_id, DimensionsInfo.NAME_EN_TEXT, lmi.cookie)
    lmi.open_result_survey_tab(survey_id)
    lmi.result_detail_survey.edit_link()


@allure.title('Check delete link')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_delete_link(login_lmi_user, survey_id):
    lmi.qiwa_api.survey_result_api_actions.delete_all_links(survey_id, lmi.cookie)
    lmi.qiwa_api.survey_result_api_actions.post_link(survey_id, DimensionsInfo.NAME_EN_TEXT, lmi.cookie)
    lmi.open_result_survey_tab(survey_id)
    lmi.result_detail_survey.delete_link()


@allure.title('Check counter of views')
@case_id(11934)
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
def test_counter_of_views(login_lmi_user, survey_id):
    lmi.qiwa_api.survey_result_api_actions.delete_all_links(survey_id, lmi.cookie)
    lmi.qiwa_api.survey_result_api_actions.post_link(survey_id, DimensionsInfo.NAME_EN_TEXT, lmi.cookie)
    lmi.open_result_survey_tab(survey_id)
    lmi.result_detail_survey.check_counter()
