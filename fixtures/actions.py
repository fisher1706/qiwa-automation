import allure
import pytest

from data.constants import UserInfo
from data.user_data import UserData
from src.api.actions.laborer_sso_auth_api_action import AuthApiLaborerSSOActions
from src.api.models.account import Account
from src.api.models.model_builder import ModelBuilder


@pytest.fixture(scope="function")
def parametrized_owner(api):
    """
    Configurable owner creation. Several options are currently available, red_nitaq and with_subscription.
    Usage example:
    def test_the_owner(parametrized_owner):
        owner = parametrized_owner(with_subscription=False)
        ...
    """

    def _create(
        red_nitaq=False, with_subscription=True, cr_number=None, branches=None
    ) -> UserData:
        return create_est_with_laborers(
            api,
            red_nitaq=red_nitaq,
            with_subscription=with_subscription,
            cr_number=cr_number,
            branches=branches,
        )

    return _create


@pytest.fixture(scope="module")
def owner_module() -> Account:
    """
    Single owner account for all tests within the module (suite)
    """
    return create_account()


@pytest.fixture(scope="function")
def super_user() -> Account:
    """
    Existing superuser account already registered in Qiwa
    """
    return ModelBuilder.build_random_account(
        personal_number="1215113732",
        password=UserInfo.DEFAULT_PASSWORD,
        email="api-tests-super-user@qa.qiwa.tech",
    )


@pytest.fixture(scope="function")
def clean_up_session(api):
    api.session.cookies.clear()


@allure.step("Create new account")
def create_account(
    user_type=None,
    personal_number=None,
    branches=None,
    wp_type=None,
    saudi_count=None,
    expat_count=None,
):
    test_data = UserData()
    test_data.prepare_owner_account(
        user_type=user_type,
        personal_number=personal_number,
        branches=branches,
        wp_type=wp_type,
        saudi_count=saudi_count,
        expat_count=expat_count,
    )
    AuthApiLaborerSSOActions().complete_create_account_via_laborer_sso_api(test_data.account)
    return test_data.account


@allure.step("Create establishment with laborers")
def create_est_with_laborers(
    api, red_nitaq=False, with_subscription=True, cr_number=None, branches=None
) -> UserData:
    """
    Configurable owner creation. Several options are currently available, red_nitaq and with_subscription.
    Usage example:
    def test_the_owner(parametrized_owner):
        owner = parametrized_owner(with_subscription=False)
        ...
    """
    test_data = UserData()
    test_data.prepare_establishment(
        red_nitaq=red_nitaq,
        with_subscription=with_subscription,
        cr_number=cr_number,
        branches=branches,
    )
    auth = AuthApiLaborerSSOActions(api)
    auth.complete_create_account_via_laborer_sso_api(test_data.account)
    return test_data
