from data.dedicated.models.user import User
from src.api.app import QiwaApi
from src.database.actions.user_management_db_actions import delete_subscription
from src.ui.qiwa import qiwa
from utils.helpers import set_cookies_for_browser


def log_in_and_open_user_management(user: User, language: str):
    qiwa_api = QiwaApi.login_as_user(user.personal_number).select_company(
        int(user.sequence_number)
    )
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_user_management_page()
    set_cookies_for_browser(cookies)
    qiwa.main_page.wait_until_page_is_loaded()
    qiwa.header.change_local(language)


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
