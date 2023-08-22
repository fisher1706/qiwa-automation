import allure
import pytest

from data.sso.dataset import SpacesDataset
from data.validation_message import ErrorMessage, SuccessMessage
from src.api.actions.workspaces_api_actions import WorkspacesApiActions
from src.api.clients.spaces_api import SpacesApi
from src.ui.actions.sign_in import LoginActions
from src.ui.actions.spaces import SpacesActions
from src.ui.pages.admin_page import AdminPage
from src.ui.pages.workspaces_page import WorkspacesPage


@allure.feature('Spaces')
@pytest.mark.auth_suite
@pytest.mark.daily
@pytest.mark.ui
@pytest.mark.sso
@pytest.mark.usefixtures("go_to_auth_page")
class TestAdminSpaces:

    @pytest.fixture(autouse=True)
    def pre_test(self):
        self.login_action = LoginActions()
        self.workspace_actions = WorkspacesPage()
        self.spaces_action = SpacesActions()
        self.admin_actions = AdminPage()

    @pytest.fixture(autouse=True)
    def create_and_delete_space(self, super_user, api, request):
        if 'disable_auto_use' in request.keywords:
            yield
        else:
            self.auth_api = WorkspacesApiActions(api)
            self.spaces_api = SpacesApi(api)
            self.auth_api.login_user(super_user.personal_number,
                                     super_user.password)
            self.spaces_api.get_spaces()
            self.spaces_api.create_space()
            self.space_name = self.spaces_api.space_title
            yield
            if 'disable_deleting' in request.keywords:
                pass
            else:
                self.spaces_api.delete_space()

    @allure.title("Create space - positive test")
    @pytest.mark.disable_auto_use
    @pytest.mark.parametrize("english_title, arabic_title, arabic_link, english_link, redirect_key_name, user_type",
                             SpacesDataset.valid_data_for_new_space)
    @pytest.mark.parametrize("title", SpacesDataset.spaces_titles[1])
    def test_add_space(self, super_user, english_title, arabic_title, english_link, arabic_link,
                       redirect_key_name, user_type, title):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()

        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_spaces_tab()
        self.spaces_action.create_new_space(english_title, arabic_title, english_link, arabic_link,
                                            redirect_key_name, user_type, title)
        self.spaces_action.check_message(SuccessMessage.SPACE_CREATED_MESSAGE)

        self.spaces_action.wait_page_to_load()
        self.spaces_action.filter_space_by_en_title(english_title)
        self.spaces_action.delete_space()

    @allure.title("Edit created space - positive test")
    def test_edit_space(self, super_user):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.go_to_spaces_tab()
        self.spaces_action.wait_page_to_load()

        self.spaces_action.filter_space_by_en_title(self.space_name)
        new_title = "new english title"
        self.spaces_action.edit_space(new_title)
        self.spaces_action.check_message(SuccessMessage.SPACE_EDIT_MESSAGE)

    @allure.title("Delete created space - positive test")
    @pytest.mark.disable_deleting
    def test_delete_space(self, super_user):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.go_to_spaces_tab()
        self.spaces_action.wait_page_to_load()

        self.spaces_action.filter_space_by_en_title(self.space_name)
        self.spaces_action.delete_space()
        self.spaces_action.check_message(SuccessMessage.SPACE_DELETED_MESSAGE)

    @allure.title("Check reset data button - positive test")
    def test_check_reset_data_button(self, super_user):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.go_to_spaces_tab()
        self.spaces_action.wait_page_to_load()

        self.spaces_action.filter_space_by_en_title(self.space_name)
        self.spaces_action.filter_space_by_en_title(self.space_name)
        new_title = "new english title"
        self.spaces_action.edit_space(new_title, save=False)
        self.spaces_action.click_reset_changes_button()
        self.spaces_action.comparison_text_from_title_english_field(self.space_name)

    @allure.title("Check message for invalid format for field - negative test")
    def test_invalid_text_format_for_field(self, super_user):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.go_to_spaces_tab()
        self.spaces_action.wait_page_to_load()

        self.spaces_action.filter_space_by_en_title(self.space_name)
        wrong_format = "new1english#title"
        self.spaces_action.edit_space(wrong_format, save=False)
        self.spaces_action.check_invalid_format_message(ErrorMessage.INVALID_SPACE_ENGLISH_NAME)

    @allure.title("Check required field - negative test")
    def test_save_space_with_empty_fields(self, super_user):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.go_to_spaces_tab()
        self.spaces_action.wait_page_to_load()

        self.spaces_action.filter_space_by_en_title(self.space_name)
        self.spaces_action.go_to_edit_space_page()
        self.spaces_action.check_empty_fields()

    @allure.title("Check filtration on spaces page")
    def test_filtration(self, super_user):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.go_to_spaces_tab()
        self.spaces_action.wait_page_to_load()
        self.spaces_action.check_space_filters(self.space_name)

    @allure.title("Check clear filter button")
    def test_clear_filters(self, super_user):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.go_to_spaces_tab()
        self.spaces_action.wait_page_to_load()
        self.spaces_action.check_space_filters(self.space_name, clear_filter=True)
