from src.api.app import QiwaApi
from src.ui.qiwa import qiwa
from utils.helpers import set_cookies_for_browser


def login_and_open_delegation_dashboard_page(personal_number: str, sequence_number: int | str):
    qiwa_api = QiwaApi.login_as_user(personal_number=personal_number).select_company(
        sequence_number=int(sequence_number)
    )
    cookies = qiwa_api.sso.oauth_api.get_context()
    qiwa.open_delegation_dashboard_page()
    set_cookies_for_browser(cookies)
    qiwa.delegation_dashboard_page.wait_delegation_dashboard_page_to_load().select_english_localization_on_delegation_dashboard()
    return qiwa_api
