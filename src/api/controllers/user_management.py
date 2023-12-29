from __future__ import annotations

from datetime import datetime, timedelta

import allure

from data.dedicated.models.user import User
from data.user_management.user_management_datasets import Privileges
from src.api.clients.user_management import UserManagementApi
from src.database.sql_requests.user_management.user_management_requests import (
    UserManagementRequests,
)


class UserManagementControllers(UserManagementApi):
    @allure.step("Compare expired date in db and endpoint")
    def compare_expired_date_in_db_and_in_endpoint(
        self, cookie: dict, personal_number: str, unified_number: int
    ) -> UserManagementControllers:
        time = int(self.get_user_subscription_info(cookie))
        utc_time = datetime.utcfromtimestamp(time)
        expired_date = UserManagementRequests().get_expired_date(personal_number, unified_number)
        assert utc_time == expired_date
        return self

    @allure.step("Expiry user subscription")
    def expiry_user_subscription(
        self, personal_number: str, unified_number: int, expiry_date: datetime
    ) -> UserManagementControllers:
        # expiry_date should be in format '2024-10-20 06:00:00.000'
        UserManagementRequests().update_expiry_date_for_um_subscriptions(
            personal_number, unified_number, expiry_date
        )
        self.cron_job_for_expiry_subscription()
        return self

    @allure.step
    def terminate_user_subscription(
        self, cookie: dict, users_personal_number: str, requester_id_number: str
    ) -> int:
        self.patch_terminate_subscription(
            cookie=cookie, users_personal_number=users_personal_number
        )
        subscription_status = UserManagementRequests().get_subscription_status(
            personal_number=users_personal_number, requester_id_number=requester_id_number
        )
        return subscription_status

    def renew_owner_subscription(
        self, cookie: dict, subscribed_user: User, subscription_type: str
    ) -> int:
        subscription_price = float(
            self.get_owner_subscription_price(
                cookie=cookie, subscribed_user_personal_number=subscribed_user.personal_number
            )
        )
        return int(
            self.post_owner_subscription_flow(
                cookie=cookie,
                subscription_type=subscription_type,
                subscription_price=subscription_price,
                subscribed_user_personal_number=subscribed_user.personal_number,
                labor_office_id=subscribed_user.labor_office_id,
                sequence_number=subscribed_user.sequence_number,
                privilege_ids=Privileges.default_privileges,
            )
        )

    @allure.step
    def check_error_on_renew_owner_subscription_for_not_allowed_establishment(
        self, cookie: dict, subscribed_user: User, subscription_type: str
    ) -> UserManagementControllers:
        subscription_price = float(
            self.get_owner_subscription_price(
                cookie=cookie, subscribed_user_personal_number=subscribed_user.personal_number
            )
        )
        self.post_owner_subscription_flow_for_not_allowed_establishment(
            cookie=cookie,
            subscription_type=subscription_type,
            subscription_price=subscription_price,
            personal_number=subscribed_user.personal_number,
            labor_office_id=subscribed_user.labor_office_id,
            sequence_number=subscribed_user.sequence_number,
            privilege_ids=Privileges.default_privileges,
        )
        return self

    def renew_self_subscription(self, cookie: dict, user: User, subscription_type: str) -> int:
        self_price = float(
            self.get_self_subscription_price(
                cookie=cookie,
                labor_office_id=user.labor_office_id,
                sequence_number=user.sequence_number,
            )
        )
        return int(
            self.post_self_flow(
                cookie=cookie,
                labor_office_id=user.labor_office_id,
                sequence_number=user.sequence_number,
                subscription_price=self_price,
                subscription_type=subscription_type,
            )
        )

    @allure.step
    def update_expiry_date_for_owner_subscription(self, user: User) -> UserManagementControllers:
        current_date = datetime.now()
        future_date = current_date + timedelta(days=29)
        UserManagementRequests().update_expiry_date_for_um_subscriptions(
            personal_number=user.personal_number,
            unified_number=user.unified_number_id,
            expiry_date=future_date.strftime("%Y-%m-%d %H:%M:%S.000"),
        )
        return self
