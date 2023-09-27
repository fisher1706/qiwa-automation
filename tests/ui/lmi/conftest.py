import pytest
from selene import be

from data.lmi.constants import UserInfo
from src.ui.lmi import lmi
from src.ui.qiwa import qiwa


@pytest.fixture
def login_lmi_user():
    qiwa.login_as_user(UserInfo.LMI_ADMIN_LOGIN)
    qiwa.workspace_page.lmi_admin_card.wait_until(be.visible)
    lmi.perform_preconditions()
    qiwa.workspace_page.select_lmi_admin()
