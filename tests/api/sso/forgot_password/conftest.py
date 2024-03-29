import pytest

from data.account import Account
from data.sso import account_data_constants as users_data
from src.api.app import QiwaApi
from src.database.actions.auth_db_actions import delete_account_data_from_db


@pytest.fixture
def account_data():
    account = Account(personal_number=users_data.ACCOUNT_FOR_RESET_PASSWORD)
    qiwa = QiwaApi()
    try:
        qiwa.sso.register_account_via_sso_api(account)
    except AssertionError:
        pass
    yield account
    delete_account_data_from_db(personal_number=account.personal_number)


@pytest.fixture
def account_for_many_times_reset():
    account = Account(personal_number=users_data.ACCOUNT_FOR_MANY_TIMES_RESET)
    qiwa = QiwaApi()
    try:
        qiwa.sso.register_account_via_sso_api(account)
    except AssertionError:
        pass
    yield account
    delete_account_data_from_db(personal_number=account.personal_number)
