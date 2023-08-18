import allure
import pytest

from data.dataset import UserDataset
from src.api.actions.auth_api_actions import AuthApiActions
from src.api.clients.nitaqat_api import NitaqatApi


@allure.feature('Nitaqat suite')
@pytest.mark.nitaqat_suite
@pytest.mark.daily
@pytest.mark.api
@pytest.mark.sso
@pytest.mark.usefixtures("clean_up_session")
class TestNitaqat:

    @pytest.fixture(autouse=True)
    def pre_test(self, api):
        self.auth_api = AuthApiActions(api)
        self.nitaqat_api = NitaqatApi(api)

    @allure.title('Calculate nitaqat with invalid data')
    @pytest.mark.parametrize("input_data", UserDataset.invalid_phone_api)
    def test_calculate_nitaqat_invalid_data(self, owner_module, input_data):
        self.auth_api.login_user(owner_module.personal_number, owner_module.password)
        self.auth_api.select_first_company()
        self.nitaqat_api.calculate_nitaqat(new_expats=input_data, new_saudis=input_data, expect_code=422)
        # TODO: add response message verification

    @allure.title('Calculate nitaqat without selecting workspace')
    def test_calculate_nitaqat_without_select_workspace(self, owner_module):
        self.auth_api.login_user(owner_module.personal_number, owner_module.password)
        self.nitaqat_api.calculate_nitaqat(new_expats=10, new_saudis=200, expect_code=403)
        # TODO: add response message verification
