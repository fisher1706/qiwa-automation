from datetime import datetime
from typing import Any

from sqlalchemy import or_

import config
from src.database.client.db_client import DBClient
from src.database.models.laborer_sso_tables_description import (
    AccountsPhone,
    ChangePhoneOnLoginActivityTrails,
    ChangePhoneOnResetPasswordActivityTrails,
    Phones,
)


class AccountsPhonesRequest:
    def __init__(self):
        self.db_client = DBClient(db_url=config.settings.sso_auth_db_url)
        self.session = self.db_client.set_db_session

    def update_phone_enabled_time(self, account_id: str, new_time: datetime) -> None:
        phone_record = (
            self.session.query(AccountsPhone)
            .filter(AccountsPhone.account_id == account_id)
            .first()
        )
        phone_record.enabled_at = new_time
        self.session.commit()

    def get_phone_state_request(self, account_id: str) -> str:
        phone_record = (
            self.session.query(AccountsPhone)
            .filter(AccountsPhone.account_id == account_id)
            .first()
        )
        return phone_record.state

    def get_phone_id(self, account_id: str) -> Any:
        phone_record = (
            self.session.query(AccountsPhone)
            .filter(AccountsPhone.account_id == account_id)
            .first()
        )
        try:
            return phone_record.phone_id
        except AttributeError:
            return None

    def update_phone_state(
        self,
        account_id: str,
        state: str = "disabled",
        enabled: bool = False,
        disabled_time: datetime = datetime.now(),
    ):
        phone_record = (
            self.session.query(AccountsPhone)
            .filter(AccountsPhone.account_id == account_id)
            .first()
        )
        phone_record.state = state
        phone_record.enabled = enabled
        phone_record.disabled_at = disabled_time
        self.session.commit()

    def delete_account_phone_data(self, phone_id: str, account_id: str) -> None:
        self.session.query(AccountsPhone).filter(
            or_(AccountsPhone.phone_id == phone_id, AccountsPhone.account_id == account_id)
        ).delete()
        self.session.commit()

    def delete_phone(self, phone_id: str) -> None:
        phone_records = self.session.query(Phones).filter(Phones.id == phone_id).all()
        for phone_record in phone_records:
            self.session.delete(phone_record)
            self.session.commit()

    def delete_change_phone_activities_on_login_data(self, personal_number: str) -> None:
        self.session.query(ChangePhoneOnLoginActivityTrails).filter(
            ChangePhoneOnLoginActivityTrails.personal_number == personal_number
        ).delete()
        self.session.commit()

    def delete_change_phone_activities_on_reset_pass_data(self, personal_number: str) -> None:
        self.session.query(ChangePhoneOnResetPasswordActivityTrails).filter(
            ChangePhoneOnResetPasswordActivityTrails.personal_number == personal_number
        ).delete()
        self.session.commit()
