import config
from src.database.client.db_client import DBClient
from src.database.models.laborer_sso_tables_description import (
    AccountPasswordResetKeys,
    ResetPasswordActivityTrails,
)


class AccountPasswordResetRequest:
    session = DBClient(db_url=config.settings.sso_auth_db_url).set_db_session

    def delete_account_password_reset_keys(self, account_id: str) -> None:
        password_reset_key_records = (
            self.session.query(AccountPasswordResetKeys)
            .filter(AccountPasswordResetKeys.id == account_id)
            .all()
        )
        for record in password_reset_key_records:
            self.session.delete(record)
            self.session.commit()

    def delete_reset_password_activities(self, personal_number: str) -> None:
        reset_password_activities_records = (
            self.session.query(ResetPasswordActivityTrails)
            .filter(ResetPasswordActivityTrails.personal_number == personal_number)
            .all()
        )
        for record in reset_password_activities_records:
            self.session.delete(record)
            self.session.commit()
