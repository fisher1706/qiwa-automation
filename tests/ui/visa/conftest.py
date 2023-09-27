from time import sleep

import pytest

from data.visa.constants import Languages, VisaUser
from src.api.controllers.visa_mock_api import VisaMockApi
from src.ui.qiwa import qiwa


@pytest.fixture
def visa_mock():
    mock = VisaMockApi()
    mock.delete_company_address()
    yield mock
    mock.teardown_company()
    mock.change_visa_quantity(1, 4)
    mock.change_visa_quantity(2, 20)
    mock.change_visa_quantity(3, 55)
    mock.change_visa_quantity(4, 75)


@pytest.fixture(scope="function", autouse=True)
def pre_test():
    qiwa.login_as_user(VisaUser.NAME, VisaUser.PASSWORD)
    qiwa.transitional.select_language(Languages.ENGLISH)
    qiwa.workspace_page.select_company_account_with_sequence_number(VisaUser.ESTABLISHMENT_ID)
    qiwa.open_visa_page()
