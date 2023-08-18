import allure
import pytest

from data.constants import UserInfo
from data.user_data import UserData
from src.api.actions.auth_api_actions import AuthApiActions
from src.api.models.user_management import test_account_um_2


@allure.feature("Main API")
@pytest.mark.subscription_suite
@pytest.mark.daily
@pytest.mark.api
@pytest.mark.um
@pytest.mark.usefixtures("clean_up_session")
class TestMainAPI:  # pylint: disable=duplicate-code
    @pytest.fixture(autouse=True)
    def pre_test(self, api):
        self.auth_api = AuthApiActions(api)
        self.test_data = UserData()

    @allure.title(
        "7872 Check that only User with access to User Management has access to the page"
    )
    def test_access_for_user_without_um_permission(self):
        owner = test_account_um_2
        self.auth_api.login_user(owner.account.personal_number, UserInfo.DEFAULT_PASSWORD)
        self.auth_api.select_company_with_sequence_number(owner.sequence_number)
