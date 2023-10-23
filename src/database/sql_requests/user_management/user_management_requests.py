from __future__ import annotations

from datetime import datetime

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
        return subscription.expire_date
