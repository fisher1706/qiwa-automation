from datetime import datetime, timezone, timedelta

import pytest

from data.sso import account_data_constants as users_data
from data.sso import data_constants
from data.sso import account_data_constants as constants
from src.api.app import QiwaApi
from src.database.actions.account_db_action import update_account_email
from src.database.sql_requests.account_request import AccountRequests
from src.database.sql_requests.accounts_phone import AccountsPhonesRequest
from utils.allure import TestmoProject, project

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
def test_change_phone_number_during_login(account_data, second_account_data):
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
    qiwa.sso.init_hsm_for_change_phone_on_login(constants.INVALID_PERSONAL_NUMBER, account_data.birth_day, expected_code=422)


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
    qiwa.sso.init_hsm_for_change_phone_on_login(second_account_data.personal_number, second_account_data.birth_day,
                                                expected_code=422)


@case_id(42059)
def test_change_phone_number_during_login_use_valid_data_but_email_is_not_verified(account_data):
    #TODO: not finished need to check with dev
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


