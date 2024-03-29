import allure
import pytest

from data.user_management.user_management_datasets import (
    DefaultVatValue,
    SubscriptionData,
)
from src.api.app import QiwaApi
from src.api.models.qiwa.raw.user_management_models import SubscriptionCookie
from utils.allure import TestmoProject, project
from utils.assertion import assert_that
from utils.helpers import dround

case_id = project(TestmoProject.USER_MANAGEMENT)


@allure.title("Check that subscription price calculated according to number of Users")
@case_id(16968, 16969, 16970, 16971, 41670, 41671, 41672, 41679)
@pytest.mark.parametrize("user, price, discount", SubscriptionData.subscription_data)
def test_subscription_price_discount(user, price, discount):
    qiwa = QiwaApi.login_as_user(user.personal_number).select_company()
    subscription_cookie = SubscriptionCookie(
        user_id=user.user_id,
        company_sequence_number=user.sequence_number,
        company_labor_office_id=user.labor_office_id,
        user_personal_number=user.personal_number,
    ).dict(by_alias=True)

    subscription_price = qiwa.user_management_api.get_subscription_price_number_of_users(
        cookie=subscription_cookie,
    )

    assert_that(
        dround(price * DefaultVatValue.default_vat_value * discount)
    ).equals_to(subscription_price)
