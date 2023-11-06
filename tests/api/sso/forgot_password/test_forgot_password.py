from datetime import datetime, timedelta, timezone

import pytest

from data.account import Account
from data.sso import account_data_constants as users_data, data_constants
from src.api.app import QiwaApi
from src.database.actions.account_db_action import update_account_email
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.QIWA_SSO)


@case_id(42021)
def test_reset_password_with_valid_data(account_data):
    qiwa = QiwaApi()
    token = qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_with_out_birthday(account_data.personal_number) \
        .hsm_on_reset_password() \
        .reset_password(new_password=users_data.CHANGED_PASSWORD, token=token)


@case_id(42022)
def test_reset_password_with_invalid_token(account_data):
    qiwa = QiwaApi()
    token = "invalid token"
    qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_with_out_birthday(account_data.personal_number) \
        .hsm_on_reset_password() \
        .reset_password(new_password="123456789aA!", token=token, expected_code=422)

@case_id(42023)
def test_three_attempts_to_reset_the_password_with_invalid_absher_code(account_data):
    pass


@case_id(42040)
def test_that_user_is_unable_to_reset_password_six_times(account_for_many_times_reset):
    qiwa = QiwaApi()
    for number in range(7):
        token = qiwa.sso.init_reset_password(account_for_many_times_reset.personal_number)
        qiwa.sso.init_hsm_with_out_birthday(account_for_many_times_reset.personal_number) \
            .hsm_on_reset_password()
        if number < 7:
            qiwa.sso.reset_password(new_password=users_data.CHANGED_PASSWORD+str(number), token=token)
        else:
            qiwa.sso.reset_password(new_password=users_data.CHANGED_PASSWORD+str(number), token=token,
                                    expected_code=422)


@case_id(42042)
def test_init_reset_password_with_invalid_national_id():
    qiwa = QiwaApi()
    token = "invalid token"
    qiwa.sso.init_reset_password(personal_number="12345678", expected_code=422)


@case_id(42025)
def test_temporary_block_user_for_more_than_three_hsm_session(account_for_many_times_reset):
    qiwa = QiwaApi()
    token = qiwa.sso.init_reset_password(account_for_many_times_reset.personal_number)
    qiwa.sso.init_hsm_with_out_birthday(account_for_many_times_reset.personal_number) \
            .hsm_on_reset_password()
    token = qiwa.sso.init_reset_password(account_for_many_times_reset.personal_number)
    qiwa.sso.init_hsm_with_out_birthday(account_for_many_times_reset.personal_number) \
            .hsm_on_reset_password()
    token = qiwa.sso.init_reset_password(account_for_many_times_reset.personal_number)
    qiwa.sso.init_hsm_with_out_birthday(account_for_many_times_reset.personal_number) \
            .hsm_on_reset_password(expected_code=422)


@pytest.mark.parametrize("absher_code", data_constants.INVALID_ABSHER_CODE)
@case_id(42036, 42046)
def test_activ_hsm_on_reset_password_flow_with_invalid_absher(account_data, absher_code):
    qiwa = QiwaApi()
    token = qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_with_out_birthday(account_data.personal_number) \
        .hsm_on_reset_password(absher_code=absher_code)
