from src.api.app import QiwaApi
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.QIWA_SSO)


@case_id(42021, 42038)
def test__user_is_able_to_login_into_qiwa_with_nafath(account_data):
    qiwa = QiwaApi()
    transaction_id = qiwa.nafath_sso.init_nafath_login(personal_number=account_data.personal_number)
    qiwa.nafath_sso.nafath_callback(trans_id=transaction_id)
    qiwa.nafath_sso.nafath_authorize_login()

