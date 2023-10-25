from sqlalchemy.exc import IntegrityError

from src.database.sql_requests.user_management.delete_subscription_requests import (
    UserManagementRequestsDeleteSubscription,
)


def delete_subscription(personal_number: str, unified_number: int):
    user_management_request = UserManagementRequestsDeleteSubscription()
    try:
        transaction_id = user_management_request.get_transaction_id(
            personal_number, unified_number
        )
        user_management_request.subscription_payment(personal_number, unified_number).um_payment(
            transaction_id
        ).establishment_access(personal_number, unified_number).subscription(
            personal_number, unified_number
        ).user_privileges(
            personal_number, unified_number
        ).user_subscriptions(
            personal_number, unified_number
        )
    except (IntegrityError, AttributeError):
        pass
