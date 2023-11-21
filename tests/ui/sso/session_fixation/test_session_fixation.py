import pytest

from src.ui.qiwa import qiwa
from src.api.app import QiwaApi
from utils.allure import TestmoProject, project
from utils.helpers import set_cookies_for_browser

case_id = project(TestmoProject.QIWA_SSO)


@case_id(162960)
def test_user_with_stolen_session_try_get_access(account_data):
    account = account_data
    qiwa_api = QiwaApi()
    qiwa_api.sso.login_user(account.personal_number, account.password)
    qiwa_session = qiwa_api.sso.oauth_api.get_context()
    qiwa_api.sso.logout()
    qiwa.open_login_page()
    set_cookies_for_browser(qiwa_session)
    qiwa.open_delegation_dashboard_page()
    qiwa.header.change_local("en")
    qiwa.login_page.check_login_page_is_displayed()
