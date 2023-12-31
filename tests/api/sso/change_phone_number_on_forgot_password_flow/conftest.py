import time

import pytest

from data.account import Account
from data.sso import account_data_constants as users_data
from src.api.app import QiwaApi
from src.database.actions.auth_db_actions import delete_account_data_from_db


@pytest.fixture
def account_data():
    account = Account(personal_number=users_data.SAUDI_FOR_SIGN_IN)
    qiwa = QiwaApi()
    try:
        qiwa.sso.register_account_via_sso_api(account)
        qiwa.sso.login_user(account.personal_number, account.password)
        qiwa.sso.check_acceptance_criteria()
        qiwa.sso.pass_account_security()
    except AssertionError:
        pass
    yield account
    delete_account_data_from_db(personal_number=account.personal_number)


@pytest.fixture
def expat_account_data():
    account = Account(personal_number=users_data.EXPAT_FOR_SIGN_UP, birth_day="2010-01-01")
    qiwa = QiwaApi()
    try:
        qiwa.sso.register_account_via_sso_api(account)
    except AssertionError:
        pass
    yield account
    delete_account_data_from_db(personal_number=account.personal_number)


@pytest.fixture
def second_account_data():
    account = Account(personal_number=users_data.SECOND_ACCOUNT_FOR_SIGN_IN)
    qiwa = QiwaApi()
    try:
        qiwa.sso.register_account_via_sso_api(account)
    except AssertionError:
        pass
    yield account
    delete_account_data_from_db(personal_number=account.personal_number)


def waiting_to_resent_codes(waiting_time: int):
    # This sleep is needed because we have a timeout on sending reset codes on changing phone number flow
    time.sleep(waiting_time)
