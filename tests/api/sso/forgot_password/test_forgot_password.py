import pytest

from data.sso import account_data_constants as users_data
from data.sso import data_constants
from src.api.app import QiwaApi
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.QIWA_SSO)


@case_id(42021, 42038)
def test_reset_password_with_valid_data(account_data):
    qiwa = QiwaApi()
    new_password = users_data.CHANGED_PASSWORD
    token = qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_reset_password(token=token)
    qiwa.sso.hsm_on_reset_password() \
        .reset_password(new_password=new_password, confirm_password=new_password, token=token)


@case_id(42022)
def test_reset_password_with_invalid_token(account_data):
    qiwa = QiwaApi()
    token = "invalid token"
    qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_reset_password(token=token, expected_code=422)


@case_id(42023, 42032)
def test_three_attempts_to_reset_the_password_with_invalid_absher_code(account_data):
    qiwa = QiwaApi()
    token = qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_reset_password(token=token)
    qiwa.sso.hsm_on_reset_password(absher_code=users_data.INVALID_ABSHER_CODE, expected_code=422)
    qiwa.sso.hsm_on_reset_password(absher_code=users_data.INVALID_ABSHER_CODE, expected_code=422)
    qiwa.sso.hsm_on_reset_password(absher_code=users_data.INVALID_ABSHER_CODE, expected_code=422)


@case_id(42040)
def test_that_user_is_unable_to_reset_password_more_than_five_times(account_for_many_times_reset):
    qiwa = QiwaApi()
    new_password = users_data.CHANGED_PASSWORD
    for number in range(5):
        if number < 5:
            token = qiwa.sso.init_reset_password(account_for_many_times_reset.personal_number)
            qiwa.sso.init_hsm_for_reset_password(token=token)
            qiwa.sso.hsm_on_reset_password()
            qiwa.sso.reset_password(new_password=new_password+str(number),
                                    confirm_password=new_password+str(number),
                                    token=token)
        else:
            qiwa.sso.init_reset_password(account_for_many_times_reset.personal_number, expected_code=422)


@case_id(42042)
def test_init_reset_password_with_invalid_national_id():
    qiwa = QiwaApi()
    qiwa.sso.init_reset_password(personal_number=users_data.INVALID_PERSONAL_NUMBER, expected_code=422)


@case_id(42025)
def test_temporary_block_user_for_more_than_three_hsm_session(account_for_many_times_reset):
    qiwa = QiwaApi()
    token = qiwa.sso.init_reset_password(account_for_many_times_reset.personal_number)
    qiwa.sso.init_hsm_for_reset_password(token=token)
    token = qiwa.sso.init_reset_password(account_for_many_times_reset.personal_number)
    qiwa.sso.init_hsm_for_reset_password(token=token, expected_code=422)


@pytest.mark.parametrize("absher_code", data_constants.INVALID_ABSHER_CODE)
@case_id(42036, 42046)
def test_activ_hsm_on_reset_password_flow_with_invalid_absher(account_data, absher_code):
    qiwa = QiwaApi()
    token = qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_reset_password(token=token)
    qiwa.sso.hsm_on_reset_password(absher_code=absher_code, expected_code=422)


@case_id(42034)
def test_resend_sms_link(account_data):
    qiwa = QiwaApi()
    token = qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_reset_password(token=token)
    qiwa.sso.resend_absher_code_on_reset_password_flow()
    qiwa.sso.resend_absher_code_on_reset_password_flow()
    qiwa.sso.resend_absher_code_on_reset_password_flow(expected_code=422)


def test_user_cant_reset_with_different_passwords(account_data):
    qiwa = QiwaApi()
    token = qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_reset_password(token=token)
    qiwa.sso.hsm_on_reset_password() \
        .reset_password(new_password=users_data.CHANGED_PASSWORD,
                        confirm_password=users_data.DEFAULT_PASSWORD,
                        token=token, expected_code=422)
