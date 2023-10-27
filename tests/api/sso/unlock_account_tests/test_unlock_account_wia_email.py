from data.sso import users_data_constants as users_data
from data.sso.messages import TOO_MANY_ABSHER_ATTEMPTS
from src.api.app import QiwaApi
from tests.api.sso.unlock_account_tests.conftest import get_unlock_account_key
from utils.allure import TestmoProject, project
from utils.assertion import assert_that

case_id = project(TestmoProject.QIWA_SSO)


@case_id(57469, 57470)
def test_user_is_able_to_unlock_his_account_by_absher(unlock_account_data):
    qiwa = QiwaApi()
    qiwa.sso.enter_incorrect_password_numerous_times(
        login=unlock_account_data.personal_number, password=users_data.INVALID_PASSWORD
    )
    qiwa.sso.init_hsm_with_out_birthday(unlock_account_data.personal_number)
    qiwa.sso.active_sso_hsm()
    qiwa.sso.unlock_account()


@case_id(57471, 57472)
def test_user_is_able_to_unlock_his_account_by_email(unlock_account_data):
    qiwa = QiwaApi()
    qiwa.sso.enter_incorrect_password_numerous_times(
        login=unlock_account_data.personal_number, password=users_data.INVALID_PASSWORD
    )
    account_id, unlock_key = get_unlock_account_key(unlock_account_data.personal_number)
    qiwa.sso.init_unlock_account_through_email().unlock_account_through_email(
        unlock_key=f"{account_id}A{unlock_key}"
    ).unlock_account_with_otp()


@case_id(57506)
def test_error_message_is_received_after_entering_invalid_otp_code_four_times(unlock_account_data):
    qiwa = QiwaApi()
    qiwa.sso.enter_incorrect_password_numerous_times(
        login=unlock_account_data.personal_number, password=users_data.INVALID_PASSWORD
    )
    qiwa.sso.init_hsm_with_out_birthday(unlock_account_data.personal_number)
    error_message = ...
    for _ in range(4):
        error_message = qiwa.sso.active_sso_hsm(expected_code=422, absher="123456")["errors"][0]["details"]["en"]
    assert_that(error_message).equals_to(TOO_MANY_ABSHER_ATTEMPTS)


@case_id(57474)
def test_resend_otp_code_endpoint_works_on_unlock_account_through_absher(unlock_account_data):
    qiwa = QiwaApi()
    qiwa.sso.enter_incorrect_password_numerous_times(
        login=unlock_account_data.personal_number, password=users_data.INVALID_PASSWORD
    )
    qiwa.sso.init_hsm_with_out_birthday(unlock_account_data.personal_number)
    qiwa.sso.resend_absher_code_on_unlock_account_flow()
