import pytest

import config
from data.account import Account
from data.constants import UserInfo
from data.dedicated.models.user import User
from data.user_management.user_management_datasets import Privileges
from src.api.app import QiwaApi
from src.api.controllers.mock_mlsd_data import MockMlsdDataController
from src.api.controllers.sso.sso_auth import AuthApiSSOController
from src.api.http_client import HTTPClient


@pytest.fixture
def http_client():
    return HTTPClient()


@pytest.fixture(scope="class")
def delete_service_categories():
    yield
    api = QiwaApi.login_as_admin()
    response = api.e_service.client.get_admin_tags()
    tags = response.json()["data"]
    for tag in tags:
        if tag["attributes"]["code"] not in ("businesses", "employees", "visas"):
            api.e_service.client.delete_tag(tag["id"])
    api.e_service.client.get_admin_tags()


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
    auth = AuthApiSSOController(http_client)
    auth.register_account_via_sso_api(test_data.account)
    return test_data


@pytest.fixture(scope="module")
def owner_module() -> Account:
    """
    Single owner account for all tests within the module (suite)
    """
    mock_data = MockMlsdDataController()
    personal_number = mock_data.get_laborers_new(user_type="saudi")
    account = Account(personal_number)
    AuthApiSSOController().register_account_via_sso_api(account)
    return account


@pytest.fixture
def super_user() -> Account:
    """
    Existing superuser account already registered in Qiwa
    """
    return Account(
        personal_number="1215113732",
        password=UserInfo.PASSWORD,
        email="api-tests-super-user@qa.qiwa.tech",
    )


@pytest.fixture
def clean_up_session(http_client):
    http_client.session.cookies.clear()


@pytest.fixture(scope="session", autouse=True)
def log_env_config(record_testsuite_property):
    record_testsuite_property("ENV", config.settings.env)


def prepare_data_for_free_subscription(qiwa_api: QiwaApi, cookie: dict, user: User):
    user_establishments = qiwa_api.user_management_api.get_user_subscribed_establishments(
        cookie=cookie,
        users_personal_number=user.personal_number,
        subscribed_state=True,
    )
    if int(user.sequence_number) in user_establishments:
        qiwa_api.user_management_api.patch_remove_establishment_from_user(
            cookie=cookie,
            users_personal_number=user.personal_number,
            labor_office_id=user.labor_office_id,
            sequence_number=user.sequence_number,
        )


def prepare_data_for_terminate_company(qiwa_api: QiwaApi, cookie: dict, subscribed_user: User):
    user_establishments = qiwa_api.user_management_api.get_user_subscribed_establishments(
        cookie=cookie,
        users_personal_number=subscribed_user.personal_number,
        subscribed_state=True,
    )
    if int(subscribed_user.sequence_number) not in user_establishments:
        qiwa_api.user_management_api.post_subscribe_user_to_establishment(
            cookie=cookie,
            users_personal_number=subscribed_user.personal_number,
            labor_office_id=subscribed_user.labor_office_id,
            sequence_number=subscribed_user.sequence_number,
            privileges=Privileges.default_privileges,
        )
