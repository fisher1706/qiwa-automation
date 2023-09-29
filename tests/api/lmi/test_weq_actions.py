import allure
import pytest

from data.lmi.constants import Actions, DimensionsInfo, UserInfo
from data.lmi.data_set import DimensionDataSet, SurveyDataSet
from src.api.app import QiwaApi
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Check dimension actions: Create/Edit/Delete')
@case_id(11901)
@pytest.mark.parametrize('values', DimensionDataSet.dimension_action_data[:-2])
def test_dimension_action(values):
    qiwa = QiwaApi.login_as_user(personal_number=UserInfo.LMI_ADMIN_LOGIN)
    qiwa.dimensions_api_actions.delete_all_dimensions()
    qiwa.dimensions_api_actions.create_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT,
                                                 DimensionsInfo.NAME_EN_TEXT)
    if values[0] == Actions.EDIT or values[0] == Actions.DELETE:
        qiwa.dimensions_api_actions.define_action(values[0], (DimensionsInfo.NAME_EN_CODE_EDIT,
                                                              DimensionsInfo.NAME_AR_TEXT_EDIT,
                                                              DimensionsInfo.NAME_EN_TEXT_EDIT))


@allure.title('Overall index calculation')
@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2343')
@pytest.mark.parametrize('survey, survey_results, target_group', SurveyDataSet.survey_data)
def test_overall_index_calculation(survey, survey_results, target_group):
    qiwa = QiwaApi.login_as_user(personal_number=UserInfo.LMI_ADMIN_LOGIN)
    qiwa.dashboard_api_actions.put_target_group(survey, target_group)
    qiwa.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT)
    qiwa.dimensions_api_actions.attach_questions(survey)
    qiwa.weq_api_actions.perform_calculation(survey, survey_results)
