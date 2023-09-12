from datetime import datetime, timedelta, timezone

import allure
import pytest

from data.account import Account
from data.sso import users_data
from src.api.app import QiwaApi
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.QIWA_SSO)
qiwa = QiwaApi()


@case_id(6171)
def test_user_with_national_id_registration(clear_db_registration_data_saudi):
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID)
    qiwa.sso.init_sso_hsm(account.personal_number) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number) \
        .pre_check_user_email(account.email) \
        .register_user(account)
    qiwa.login_as_user(personal_number=account.personal_number)


@case_id(6172)
def test_registration_expat_with_valid_data(clear_db_registration_data_expat):
    account = Account(personal_number=users_data.EXPAT_IQAMA_ID)
    qiwa.sso.init_sso_hsm(account.personal_number) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number) \
        .pre_check_user_email(account.email) \
        .register_user(account)
    qiwa.login_as_user(personal_number=account.personal_number)


@case_id(6172)
def test_registration_without_high_security_mode():
    account = Account(personal_number=users_data.EXPAT_IQAMA_ID)
    qiwa.sso.register_user(account, expected_code=403)


@case_id(6173)
def test_pre_check_user_with_already_used_nid(clear_db_registration_data_saudi):
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID)
    qiwa.sso.init_sso_hsm(account.personal_number) \
        .register_account_via_sso_api() \
        .logout()
    qiwa.sso.init_sso_hsm(account.personal_number) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number, expected_code=422)


@case_id(6174)
def test_register_user_with_already_used_iqama(clear_db_registration_data_expat):
    account = Account(personal_number=users_data.EXPAT_IQAMA_ID)
    qiwa.sso.init_sso_hsm(account.personal_number) \
        .register_account_via_sso_api() \
        .logout()
    qiwa.sso.init_sso_hsm(account.personal_number) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number, expected_code=422)


@case_id(6175)
@pytest.mark.parametrize("invalid_nid", ["6277273053", "12772751"])
def test_registration_with_invalid_nids(invalid_nid):
    account = Account(personal_number=invalid_nid)
    qiwa.sso.init_sso_hsm(account.personal_number, expected_code=422)


@pytest.mark.parametrize("email", ["email-mail.com", "email@mail", "email@.com", "@mail.com", '["email-mail.com"]'])
def test_registration_with_invalid_email(email):
    account = Account(personal_number=users_data.EXPAT_IQAMA_ID, email=email)
    qiwa.sso.init_sso_hsm(account.personal_number) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number) \
        .pre_check_user_email(account.email, expected_code=422)


@pytest.mark.parametrize("invalid_password", [" ", "1q", "12345qewrq", "qwertyu123@", "1234Qwerew", "12345@#$%^&"])
def test_registration_with_invalid_password(invalid_password):
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID, password=invalid_password)
    qiwa.sso.init_sso_hsm(account.personal_number) \
        .active_sso_hsm() \
        .phone_verification(account.phone_number) \
        .pre_check_user_email(account.email) \
        .register_user(account)


@case_id()
def test_registration_without_phone_verification(self):
    account = Account(personal_number=users_data.SAUDI_NATIONAL_ID, confirmation_code="")
    qiwa.sso.init_sso_hsm(account.personal_number) \
        .active_sso_hsm() \
        .register_user(account)



