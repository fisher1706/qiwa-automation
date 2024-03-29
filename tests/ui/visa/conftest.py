from time import sleep

import pytest

from data.visa.constants import Languages, VisaUser
from src.api.controllers.visa_mock_api import VisaMockApi
from src.database.sql_requests.visa_balance_requests import VisaBalanceRequests
from src.ui.qiwa import qiwa


@pytest.fixture
def visa_mock():
    mock = VisaMockApi()
    yield mock
    mock.teardown_company()
    mock.change_visa_quantity(1, 4)
    mock.change_visa_quantity(2, 20)
    mock.change_visa_quantity(3, 55)
    mock.change_visa_quantity(4, 75)


@pytest.fixture(scope="function", autouse=True)
def pre_test():
    qiwa.login_page.open_login_page()
    qiwa.header.change_local("en")
    qiwa.login_as_user(VisaUser.NAME, VisaUser.PASSWORD)
    sleep(10)
    qiwa.header.change_local("en")
    qiwa.workspace_page.select_company_account_with_sequence_number(VisaUser.ESTABLISHMENT_ID)
    qiwa.open_visa_page()


@pytest.fixture
def visa_db():
    db = VisaBalanceRequests()
    yield db
    db.remove_balance_request_records()
