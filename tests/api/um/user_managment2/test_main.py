import allure
import pytest

from data.constants import UserInfo
from data.um.user_management_models2 import test_account_um_2
from src.api.controllers.workspaces import WorkspacesApiController


@allure.feature("Main API")
@pytest.mark.subscription_suite
@pytest.mark.daily
@pytest.mark.api
@pytest.mark.um
@pytest.mark.usefixtures("clean_up_session")
class TestMainAPI:  # pylint: disable=duplicate-code
    @pytest.fixture(autouse=True)
    def pre_test(self, http_client):
        self.auth_api = WorkspacesApiController(http_client)

    @allure.title(
        "7872 Check that only User with access to User Management has access to the page"
    )
    def test_access_for_user_without_um_permission(self):
        owner = test_account_um_2
        self.auth_api.login_user(owner.account.personal_number, UserInfo.DEFAULT_PASSWORD)
        self.auth_api.select_company_with_sequence_number(owner.sequence_number)
