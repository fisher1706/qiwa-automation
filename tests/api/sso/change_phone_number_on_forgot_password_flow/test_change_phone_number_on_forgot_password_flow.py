import pytest

from data.sso import account_data_constants as constants
from src.api.app import QiwaApi
from tests.api.sso.change_phone_number_on_forgot_password_flow.conftest import (
    waiting_to_resent_codes,
)
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.QIWA_SSO)


@case_id(57483, 57485)
def test_check_that_user_is_able_to_change_phone_number_from_reset_password_flow(account_data):
    qiwa = QiwaApi()
    qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_reset_password()
    qiwa.sso.get_security_question_for_change_phone_on_reset_password()
    qiwa.sso.validate_security_answer_for_chane_phone_on_reset_password()
    qiwa.sso.verify_phone_number_on_reset_password(new_phone=constants.NEW_PHONE_NUMBER)
    qiwa.sso.confirm_new_phone_verification_on_reset_password()


@case_id(42054)
def test_change_phone_number_during_login_use_wrong_id_and_dob(account_data):
    qiwa = QiwaApi()
    qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(constants.INVALID_PERSONAL_NUMBER, account_data.birth_day,
                                                         expected_code=422)


@case_id(57488)
def test_validation_on_wrong_answers_on_security_questions(account_data):
    qiwa = QiwaApi()
    qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_reset_password()
    qiwa.sso.get_security_question_for_change_phone_on_reset_password()
    qiwa.sso.validate_security_answer_for_chane_phone_on_reset_password(first_answer="01",
                                                                        second_answer="@",
                                                                        expected_code=422)


@case_id(57490)
def test_init_hsm_is_blocked_after_the_third_init(account_data):
    qiwa = QiwaApi()
    qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day,
                                                         expected_code=422)


@case_id(57491)
def test_resend_otp_code_endpoint_on_mobile_verification_step(account_data):
    qiwa = QiwaApi()
    qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_reset_password()
    qiwa.sso.get_security_question_for_change_phone_on_reset_password()
    qiwa.sso.validate_security_answer_for_chane_phone_on_reset_password()
    qiwa.sso.verify_phone_number_on_reset_password(new_phone=constants.NEW_PHONE_NUMBER)
    qiwa.sso.resend_otp_for_change_phone_on_reset_pass_flow()


@case_id()
@pytest.mark.xfail(reasone="number of init can be changed on the env")
def test_init_and_resend_is_blocked_after_the_third_init_hsm(account_data):
    qiwa = QiwaApi()
    qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    waiting_to_resent_codes(31)
    qiwa.sso.resend_absher_for_change_phone_on_reset_pass_flow()
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    waiting_to_resent_codes(31)
    qiwa.sso.resend_absher_for_change_phone_on_reset_pass_flow()
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    waiting_to_resent_codes(31)
    qiwa.sso.resend_absher_for_change_phone_on_reset_pass_flow()
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day,
                                                         expected_code=422)
    waiting_to_resent_codes(31)
    qiwa.sso.resend_absher_for_change_phone_on_reset_pass_flow(expected_code=422)


@case_id()
@pytest.mark.xfail(reasone="time of session can be changed on env")
def test_resend_otp_code_endpoint_on_mobile_verification_step_is_blocked_after_third_try(account_data):
    qiwa = QiwaApi()
    qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_reset_password()
    qiwa.sso.get_security_question_for_change_phone_on_reset_password()
    qiwa.sso.validate_security_answer_for_chane_phone_on_reset_password()
    qiwa.sso.verify_phone_number_on_reset_password(new_phone=constants.NEW_PHONE_NUMBER)
    qiwa.sso.resend_otp_for_change_phone_on_reset_pass_flow()
    waiting_to_resent_codes(61)
    qiwa.sso.verify_phone_number_on_reset_password(new_phone=constants.NEW_PHONE_NUMBER)
    waiting_to_resent_codes(61)
    qiwa.sso.resend_otp_for_change_phone_on_reset_pass_flow()
    qiwa.sso.verify_phone_number_on_reset_password(new_phone=constants.NEW_PHONE_NUMBER)
    waiting_to_resent_codes(61)
    qiwa.sso.resend_otp_for_change_phone_on_reset_pass_flow(expected_code=403)
    qiwa.sso.verify_phone_number_on_reset_password(new_phone=constants.NEW_PHONE_NUMBER, expected_code=403)


@case_id()
def test_resend_unifonic_code_on_mobile_verification_step_after_init_phone_is_blocked(account_data):
    qiwa = QiwaApi()
    qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_reset_password()
    qiwa.sso.get_security_question_for_change_phone_on_reset_password()
    qiwa.sso.validate_security_answer_for_chane_phone_on_reset_password()
    qiwa.sso.verify_phone_number_on_reset_password(new_phone=constants.NEW_PHONE_NUMBER)
    qiwa.sso.verify_phone_number_on_reset_password(new_phone=constants.NEW_PHONE_NUMBER, expected_code=422)
    qiwa.sso.resend_otp_for_change_phone_on_reset_pass_flow(expected_code=422)

