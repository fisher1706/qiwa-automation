from __future__ import annotations

from datetime import datetime
from typing import Any

import config
from src.database.client.db_client import DBClient
from src.database.models.user_management_tables_description import (
    EstablishmentAddress,
    UMPrivilegesAuditLog,
    UMSubscriptions,
)


class UserManagementRequests:
    def __init__(self):
        self.db_client = DBClient(db_url=config.settings.sso_auth_db_url)
        self.session = self.db_client.set_db_session

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
        self, personal_number: str, unified_number: int, expiry_date: datetime | str
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

    def get_subscription_data(self, personal_number: str, unified_number: int) -> tuple[Any, Any]:
        subscription = (
            self.session.query(UMSubscriptions)
            .filter(
                UMSubscriptions.personal_number == personal_number,
                UMSubscriptions.unified_number == unified_number,
            )
            .first()
        )
        return (
            subscription.subscription_status_id,
            subscription.expiry_date.year - subscription.modified_on.year,
        )

    def update_establishment_data_en(
        self, labor_office: str | int, sequence_id: str | int, district_en: str, street_en: str
    ) -> UserManagementRequests:
        establishment_data = (
            self.session.query(EstablishmentAddress)
            .filter(
                EstablishmentAddress.sequence_id == sequence_id,
                EstablishmentAddress.labor_office == labor_office,
            )
            .first()
        )
        establishment_data.district_en = district_en
        establishment_data.street_en = street_en
        self.session.commit()
        return self

    def clear_establishment_data(
        self, labor_office: str | int, sequence_id: str | int
    ) -> UserManagementRequests:
        establishment_data = (
            self.session.query(EstablishmentAddress)
            .filter(
                EstablishmentAddress.sequence_id == sequence_id,
                EstablishmentAddress.labor_office == labor_office,
            )
            .first()
        )
        establishment_data.district_ar = None
        establishment_data.street_ar = None
        establishment_data.building_number = None
        establishment_data.additional_number = None
        establishment_data.district_en = None
        establishment_data.city_en = None
        establishment_data.street_en = None
        self.session.commit()
        return self
