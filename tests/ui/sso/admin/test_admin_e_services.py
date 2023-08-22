import allure
import pytest

from data.dataset import EServiceDataset
from data.validation_message import SuccessMessage
from src.ui.qiwa import qiwa

pytestmark = [pytest.mark.demo, pytest.mark.ui, pytest.mark.sso, pytest.mark.admin]


@allure.title("Check admin e-services page is displayed")
def test_check_admin_e_service_page_is_displayed():
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .check_button_block_is_displayed() \
        .check_e_services_table_is_displayed()


@allure.title("Check e-service creation")
@pytest.mark.parametrize("en_title, ar_title, service_code, en_link, ar_link", EServiceDataset.e_service_valid_data)
def test_creation_e_service(en_title, ar_title, service_code, en_link, ar_link):
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .open_e_services_page() \
        .add_e_service() \
        .fill_in_the_fields_for_new_e_service(en_title, ar_title, service_code, en_link, ar_link) \
        .select_privilege_checkbox() \
        .click_on_save_e_service_button() \
        .check_successful_action(SuccessMessage.E_SERVICE_CREATED_MESSAGE)
    qiwa.e_services_page.enter_e_service_en_filter(en_title) \
        .click_delete_e_service() \
        .confirm_js_alert("Are you sure you want to delete this service?")
    qiwa.admin_page.check_successful_action(SuccessMessage.E_SERVICE_DELETED_MESSAGE)


@allure.title("Edit e-services")
def test_edit_e_service(create_e_service_via_api, delete_e_service_via_api):
    e_service_title = create_e_service_via_api
    new_title = "new english title"
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .open_e_services_page() \
        .filter_by_english_title(e_service_title) \
        .check_e_service_detail() \
        .click_edit_button() \
        .edit_english_title_field(new_title) \
        .click_on_save_e_service_button() \
        .check_successful_action(SuccessMessage.E_SERVICE_EDITED_MESSAGE) \
        .filter_by_english_title(new_title) \
        .check_e_service_detail()


@allure.title("reset changes and data")
def test_reset_changes(create_e_service_via_api, delete_e_service_via_api):
    e_service_title = create_e_service_via_api
    new_title = "new english title"
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .open_e_services_page() \
        .filter_by_english_title(e_service_title) \
        .click_edit_button() \
        .edit_english_title_field(new_title) \
        .select_privilege_checkbox() \
        .click_reset_changes_button() \
        .comparison_text_from_title_english_field(e_service_title) \
        .check_privilege_checkbox_is_not_checked()


@allure.title("view created e-service")
@pytest.mark.slow
def test_view_created_e_service(create_e_service_via_api, delete_e_service_via_api):
    e_service_title = create_e_service_via_api
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .open_e_services_page() \
        # switch account
    qiwa.user_profile.click_on_profile_menu()
    qiwa.dashboard_action.click_on_switch_account_link()
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.workspace_page.select_first_company_account()
    qiwa.e_services_page.switch_to_e_services() \
        .search_by_category_name(category_name=e_service_title)


@allure.title("filtration on the e-service page")
def test_filtration_e_service_page(create_e_service_via_api, delete_e_service_via_api):
    e_service_title = create_e_service_via_api
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .open_e_services_page() \
        .filter_e_services(english_title=e_service_title)


@allure.title("check clear all filters functionality")
def test_check_clear_filters(create_e_service_via_api, delete_e_service_via_api):
    e_service_title = create_e_service_via_api
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .open_e_services_page() \
        .filter_e_services(english_title=e_service_title) \
        .filter_e_services(english_title=e_service_title) \
        .clear_e_services_filter()


@allure.title("Add and edit icon to the e-service")
def test_add_icon(create_e_service_via_api, delete_e_service_via_api):
    e_service_title = create_e_service_via_api
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .open_e_services_page() \
        .filter_e_services(english_title=e_service_title) \
        .click_edit_button() \
        .add_icon() \
        .click_on_save_e_service_button() \
        .check_successful_action(SuccessMessage.E_SERVICE_EDITED_MESSAGE) \
        .filter_e_services(english_title=e_service_title) \
        .click_edit_button() \
        .check_icon()


@allure.title("Change icon for the e-service")
def test_delete_icon(create_e_service_via_api, delete_e_service_via_api):
    e_service_title = create_e_service_via_api
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .open_e_services_page() \
        .filter_e_services(english_title=e_service_title) \
        .click_edit_button() \
        .add_icon() \
        .click_on_save_e_service_button() \
        .check_successful_action(SuccessMessage.E_SERVICE_EDITED_MESSAGE) \
        .filter_e_services(english_title=e_service_title) \
        .click_edit_button() \
        .delete_icon() \
        .click_on_save_e_service_button() \
        .check_successful_action(SuccessMessage.E_SERVICE_EDITED_MESSAGE)
