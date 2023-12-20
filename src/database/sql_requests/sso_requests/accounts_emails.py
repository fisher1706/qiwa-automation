from datetime import datetime
from typing import Any

import config
from src.database.client.db_client import DBClient
from src.database.models.laborer_sso_tables_description import AccountsEmails, Emails


class AccountsEmailsRequest:
    def __init__(self):
        self.db_client = DBClient(db_url=config.settings.sso_auth_db_url)
        self.session = self.db_client.set_db_session

    def get_email_confirmation_token_request(self, account_id: str, state: str = "pending") -> str:
        email_token_data = (
            self.session.query(AccountsEmails)
            .filter(AccountsEmails.account_id == account_id, AccountsEmails.state == state)
            .first()
        )
        return email_token_data.confirmation_token

    def get_email_status_request(self, account_id: str, confirmation_token: str):
        email_data = (
            self.session.query(AccountsEmails)
            .filter(
                AccountsEmails.account_id == account_id,
                AccountsEmails.confirmation_token == confirmation_token,
            )
            .first()
        )
        return email_data.state

    def get_email_id(self, account_id: str) -> Any:
        email_data = (
            self.session.query(AccountsEmails)
            .filter(AccountsEmails.account_id == account_id)
            .first()
        )
        try:
            return email_data.email_id
        except AttributeError:
            return None

    def update_email_date_request(self, account_id: str, created_at: datetime) -> None:
        email_data = (
            self.session.query(AccountsEmails)
            .filter(AccountsEmails.account_id == account_id)
            .first()
        )
        email_data.enabled_at = created_at
        self.session.commit()

    def update_email_state(self, account_id: str, new_state: str) -> None:
        email_data = (
            self.session.query(AccountsEmails)
            .filter(AccountsEmails.account_id == account_id)
            .first()
        )
        email_data.enabled_at = None
        email_data.state = new_state
        email_data.enabled = False
        self.session.commit()

    def delete_account_email_data(self, email_id: str) -> None:
        email_records = (
            self.session.query(AccountsEmails).filter(AccountsEmails.email_id == email_id).all()
        )
        for email_record in email_records:
            self.session.delete(email_record)
            self.session.commit()

    def delete_email_record(self, email_id: str) -> None:
        email_records = self.session.query(Emails).filter(Emails.id == email_id).all()
        for email_record in email_records:
            self.session.delete(email_record)
            self.session.commit()
