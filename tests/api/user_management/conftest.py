import allure

from data.dedicated.models.user import User
from data.user_management.user_management_datasets import (
    PaymentHeaders,
    Privileges,
    SubscriptionStatuses,
)
from src.api.app import QiwaApi
from src.database.sql_requests.user_management.user_management_requests import (
    UserManagementRequests,
)
from utils.assertion import assert_that


@allure.step
def get_user_establishments(
    qiwa: QiwaApi, cookie: dict, users_personal_number: str, subscribed_state: bool
) -> list:
    user_establishments = qiwa.user_management_api.get_user_subscribed_establishments(
        cookie=cookie,
        users_personal_number=users_personal_number,
        subscribed_state=subscribed_state,
    )
    establishments_list = []
    for establishment in user_establishments:
        establishments_list.append(establishment["sequenceNumber"])
    return establishments_list


def prepare_data_for_free_subscription(qiwa: QiwaApi, cookie: dict, subscribed_user: User):
    user_establishments = get_user_establishments(
        qiwa=qiwa,
        cookie=cookie,
        users_personal_number=subscribed_user.personal_number,
        subscribed_state=True,
    )
    if int(subscribed_user.sequence_number) in user_establishments:
        qiwa.user_management_api.patch_remove_establishment_from_user(
            cookie=cookie,
            users_personal_number=subscribed_user.personal_number,
            labor_office_id=subscribed_user.labor_office_id,
            sequence_number=subscribed_user.sequence_number,
        )


def prepare_data_for_terminate_company(qiwa: QiwaApi, cookie: dict, subscribed_user: User):
    user_establishments = get_user_establishments(
        qiwa=qiwa,
        cookie=cookie,
        users_personal_number=subscribed_user.personal_number,
        subscribed_state=True,
    )
    if int(subscribed_user.sequence_number) not in user_establishments:
        qiwa.user_management_api.post_subscribe_user_to_establishment(
            cookie=cookie,
            users_personal_number=subscribed_user.personal_number,
            labor_office_id=subscribed_user.labor_office_id,
            sequence_number=subscribed_user.sequence_number,
            privileges=Privileges.default_privileges,
        )


def get_subscription_status_and_renew_owner_subscription(
    qiwa: QiwaApi, cookie: dict, subscribed_user: User, owner: User
):
    subscription_status = UserManagementRequests().get_subscription_status(
        personal_number=subscribed_user.personal_number, requester_id_number=owner.personal_number
    )
    if subscription_status == SubscriptionStatuses.terminated:
        payment_id = qiwa.user_management.renew_owner_subscription(
            cookie=cookie, subscribed_user=subscribed_user, subscription_type="renew-terminated"
        )
        qiwa.payment.post_create_payment(payment_id=payment_id)
        qiwa.payment.post_confirm_payment(
            token=PaymentHeaders.authorization, payment_id=payment_id
        )
        qiwa.user_management_api.get_thank_you_page(cookie=cookie, transaction_id=payment_id)


def renew_self_subscription(qiwa: QiwaApi, cookie: dict, owner: User):
    payment_id = qiwa.user_management.renew_self_subscription(
        cookie=cookie, user=owner, subscription_type="renew-expired"
    )
    qiwa.payment.post_create_payment(payment_id=payment_id)
    qiwa.payment.post_confirm_payment(token=PaymentHeaders.authorization, payment_id=payment_id)
    qiwa.user_management_api.get_thank_you_page(cookie=cookie, payment_id=payment_id)


@allure.step
def check_deleted_status_of_privilege_log(
    personal_number: str, sequence_number: int, deleted_status: bool
):
    deleted_status_of_subscription = UserManagementRequests().get_deleted_status(
        personal_number=personal_number, service_id=32, sequence_number=sequence_number
    )
    assert_that(deleted_status_of_subscription).equals_to(deleted_status)
