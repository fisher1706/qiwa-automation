from data.sso import account_data_constants as users_data
from src.api.app import QiwaApi
from utils.allure import TestmoProject, project
from utils.assertion import assert_that

case_id = project(TestmoProject.QIWA_SSO)


@case_id(57403, 57404, 57407)
def test_new_registered_user_navigated_to_secure_account_flow_after_login(account_data):
    qiwa = QiwaApi()
    qiwa.sso.login_user(personal_number=account_data.personal_number, password=account_data.password)
    acceptance_criteria = qiwa.sso.check_acceptance_criteria()
    assert_that(acceptance_criteria["data"]["attributes"]["email"]).equals_to(False)
    assert_that(acceptance_criteria["data"]["attributes"]["security-questions"]).equals_to(False)
    qiwa.sso.verify_email_with_otp_code()
    qiwa.sso.confirm_verify_email_with_otp_code()
    qiwa.sso.answer_security_question()
    acceptance_criteria = qiwa.sso.check_acceptance_criteria()
    assert_that(acceptance_criteria["data"]["attributes"]["email"]).equals_to(True)
    assert_that(acceptance_criteria["data"]["attributes"]["security-questions"]).equals_to(True)


@case_id(57408)
def test_that_user_is_able_to_resend_otp_on_confirm_e_mail_step(account_data):
    qiwa = QiwaApi()
    qiwa.sso.login_user(personal_number=account_data.personal_number, password=account_data.password)
    qiwa.sso.verify_email_with_otp_code()
    response = qiwa.sso.resend_otp_on_secure_otp_flow()
    assert_that(response["value"]).equals_to(account_data.email)


@case_id(57415)
def test_that_user_is_able_to_save_answers_for_security_questions_for_his_account(account_data):
    qiwa = QiwaApi()
    qiwa.sso.login_user(personal_number=account_data.personal_number, password=account_data.password)
    acceptance_criteria = qiwa.sso.check_acceptance_criteria()
    assert_that(acceptance_criteria["data"]["attributes"]["security-questions"]).equals_to(False)
    qiwa.sso.answer_security_question()
    acceptance_criteria = qiwa.sso.check_acceptance_criteria()
    assert_that(acceptance_criteria["data"]["attributes"]["security-questions"]).equals_to(True)


@case_id(57416)
def test_user_cant_gave_the_same_answer_for_security_question_twice(account_data):
    qiwa = QiwaApi()
    qiwa.sso.login_user(personal_number=account_data.personal_number, password=account_data.password)
    acceptance_criteria = qiwa.sso.check_acceptance_criteria()
    assert_that(acceptance_criteria["data"]["attributes"]["security-questions"]).equals_to(False)
    qiwa.sso.same_answer()
