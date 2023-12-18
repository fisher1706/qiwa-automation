import config
from src.database.client.db_client import DBClient
from src.database.models.laborer_sso_tables_description import Logins


class LoginRequest:
    session = DBClient(db_url=config.settings.sso_auth_db_url).set_db_session

    def delete_login_data_request(self, account_id: str) -> None:
        logins_data = self.session.query(Logins).filter(Logins.account_id == account_id).all()
        for login_record in logins_data:
            self.session.delete(login_record)
            self.session.commit()
