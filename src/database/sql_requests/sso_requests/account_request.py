import config
from src.database.client.db_client import DBClient
from src.database.models.laborer_sso_tables_description import (
    AccountActiveSessionKeys,
    AccountAuthenticationAuditLogs,
    AccountPasswordHashes,
    AccountPreviousPasswordHashes,
    Accounts,
)


class AccountRequests:
    def __init__(self):
        self.db_client = DBClient(db_url=config.settings.sso_auth_db_url)
        self.session = self.db_client.set_db_session

    def update_users_birthday(self, national_id: str) -> None:
        account_record = (
            self.session.query(Accounts).filter(Accounts.national_id == national_id).first()
        )
        account_record.hijri_birth_date = None
        self.session.commit()

    def get_account_national_id(self, national_id: str) -> str:
        account_record = (
            self.session.query(Accounts).filter(Accounts.national_id == national_id).first()
        )
        return account_record.id

    def get_account_iqama_id(self, iqama_id: str) -> str:
        account_record = self.session.query(Accounts).filter(Accounts.iqama_id == iqama_id).first()
        return account_record.id

    def delete_account_record(self, account_id: str) -> None:
        account_records = self.session.query(Accounts).filter(Accounts.id == account_id).all()
        for account_record in account_records:
            self.session.delete(account_record)
            self.session.commit()

    def delete_accounts_password_hashes(self, account_id: str) -> None:
        hashes_record = (
            self.session.query(AccountPasswordHashes)
            .filter(AccountPasswordHashes.id == account_id)
            .first()
        )
        if hashes_record is not None:
            self.session.delete(hashes_record)
            self.session.commit()

    def delete_account_previous_password_hashes(self, account_id: str) -> None:
        previous_hashes_records = (
            self.session.query(AccountPreviousPasswordHashes)
            .filter(AccountPreviousPasswordHashes.account_id == account_id)
            .all()
        )
        for hash_record in previous_hashes_records:
            self.session.delete(hash_record)
            self.session.commit()

    def delete_account_auth_audit_logs(self, account_id: str) -> None:
        account_auth_logs_records = (
            self.session.query(AccountAuthenticationAuditLogs)
            .filter(AccountAuthenticationAuditLogs.account_id == account_id)
            .all()
        )
        for log in account_auth_logs_records:
            self.session.delete(log)
            self.session.commit()

    def delete_account_active_session_key(self, account_id: str) -> None:
        account_active_session_record = (
            self.session.query(AccountActiveSessionKeys)
            .filter(AccountActiveSessionKeys.account_id == account_id)
            .all()
        )
        if account_active_session_record is not None:
            for active_session in account_active_session_record:
                self.session.delete(active_session)
                self.session.commit()

    def delete_account_hijri_birth_date(self, national_id: str) -> None:
        account_data = (
            self.session.query(Accounts).filter(Accounts.national_id == national_id).first()
        )
        account_data.hijri_birth_date = None
        self.session.commit()

    def get_account_hijri_birth_date(self, national_id: str) -> str:
        account_data = (
            self.session.query(Accounts).filter(Accounts.national_id == national_id).first()
        )
        return account_data.hijri_birth_date[0]
