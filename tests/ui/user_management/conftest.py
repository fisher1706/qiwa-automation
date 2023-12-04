from data.dedicated.models.user import User
from src.api.app import QiwaApi
from src.api.models.qiwa.raw.user_management_models import SubscriptionCookie
from src.database.actions.user_management_db_actions import delete_subscription
from src.ui.qiwa import qiwa
from tests.conftest import prepare_data_for_free_subscription
from utils.helpers import set_cookies_for_browser


def log_in_and_open_user_management(user: User, language: str) -> QiwaApi:
    qiwa_api = QiwaApi.login_as_user(user.personal_number).select_company(
        int(user.sequence_number)
    )
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_user_management_page()
    set_cookies_for_browser(cookies)
    qiwa.main_page.wait_until_page_is_loaded()
    qiwa.header.change_local(language)
    return qiwa_api


def log_in_and_open_establishment_account(user: User, language: str):
    qiwa_api = QiwaApi.login_as_user(user.personal_number).select_company_subscription(
        int(user.sequence_number)
    )
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_establishment_account_page()
    set_cookies_for_browser(cookies)
    qiwa.header.change_local(language)


def delete_self_subscription(user: User):
    delete_subscription(user.personal_number, user.unified_number_id)


def get_subscription_cookie(owner: User) -> dict:
    return SubscriptionCookie(
        user_id=owner.user_id,
        company_sequence_number=owner.sequence_number,
        company_labor_office_id=owner.labor_office_id,
        user_personal_number=owner.personal_number,
    ).dict(by_alias=True)


def prepare_data_for_add_access_to_company(owner: User, qiwa_api: QiwaApi, users: list):
    subscription_cookie = get_subscription_cookie(owner)
    for user in users:
        prepare_data_for_free_subscription(qiwa_api, subscription_cookie, user)
