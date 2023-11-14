import allure
import pytest

from data.data_portal.constants import Admin
from data.data_portal.dataset import AdminData
from data.lmi.data_set import AdminDataSet
from src.ui.dataportal import data_portal
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LMI)


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to log in')
@case_id(44533, 72802)
def test_ability_to_log_in(login_to_data_portal_admin):
    pass


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify inability to login with invalid data')
@case_id(44534, 72803)
@pytest.mark.parametrize('login, password', AdminData.invalid_data)
def test_inability_to_log_in_invalid_data(login, password):
    data_portal.open_data_portal_admin_login_page()
    data_portal.data_portal_admin.input_creds(login, password)
    data_portal.data_portal_admin.check_validation()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Copy past into another browser')
@case_id(51830)
def test_copy_past_link_into_another_browser(login_to_data_portal_admin):
    data_portal.data_portal_admin.check_copy_past_link_into_another_browser()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Create report with mandatory fields')
@case_id(74930, 46616, 46617, 46630, 46632)
def test_create_report_using_mandatory_fields(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.create_report()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Edit report')
@case_id(74930, 102050)
def test_edit_report_using(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.create_report()
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.edit_report()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Delete report')
@case_id(74930, 102053)
def test_delete_report(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.create_report()
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.delete_report()
    data_portal.data_portal_admin.check_deleted_report()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Add terms to Category')
@case_id(74939)
def test_add_terms(login_to_data_portal_admin, clear_categories):
    data_portal.open_data_portal_admin_category_page()
    data_portal.data_portal_admin.add_terms()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Edit terms to Category')
@case_id(74939)
def test_edit_terms(login_to_data_portal_admin, clear_categories):
    data_portal.open_data_portal_admin_category_page()
    data_portal.data_portal_admin.add_terms()
    data_portal.open_data_portal_admin_category_page()
    data_portal.data_portal_admin.edit_terms()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Delete terms to Category')
@case_id(74939)
def test_delete_terms(login_to_data_portal_admin, clear_categories):
    data_portal.open_data_portal_admin_category_page()
    data_portal.data_portal_admin.add_terms()
    data_portal.open_data_portal_admin_category_page()
    data_portal.data_portal_admin.delete_terms()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Add Takeaway Section')
@case_id(74931, 74932)
def test_add_takeaway_section(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_takeaway_section()
    data_portal.data_portal_admin.check_takeaway_section()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Check validation title for Takeaway Section')
@case_id(71701)
def test_validation_title_for_takeaway_section(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_takeaway_section()
    data_portal.data_portal_admin.check_title_validation()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Check validation content for Takeaway Section')
@case_id(71701)
def test_validation_content_for_takeaway_section(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_takeaway_section()
    data_portal.data_portal_admin.check_title_validation()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Edit Takeaway Section')
@case_id(74931, 74932, 71699)
def test_edit_takeaway_section(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_takeaway_section()
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.edit_takeaway_section()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Delete Takeaway Section')
@case_id(74931, 74932, 71700)
def test_delete_takeaway_section(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_takeaway_section()
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.delete_takeaway_section()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to open and view Reports page')
@case_id(46616)
def test_ability_to_open_and_view_report_page(login_to_data_portal_admin, clear_reports, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.check_report_tabs()
    data_portal.data_portal_admin.check_report_filters()
    data_portal.data_portal_admin.check_report_categories()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to open "Translation" page for selected report.')
@case_id(102052)
def test_ability_to_open_translation_page(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.create_report()
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.check_translation_page()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to use Filter')
@case_id(101967, 102011, 102030, 102034, 102035, 102029, 102033, 102032, 102031, 102028,
         102025, 102026, 102019, 102012, 101966, 101965, 101963, 99863)
@pytest.mark.parametrize('criteria', AdminDataSet.criteria)
def test_ability_to_use_filter(login_to_data_portal_admin, clear_categories, criteria):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.perform_filtration(*criteria)
    data_portal.data_portal_admin.check_filtration()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to Sort reports by title')
@case_id(102049)
def test_ability_to_sort_by_title(login_to_data_portal_admin, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.create_report(report_name=Admin.AUTOMATION_EDIT, exist_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.sort_by_title()
    data_portal.data_portal_admin.check_sorting()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to Sort reports by status')
@case_id(102049)
def test_ability_to_sort_by_status(login_to_data_portal_admin, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.create_report(report_name=Admin.AUTOMATION_EDIT, exist_category=True,
                                                unpublished=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.sort_by_status()
    data_portal.data_portal_admin.check_sorting()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to Sort reports by updated')
@case_id(102049)
def test_ability_to_sort_by_updated(login_to_data_portal_admin, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.create_report(report_name=Admin.AUTOMATION_EDIT, exist_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.sort_by_updated()
    data_portal.data_portal_admin.check_sorting()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to select reports')
@case_id(102042)
def test_ability_to_select_reports(login_to_data_portal_admin, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.select_report()
    data_portal.data_portal_admin.check_checkbox_status(checked=True)
    data_portal.data_portal_admin.check_action_form(visible=True)


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to deselect reports')
@case_id(102042)
def test_ability_to_deselect_reports(login_to_data_portal_admin, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    for _ in range(2):
        data_portal.data_portal_admin.select_report()
    data_portal.data_portal_admin.check_checkbox_status(unchecked=True)
    data_portal.data_portal_admin.check_action_form(invisible=True)


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to select all reports')
@case_id(102042)
def test_ability_to_select_all_reports(login_to_data_portal_admin, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.select_all_reports()
    data_portal.data_portal_admin.check_checkbox_status(checked=True)
    data_portal.data_portal_admin.check_action_form(visible=True)


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to deselect all reports')
@case_id(102042)
def test_ability_to_deselect_all_reports(login_to_data_portal_admin, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    for _ in range(2):
        data_portal.data_portal_admin.select_all_reports()
    data_portal.data_portal_admin.check_checkbox_status(unchecked=True)
    data_portal.data_portal_admin.check_action_form(invisible=True)


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to bulk editing to Change Category')
@case_id(102062)
def test_ability_to_bulk_editing_to_change_category(login_to_data_portal_admin, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_category_page()
    data_portal.data_portal_admin.add_terms(name=Admin.AUTOMATION_EDIT)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.select_report()
    data_portal.data_portal_admin.change_category_by_action_form()
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.check_change_category()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to add "Takeaway content" with an empty state.')
@case_id(71703, 71698)
def test_ability_to_add_takeaway_content_with_empty_state(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_content_page()
    data_portal.data_portal_admin.add_content_as_takeaway_section()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to add translation.')
@case_id(71702)
def test_ability_to_add_translation(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_translation()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to delete translation.')
@case_id(71704)
def test_ability_to_delete_translation(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_translation()
    data_portal.data_portal_admin.delete_translation()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify the display of elements on the report editor page.')
@case_id(46631)
def test_display_of_elements_on_report_editor_page(login_to_data_portal_admin):
    data_portal.data_portal_admin.check_display_of_elements_on_report_editor_page()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify inability to create report without any fields')
@case_id(46640)
def test_create_report_without_values(login_to_data_portal_admin):
    data_portal.data_portal_admin.create_report_without_values()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify inability to create report without name')
@case_id(46640)
def test_create_report_without_name(login_to_data_portal_admin):
    data_portal.data_portal_admin.create_report_without_name()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify inability to create report without duration')
@case_id(46640)
def test_create_report_without_duration(login_to_data_portal_admin):
    data_portal.data_portal_admin.create_report_without_duration()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify inability to create report without file')
@case_id(46640)
def test_create_report_without_file(login_to_data_portal_admin):
    data_portal.data_portal_admin.create_report_without_file()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify inability to create report with invalid duration')
@pytest.mark.parametrize('value', AdminData.invalid_duration)
@case_id(46890)
def test_create_report_without_duration(login_to_data_portal_admin, value):
    data_portal.data_portal_admin.create_report_with_invalid_duration(value=value)


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to add Alternative text and title into the Hero image')
@case_id(46642)
def test_create_report_with_alternative_text_and_title(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.create_report_with_alternative_text_and_title()


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify ability to add allowed types of image.')
@pytest.mark.parametrize('file_format', AdminData.file_format)
@case_id(46647, 46868, 46869)
def test_ability_add_allowed_types_of_image(login_to_data_portal_admin, clear_reports, file_format):
    data_portal.data_portal_admin.check_ability_add_allowed_types_of_image(file_format=file_format)


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify inability to add other types of image.')
@pytest.mark.parametrize('other_file_format', AdminData.other_file_format)
@case_id(46647)
def test_inability_add_other_types_of_image(login_to_data_portal_admin, other_file_format):
    data_portal.data_portal_admin.check_inability_add_other_types_of_image(file_format=other_file_format)


@pytest.mark.skip('Skipped due to https://employeesgate.atlassian.net/browse/LR-2664')
@allure.title('Verify limitation of the size for Hero images')
@pytest.mark.parametrize('file_format_less_1280', AdminData.file_format_less_1280)
@case_id(46868)
def test_limitation_size_of_image(login_to_data_portal_admin, file_format_less_1280):
    data_portal.data_portal_admin.check_limitation_size_of_image(file_format=file_format_less_1280)
