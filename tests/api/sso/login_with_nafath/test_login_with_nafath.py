import pytest

from data.sso.account_data_constants import INVALID_PERSONAL_NUMBER
from data.sso.error_codes import (
    INVALID_NID_NAFATH,
    NAFATH_INVALID_ATTEMPT_CODE,
    PERSONAL_NUMBER_INVALID,
    USER_HAS_SESSION,
)
from data.sso.messages import NAFATH_INVALID_ATTEMPT, USER_HAS_SESSION_MESSAGE
from src.api.app import QiwaApi
from src.database.sql_requests.sso_requests.account_request import AccountRequests
from utils.allure import TestmoProject, project
from utils.assertion.asserts import assert_that

case_id = project(TestmoProject.QIWA_SSO)


@case_id(129673)
def test_user_is_able_to_login_into_qiwa_with_nafath(account_for_nafath):
    account = account_for_nafath
    qiwa = QiwaApi()
    init_response = qiwa.nafath_sso.init_nafath_login(personal_number=account.personal_number)
    transaction_id = init_response["data"]["attributes"]["transaction-id"]
    qiwa.nafath_sso.nafath_callback(trans_id=transaction_id)
    qiwa.nafath_sso.nafath_authorize_login()
    actual_account_id = qiwa.sso.get_session()["data"]["attributes"]["account-id"]
    assert_that(AccountRequests().get_account_national_id(national_id=account.personal_number)). \
        equals_to(actual_account_id)


@case_id(129674)
def test_user_cant_login_when_nafath_callback_status_is_rejected(account_for_nafath_negative_test):
    account = account_for_nafath_negative_test
    qiwa = QiwaApi()
    init_response = qiwa.nafath_sso.init_nafath_login(personal_number=account.personal_number)
    transaction_id = init_response["data"]["attributes"]["transaction-id"]
    qiwa.nafath_sso.nafath_callback(trans_id=transaction_id, status="REJECTED")
    response = qiwa.nafath_sso.nafath_authorize_login(expected_code=422)
    assert_that(NAFATH_INVALID_ATTEMPT).equals_to(response.json()["errors"][0]["details"]["en"])
    assert_that(NAFATH_INVALID_ATTEMPT_CODE).equals_to(response.json()["errors"][0]["code"])


@pytest.mark.parametrize("invalid_nid", ["1qeqw", INVALID_PERSONAL_NUMBER])
@case_id(129678)
def test_check_init_nafath_with_invalid_nid(invalid_nid):
    qiwa = QiwaApi()
    init_response = qiwa.nafath_sso.init_nafath_login(personal_number=invalid_nid, expected_code=422)
    assert_that(init_response["errors"][0]["code"]).equals_to(INVALID_NID_NAFATH)


@case_id(129677)
def test_check_init_nafath_with_empty_nid():
    qiwa = QiwaApi()
    init_response = qiwa.nafath_sso.init_nafath_login(personal_number="", expected_code=422)
    assert_that(init_response["errors"][0]["code"]).equals_to(PERSONAL_NUMBER_INVALID)


@case_id(129679)
def test_user_cant_start_second_session(account_for_nafath):
    account = account_for_nafath
    qiwa = QiwaApi()
    init_response = qiwa.nafath_sso.init_nafath_login(personal_number=account.personal_number)
    transaction_id = init_response["data"]["attributes"]["transaction-id"]
    qiwa.nafath_sso.nafath_callback(trans_id=transaction_id)
    qiwa.nafath_sso.nafath_authorize_login()
    session_response = qiwa.sso.get_session()["data"]["attributes"]["account-id"]
    assert_that(AccountRequests().get_account_national_id(national_id=account.personal_number))\
        .equals_to(session_response)
    init_response = qiwa.nafath_sso.init_nafath_login(personal_number=account.personal_number, expected_code=403)
    assert_that(USER_HAS_SESSION).equals_to(init_response["errors"][0]["code"])
    assert_that(USER_HAS_SESSION_MESSAGE).equals_to(init_response["errors"][0]["details"]["en"])
