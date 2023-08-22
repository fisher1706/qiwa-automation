import allure
import pytest

from data.sso.dataset import EServiceDataset
from data.validation_message import SuccessMessage
from src.api.controllers.e_service_controller import EServiceController
from src.api.controllers.workspaces_api_actions import WorkspacesApiActions
from src.ui.actions.e_services import EServiceActions
from src.ui.actions.sign_in import LoginActions
from src.ui.pages.admin_page import AdminPage
from src.ui.pages.workspaces_page import WorkspacesPage


@allure.feature('Admin E-Services')
@pytest.mark.e_service_suite
@pytest.mark.daily
@pytest.mark.ui
@pytest.mark.core
@pytest.mark.usefixtures("go_to_auth_page", "delete_service_categories")
class TestAdminEServicesCategory:

    @pytest.fixture(autouse=True)
    def pre_test(self, http_client):
        self.login_action = LoginActions()
        self.workspace_actions = WorkspacesPage()
        self.e_services_action = EServiceActions()
        self.auth_api = WorkspacesApiActions(http_client)
        self.admin_actions = AdminPage()

    @pytest.fixture
    def create_category(self, super_user, http_client):
        self.auth_api = WorkspacesApiActions(http_client)
        self.e_service_api = EServiceController(http_client)
        self.auth_api.login_user(super_user.personal_number, super_user.password)
        self.e_service.api.create_tag()
        self.category_name = self.e_service.api.tag_english_name

    @allure.title("add-edit-delete category")
    @pytest.mark.parametrize("arabic_name, english_name, code", EServiceDataset.e_service_category_valid_data)
    def test_edit_category(self, super_user, arabic_name, english_name, code):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()
        self.admin_actions.go_to_e_services_categories_list_page()
        self.admin_actions.check_e_services_category_page()
        self.admin_actions.click_add_category_button()
        self.admin_actions.create_new_category_field(arabic_name, english_name, code)
        self.admin_actions.filter_category_by_english_name(english_name)
        new_en_name = 'new_en_name'
        self.admin_actions.edit_category(new_en_name)
        self.admin_actions.check_successful_action(SuccessMessage.E_SERVICE_CATEGORY_UPDATE_MESSAGE)
        self.admin_actions.filter_category_by_english_name(new_en_name)
        self.admin_actions.delete_category()
        self.admin_actions.check_successful_action(SuccessMessage.E_SERVICE_CATEGORY_DELETED)

    @allure.title("cancel creation category")
    @pytest.mark.parametrize("arabic_name, english_name, code", EServiceDataset.e_service_category_valid_data)
    def test_cancel_category_creation(self, super_user, arabic_name, english_name, code):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()
        self.admin_actions.go_to_e_services_categories_list_page()
        self.admin_actions.click_add_category_button()
        self.admin_actions.create_new_category_field(arabic_name, english_name, code, is_cancel=True)
        self.admin_actions.check_cancel_action()

    @allure.title("cancel editing category")
    def test_cancel_category_editing(self, create_category, super_user):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()
        self.admin_actions.go_to_e_services_categories_list_page()
        new_en_name = 'new_en_name'
        self.admin_actions.edit_category(new_en_name, is_cancel=True)
        self.admin_actions.filter_category_by_english_name(self.category_name)
        self.admin_actions.check_filtration_on_category_page(self.category_name)

    @allure.title("filtration on e-services categories page")
    def test_filtration_on_e_services_categories_page(self, super_user, create_category):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()
        self.admin_actions.go_to_e_services_categories_list_page()
        self.admin_actions.filter_category_by_english_name(self.category_name)
        self.admin_actions.check_filtration_on_category_page(self.category_name)

    @allure.title("check clear filtration on e-services categories page")
    def test_clear_filtration_on_e_services_categories_page(self, super_user, create_category):
        self.login_action.complete_login(super_user)
        self.workspace_actions.select_admin_account()
        self.admin_actions.wait_page_to_load()
        self.admin_actions.go_to_e_services_tab()
        self.admin_actions.go_to_e_services_categories_list_page()
        self.admin_actions.filter_category_by_english_name(self.category_name)
        self.admin_actions.clear_filters_on_category_page()
