import config
from src.database.client.db_client import DBClient
from src.database.models.db_tables_description import AccountLockouts


class AccountLockoutsRequest:
    session = DBClient(db_url=config.settings.sso_auth_db_url).set_db_session()

    def get_unlock_key(self, account_id: str) -> str:
        key_data = (
            self.session.query(AccountLockouts).filter(AccountLockouts.id == account_id).first()
        )
        return key_data.key
