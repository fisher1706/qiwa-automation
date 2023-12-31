from src.database.sql_requests.sso_requests.account_lockouts import (
    AccountLockoutsRequest,
)
from src.database.sql_requests.sso_requests.account_request import AccountRequests
from src.database.sql_requests.sso_requests.accounts_emails import AccountsEmailsRequest
from src.database.sql_requests.sso_requests.accounts_password_reset_keys import (
    AccountPasswordResetRequest,
)
from src.database.sql_requests.sso_requests.accounts_phone import AccountsPhonesRequest
from src.database.sql_requests.sso_requests.activities_request import ActivityRequest
from src.database.sql_requests.sso_requests.logins import LoginRequest
from src.database.sql_requests.sso_requests.oauth_applications import AppRequest
from src.database.sql_requests.sso_requests.security_question_request import (
    SecurityQuestionsRequest,
)


def delete_account_data_from_db(personal_number: str):
    if personal_number.startswith("1"):
        account_id = AccountRequests().get_account_national_id(national_id=personal_number)
    else:
        account_id = AccountRequests().get_account_iqama_id(iqama_id=personal_number)
    email_id = AccountsEmailsRequest().get_email_id(account_id=account_id)
    phone_id = AccountsPhonesRequest().get_phone_id(account_id=account_id)
    ActivityRequest().delete_activities_request(national_id=personal_number)
    AccountsEmailsRequest().delete_account_email_data(email_id=email_id)
    if email_id is not None:
        AccountsEmailsRequest().delete_email_record(email_id=email_id)
    AccountsPhonesRequest().delete_account_phone_data(phone_id=phone_id, account_id=account_id)
    if phone_id is not None:
        AccountsPhonesRequest().delete_phone(phone_id=phone_id)
    try:
        AccountPasswordResetRequest().delete_account_password_reset_keys(account_id=account_id)
        AccountPasswordResetRequest().delete_reset_password_activities(
            personal_number=personal_number
        )
    finally:
        pass
    AccountRequests().delete_account_auth_audit_logs(account_id=account_id)
    LoginRequest().delete_login_data_request(account_id=account_id)
    AccountRequests().delete_account_previous_password_hashes(account_id=account_id)
    AccountRequests().delete_accounts_password_hashes(account_id=account_id)
    AccountRequests().delete_account_active_session_key(account_id=account_id)
    AppRequest().delete_oauth_grants_data_request(account_id=account_id)
    AccountLockoutsRequest().delete_login_failure(account_id=account_id)
    AccountLockoutsRequest().delete_unlock_key_data(account_id=account_id)
    SecurityQuestionsRequest().delete_security_question_request(account_id=account_id)
    AccountRequests().delete_account_record(account_id=account_id)
    AccountsPhonesRequest().delete_change_phone_activities_on_login_data(
        personal_number=personal_number
    )
    AccountsPhonesRequest().delete_change_phone_activities_on_reset_pass_data(
        personal_number=personal_number
    )


def delete_account_activities_data(personal_number: str):
    ActivityRequest().delete_activities_request(national_id=personal_number)
