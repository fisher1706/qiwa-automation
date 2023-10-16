import allure
import pytest

from data.data_portal.dataset import AdminData
from src.ui.dataportal import data_portal
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@allure.title('Verify ability to log in')
@case_id(44533, 72802)
def test_ability_to_log_in(login_to_data_portal_admin):
    pass


@allure.title('Verify inability to login with invalid data')
@case_id(44534, 72803)
@pytest.mark.parametrize('login, password', AdminData.invalid_data)
def test_inability_to_log_in_invalid_data(login, password):
    data_portal.open_data_portal_admin_login_page()
    data_portal.data_portal_admin.input_creds(login, password)
    data_portal.data_portal_admin.check_validation()


@allure.title('Copy past into another browser')
@case_id(51830)
def test_copy_past_link_into_another_browser(login_to_data_portal_admin):
    data_portal.data_portal_admin.check_copy_past_link_into_another_browser()


@allure.title('Create report with mandatory fields')
@case_id(74930)
def test_create_report_using_mandatory_fields(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.create_report_using_mandatory_fields()


@allure.title('Edit report')
@case_id(74930)
def test_edit_report_using(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.create_report_using_mandatory_fields()
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.edit_report()


@allure.title('Delete report')
@case_id(74930)
def test_delete_report(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.create_report_using_mandatory_fields()
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.delete_report()


@allure.title('Add terms to Category')
@case_id(74939)
def test_add_terms(login_to_data_portal_admin, clear_categories):
    data_portal.open_data_portal_admin_category_page()
    data_portal.data_portal_admin.add_terms()


@allure.title('Edit terms to Category')
@case_id(74939)
def test_edit_terms(login_to_data_portal_admin, clear_categories):
    data_portal.open_data_portal_admin_category_page()
    data_portal.data_portal_admin.add_terms()
    data_portal.open_data_portal_admin_category_page()
    data_portal.data_portal_admin.edit_terms()


@allure.title('Delete terms to Category')
@case_id(74939)
def test_delete_terms(login_to_data_portal_admin, clear_categories):
    data_portal.open_data_portal_admin_category_page()
    data_portal.data_portal_admin.add_terms()
    data_portal.open_data_portal_admin_category_page()
    data_portal.data_portal_admin.delete_terms()


@allure.title('Add Takeaway Section')
@case_id(74931, 74932)
def test_add_takeaway_section(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_takeaway_section()


@allure.title('Edit Takeaway Section')
@case_id(74931, 74932)
def test_edit_takeaway_section(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_takeaway_section()
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.edit_takeaway_section()


@allure.title('Delete Takeaway Section')
@case_id(74931, 74932)
def test_delete_takeaway_section(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_takeaway_section()
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.delete_takeaway_section()
