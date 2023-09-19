import allure
import pytest

from data.lmi.constants import UserInfo
from data.lmi.data_set import QuestionDataSet
from src.api.app import QiwaApi


@allure.title('Check question/answer weight actions')
@pytest.mark.parametrize('action', QuestionDataSet.setup_action_data[:3])
@pytest.mark.parametrize('values', QuestionDataSet.setup_action_api_data)
def test_question_weight_actions(action, values):
    qiwa = QiwaApi.login_as_user(personal_number=UserInfo.LMI_ADMIN_LOGIN)
    qiwa.dimensions_api_actions.delete_all_dimensions()
    qiwa.survey_questions_api_actions.define_weight_action(action[0], values)
