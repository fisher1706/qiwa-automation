from data.lo.constants import LOAdmin, LOAgent, LOUser
from src.api.app import QiwaApi


def test_sign_in_lo_agent():
    qiwa = QiwaApi.login_as_user(LOAgent.ID)
    qiwa.sso.logout()


def test_sign_in_lo_admin():
    qiwa = QiwaApi.login_as_user(LOAdmin.ID)
    qiwa.sso.logout()


def test_sign_in_lo_user():
    qiwa = QiwaApi.login_as_user(LOUser.ID)
    qiwa.sso.logout()
