import allure
import pytest

from data.user_management import user_management_data
from data.user_management.user_management_datasets import (
    Privileges,
    SubscriptionStatuses,
)
from data.user_management.user_management_users import (
    delegator_for_add_and_terminate_subscription_flow,
    delegator_for_full_terminate_flow,
    owner_account,
    owner_account_for_expire_subscription,
)
from src.api.app import QiwaApi
from src.api.models.qiwa.raw.user_management_models import SubscriptionCookie
from tests.api.user_management.conftest import (
    check_deleted_status_of_privilege_log,
    get_subscription_status_and_renew_owner_subscription,
    renew_self_subscription,
)
from tests.conftest import (
    prepare_data_for_free_subscription,
    prepare_data_for_terminate_company,
)
from utils.allure import TestmoProject, project
from utils.assertion import assert_that

case_id = project(TestmoProject.USER_MANAGEMENT)


@allure.title("E2e free subscription flow")
@case_id(54991)
def test_free_subscription_flow():
    owner = owner_account
    subscribed_user = delegator_for_add_and_terminate_subscription_flow
    qiwa = QiwaApi.login_as_user(owner.personal_number).select_company()
    subscription_cookie = SubscriptionCookie(
        user_id=owner.user_id,
        company_sequence_number=owner.sequence_number,
        company_labor_office_id=owner.labor_office_id,
        user_personal_number=owner.personal_number,
    ).dict(by_alias=True)
    prepare_data_for_free_subscription(qiwa_api=qiwa, cookie=subscription_cookie, user=subscribed_user)
    qiwa.user_management_api.post_subscribe_user_to_establishment(
        cookie=subscription_cookie,
        users_personal_number=subscribed_user.personal_number,
        labor_office_id=subscribed_user.labor_office_id,
        sequence_number=subscribed_user.sequence_number,
        privileges=Privileges.default_privileges,
    )
    user_privileges = qiwa.user_management_api.get_user_privileges(
        cookie=subscription_cookie,
        users_personal_number=subscribed_user.personal_number
    )
    assert_that(user_privileges["sequenceNumber"]).equals_to(int(subscribed_user.sequence_number))
    assert_that(sorted(user_privileges["privilegeIds"])).equals_to(Privileges.default_privileges)


@allure.title("E2e terminate company from subscription to user")
@case_id(57128)
def test_terminate_company_from_subscription():
    owner = owner_account
    subscribed_user = delegator_for_add_and_terminate_subscription_flow
    qiwa = QiwaApi.login_as_user(owner.personal_number).select_company()
    subscription_cookie = SubscriptionCookie(
        user_id=owner.user_id,
        company_sequence_number=owner.sequence_number,
        company_labor_office_id=owner.labor_office_id,
        user_personal_number=owner.personal_number,
    ).dict(by_alias=True)
    prepare_data_for_terminate_company(
        qiwa_api=qiwa,
        cookie=subscription_cookie,
        subscribed_user=subscribed_user
    )
    qiwa.user_management_api.patch_remove_establishment_from_user(
        cookie=subscription_cookie,
        users_personal_number=subscribed_user.personal_number,
        labor_office_id=subscribed_user.labor_office_id,
        sequence_number=subscribed_user.sequence_number,
    )
    terminated_establishments = qiwa.user_management_api.get_user_subscribed_establishments(
        cookie=subscription_cookie,
        users_personal_number=subscribed_user.personal_number,
        subscribed_state=False
    )
    assert_that(int(subscribed_user.sequence_number)).in_(terminated_establishments)


@allure.title("E2e full terminate flow")
@pytest.mark.skip("confirm payment is unavailable on api side")
@case_id(57129)
def test_full_terminate_flow():
    owner = owner_account
    subscribed_user = delegator_for_full_terminate_flow
    qiwa = QiwaApi.login_as_user(owner.personal_number).select_company()
    subscription_cookie = SubscriptionCookie(
        user_id=owner.user_id,
        company_sequence_number=owner.sequence_number,
        company_labor_office_id=owner.labor_office_id,
        user_personal_number=owner.personal_number,
    ).dict(by_alias=True)
    get_subscription_status_and_renew_owner_subscription(
        qiwa_api=qiwa,
        cookie=subscription_cookie,
        subscribed_user=subscribed_user,
        owner=owner
    )
    subscription_status = qiwa.user_management.terminate_user_subscription(
        cookie=subscription_cookie,
        users_personal_number=subscribed_user.personal_number,
        requester_id_number=owner.personal_number
    )
    assert_that(subscription_status).equals_to(SubscriptionStatuses.terminated)
    get_subscription_status_and_renew_owner_subscription(
        qiwa_api=qiwa,
        cookie=subscription_cookie,
        subscribed_user=subscribed_user,
        owner=owner
    )


@allure.title("Check Deleted value is equal to 1 after owner subscription was expired")
@pytest.mark.skip("confirm payment is unavailable on api side")
@case_id(80279)
def test_expire_owner_subscription():
    owner = owner_account_for_expire_subscription
    qiwa = QiwaApi.login_as_user(owner.personal_number).select_company()
    subscription_cookie = SubscriptionCookie(
        user_id=owner.user_id,
        company_sequence_number=owner.sequence_number,
        company_labor_office_id=owner.labor_office_id,
        user_personal_number=owner.personal_number,
    ).dict(by_alias=True)
    check_deleted_status_of_privilege_log(
        personal_number=owner.personal_number,
        sequence_number=owner.sequence_number,
        deleted_status=False
    )
    qiwa.user_management.expiry_user_subscription(
        personal_number=owner.personal_number,
        unified_number=owner.unified_number_id,
        expiry_date=user_management_data.PAST_EXPIRY_DATE
    )
    check_deleted_status_of_privilege_log(
        personal_number=owner.personal_number,
        sequence_number=owner.sequence_number,
        deleted_status=True
    )
    renew_self_subscription(qiwa=qiwa, cookie=subscription_cookie, owner=owner)
