from datetime import datetime, timedelta, timezone

import pytest

from data.account import Account
from data.sso import account_data_constants as users_data
from src.api.app import QiwaApi
from src.database.actions.auth_db_actions import delete_account_data_from_db
from src.database.sql_requests.sso_requests.account_request import AccountRequests
from src.database.sql_requests.sso_requests.accounts_emails import AccountsEmailsRequest
from src.database.sql_requests.sso_requests.accounts_phone import AccountsPhonesRequest


@pytest.fixture
def first_account_data():
    account = Account(
        personal_number=users_data.SAUDI_FOR_SIGN_IN, email="email-for-sign-in@gmail.com"
    )
    qiwa = QiwaApi()
    try:
        qiwa.sso.register_account_via_sso_api(account)
    except AssertionError:
        pass
    qiwa.sso.login(login=account.personal_number, password=account.password)
    qiwa.sso.login_with_otp()
    qiwa.sso.pass_account_security()
    yield account
    delete_account_data_from_db(account.personal_number)


@pytest.fixture
def second_account_data():
    account = Account(
        personal_number=users_data.SECOND_ACCOUNT_FOR_SIGN_IN, email="email-for-signin2@gmail.com"
    )
    qiwa = QiwaApi()
    try:
        qiwa.sso.register_account_via_sso_api(account)
    except AssertionError:
        pass
    qiwa.sso.login(login=account.personal_number, password=account.password)
    qiwa.sso.login_with_otp()
    qiwa.sso.pass_account_security()
    yield account
    delete_account_data_from_db(account.personal_number)


@pytest.fixture
def account_without_hijiri_birth_day(first_account_data):
    AccountRequests().delete_account_hijri_birth_date(
        national_id=first_account_data.personal_number
    )
    return first_account_data


@pytest.fixture
def account_with_unconfirmed_email_status(first_account_data):
    account_id = AccountRequests().get_account_national_id(
        national_id=first_account_data.personal_number
    )
    AccountsEmailsRequest().update_email_state(account_id=account_id, new_state="pending")
    return first_account_data


@pytest.fixture
def account_without_phone(first_account_data):
    account_id = AccountRequests().get_account_national_id(
        national_id=first_account_data.personal_number
    )
    phone_id = AccountsPhonesRequest().get_phone_id(account_id=account_id)
    AccountsPhonesRequest().delete_account_phone_data(phone_id=phone_id, account_id=account_id)
    AccountsPhonesRequest().delete_phone(phone_id=phone_id)
    return first_account_data


@pytest.fixture
def prepare_data_for_sign_in_with_expired_phone(first_account_data):
    account_id = AccountRequests().get_account_national_id(
        national_id=first_account_data.personal_number
    )
    AccountsPhonesRequest().update_phone_enabled_time(
        account_id=account_id, new_time=datetime.now(timezone.utc) - timedelta(weeks=28)
    )
    second_account = Account(
        personal_number=users_data.SECOND_ACCOUNT_FOR_SIGN_IN,
        phone_number=first_account_data.phone_number,
    )
    QiwaApi().sso.register_account_via_sso_api(second_account)
    return first_account_data
