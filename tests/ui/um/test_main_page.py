import allure
import pytest

from data.um.user_management_models2 import test_account_um_2
from src.ui.actions.um_actions.um_main import MainPageActions
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.USER_MANAGEMENT)


@allure.feature('Main page UI')
@pytest.mark.usefixtures("go_to_auth_page")
class TestMainPageUI:

    @pytest.fixture(autouse=True)
    def pre_test(self):
        self.um_main = MainPageActions()

    @allure.title("Check Main page UI")
    @case_id(7873)
    def test_main_page_elements(self):
        owner = test_account_um_2
        self.um_main.log_in_and_navigate_to_um(owner)
        self.um_main.wait_until_page_is_loaded()
        user_name = self.um_main.get_user_name()
        self.um_main.check_texts_on_main_page()
        self.um_main.check_search_main_page([owner.account.personal_number, user_name])

    @allure.title("Check the 'Users in _' tab and 'Users in Establishment Group' tab")
    @case_id(7880)
    def test_all_users_table(self):
        owner = test_account_um_2
        self.um_main.log_in_and_navigate_to_um(owner)
        self.um_main.check_company_title_in_users_table(labor_office_id=owner.labor_office_id,
                                                        seq_number=owner.sequence_number)
        self.um_main.compare_number_of_users_in_table()

    @allure.title("Check that User redirected to the 'All establishments under your Unified ID' section")
    @case_id(7877)
    def test_user_is_redirected_to_user_details(self):
        owner = test_account_um_2
        self.um_main.log_in_and_navigate_to_um(owner)
        self.um_main.navigate_to_view_details_page()

    @allure.title("Check that User redirected to the owner subscription flow")
    def test_user_is_redirected_to_owner_flow(self):
        owner = test_account_um_2
        self.um_main.log_in_and_navigate_to_um(owner)
        self.um_main.navigate_to_owner_flow()

    @allure.title("Check User has access to Establishments than subscription is Active/Inactive")
    @case_id(7875, 7876)
    def test_active_user_has_access(self):
        owner = test_account_um_2
        self.um_main.log_in_and_navigate_to_um(owner)
        self.um_main.check_user_status()
        self.um_main.check_user_status(False)

    @allure.title("Check 'Users in Establishment Group' table pagination")
    @case_id(7878)
    def test_pagination_for_users_table(self):
        owner = test_account_um_2
        self.um_main.log_in_and_navigate_to_um(owner)
        self.um_main.check_pagination_btns()

    @allure.title("Check that Group Manager displayed at the top of the users list")
    @case_id(23717)
    def test_that_owner_is_first_in_table(self):
        owner = test_account_um_2
        self.um_main.log_in_and_navigate_to_um(owner)
        self.um_main.check_owner_role_in_table()

    @allure.title("Check that 'User Management' page has AR localization")
    @case_id(7879)
    def test_localization(self):
        owner = test_account_um_2
        self.um_main.log_in_and_navigate_to_um(owner)
        self.um_main.check_localization()
