import allure
import pytest

from data.lmi.constants import UserInfo
from data.lmi.data_set import SurveyDataSet
from src.api.app import QiwaApi


@allure.title('Get all surveys')
def test_surveys():
    qiwa = QiwaApi.login_as_user(personal_number=UserInfo.LMI_ADMIN_LOGIN)
    qiwa.dashboard_api_actions.get_surveys()


@allure.title('Synchronization surveys')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_type_data)
def test_sync_surveys(survey_id):
    qiwa = QiwaApi.login_as_user(UserInfo.LMI_ADMIN_LOGIN, UserInfo.DEFAULT_PASSWORD_API)
    qiwa.dashboard_api_actions.sync_surveys(survey_id)


@allure.title('Get survey details')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_type_data)
def test_surveys_detail(survey_id):
    qiwa = QiwaApi.login_as_user(UserInfo.LMI_ADMIN_LOGIN, UserInfo.DEFAULT_PASSWORD_API)
    qiwa.dashboard_api_actions.get_surveys_detail(survey_id)


@allure.title('Setup survey_attribute')
@pytest.mark.parametrize('survey_id', SurveyDataSet.survey_type_data)
@pytest.mark.parametrize('attribute_json, group', SurveyDataSet.survey_attribute_json)
def test_setup_survey_attribute(survey_id, attribute_json, group):
    qiwa = QiwaApi.login_as_user(UserInfo.LMI_ADMIN_LOGIN, UserInfo.DEFAULT_PASSWORD_API)
    print(attribute_json)
    qiwa.dashboard_api_actions.setup_survey_attribute(survey_id, attribute_json, group)
