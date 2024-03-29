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
        qiwa.sso.pass_account_security()
    except AssertionError:
        pass
    yield account
    delete_account_data_from_db(account.personal_number)
