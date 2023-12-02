from datetime import datetime, timedelta, timezone

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


@case_id(42052, 42053)
def test_check_that_user_is_able_to_change_phone_number_from_reset_password_flow(account_data):
    qiwa = QiwaApi()
    new_password = users_data.CHANGED_PASSWORD
    token = qiwa.sso.init_reset_password(account_data.personal_number)
    qiwa.sso.init_hsm_for_change_phone_on_reset_password(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_reset_password()


    qiwa.sso.init_hsm_for_reset_password(token=token)

    qiwa.sso.init_hsm_for_change_phone_on_login(account_data.personal_number, account_data.birth_day)
    qiwa.sso.activate_hsm_for_change_phone_on_login(account_data.absher_confirmation_code)
    qiwa.sso.phone_verification_for_change_phone_on_login(phone_number=constants.NEW_PHONE_NUMBER)
    qiwa.sso.confirm_phone_verification_for_change_on_login()


