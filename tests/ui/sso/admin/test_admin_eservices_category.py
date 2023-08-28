import allure
import pytest

from data.sso.dataset import EServiceDataset
from data.validation_message import SuccessMessage
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

testmo_case_id = project(TestmoProject.QIWA_ADMIN)


@allure.title("Add delete category")
@pytest.mark.parametrize("arabic_name, english_name, code", EServiceDataset.e_service_category_valid_data)
@testmo_case_id(6327, 6328, 6329)
def test_add_category(arabic_name, english_name, code):
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .check_e_services_category_page() \
        .click_add_category_button() \
        .fill_new_category_field(arabic_name, english_name, code) \
        .click_save_category_button() \
        .filter_category_by_english_name(english_name) \
        .delete_category() \
        .check_successful_action(SuccessMessage.E_SERVICE_CATEGORY_DELETED)


@allure.title("Edit category")
@testmo_case_id(6330)
def test_edit_category(create_category):
    category_english_name = create_category
    category_new_en_name = 'new_en_name'
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .filter_category_by_english_name(category_english_name) \
        .edit_category(category_new_en_name) \
        .click_save_category_button() \
        .check_successful_action(SuccessMessage.E_SERVICE_CATEGORY_UPDATE_MESSAGE) \
        .filter_category_by_english_name(category_new_en_name) \
        .delete_category() \
        .check_successful_action(SuccessMessage.E_SERVICE_CATEGORY_DELETED)


@allure.title("Cancel creation category")
@testmo_case_id(6333)
@pytest.mark.parametrize("arabic_name, english_name, code", EServiceDataset.e_service_category_valid_data)
def test_cancel_category_creation(arabic_name, english_name, code):
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .click_add_category_button() \
        .fill_new_category_field(arabic_name, english_name, code) \
        .click_cansel_creating_category_button() \
        .check_cancel_action()


@allure.title("Cancel editing category")
@testmo_case_id(6334)
def test_cancel_category_editing(create_category):
    category_english_name = create_category
    category_new_en_name = 'new_en_name'
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .filter_category_by_english_name(category_english_name) \
        .edit_category(category_new_en_name) \
        .click_cansel_creating_category_button() \
        .filter_category_by_english_name(category_english_name) \
        .check_filtration_on_category_page(category_english_name)


@allure.title("Filtration on e-services categories page")
@testmo_case_id(6331)
def test_filtration_on_e_services_categories_page(create_category):
    category_english_name = create_category
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .filter_category_by_english_name(category_english_name) \
        .check_filtration_on_category_page(category_english_name)


@allure.title("Check clear filtration on e-services categories page")
@testmo_case_id(6332)
def test_clear_filtration_on_e_services_categories_page(create_category):
    category_english_name = create_category
    qiwa.login_as_admin() \
        .admin_page.wait_page_to_load() \
        .go_to_e_services_tab() \
        .go_to_e_services_categories_list_page() \
        .filter_category_by_english_name(category_english_name) \
        .clear_filters_on_category_page()
