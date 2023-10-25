import allure
import pytest

from data.user_management.user_management_datasets import (
    PaymentHeaders,
    SelfSubscriptionType,
)
from data.user_management.user_management_users import owner_account, terminated_owner
from src.api.app import QiwaApi
from src.api.models.qiwa.raw.user_management_models import SubscriptionCookie
from src.database.actions.user_management_db_actions import delete_subscription
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.USER_MANAGEMENT)


@allure.title("E2e self renew/terminate renew/extend subscription flows")
@pytest.mark.skip(
    "waiting to confirmation payment endpoint from IBM team + need a script how to expire user"
)
@case_id(46665, 47002, 46667)
@pytest.mark.parametrize("subscription_type", SelfSubscriptionType.subscription_type)
def test_self_renew_extend_subscription_flows(subscription_type):
    user = owner_account
    delete_subscription(user.personal_number, user.unified_number_id)
    qiwa = QiwaApi.login_as_user(user.personal_number)
    self_subscription_cookie = SubscriptionCookie(
        user_id=user.user_id,
        company_sequence_number=user.sequence_number,
        company_labor_office_id=user.labor_office_id,
        user_personal_number=user.personal_number,
    ).dict(by_alias=True, exclude={"permissions"})
    self_price = float(
        qiwa.user_management_api.get_self_subscription_price(
            cookie=self_subscription_cookie,
            labor_office_id=user.labor_office_id,
            sequence_number=user.sequence_number,
        )
    )
    payment_id = int(
        qiwa.user_management_api.post_self_flow(
            cookie=self_subscription_cookie,
            labor_office_id=user.labor_office_id,
            sequence_number=user.sequence_number,
            subscription_price=self_price,
            subscription_type=subscription_type,
        )
    )
    qiwa.payment.post_create_payment(payment_id=payment_id)
    qiwa.payment.post_confirm_payment(token=PaymentHeaders.authorization, payment_id=payment_id)
    qiwa.user_management_api.get_thank_you_page(self_subscription_cookie, payment_id)


@allure.title("E2e self subscription flows")
@case_id(47003)
@pytest.mark.skip("waiting to confirmation payment endpoint from IBM team")
def test_self_new_subscription_flow():
    user = terminated_owner
    delete_subscription(user.personal_number, user.unified_number_id)
    qiwa = QiwaApi.login_as_user(user.personal_number)
    self_subscription_cookie = SubscriptionCookie(
        user_id=user.user_id,
        company_sequence_number=user.sequence_number,
        company_labor_office_id=user.labor_office_id,
        user_personal_number=user.personal_number,
    ).dict(by_alias=True, exclude={"permissions"})
    self_price = float(
        qiwa.user_management_api.get_self_subscription_price(
            cookie=self_subscription_cookie,
            labor_office_id=user.labor_office_id,
            sequence_number=user.sequence_number,
        )
    )
    payment_id = int(
        qiwa.user_management_api.post_self_flow(
            cookie=self_subscription_cookie,
            labor_office_id=user.labor_office_id,
            sequence_number=user.sequence_number,
            subscription_price=self_price,
            subscription_type="new",
        )
    )
    qiwa.payment.post_create_payment(payment_id=payment_id)
    qiwa.payment.post_confirm_payment(token=PaymentHeaders.authorization, payment_id=payment_id)
    qiwa.user_management_api.get_thank_you_page(self_subscription_cookie, payment_id)
