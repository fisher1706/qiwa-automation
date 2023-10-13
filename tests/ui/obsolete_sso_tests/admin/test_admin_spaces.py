import allure

from data.validation_message import ErrorMessage, SuccessMessage
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.QIWA_SSO)


@case_id(54975)
@allure.title("Create space - positive test")
def test_add_space():
    qiwa.login_as_admin() \
        .admin_page.wait_admin_page_to_load() \
        .go_to_spaces_tab()
    qiwa.admin_spaces_page.wait_admin_spaces_page_to_load() \
        .go_to_add_space_page() \
        .check_elements_on_create_space_page() \
        .fill_in_the_fields_for_new_space() \
        .click_create_space_button() \
        .check_message(SuccessMessage.SPACE_CREATED_MESSAGE) \
        .wait_admin_page_to_load() \
        .filter_space_by_en_title("English") \
        .delete_space()


@allure.title("Edit created space - positive test")
@case_id(54976)
def test_edit_space(create_space, delete_spase):
    space_title = create_space
    new_space_title = "new english title"
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .check_e_services_category_page() \
        .wait_page_to_load() \
        .filter_space_by_en_title(space_title) \
        .go_to_edit_space_page() \
        .enter_data_to_eng_name_field(new_space_title) \
        .click_create_space_button() \
        .check_message(SuccessMessage.SPACE_EDIT_MESSAGE)


@allure.title("Delete created space - positive test")
@case_id(54977)
def test_delete_space(create_space, delete_spase):
    space_title = create_space
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .check_e_services_category_page() \
        .wait_page_to_load() \
        .filter_space_by_en_title(space_title) \
        .delete_space_request() \
        .check_message(SuccessMessage.SPACE_DELETED_MESSAGE)


@allure.title("Check reset data button - positive test")
@case_id(54978)
def test_check_reset_data_button(create_space, delete_spase):
    space_title = create_space
    new_space_title = "new english title"
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .check_e_services_category_page() \
        .wait_page_to_load() \
        .filter_space_by_en_title(space_title) \
        .go_to_edit_space_page() \
        .enter_data_to_eng_name_field(new_space_title) \
        .click_reset_space_changes_button() \
        .should_space_english_title_have_text(space_title)


@allure.title("Check message for invalid format for field - negative test")
@case_id(54979)
def test_invalid_text_format_for_field(create_space, delete_spase):
    space_title = create_space
    invalid_space_format = "new1english#title"
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .check_e_services_category_page() \
        .wait_page_to_load() \
        .filter_space_by_en_title(space_title) \
        .go_to_edit_space_page() \
        .enter_data_to_eng_name_field(invalid_space_format) \
        .check_invalid_format_message(ErrorMessage.INVALID_SPACE_ENGLISH_NAME)


@allure.title("Check required field - negative test")
@case_id(54980)
def test_save_space_with_empty_fields(create_space, delete_spase):
    space_title = create_space
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .check_e_services_category_page() \
        .wait_page_to_load() \
        .filter_space_by_en_title(space_title) \
        .go_to_edit_space_page() \
        .empty_fields_should_have_proper_error_message()


@allure.title("Check filtration on spaces page - positive tests")
@case_id(54981)
def test_filtration(create_space, delete_spase):
    space_title = create_space
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .check_e_services_category_page() \
        .wait_page_to_load() \
        .filtration_should_have_results(space_title)


@allure.title("Check clear filter button - positive tests")
@case_id(54982)
def test_clear_filters(create_space, delete_spase):
    space_title = create_space
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .check_e_services_category_page() \
        .wait_page_to_load() \
        .filtration_should_have_results(space_title) \
        .clear_filters()
