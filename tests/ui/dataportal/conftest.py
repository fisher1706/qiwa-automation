import pytest

from data.data_portal.constants import Admin
from src.api.dataportal.admin_api import admin_api
from src.ui.dataportal import data_portal


@pytest.fixture
def login_to_data_portal_admin():
    data_portal.open_data_portal_admin_login_page()
    data_portal.data_portal_admin.login_to_data_portal_admin()
    data_portal.get_cookie()
    admin_api.get_session_token(data_portal.cookies)


@pytest.fixture
def clear_reports():
    admin_api.clear_test_report(data_portal.cookies, Admin.AUTOMATION)
    admin_api.clear_test_report(data_portal.cookies, Admin.AUTOMATION_EDIT)


@pytest.fixture
def clear_categories():
    admin_api.clear_test_category(data_portal.cookies, Admin.AUTOMATION)
    admin_api.clear_test_category(data_portal.cookies, Admin.AUTOMATION_EDIT)


@pytest.fixture
def clear_takeaway_section():
    admin_api.clear_test_takeaway_section(data_portal.cookies, Admin.AUTOMATION)
    admin_api.clear_test_takeaway_section(data_portal.cookies, Admin.AUTOMATION_EDIT)
