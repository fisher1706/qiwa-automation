from __future__ import annotations

from datetime import datetime

import config
from src.database.client.db_client import DBClient
from src.database.models.user_management_tables_description import (
    UMPrivilegesAuditLog,
    UMSubscriptions,
)


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
        subscription = (
            self.session.query(UMSubscriptions)
            .filter(
                UMSubscriptions.personal_number == personal_number,
                UMSubscriptions.unified_number == unified_number,
            )
            .first()
        )
        subscription.expiry_date = expiry_date
        self.session.commit()
        return self

    def get_subscription_status(self, personal_number: str, requester_id_number: str) -> int:
        subscription = (
            self.session.query(UMSubscriptions)
            .filter(
                UMSubscriptions.personal_number == personal_number,
                UMSubscriptions.requester_id_number == requester_id_number,
            )
            .first()
        )
        return subscription.subscription_status_id

    def get_deleted_status(
        self, personal_number: str, service_id: int, sequence_number: int
    ) -> bool:
        privilege_audit_log = (
            self.session.query(UMPrivilegesAuditLog)
            .filter(
                UMPrivilegesAuditLog.personal_number == personal_number,
                UMPrivilegesAuditLog.service_id == service_id,
                UMPrivilegesAuditLog.sequence_number == sequence_number,
            )
            .order_by(UMPrivilegesAuditLog.log_create_date.desc())
            .first()
        )
        self.session.commit()
        return privilege_audit_log.deleted_status
