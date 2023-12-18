from __future__ import annotations

import config
from src.database.client.db_client import DBClient
from src.database.models.user_management_tables_description import (
    UMEstablishmentAccess,
    UMPayments,
    UMPrivileges,
    UMSubscriptionPayments,
    UMSubscriptions,
    UserPrivileges,
    Users,
    UserSubscriptions,
)


class UserManagementRequestsDeleteSubscription:
    session = DBClient(db_url=config.settings.um_db_url).set_db_session

    def get_transaction_id(self, personal_number: str, unified_number: int) -> int:
        subscription = (
            self.session.query(UMSubscriptionPayments)
            .filter(
                UMSubscriptionPayments.personal_number == personal_number,
                UMSubscriptionPayments.unified_number == unified_number,
            )
            .first()
        )
        transaction_id = subscription.transaction_id
        return transaction_id

    def subscription_payment(
        self, personal_number: str, unified_number: int
    ) -> UserManagementRequestsDeleteSubscription:
        subscription_payment_to_delete = (
            self.session.query(UMSubscriptionPayments)
            .filter(
                UMSubscriptionPayments.personal_number == personal_number,
                UMSubscriptionPayments.unified_number == unified_number,
            )
            .all()
        )
        for subscription_payment in subscription_payment_to_delete:
            self.session.delete(subscription_payment)
            self.session.commit()
        return self

    def um_payment(self, transaction_id: int) -> UserManagementRequestsDeleteSubscription:
        user_management_payment_to_delete = (
            self.session.query(UMPayments)
            .filter(UMPayments.transaction_id == transaction_id)
            .all()
        )
        for user_management_payment in user_management_payment_to_delete:
            self.session.delete(user_management_payment)
            self.session.commit()
        return self

    def establishment_access(
        self, personal_number: str, unified_number: int
    ) -> UserManagementRequestsDeleteSubscription:
        establishment_access_to_delete = (
            self.session.query(UMEstablishmentAccess)
            .filter(
                UMEstablishmentAccess.personal_number == personal_number,
                UMEstablishmentAccess.unified_number == unified_number,
            )
            .all()
        )
        for establishment_access in establishment_access_to_delete:
            self.session.delete(establishment_access)
            self.session.commit()
        return self

    def subscription(
        self, personal_number: str, unified_number: int
    ) -> UserManagementRequestsDeleteSubscription:
        subscription_to_delete = (
            self.session.query(UMSubscriptions)
            .filter(
                UMSubscriptions.personal_number == personal_number,
                UMSubscriptions.unified_number == unified_number,
            )
            .all()
        )
        for subscription in subscription_to_delete:
            self.session.delete(subscription)
            self.session.commit()
        return self

    def user_subscriptions(
        self, personal_number: str, unified_number: int
    ) -> UserManagementRequestsDeleteSubscription:
        user_info = (
            self.session.query(Users).filter(Users.personal_number == personal_number).first()
        )
        user_id = user_info.id
        user_subscription_to_delete = (
            self.session.query(UserSubscriptions)
            .filter(
                UserSubscriptions.user_id == user_id,
                UserSubscriptions.unified_number == unified_number,
            )
            .all()
        )
        for user_subscription in user_subscription_to_delete:
            self.session.delete(user_subscription)
            self.session.commit()
        return self

    def user_privileges(
        self, personal_number: str, unified_number: int
    ) -> UserManagementRequestsDeleteSubscription:
        user_info = (
            self.session.query(Users).filter(Users.personal_number == personal_number).first()
        )
        user_id = user_info.id
        user_privileges_to_delete = (
            self.session.query(UserPrivileges, UserSubscriptions)
            .join(UserSubscriptions, UserPrivileges.subscription_id == UserSubscriptions.id)
            .filter(
                UserSubscriptions.user_id == user_id,
                UserSubscriptions.unified_number == unified_number,
            )
            .all()
        )
        for user_privileges in user_privileges_to_delete:
            self.session.delete(user_privileges)
            self.session.commit()
        return self

    def um_privileges(
        self, personal_number: str, unified_number: int
    ) -> UserManagementRequestsDeleteSubscription:
        um_privileges_to_delete = (
            self.session.query(UMEstablishmentAccess)
            .select_from(UMPrivileges)
            .join(
                UMPrivileges,
                UMEstablishmentAccess.sequence_number == UMPrivileges.sequence_number,
                UMEstablishmentAccess.personal_number == UMPrivileges.personal_number,
            )
            .filter(
                UMEstablishmentAccess.unified_number == unified_number,
                UMPrivileges.personal_number == personal_number,
            )
            .all()
        )
        for um_privileges in um_privileges_to_delete:
            self.session.delete(um_privileges)
            self.session.commit()
        return self
