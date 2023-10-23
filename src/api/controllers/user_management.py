from __future__ import annotations

from datetime import datetime

import allure

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
