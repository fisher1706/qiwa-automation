import allure
import pytest

from data.sso.dataset import SpacesDataset
from src.api.actions.workspaces_api_actions import WorkspacesApiActions
from src.api.clients.spaces_api import SpacesApi


@allure.feature('Space suite')
@pytest.mark.auth_suite
@pytest.mark.daily
@pytest.mark.api
@pytest.mark.sso
@pytest.mark.usefixtures("clean_up_session")
class TestAdminSpaces:

    @pytest.fixture(autouse=True)
    def pre_test(self, api):
        self.auth_api = WorkspacesApiActions(api)
        self.spaces_api = SpacesApi(api)

    @allure.title('create space with active status')
    @pytest.mark.parametrize('status', SpacesDataset.status)
    def test_create_space_with_different_statuses(self, super_user, status):
        self.auth_api.login_user(super_user.personal_number, super_user.password)
        self.spaces_api.get_spaces()
        self.spaces_api.create_space(enabled=status)
        self.spaces_api.check_space_status()
        self.spaces_api.delete_space()

    @allure.title('update space with active status')
    @pytest.mark.parametrize('status', SpacesDataset.status)
    def test_edit_space_with__different_statuses(self, super_user, status):
        self.auth_api.login_user(super_user.personal_number, super_user.password)
        self.spaces_api.get_spaces()
        self.spaces_api.create_space()
        self.spaces_api.update_e_service(enabled=status)
        self.spaces_api.check_space_status()
        self.spaces_api.delete_space()

    @allure.title('positive scenario for delete existing space')
    def test_delete_space(self, super_user):
        self.auth_api.login_user(super_user.personal_number, super_user.password)
        self.spaces_api.get_spaces()
        self.spaces_api.create_space()
        self.spaces_api.delete_space()
        self.spaces_api.check_space_status(expect_code=404)

    @allure.title('negative scenario for creation space')
    def test_create_space_with_empty_data(self, super_user):
        self.auth_api.login_user(super_user.personal_number, super_user.password)
        self.spaces_api.get_spaces()
        self.spaces_api.create_space(body=False, expect_code=422)
