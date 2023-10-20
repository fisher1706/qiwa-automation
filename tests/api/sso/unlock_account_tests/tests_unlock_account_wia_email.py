from src.api.app import QiwaApi
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.QIWA_SSO)


@case_id(57472)
def test_user_is_able_to_unlock_his_account_by_email(unlock_account_data, clear_saudi_db_registration_data):
    qiwa = QiwaApi()
    account = unlock_account_data
    qiwa.login_as_user(personal_number=account.personal_number)
