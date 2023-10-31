from __future__ import annotations

from datetime import datetime

from sqlalchemy import update

import config
from src.database.client.db_client import DBClient
from src.database.models.user_management_tables_description import UMSubscriptions


class UserManagementRequests:
    session = DBClient(db_url=config.settings.um_db_url).set_db_session()

    def get_expired_date(self, personal_number: str, unified_number: int) -> datetime:
        subscription = (
            self.session.query(UMSubscriptions)
            .filter(
                UMSubscriptions.personal_number == personal_number,
                UMSubscriptions.unified_number == unified_number,
            )
            .first()
        )
        return subscription.expiry_date

    def update_expiry_date_for_um_subscriptions(
        self, personal_number: str, unified_number: int, expiry_date: datetime
    ) -> UserManagementRequests:
        update(UMSubscriptions).where(
            UMSubscriptions.personal_number == personal_number,
            UMSubscriptions.unified_number == unified_number,
        ).value(UMSubscriptions.expiry_date == expiry_date)
        self.session.commit()
        return self
