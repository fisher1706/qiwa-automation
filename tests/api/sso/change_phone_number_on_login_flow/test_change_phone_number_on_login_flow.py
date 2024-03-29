import time
from datetime import datetime, timedelta, timezone

import pytest

from data.sso import account_data_constants as constants
from data.sso.messages import INVALID_NID_FOR_INIT
from src.api.app import QiwaApi
from src.database.actions.account_db_action import update_account_email
from src.database.sql_requests.sso_requests.account_request import AccountRequests
from src.database.sql_requests.sso_requests.accounts_phone import AccountsPhonesRequest
from tests.api.sso.change_phone_number_on_login_flow.conftest import (
    waiting_to_resent_codes,
)
from utils.allure import TestmoProject, project
from utils.assertion import assert_that

case_id = project(TestmoProject.QIWA_SSO)


@case_id(42052, 42053)
def test_change_phone_number_during_login(account_data):
    qiwa = QiwaApi()
    qiwa.sso.login(account_data.personal_number, account_data.password)
    qiwa.sso.init_hsm_for_change_phone_on_login(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_login(account_data.absher_confirmation_code)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER)
    qiwa.sso.confirm_phone_verification_for_change_on_login()


@case_id(57393)
def test_change_phone_number_which_belongs_to_another_account_less_than_six_month(account_data, second_account_data):
    qiwa = QiwaApi()
    qiwa.sso.login(account_data.personal_number, account_data.password)
    qiwa.sso.init_hsm_for_change_phone_on_login(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_login(account_data.absher_confirmation_code)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=second_account_data.phone_number,
                                                          expected_code=422)


@case_id(42054)
def test_change_phone_number_during_login_use_wrong_id_and_dob(account_data):
    qiwa = QiwaApi()
    qiwa.sso.login(account_data.personal_number, account_data.password)
    qiwa.sso.init_hsm_for_change_phone_on_login(constants.INVALID_PERSONAL_NUMBER, account_data.birth_day,
                                                expected_code=422)


@case_id(42055)
def test_change_phone_number_during_login_use_valid_data_and_same_phone_number(account_data):
    qiwa = QiwaApi()
    qiwa.sso.login(account_data.personal_number, account_data.password)
    qiwa.sso.init_hsm_for_change_phone_on_login(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_login(account_data.absher_confirmation_code)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=account_data.phone_number, expected_code=422)


@case_id(42056)
def test_change_phone_number_during_login_use_id_and_dob_from_another_registered_account(account_data,
                                                                                         second_account_data):
    qiwa = QiwaApi()
    qiwa.sso.login(account_data.personal_number, account_data.password)
    qiwa.sso.init_hsm_for_change_phone_on_login(second_account_data.personal_number, second_account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_login(account_data.absher_confirmation_code)
    response = qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER,
                                                                     expected_code=403)
    assert_that(response["errors"][0]["details"]["en"]).equals_to(INVALID_NID_FOR_INIT)


@case_id(42059)
def test_change_phone_number_during_login_use_valid_data_but_email_is_not_verified(account_data):
    qiwa = QiwaApi()
    qiwa.sso.login(account_data.personal_number, account_data.password)
    qiwa.sso.init_hsm_for_change_phone_on_login(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_login(account_data.absher_confirmation_code)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER)
    qiwa.sso.confirm_phone_verification_for_change_on_login()


@case_id(42060)
def test_change_phone_number_during_login_where_user_expired_phone_number(account_data):
    qiwa = QiwaApi()
    account_id = AccountRequests().get_account_national_id(national_id=account_data.personal_number)
    AccountsPhonesRequest().update_phone_enabled_time(
        account_id=account_id, new_time=datetime.now(timezone.utc) - timedelta(weeks=28)
    )
    qiwa.sso.login(account_data.personal_number, account_data.password)
    qiwa.sso.init_hsm_for_change_phone_on_login(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_login(account_data.absher_confirmation_code)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER)
    qiwa.sso.confirm_phone_verification_for_change_on_login()


@case_id(42061)
def test_change_phone_number_during_login_for_gregorian_date_user(expat_account_data):
    qiwa = QiwaApi()
    qiwa.sso.login(expat_account_data.personal_number, expat_account_data.password)
    qiwa.sso.init_hsm_for_change_phone_on_login(expat_account_data.personal_number, expat_account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_login(expat_account_data.absher_confirmation_code)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER)
    qiwa.sso.confirm_phone_verification_for_change_on_login()


@case_id(42063)
def test_change_phone_number_during_login_for_user_with_expired_email(expat_account_data):
    qiwa = QiwaApi()
    update_account_email(iqama_id=expat_account_data.personal_number,
                         created_at=datetime.now(timezone.utc) - timedelta(weeks=28))
    qiwa.sso.login(expat_account_data.personal_number, expat_account_data.password)
    qiwa.sso.init_hsm_for_change_phone_on_login(expat_account_data.personal_number, expat_account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_login(expat_account_data.absher_confirmation_code)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER)
    qiwa.sso.confirm_phone_verification_for_change_on_login()


@case_id(183256, 183258)
@pytest.mark.xfail(reasone="number of init can be changed on the env")
def test_init_hsm_and_resend_code_during_change_phone_on_login_page_flow_more_than_three_times(account_data):
    qiwa = QiwaApi()
    qiwa.sso.login(account_data.personal_number, account_data.password)
    qiwa.sso.init_hsm_for_change_phone_on_login(account_data.personal_number, account_data.birth_day)
    qiwa.sso.resend_init_hsm_for_change_phone_on_login()
    waiting_to_resent_codes(31)
    qiwa.sso.init_hsm_for_change_phone_on_login(account_data.personal_number, account_data.birth_day)
    qiwa.sso.resend_init_hsm_for_change_phone_on_login()
    waiting_to_resent_codes(31)
    qiwa.sso.init_hsm_for_change_phone_on_login(account_data.personal_number, account_data.birth_day)
    qiwa.sso.resend_init_hsm_for_change_phone_on_login()
    waiting_to_resent_codes(31)
    qiwa.sso.init_hsm_for_change_phone_on_login(account_data.personal_number, account_data.birth_day, expected_code=422)
    qiwa.sso.resend_init_hsm_for_change_phone_on_login(expected_code=422)


@case_id(183257)
@pytest.mark.xfail(reasone="time of session can be changed on env")
def test_resend_init_phone_during_change_phone_on_login_page_flow(account_data):
    qiwa = QiwaApi()
    qiwa.sso.login(account_data.personal_number, account_data.password)
    qiwa.sso.init_hsm_for_change_phone_on_login(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_login(account_data.absher_confirmation_code)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER)
    waiting_to_resent_codes(61)
    qiwa.sso.resend_phone_init_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER)
    waiting_to_resent_codes(61)
    qiwa.sso.resend_phone_init_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER)
    waiting_to_resent_codes(61)
    qiwa.sso.resend_phone_init_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER, expected_code=403)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER, expected_code=403)


@case_id(183262, 183265)
def test_resend_init_phone_do_not_work_during_change_phone_on_login_page_flow_after_init_phone_is_blocked(account_data):
    qiwa = QiwaApi()
    qiwa.sso.login(account_data.personal_number, account_data.password)
    qiwa.sso.init_hsm_for_change_phone_on_login(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_login(account_data.absher_confirmation_code)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER, expected_code=422)
    qiwa.sso.resend_phone_init_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER, expected_code=422)
