import allure
import pytest

from data.lmi.constants import UserInfo
from data.lmi.data_set import ResultDataSet, SurveyDataSet
from src.api.app import QiwaApi


@allure.title('Check download xlsx result')
@pytest.mark.parametrize('values', SurveyDataSet.survey_data)
def test_download_xlsx_result(values):
    qiwa = QiwaApi.login_as_user(personal_number=UserInfo.LMI_ADMIN_LOGIN)
    qiwa.survey_result_api_actions.get_download_xls_result(*values[:-1])


@allure.title('Check link actions: Create/Edit/Delete/Counter')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_ids_data)
@pytest.mark.parametrize('values', ResultDataSet.result_action_data)
def test_link_action(survey_id, values):
    qiwa = QiwaApi.login_as_user(personal_number=UserInfo.LMI_ADMIN_LOGIN)
    qiwa.survey_result_api_actions.delete_all_links(survey_id)
    qiwa.survey_result_api_actions.create_new_link(survey_id, values[0])
    qiwa.survey_result_api_actions.define_action(values[0], survey_id, values[1])
