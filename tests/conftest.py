import pytest

from data.account import Account
from data.constants import UserInfo
from src.api.app import QiwaApi
from src.api.controllers.mock_mlsd_data import MockMlsdDataController
from src.api.controllers.sso_auth import AuthApiLaborerSSOController
from src.api.http_client import HTTPClient


@pytest.fixture
def http_client():
    return HTTPClient()


@pytest.fixture(scope="class")
def delete_service_categories():
    yield
    api = QiwaApi.login_as_admin()
    response = api.e_service.api.get_admin_tags()
    tags = response.json()["data"]
    for tag in tags:
        if tag["attributes"]["code"] not in ("businesses", "employees", "visas"):
            api.e_service.api.delete_tag(tag["id"])
    api.e_service.api.get_admin_tags()


@pytest.fixture
def parametrized_owner(http_client):
    """
    Configurable owner creation. Several options are currently available, red_nitaq and with_subscription.
    Usage example:
    def test_the_owner(parametrized_owner):
        owner = parametrized_owner(with_subscription=False)
        ...
    """

    test_data = MockMlsdDataController()
    test_data.prepare_establishment()
    auth = AuthApiLaborerSSOController(http_client)
    auth.complete_create_account_via_laborer_sso_api(test_data.account)
    return test_data


@pytest.fixture(scope="module")
def owner_module() -> Account:
    """
    Single owner account for all tests within the module (suite)
    """
    test_data = MockMlsdDataController()
    test_data.prepare_owner_account()
    AuthApiLaborerSSOController().complete_create_account_via_laborer_sso_api(test_data.account)
    return test_data.account


@pytest.fixture
def super_user() -> Account:
    """
    Existing superuser account already registered in Qiwa
    """
    return Account(
        personal_number="1215113732",
        password=UserInfo.DEFAULT_PASSWORD,
        email="api-tests-super-user@qa.qiwa.tech",
    )


@pytest.fixture
def clean_up_session(http_client):
    http_client.session.cookies.clear()
