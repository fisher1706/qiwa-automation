import allure
import pytest
from selene import browser

from data.sso.dataset import EServiceDataset
from data.validation_message import SuccessMessage
from src.api.controllers.e_service import EServiceApiController
from src.api.controllers.workspaces import WorkspacesApiController
from src.ui.actions.e_services import EServiceActions
from src.ui.actions.sign_in import LoginActions
from src.ui.components.profile_menu import UserProfileMenu
from src.ui.pages.admin_page import AdminPage
from src.ui.pages.dashboard_page import DashboardPage
from src.ui.pages.workspaces_page import WorkspacesPage


@allure.feature('Admin E-Services')
@pytest.mark.usefixtures("go_to_auth_page")
class TestAdminEServices:

    @pytest.fixture(autouse=True)
    def pre_test(self, http_client):
        self.login_action = LoginActions()
        self.workspace_actions = WorkspacesPage()
        self.e_services_action = EServiceActions()
        self.auth_api = WorkspacesApiController(http_client)
        self.admin_actions = AdminPage()
        self.dashboard_action = DashboardPage()

    @pytest.fixture
    def create_and_delete_e_service(self, super_user, http_client, request):
        self.auth_api = WorkspacesApiController(http_client)
        self.e_service_api = EServiceApiController(http_client)
        self.auth_api.login_user(super_user.personal_number, super_user.password)
        self.e_service.api.get_e_services(is_admin=True)
        self.e_service.api.create_e_services()
        self.e_service_title = self.e_service.api.e_service_english_title
        yield
        self.auth_api.login_user(super_user.personal_number, super_user.password)
        self.e_service.api.delete_e_service()
        self.e_service.api.get_e_services(expect_code=404)

    @allure.title("Add and delete e-services")
    @pytest.mark.parametrize("en_title, ar_title, service_code, en_link, ar_link", EServiceDataset.e_service_valid_data)
    def test_add_e_service(self, super_user, en_title, ar_title, service_code, en_link, ar_link):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()

        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()
        self.admin_actions.add_e_service()
        self.admin_actions.fill_in_the_fields_for_new_e_service(en_title, ar_title, service_code, en_link, ar_link)
        self.admin_actions.select_privilege_checkbox()
        self.admin_actions.click_on_save_e_service_button()
        self.admin_actions.check_successful_action(SuccessMessage.E_SERVICE_CREATED_MESSAGE)

        self.e_services_action.delete_e_service_by_en_title(en_title)
        self.admin_actions.check_successful_action(SuccessMessage.E_SERVICE_DELETED_MESSAGE)

    @allure.title("Edit e-services")
    def test_edit_e_service(self, super_user, create_and_delete_e_service):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()

        self.admin_actions.filter_by_english_title(self.e_service_title)
        self.admin_actions.check_e_service_detail()
        self.admin_actions.click_edit_button()
        new_title = "new english title"
        self.admin_actions.edit_english_title_field(new_title)
        self.admin_actions.click_on_save_e_service_button()
        self.admin_actions.check_successful_action(SuccessMessage.E_SERVICE_EDITED_MESSAGE)
        self.admin_actions.filter_by_english_title(new_title)
        self.admin_actions.check_e_service_detail()

    @allure.title("reset changes and data")
    def test_reset_changes(self, super_user, create_and_delete_e_service):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()

        self.admin_actions.filter_by_english_title(self.e_service_title)
        self.admin_actions.click_edit_button()
        new_title = "new english title"
        self.admin_actions.edit_english_title_field(new_title)
        self.admin_actions.select_privilege_checkbox()
        self.admin_actions.click_reset_changes_button()

        self.admin_actions.comparison_text_from_title_english_field(self.e_service_title)
        self.admin_actions.check_privilege_checkbox_is_not_checked()

    @allure.title("view created e-service")
    @pytest.mark.slow
    def test_view_created_e_service(self, super_user, create_and_delete_e_service):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()

        # switch account
        profile_menu = UserProfileMenu(browser.element(".q-user__info"))
        profile_menu.click_on_menu()
        self.dashboard_action.click_on_switch_account_link()
        self.workspace_actions.should_have_workspace_list_appear()

        self.workspace_actions.select_first_company_account()
        self.e_services_action.switch_to_e_services()
        self.e_services_action.search_by_category_name(category_name=self.e_service_title)

    @allure.title("filtration on the e-service page")
    def test_filtration_e_service_page(self, super_user, create_and_delete_e_service):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()
        self.admin_actions.filter_e_services(english_title=self.e_service_title)

    @allure.title("check clear all filters functionality")
    def test_check_clear_filters(self, super_user, create_and_delete_e_service):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()
        self.admin_actions.filter_e_services(english_title=self.e_service_title)

    @allure.title("Add and edit icon to the e-service")
    def test_add_icon(self, super_user, create_and_delete_e_service):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()
        self.admin_actions.filter_e_services(english_title=self.e_service_title)
        self.admin_actions.click_edit_button()
        self.admin_actions.add_icon()
        self.admin_actions.click_on_save_e_service_button()
        self.admin_actions.check_successful_action(SuccessMessage.E_SERVICE_EDITED_MESSAGE)
        self.admin_actions.filter_e_services(english_title=self.e_service_title)
        self.admin_actions.click_edit_button()
        self.admin_actions.check_icon()
        self.admin_actions.add_icon()
        self.admin_actions.click_on_save_e_service_button()
        self.admin_actions.check_successful_action(SuccessMessage.E_SERVICE_EDITED_MESSAGE)

    @allure.title("Change icon for the e-service")
    def test_delete_icon(self, super_user, create_and_delete_e_service):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()
        self.admin_actions.filter_e_services(english_title=self.e_service_title)
        self.admin_actions.click_edit_button()
        self.admin_actions.add_icon()
        self.admin_actions.click_on_save_e_service_button()
        self.admin_actions.filter_e_services(english_title=self.e_service_title)
        self.admin_actions.click_edit_button()
        self.admin_actions.delete_icon()
        self.admin_actions.click_on_save_e_service_button()
