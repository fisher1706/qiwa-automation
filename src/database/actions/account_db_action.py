from src.database.sql_requests.sso_requests.account_request import AccountRequests
from src.database.sql_requests.sso_requests.accounts_emails import AccountsEmailsRequest


def update_account_email(iqama_id, created_at):
    account_id = AccountRequests().get_account_iqama_id(iqama_id=iqama_id)
    AccountsEmailsRequest().update_email_date_request(account_id=account_id, created_at=created_at)
