import config
from src.database.client.db_client import DBClient
from src.database.models.laborer_sso_tables_description import (
    AccountLockouts,
    AccountLoginFailures,
)


class AccountLockoutsRequest:
    session = DBClient(db_url=config.settings.sso_auth_db_url).set_db_session

    def get_unlock_key(self, account_id: str) -> str:
        key_data = (
            self.session.query(AccountLockouts).filter(AccountLockouts.id == account_id).first()
        )
        return key_data.key

    def delete_unlock_key_data(self, account_id: str):
        records = (
            self.session.query(AccountLockouts).filter(AccountLockouts.id == account_id).all()
        )
        if records:
            for record in records:
                self.session.delete(record)
                self.session.commit()

    def delete_login_failure(self, account_id: str):
        login_failure_records = (
            self.session.query(AccountLoginFailures)
            .filter(AccountLoginFailures.id == account_id)
            .all()
        )
        if login_failure_records:
            for failure_record in login_failure_records:
                self.session.delete(failure_record)
                self.session.commit()
