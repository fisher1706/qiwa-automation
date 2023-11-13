import allure
import pytest

from data.user_management.user_management_datasets import (
    SubscriptionUsers,
    DefaultPercentValue,
)


from src.api.app import QiwaApi
from src.api.models.qiwa.raw.user_management_models import SubscriptionCookie
from utils.allure import TestmoProject, project
from src.api.clients.user_management_response import UmResponse
from src.api.payloads.raw.user_management.um_response_schemas import SubscriptionNumberOfUsers

case_id = project(TestmoProject.USER_MANAGEMENT)


@allure.title("Check that subscription price calculated according to number of Users")
@case_id(16968)
@pytest.mark.parametrize("users", SubscriptionUsers.subscription_users)
def test_subscription_price(users):
    user = users
    qiwa = QiwaApi.login_as_user(user.personal_number).select_company()
    subscription_cookie = SubscriptionCookie(
        user_id=user.user_id,
        company_sequence_number=user.sequence_number,
        company_labor_office_id=user.labor_office_id,
        user_personal_number=user.personal_number,
    ).dict(by_alias=True)

    resp = qiwa.user_management_api.get_subscription_price_number_of_users(
        cookie=subscription_cookie,
    )
    response = UmResponse(resp)
    response.validate_response_schema(SubscriptionNumberOfUsers)\
        .validate_price_value_number_of_users(
        user=user,
        default_percent_value=DefaultPercentValue.percent_value
    )
