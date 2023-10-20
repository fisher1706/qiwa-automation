import pytest

from data.account import Account
from data.sso import users_data_constants as users_data
from src.api.app import QiwaApi
from src.database.actions.auth_db_actions import (
    delete_account_data_from_db,
)


@pytest.fixture
def unlock_account_data():
    account = Account(
        personal_number=users_data.ACCOUNT_FOR_UNLOCK
    )
    qiwa = QiwaApi()
    qiwa.sso.register_account_via_sso_api(account)
    qiwa.sso.login_user(account.personal_number, account.password)
    qiwa.sso.pass_account_security()
    return account


@pytest.fixture
def clear_saudi_db_registration_data():
    yield
    delete_account_data_from_db(personal_number=users_data.ACCOUNT_FOR_UNLOCK)
