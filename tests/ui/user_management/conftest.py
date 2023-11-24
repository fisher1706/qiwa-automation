from data.dedicated.models.user import User
from src.api.app import QiwaApi
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
