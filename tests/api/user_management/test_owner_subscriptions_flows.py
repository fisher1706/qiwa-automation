import allure
import pytest

from data.user_management.user_management_datasets import (
    PaymentHeaders,
    Privileges,
    SelfSubscriptionType,
)
from data.user_management.user_management_users import (
    delegator_for_edit_flow,
    delegator_for_owner_new_flow,
    owner_account,
)
from src.api.app import QiwaApi
from src.api.models.qiwa.raw.user_management_models import SubscriptionCookie
from src.database.actions.user_management_db_actions import delete_subscription
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.USER_MANAGEMENT)


@allure.title("E2e owner subscription flow")
@pytest.mark.skip("waiting to confirmation payment endpoint from IBM team")
@case_id(43453)
def test_owner_subscription_flow():
    owner = owner_account
    subscribed_user = delegator_for_owner_new_flow
    delete_subscription(subscribed_user.personal_number, owner.unified_number_id)
    qiwa = QiwaApi.login_as_user(owner.personal_number).select_company()
    subscription_cookie = SubscriptionCookie(
        user_id=owner.user_id,
        company_sequence_number=owner.sequence_number,
        company_labor_office_id=owner.labor_office_id,
        user_personal_number=owner.personal_number,
    ).dict(by_alias=True)

    subscription_price = float(
        qiwa.user_management_api.get_owner_subscription_price(
            subscription_cookie, subscribed_user.personal_number
        )
    )
    payment_id = int(
        qiwa.user_management_api.post_owner_subscription_flow(
            cookie=subscription_cookie,
            subscription_type="new",
            subscription_price=subscription_price,
            labor_office_id=owner.labor_office_id,
            sequence_number=owner.sequence_number,
            privilege_ids=Privileges.default_privileges,
            subscribed_user_personal_number=subscribed_user.personal_number,
        )
    )
    qiwa.payment.post_create_payment(payment_id=payment_id)
    qiwa.payment.post_confirm_payment(token=PaymentHeaders.authorization, payment_id=payment_id)
    qiwa.user_management_api.get_thank_you_page(subscription_cookie, payment_id)


@allure.title("E2e owner renew/terminate renew/extend subscription flows")
@pytest.mark.skip(
    "waiting to confirmation payment endpoint from IBM team + need a script how to expire user"
)
@case_id(49410, 49409, 49408)
@pytest.mark.parametrize("subscription_type", SelfSubscriptionType.subscription_type)
def test_owner_renew_subscription_flows(subscription_type):
    owner = owner_account
    subscribed_user = delegator_for_edit_flow
    delete_subscription(owner.personal_number, owner.unified_number_id)
    qiwa = QiwaApi.login_as_user(owner.personal_number).select_company()
    subscription_cookie = SubscriptionCookie(
        user_id=owner.user_id,
        company_sequence_number=owner.sequence_number,
        company_labor_office_id=owner.labor_office_id,
        user_personal_number=owner.personal_number,
    ).dict(by_alias=True)
    subscription_price = float(qiwa.user_management_api.get_owner_subscription_price())
    payment_id = int(
        qiwa.user_management_api.post_owner_subscription_flow(
            cookie=subscription_cookie,
            subscription_type=subscription_type,
            subscription_price=subscription_price,
            labor_office_id=owner.labor_office_id,
            sequence_number=owner.sequence_number,
            privilege_ids=Privileges.default_privileges,
            subscribed_user_personal_number=subscribed_user.personal_number,
        )
    )
    qiwa.payment.post_create_payment(payment_id=payment_id)
    qiwa.payment.post_confirm_payment(token=PaymentHeaders.authorization, payment_id=payment_id)
    qiwa.user_management_api.get_thank_you_page(subscription_cookie, payment_id)