#
#     @allure.title('Registration with registered phone number')
#     def test_registration_with_registered_phone_number(self, clear_db_registration_data_expat):
#         self.data.prepare_owner_account(personal_number=UserInfo.NATIONAL_ID_EXPAT)
#         self.auth_api.prepare_hsm(self.data.account)
#         self.auth_api.create_account(self.data.account)
#         self.data.prepare_owner_account(phone_number=self.data.account.phone_number)
#         self.auth_api.api.clean_session_cookies()
#         self.auth_api.prepare_hsm(self.data.account)
#         self.auth_api.phone_verification(self.data.account.phone_number, expected_code=422)
#         self.auth_api.support.validate_response_error(field_name=ApiField.CODE, expected_value=ApiCode.USED_PHONE)
#
#     @allure.title('Registration with invalid birthday')
#     @pytest.mark.parametrize("user_type", SignUpDataset.user_types)
#     def test_init_hsm_with_invalid_birthday(self, user_type):
#         self.data.prepare_owner_account(user_type=user_type)
#         self.auth_api.init_session_hsm(self.data.account.personal_number, year=2050, expected_code=422,
#                                        expect_schema='error.json')
#         self.auth_api.support.validate_response_error(field_name=ApiField.CODE,
#                                                       expected_value=ApiCode.BIRTH_DAY_MORE_CURRENT_DAY)
#
#     @allure.title('Registration with registered email')
#     def test_registration_with_registered_email(self, clear_db_registration_data_expat):
#         self.data.prepare_owner_account(personal_number=UserInfo.NATIONAL_ID_EXPAT)
#         self.auth_api.prepare_hsm(self.data.account)
#         self.auth_api.create_account(self.data.account)
#         self.auth_api.get_session()
#         confirmation_token = get_email_confirmation_token(session=self.db_session, account_id=self.auth_api.account_id)
#         self.auth_api.confirm_verify_user_email(confirmation_token)
#         self.auth_api.api.clean_session_cookies()
#         self.data.prepare_owner_account(user_type=UserType.EXPAT, email=self.data.account.email)
#         self.auth_api.prepare_hsm(self.data.account)
#         self.auth_api.phone_verification(self.data.account.phone_number)
#         self.auth_api.pre_check_user_email(self.data.account.email, expected_code=422)
#         self.auth_api.register_user(self.data.account, expected_code=422)
#         self.auth_api.support.validate_response_error(field_name=ApiField.CODE,
#                                                       expected_value=ApiCode.EMAIL_ALREADY_USED)
#
#     @allure.title('Registration with registered email which already has an expired period')
#     def test_registration_with_registered_email_but_has_an_expired_period(self, clear_db_registration_data_expat):
#         self.data.prepare_owner_account(personal_number=UserInfo.NATIONAL_ID_EXPAT)
#         self.auth_api.prepare_hsm(self.data.account)
#         self.auth_api.create_account(self.data.account)
#         self.auth_api.get_session()
#         confirmation_token = get_email_confirmation_token(session=self.db_session, account_id=self.auth_api.account_id)
#         self.auth_api.confirm_verify_user_email(confirmation_token)
#
#         update_email_date(session=self.db_session, account_id=self.auth_api.account_id,
#                           created_at=datetime.now(timezone.utc) - timedelta(weeks=28),
#                           confirmation_token=confirmation_token)
#
#         self.auth_api.api.clean_session_cookies()
#         self.data.prepare_owner_account(user_type=UserType.EXPAT, email=self.data.account.email)
#         self.auth_api.prepare_hsm(self.data.account)
#         self.auth_api.phone_verification(self.data.account.phone_number)
#         self.auth_api.pre_check_user_email(self.data.account.email)
#         self.auth_api.register_user(self.data.account)
#
#     @allure.title('Registration with invalid otp at activation hsm step')
#     def test_register_user_with_invalid_otp_at_activation_hsm_step(self, clear_expat_account_activities):
#         self.data.prepare_owner_account(personal_number=UserInfo.NATIONAL_ID_EXPAT)
#         self.auth_api.init_session_hsm(self.data.account.personal_number)
#         self.auth_api.active_session_hsm(sms_code='1', expected_code=422)
#         self.auth_api.support.validate_response_error(field_name=ApiField.CODE,
#                                                       expected_value=ApiCode.INVALID_OTP)
#
#     @allure.title('Registration with invalid otp at registration step')
#     def test_register_user_with_invalid_otp_at_registration_step(self):
#         self.data.prepare_owner_account(personal_number=UserInfo.NATIONAL_ID_EXPAT, code='1')
#         self.auth_api.prepare_hsm(self.data.account)
#         self.auth_api.phone_verification(self.data.account.phone_number)
#         self.auth_api.pre_check_user_email(self.data.account.email)
#         self.auth_api.register_user(self.data.account, expected_code=422)
#         self.auth_api.support.validate_response_error(field_name=ApiField.CODE,
#                                                       expected_value=ApiCode.INVALID_OTP)
#
#     @allure.title('Registration with invalid otp at registration step 4 time')
#     def test_register_user_with_invalid_otp_at_registration_step_four_times(self):
#         self.data.prepare_owner_account(personal_number=UserInfo.NATIONAL_ID_EXPAT, code='1')
#         self.auth_api.prepare_hsm(self.data.account)
#         self.auth_api.phone_verification(self.data.account.phone_number)
#         self.auth_api.pre_check_user_email(self.data.account.email)
#         self.auth_api.register_user(self.data.account, expected_code=422)
#         self.auth_api.support.validate_response_error(field_name=ApiField.CODE,
#                                                       expected_value=ApiCode.INVALID_OTP)
#
#     @allure.title('Init HSM to many times')
#     def test_check_hsm_with_four_attempts(self, clear_saudi_account_activities):
#         self.data.prepare_owner_account(personal_number=UserInfo.NATIONAL_ID_SAUDI)
#         self.auth_api.init_session_hsm(self.data.account.personal_number, requests_number=5,
#                                        expected_code=422, expect_schema='error.json')
#         self.auth_api.support.validate_response_error(field_name=ApiField.CODE,
#                                                       expected_value=ApiCode.TOO_MANY_ATTEMPTS_HSM)
#
#     @allure.title('Init HSM to many times with different nid')
#     def test_check_hsm_with_different_nids(self, clear_expat_account_activities):
#         self.data.prepare_owner_account(personal_number=UserInfo.NATIONAL_ID_EXPAT)
#         self.auth_api.init_session_hsm(self.data.account.personal_number, requests_number=2)
#         self.data.prepare_owner_account(user_type=UserType.EXPAT)
#         self.auth_api.init_session_hsm(self.data.account.personal_number, requests_number=3,
#                                        expected_code=422, expect_schema='error.json')
#         self.auth_api.support.validate_response_error(field_name=ApiField.CODE,
#                                                       expected_value=ApiCode.TOO_MANY_ATTEMPTS_HSM)
#
#     @allure.title('Init HSM to many times with different session')
#     def test_check_hsm_with_different_session(self, clear_expat_account_activities):
#         self.data.prepare_owner_account(personal_number=UserInfo.NATIONAL_ID_EXPAT)
#         self.auth_api.init_session_hsm(self.data.account.personal_number, requests_number=2)
#         self.auth_api.api.clean_session_cookies()
#         self.auth_api.init_session_hsm(self.data.account.personal_number, requests_number=3,
#                                        expected_code=422, expect_schema='error.json')
#         self.auth_api.support.validate_response_error(field_name=ApiField.CODE,
#                                                       expected_value=ApiCode.TOO_MANY_ATTEMPTS_HSM)
