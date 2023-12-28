import pytest

from data.account import Account
from data.sso import account_data_constants as users_data
from src.api.app import QiwaApi
from src.database.actions.auth_db_actions import delete_account_data_from_db


@pytest.fixture
def account_for_nafath():
    account = Account(personal_number=users_data.ACCOUNT_FOR_LOGIN_WITH_NAFATH)
    qiwa = QiwaApi()
    try:
        qiwa.sso.register_account_via_sso_api(account)
        qiwa.sso.login(login=account.personal_number, password=account.password)
        qiwa.sso.login_with_otp()
        qiwa.sso.pass_account_security()
    except AssertionError:
        pass
    yield account
    delete_account_data_from_db(personal_number=account.personal_number)


@pytest.fixture
def account_for_nafath_negative_test():
    account = Account(personal_number=users_data.ACCOUNT_FOR_LOGIN_WITH_NAFATH_NEGATIVE)
    qiwa = QiwaApi()
    try:
        qiwa.sso.register_account_via_sso_api(account)
        qiwa.sso.login(login=account.personal_number, password=account.password)
        qiwa.sso.login_with_otp()
        qiwa.sso.pass_account_security()
    except AssertionError:
        pass
    yield account
    delete_account_data_from_db(personal_number=account.personal_number)
