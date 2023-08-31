import allure
import pytest

from data.um.user_management_models2 import test_account_um_2
from src.api.app import QiwaApi
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.USER_MANAGEMENT)


@allure.feature("Main API")
@pytest.mark.usefixtures("clean_up_session")
class TestMainAPI:  # pylint: disable=duplicate-code

    @allure.title("Check that only User with access to User Management has access to the page")
    @case_id(7872)
    def test_access_for_user_without_um_permission(self):
        owner = test_account_um_2
        QiwaApi.login_as_user(owner.account.personal_number).select_company(owner.sequence_number)
