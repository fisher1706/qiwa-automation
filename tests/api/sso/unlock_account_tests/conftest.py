import pytest

from data.account import Account
from data.sso import account_data_constants as users_data
from src.api.app import QiwaApi
from src.database.actions.auth_db_actions import delete_account_data_from_db
from src.database.sql_requests.account_lockouts import AccountLockoutsRequest
from src.database.sql_requests.account_request import AccountRequests


@pytest.fixture
def unlock_account_data():
    account = Account(personal_number=users_data.ACCOUNT_FOR_UNLOCK)
    qiwa = QiwaApi()
    try:
        qiwa.sso.register_account_via_sso_api(account)
        qiwa.sso.login_user(account.personal_number, account.password)
        qiwa.sso.pass_account_security()
    except AssertionError:
        pass
    yield account
    delete_account_data_from_db(personal_number=account.personal_number)


def get_unlock_account_key(personal_number):
    account_id = AccountRequests().get_account_national_id(national_id=personal_number)
    unlock_key = AccountLockoutsRequest().get_unlock_key(account_id)
    return account_id, unlock_key
