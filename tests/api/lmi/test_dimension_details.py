import allure
import pytest

from data.lmi.constants import DimensionsInfo, QuestionActions, UserInfo
from data.lmi.data_set import QuestionDataSet, SurveyDataSet
from src.api.app import QiwaApi


@allure.title('Check question actions')
@pytest.mark.parametrize('survey', SurveyDataSet.survey_data)
@pytest.mark.parametrize('value', QuestionDataSet.question_action_data[:2])
def test_question_actions(survey, value):
    qiwa = QiwaApi.login_as_user(personal_number=UserInfo.LMI_ADMIN_LOGIN)
    qiwa.dimensions_api_actions.delete_all_dimensions()
    qiwa.dimensions_api_actions.post_dimension(DimensionsInfo.NAME_EN_CODE, DimensionsInfo.NAME_AR_TEXT)
    qiwa.dimensions_api_actions.attach_questions(survey[0])
    if value[0] == QuestionActions.DETACH:
        qiwa.dimensions_api_actions.detach_questions(survey[0])
