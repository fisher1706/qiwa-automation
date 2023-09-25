from datetime import datetime, timedelta, timezone

import pytest

from data.account import Account
from data.sso import users_data
from src.api.app import QiwaApi
from src.database.actions.account_db_action import update_account_email
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.QIWA_SSO)


@case_id(41861)
def test_user_with_national_id_registration(clear_saudi_db_registration_data):
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number) \
        .pre_check_user_email(account.email) \
        .register_user(account)
    qiwa.login_as_user(personal_number=account.personal_number)


@case_id(41862)
def test_expat_with_iqama_number_registration(clear_expat_db_registration_data):
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.EXPAT_IQAMA_ID, birth_day=users_data.GREGORIAN_BIRTHDAY)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number) \
        .pre_check_user_email(account.email) \
        .register_user(account)
    qiwa.login_as_user(personal_number=account.personal_number)


@case_id(41865)
def test_pre_check_user_with_already_used_nid(clear_saudi_db_registration_data):
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .register_account_via_sso_api(account=account)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number, expected_code=422)


@case_id(41865)
def test_register_user_with_already_used_iqama(clear_expat_db_registration_data):
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.EXPAT_IQAMA_ID, birth_day=users_data.GREGORIAN_BIRTHDAY)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .register_account_via_sso_api(account=account)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number, expected_code=422)


@case_id(41865, 41870)
@pytest.mark.parametrize("invalid_nid", ["", "6277273053", "12772751"])
def test_registration_with_invalid_nids(invalid_nid):
    qiwa = QiwaApi()
    account = Account(personal_number=invalid_nid)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day, expected_code=422)


@case_id(41866)
def test_user_with_incorrect_birthday_registration_via_qiwa_sso():
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID)
    qiwa.sso.init_sso_hsm(personal_number=account.personal_number, birth_date="2500-01-01", expected_code=422)


@case_id(41867)
def test_active_hsm_too_meny_times_with_different_session(clear_saudi_account_activities):
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day, requests_number=2)
    second_account = Account(personal_number=users_data.EXPAT_IQAMA_ID, birth_day=users_data.GREGORIAN_BIRTHDAY)
    qiwa.sso.init_sso_hsm(second_account.personal_number, second_account.birth_day,
                          requests_number=3, expected_code=422)


@case_id(41869, 41877)
def test_register_user_with_invalid_absher_hsm_step(clear_expat_account_activities):
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .active_sso_hsm(absher="123456", expected_code=422)


@case_id(41881, 41882, 41883)
@pytest.mark.parametrize("email", ["email-mail.com", "email@mail", "email@.com", "@mail.com", '["email-mail.com"]'])
def test_registration_with_invalid_email(email):
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID, email=email)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number) \
        .pre_check_user_email(account.email, expected_code=422)


@case_id(41885)
@pytest.mark.parametrize("invalid_password", [" ", "1q", "qwertyu123@", "12345@#$%^&"])
def test_registration_with_invalid_password(invalid_password):
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID, password=invalid_password)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number) \
        .pre_check_user_email(account.email) \
        .register_user(account, expected_code=422)


@case_id(41886)
def test_registration_without_phone_verification():
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID, confirmation_code="")
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .active_sso_hsm() \
        .register_user(account, expected_code=422)


@case_id(41889, 41890)
@pytest.mark.parametrize("invalid_otp", [" ", "1q", "1238"])
def test_register_user_with_invalid_otp_at_registration_step(invalid_otp):
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.EXPAT_IQAMA_ID, birth_day=users_data.GREGORIAN_BIRTHDAY,
                      confirmation_code=invalid_otp)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number) \
        .pre_check_user_email(account.email) \
        .register_user(account, expected_code=422)


def test_registration_with_registered_phone_number(clear_saudi_db_registration_data, clear_expat_account_activities):
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number) \
        .pre_check_user_email(account.email) \
        .register_user(account)
    qiwa = QiwaApi()
    second_account = Account(personal_number=users_data.EXPAT_IQAMA_ID, birth_day=users_data.GREGORIAN_BIRTHDAY,
                             phone_number=account.phone_number)
    qiwa.sso.init_sso_hsm(second_account.personal_number, second_account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(second_account.phone_number, expected_code=422)


def test_registration_with_registered_email(clear_expat_db_registration_data, clear_saudi_account_activities):
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.EXPAT_IQAMA_ID, birth_day=users_data.GREGORIAN_BIRTHDAY)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number) \
        .pre_check_user_email(account.email) \
        .register_user(account)
    qiwa.sso.login_user(account.personal_number, account.password)
    qiwa.sso.pass_account_security()
    qiwa = QiwaApi()
    second_account = Account(personal_number=users_data.SAUDI_NATIONAL_ID, email=account.email)
    qiwa.sso.init_sso_hsm(second_account.personal_number, second_account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(second_account.phone_number) \
        .pre_check_user_email(second_account.email, expected_code=422) \
        .register_user(second_account, expected_code=422)


def test_registration_with_registered_email_but_has_an_expired_period(clear_expat_db_registration_data,
                                                                      clear_saudi_db_registration_data):
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.EXPAT_IQAMA_ID, birth_day=users_data.GREGORIAN_BIRTHDAY)
    qiwa.sso.init_sso_hsm(account.personal_number, account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number) \
        .pre_check_user_email(account.email) \
        .register_user(account)
    qiwa.sso.login_user(account.personal_number, account.password)
    qiwa.sso.pass_account_security()
    update_account_email(iqama_id=account.personal_number, created_at=datetime.now(timezone.utc) - timedelta(weeks=28))
    second_account = Account(personal_number=users_data.SAUDI_NATIONAL_ID, email=account.email)
    qiwa.sso.init_sso_hsm(second_account.personal_number, second_account.birth_day) \
        .active_sso_hsm() \
        .phone_verification(second_account.phone_number) \
        .pre_check_user_email(second_account.email) \
        .register_user(second_account)


def test_registration_without_high_security_mode():
    qiwa = QiwaApi()
    account = Account(personal_number=users_data.EXPAT_IQAMA_ID)
    qiwa.sso.register_user(account, expected_code=403)
