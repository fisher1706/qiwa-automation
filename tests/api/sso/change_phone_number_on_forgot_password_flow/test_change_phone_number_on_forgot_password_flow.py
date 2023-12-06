import pytest

from data.sso import account_data_constants as constants
from data.sso import account_data_constants as users_data
from data.sso import data_constants
from data.sso.messages import INVALID_NID_FOR_INIT
from src.api.app import QiwaApi
from src.database.actions.account_db_action import update_account_email
from src.database.sql_requests.account_request import AccountRequests
from src.database.sql_requests.accounts_phone import AccountsPhonesRequest
from utils.allure import TestmoProject, project
from utils.assertion import assert_that

case_id = project(TestmoProject.QIWA_SSO)


@case_id(57483, 57485)
def test_check_that_user_is_able_to_change_phone_number_from_reset_password_flow(account_data):
    qiwa = QiwaApi()
    qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_reset_password()
    qiwa.sso.verify_phone_number_on_reset_password(new_phone=constants.NEW_PHONE_NUMBER)
    qiwa.sso.confirm_new_phone_verification_on_reset_password()


@case_id(57487)
def test_error_message_in_case_there_are_no_security_questions_for_account(account_data):
    qiwa = QiwaApi()
    qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_reset_password()
    qiwa.sso.verify_phone_number_on_reset_password(new_phone=constants.NEW_PHONE_NUMBER)
    qiwa.sso.confirm_new_phone_verification_on_reset_password()


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
    qiwa.sso.verify_phone_number_on_reset_password(new_phone=constants.NEW_PHONE_NUMBER)
    qiwa.sso.verify_phone_number_on_reset_password(new_phone=constants.NEW_PHONE_NUMBER)

