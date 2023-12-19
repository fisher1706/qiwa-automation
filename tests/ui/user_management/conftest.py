from datetime import datetime, timedelta

from sqlalchemy.exc import IntegrityError

from data.dedicated.models.user import User
from data.user_management import user_management_data
from data.user_management.user_management_datasets import (
    EstablishmentAddresses,
    SelfSubscriptionType,
)
from src.api.app import QiwaApi
from src.api.models.qiwa.raw.user_management_models import SubscriptionCookie
from src.database.actions.user_management_db_actions import delete_subscription
from src.database.sql_requests.user_management.user_management_requests import (
    UserManagementRequests,
)
from src.ui.actions.user_management_actions.user_management import UserManagementActions
from src.ui.pages.user_management_pages.base_establishment_payment_page import (
    BaseEstablishmentPayment,
)
from src.ui.qiwa import qiwa
from tests.conftest import prepare_data_for_free_subscription
from utils.helpers import set_cookies_for_browser


def log_in_and_open_user_management(user: User, language: str, has_access: bool = True) -> QiwaApi:
    qiwa_api = QiwaApi.login_as_user(user.personal_number).select_company(
        int(user.sequence_number)
    )
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_user_management_page()
    set_cookies_for_browser(cookies)
    if has_access:
        qiwa.main_page.should_main_page_be_displayed()
    qiwa.header.change_local(language)
    return qiwa_api


def log_in_and_open_establishment_account(user: User, language: str):
    qiwa_api = QiwaApi.login_as_user(user.personal_number)
    cookies = qiwa_api.sso.oauth_api.get_context()
    BaseEstablishmentPayment().open_establishment_account_page()
    set_cookies_for_browser(cookies)
    qiwa.header.change_local(language)


def delete_self_subscription(user: User):
    return delete_subscription(user.personal_number, user.unified_number_id)


def get_subscription_cookie(owner: User) -> dict:
    return SubscriptionCookie(
        user_id=owner.user_id,
        company_sequence_number=owner.sequence_number,
        company_labor_office_id=owner.labor_office_id,
        user_personal_number=owner.personal_number,
    ).dict(by_alias=True)


def remove_establishment_from_subscription(owner: User, qiwa_api: QiwaApi, users: list):
    subscription_cookie = get_subscription_cookie(owner)
    for user in users:
        prepare_data_for_free_subscription(qiwa_api, subscription_cookie, user)


def expire_user_subscription(user: User):
    try:
        QiwaApi().user_management.expiry_user_subscription(
            personal_number=user.personal_number,
            unified_number=user.unified_number_id,
            expiry_date=user_management_data.PAST_EXPIRY_DATE,
        )
    except (IntegrityError, AttributeError):
        pass


def prepare_data_for_owner_subscriptions_flows(
    owner,
    qiwa_api: QiwaApi,
    user_for_extend_subscription: User,
    user_for_renew_expired_flow: User,
    user_for_renew_terminated_flow: User,
):
    cookie = get_subscription_cookie(owner)
    current_date = datetime.now()
    future_date = current_date + timedelta(days=29)
    UserManagementRequests().update_expiry_date_for_um_subscriptions(
        personal_number=user_for_extend_subscription.personal_number,
        unified_number=user_for_extend_subscription.unified_number_id,
        expiry_date=future_date.strftime("%Y-%m-%d %H:%M:%S.000"),
    )

    past_date = current_date - timedelta(days=5)
    qiwa_api.user_management.expiry_user_subscription(
        personal_number=user_for_renew_expired_flow.personal_number,
        unified_number=user_for_renew_expired_flow.unified_number_id,
        expiry_date=past_date.strftime("%Y-%m-%d %H:%M:%S.000"),
    )

    status = qiwa_api.user_management.get_user_subscription_status(
        cookie, user_for_renew_terminated_flow.personal_number
    )
    if status == user_management_data.ACTIVE_STATUS.upper():
        qiwa_api.user_management.patch_terminate_subscription(
            cookie, user_for_renew_terminated_flow.personal_number
        )


def renew_owner_subscriptions(
    owner: User, users: list, qiwa_api: QiwaApi, user_management: UserManagementActions
):
    cookie = get_subscription_cookie(owner)
    for user, subscription_type in zip(users, SelfSubscriptionType.subscription_type):
        payment_id = qiwa_api.user_management.renew_owner_subscription(
            cookie, user, subscription_type
        )
        user_management.confirm_payment_via_ui(payment_id, "owner_flow")


def prepare_data_for_checking_the_confirmation_page(owner, qiwa_api: QiwaApi) -> dict:
    cookie = get_subscription_cookie(owner)
    UserManagementRequests().update_establishment_data_en(
        owner.labor_office_id,
        owner.sequence_number,
        EstablishmentAddresses.district_en,
        EstablishmentAddresses.street_en,
    )
    notification_email, notification_phone = qiwa_api.sso.oauth_api.get_user_data()
    establishment_data = qiwa_api.user_management.get_establishment_data(cookie)
    establishment_name = establishment_data["name"]
    establishment_address_en = [
        EstablishmentAddresses.country,
        establishment_data["cityEn"],
        establishment_data["districtEn"],
        establishment_data["streetEn"],
        establishment_data["buildingNumber"],
        str(establishment_data["additionalNumber"]),
    ]
    establishment_address_ar = [
        EstablishmentAddresses.country,
        establishment_data["cityAr"],
        establishment_data["districtAr"],
        establishment_data["streetAr"],
        establishment_data["buildingNumber"],
        str(establishment_data["additionalNumber"]),
    ]
    vat_number = establishment_data["vatNumber"]
    return {
        "notification_email": notification_email,
        "notification_phone": f"+{notification_phone}",
        "establishment_name": establishment_name,
        "establishment_address_en": establishment_address_en,
        "establishment_address_ar": establishment_address_ar,
        "vat_number": vat_number,
    }
