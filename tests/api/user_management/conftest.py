import allure

from data.dedicated.models.user import User
from data.user_management.user_management_datasets import (
    EstablishmentAddresses,
    PaymentHeaders,
    SubscriptionStatuses,
)
from src.api.app import QiwaApi
from src.database.sql_requests.user_management.user_management_requests import (
    UserManagementRequests,
)
from utils.assertion import assert_that


def get_subscription_status_and_renew_owner_subscription(
    qiwa_api: QiwaApi, cookie: dict, subscribed_user: User, owner: User
):
    subscription_status = UserManagementRequests().get_subscription_status(
        personal_number=subscribed_user.personal_number, requester_id_number=owner.personal_number
    )
    if subscription_status == SubscriptionStatuses.terminated:
        payment_id = qiwa_api.user_management.renew_owner_subscription(
            cookie=cookie, subscribed_user=subscribed_user, subscription_type="renew-terminated"
        )
        qiwa_api.payment.post_create_payment(payment_id=payment_id)
        qiwa_api.payment.post_confirm_payment(
            token=PaymentHeaders.authorization, payment_id=payment_id
        )
        qiwa_api.user_management_api.get_thank_you_page(cookie=cookie, transaction_id=payment_id)


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


def prepare_data_for_update_establishment_address(qiwa: QiwaApi):
    qiwa.user_management_api.post_update_establishment_address(
        EstablishmentAddresses.initial_address
    )


def get_establishment_address(qiwa: QiwaApi, cookie: dict) -> dict:
    establishment_data = qiwa.user_management_api.get_establishment_data(cookie)
    establishment_address = list(establishment_data.values())[4:11] + [
        establishment_data.get("additionalNumber")
    ]
    vat_number = establishment_data["vatNumber"]
    return {"establishment_address": establishment_address, "vat_number": vat_number}
