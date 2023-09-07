import allure
import pytest

from src.api.clients.spaces import SpacesApi
from src.api.controllers.workspaces import WorkspacesApiController


@allure.feature('Space suite')
@pytest.mark.usefixtures("clean_up_session")
class TestAdminSpaces:

    @pytest.fixture(autouse=True)
    def pre_test(self, http_client):
        self.auth_api = WorkspacesApiController(http_client)
        self.spaces_api = SpacesApi(http_client)

    @allure.title('create space with active status')
    @pytest.mark.parametrize('status', [[True], [False]])
    def test_create_space_with_different_statuses(self, super_user, status):
        self.auth_api.login_user(super_user.personal_number, super_user.password)
        self.spaces_api.get_spaces()
        self.spaces_api.create_space(enabled=status)
        self.spaces_api.check_space_status()
        self.spaces_api.delete_space_request()

    @allure.title('update space with active status')
    @pytest.mark.parametrize('status', [[True], [False]])
    def test_edit_space_with__different_statuses(self, super_user, status):
        self.auth_api.login_user(super_user.personal_number, super_user.password)
        self.spaces_api.get_spaces()
        self.spaces_api.create_space()
        self.spaces_api.update_e_service(enabled=status)
        self.spaces_api.check_space_status()
        self.spaces_api.delete_space_request()

    @allure.title('positive scenario for delete existing space')
    def test_delete_space(self, super_user):
        self.auth_api.login_user(super_user.personal_number, super_user.password)
        self.spaces_api.get_spaces()
        self.spaces_api.create_space()
        self.spaces_api.delete_space_request()
        self.spaces_api.check_space_status(expect_code=404)

    @allure.title('negative scenario for creation space')
    def test_create_space_with_empty_data(self, super_user):
        self.auth_api.login_user(super_user.personal_number, super_user.password)
        self.spaces_api.get_spaces()
        self.spaces_api.create_space(body=False, expect_code=422)
