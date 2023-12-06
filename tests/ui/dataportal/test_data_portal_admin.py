import allure
import pytest

from data.data_portal.constants import Admin
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
@case_id(74930, 46616, 46617, 46630, 46632)
def test_create_report_using_mandatory_fields(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.create_report()


@allure.title('Edit report')
@case_id(74930, 102050)
def test_edit_report_using(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.create_report()
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.edit_report()


@allure.title('Delete report')
@case_id(74930, 102053)
def test_delete_report(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.create_report()
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.delete_report()
    data_portal.data_portal_admin.check_deleted_report()


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


@allure.title('Check validation title for Takeaway Section')
@case_id(71701)
def test_validation_title_for_takeaway_section(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.check_title_validation()


@pytest.mark.skip("Skipped due to https://employeesgate.atlassian.net/browse/LR-2744,"
                  "https://employeesgate.atlassian.net/browse/LR-2746")
@allure.title('Check validation content for Takeaway Section')
@case_id(71701)
def test_validation_content_for_takeaway_section(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.check_content_validation()


@allure.title('Verify ability to use Filter')
@pytest.mark.skip('Skipped due to logic issue while creating new Category')
@case_id(101967, 102011, 102030, 102034, 102035, 102029, 102033, 102032, 102031, 102028,
         102025, 102026, 102019, 102012, 101966, 101965, 101963, 99863)
@pytest.mark.parametrize('criteria', AdminData.criteria)
def test_ability_to_use_filter(login_to_data_portal_admin, clear_categories, clear_reports, criteria):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.perform_filtration(*criteria)
    data_portal.data_portal_admin.check_filtration()


@pytest.mark.skip("Skipped due to https://employeesgate.atlassian.net/browse/LR-2746")
@allure.title('Verify ability to Sort reports by title')
@case_id(102049)
def test_ability_to_sort_by_title(login_to_data_portal_admin, clear_reports, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.create_report(report_name=Admin.AUTOMATION_EDIT, exist_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.sort_by_title()
    data_portal.data_portal_admin.check_sorting()


@pytest.mark.skip("Skipped due to https://employeesgate.atlassian.net/browse/LR-2746")
@allure.title('Verify ability to Sort reports by status')
@case_id(102049)
def test_ability_to_sort_by_status(login_to_data_portal_admin, clear_reports, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.create_report(report_name=Admin.AUTOMATION_EDIT, exist_category=True,
                                                unpublished=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.sort_by_status()
    data_portal.data_portal_admin.check_sorting()


@pytest.mark.skip("Skipped due to https://employeesgate.atlassian.net/browse/LR-2746")
@allure.title('Verify ability to Sort reports by updated')
@case_id(102049)
def test_ability_to_sort_by_updated(login_to_data_portal_admin, clear_reports, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.create_report(report_name=Admin.AUTOMATION_EDIT, exist_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.sort_by_updated()
    data_portal.data_portal_admin.check_sorting()


@allure.title('Verify ability to select reports')
@pytest.mark.skip('Skipped due to logic issue while creating new Category')
@case_id(102042)
def test_ability_to_select_reports(login_to_data_portal_admin, clear_reports, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.select_report()
    data_portal.data_portal_admin.check_checkbox_status(checked=True)
    data_portal.data_portal_admin.check_action_form(visible=True)


@allure.title('Verify ability to deselect reports')
@pytest.mark.skip('Skipped due to logic issue while creating new Category')
@case_id(102042)
def test_ability_to_deselect_reports(login_to_data_portal_admin, clear_reports, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.deselect_report()
    data_portal.data_portal_admin.check_checkbox_status(unchecked=True)


@allure.title('Verify ability to select all reports')
@pytest.mark.skip('Skipped due to logic issue while creating new Category')
@case_id(102042)
def test_ability_to_select_all_reports(login_to_data_portal_admin, clear_reports, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.select_all_reports()
    data_portal.data_portal_admin.check_checkbox_status(checked=True)
    data_portal.data_portal_admin.check_action_form(visible=True)


@allure.title('Verify ability to deselect all reports')
@pytest.mark.skip('Skipped due to logic issue while creating new Category')
@case_id(102042)
def test_ability_to_deselect_all_reports(login_to_data_portal_admin, clear_reports, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.deselect_all_reports()
    data_portal.data_portal_admin.check_checkbox_status(unchecked=True)


@allure.title('Verify ability to bulk editing to Change Category')
@pytest.mark.skip('Skipped due to logic issue while creating new Category')
@case_id(102062)
def test_ability_to_bulk_editing_to_change_category(login_to_data_portal_admin, clear_reports, clear_categories):
    data_portal.data_portal_admin.create_report(new_category=True)
    data_portal.open_data_portal_admin_category_page()
    data_portal.data_portal_admin.add_terms(name=Admin.AUTOMATION_EDIT)
    data_portal.open_data_portal_admin_report_page()
    data_portal.data_portal_admin.select_report()
    data_portal.data_portal_admin.change_category_by_action_form()
    data_portal.data_portal_admin.check_change_category()


@allure.title('Verify ability to add "Takeaway content" with an empty state.')
@case_id(71703, 71698)
def test_ability_to_add_takeaway_content_with_empty_state(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_content_page()
    data_portal.data_portal_admin.add_content_as_takeaway_section()


@allure.title('Verify ability to add translation.')
@case_id(71702)
def test_ability_to_add_translation(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_takeaway_section()
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_translation()


@pytest.mark.skip("Skipped due to absense success message form")
@allure.title('Verify ability to delete translation.')
@case_id(71704)
def test_ability_to_delete_translation(login_to_data_portal_admin, clear_takeaway_section):
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_takeaway_section()
    data_portal.open_data_portal_admin_takeaway_page()
    data_portal.data_portal_admin.add_translation()
    data_portal.data_portal_admin.delete_translation()


@allure.title('Verify the display of elements on the report editor page.')
@case_id(46631)
def test_display_of_elements_on_report_editor_page(login_to_data_portal_admin):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.check_display_of_elements_on_report_editor_page()


@allure.title('Verify inability to create report without any fields')
@case_id(46640)
def test_create_report_without_values(login_to_data_portal_admin):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.create_report_without_values()


@allure.title('Verify inability to create report without name')
@case_id(46640)
def test_create_report_without_name(login_to_data_portal_admin):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.create_report_without_name()


@allure.title('Verify inability to create report without duration')
@case_id(46640)
def test_create_report_without_duration(login_to_data_portal_admin):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.create_report_without_duration()


@allure.title('Verify inability to create report without file')
@case_id(46640)
def test_create_report_without_file(login_to_data_portal_admin):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.create_report_without_file()


@allure.title('Verify inability to create report with invalid duration')
@pytest.mark.parametrize('value', AdminData.invalid_duration)
@case_id(46890)
def test_create_report_without_duration(login_to_data_portal_admin, value):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.create_report_with_invalid_duration(value=value)


@allure.title('Verify ability to add Alternative text and title into the Hero image')
@case_id(46642)
def test_create_report_with_alternative_text_and_title(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.create_report_with_alternative_text_and_title()


@allure.title('Verify ability to add allowed types of image.')
@pytest.mark.parametrize('file_format', AdminData.file_format)
@case_id(46647, 46868, 46869)
def test_ability_add_allowed_types_of_image(login_to_data_portal_admin, clear_reports, file_format):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.check_ability_add_allowed_types_of_image(file_format=file_format)


@allure.title('Verify inability to add other types of image.')
@pytest.mark.parametrize('other_file_format', AdminData.other_file_format)
@case_id(46647)
def test_inability_add_other_types_of_image(login_to_data_portal_admin, other_file_format):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.check_inability_add_other_types_of_image(file_format=other_file_format)


@allure.title('Verify limitation of the size for Hero images')
@pytest.mark.parametrize('file_format_less_1280', AdminData.file_format_less_1280)
@case_id(46868)
def test_limitation_size_of_image(login_to_data_portal_admin, file_format_less_1280):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.check_limitation_size_of_image(file_format=file_format_less_1280)


@allure.title('Verify ability to add chart block. Verify ability to add description. Verify ability to add source.')
@case_id(134007, 141001, 141002)
def test_ability_to_add_chart_block(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type()
    data_portal.data_portal_admin.add_chart_block()
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify ability to add Line chart with Number, Currency and Percentage formats')
@case_id(134015, 134721, 134731)
@pytest.mark.parametrize('chart_format', [Admin.NUMBER, Admin.CURRENCY, Admin.PERCENTAGE])
def test_ability_to_add_line_chart_with_possible_formats(login_to_data_portal_admin, clear_reports, chart_format):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type()
    data_portal.data_portal_admin.fill_mandatory_fields_for_line_chart(chart_format)
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify ability to add Line chart with a comparison chart.'
              ' Verify ability to add Line chart without Title')
@case_id(134849, 134848)
def test_ability_add_line_chart_with_comparison_chart(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.add_line_chart_with_comparison_chart()


@allure.title('Verify ability to disable legend. Verify ability to disable Values')
@case_id(140997, 140999)
def test_ability_add_report_with_disabled_show_checkboxes(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type()
    data_portal.data_portal_admin.add_report_with_disabled_show_checkboxes()
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify ability to change color')
@case_id(141000)
def test_ability_change_color(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type()
    data_portal.data_portal_admin.add_chart_block_with_changed_color()
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify ability to create a chart with more than 1 tab.')
@case_id(141003)
def test_ability_create_chart_with_more_than_1_tab(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type()
    data_portal.data_portal_admin.create_chart_with_more_than_1_tab()
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify ability to delete tab.')
@case_id(141027)
def test_ability_delete_chart(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type()
    data_portal.data_portal_admin.create_chart_with_more_than_1_tab()
    data_portal.data_portal_admin.save_chart()
    data_portal.data_portal_admin.delete_chart_tab()


@allure.title('Verify ability to edit line chart.')
@case_id(141004)
def test_ability_edit_line_chart(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type()
    data_portal.data_portal_admin.fill_mandatory_fields_for_line_chart()
    data_portal.data_portal_admin.save_report_with_content()
    data_portal.data_portal_admin.edit_chart_tab()


@allure.title('Report with single image block, '
              'Single image block can contain only png, gif, jpg, jpeg images formats')
@pytest.mark.parametrize('file_format', AdminData.file_format)
@case_id(46870, 46875)
def test_create_single_image_block_with_allowed_types_of_image(login_to_data_portal_admin, clear_reports, file_format):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type(block_type=Admin.IMAGE)
    data_portal.data_portal_admin.fill_required_fields_for_image_block(file_format=file_format)
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Single images must be larger than 1280x720 pixels')
@pytest.mark.parametrize('file_format_less_1280', AdminData.file_format_less_1280)
@case_id(46877)
def test_limitation_size_of_image(login_to_data_portal_admin, file_format_less_1280):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type(block_type=Admin.IMAGE)
    data_portal.data_portal_admin.check_image_limitation_size_for_image_chart(file_format=file_format_less_1280)


@allure.title('Verify ability to add text with Bold, Italic, Underline, and Strikethrough formats, '
              'Verify ability to add text with Superscript and Subscript')
@case_id(123626, 123629)
@pytest.mark.parametrize('format_text', AdminData.format_text,
                         ids=['Bold', 'Italic', 'Underline', 'Strikethrough', 'Subscript', 'Superscript'])
def test_ability_add_formats_for_image_block(login_to_data_portal_admin, clear_reports, format_text):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type(block_type=Admin.IMAGE)
    data_portal.data_portal_admin.fill_required_fields_for_image_block()
    data_portal.data_portal_admin.set_format_text(format_text)
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify ability to add text with Special characters')
@case_id(123630)
def test_ability_add_special_characters_for_image_block(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type(block_type=Admin.IMAGE)
    data_portal.data_portal_admin.fill_required_fields_for_image_block()
    data_portal.data_portal_admin.set_special_character()
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify ability to add text with Hyperlinks')
@case_id(123628)
def test_ability_add_text_with_hyperlinks_for_image_block(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type(block_type=Admin.IMAGE)
    data_portal.data_portal_admin.fill_required_fields_for_image_block()
    data_portal.data_portal_admin.set_hyperlink()
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify ability to add text with different text alignments')
@case_id(123627)
@pytest.mark.parametrize('alignment', AdminData.alignment_text,
                         ids=['Align left', 'Align center', 'Align right', 'Justify'])
def test_ability_add_text_with_different_alignments_for_image_block(login_to_data_portal_admin, clear_reports,
                                                                    alignment):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type(block_type=Admin.IMAGE)
    data_portal.data_portal_admin.fill_required_fields_for_image_block()
    data_portal.data_portal_admin.set_alignment(alignment)
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify ability to create image block with paragraph, '
              'Verify that Image+paragraph block can contain only allowed images formats')
@pytest.mark.parametrize('file_format', AdminData.file_format)
@case_id(102083, 102084)
def test_that_image_paragraph_block_with_allowed_image_format(login_to_data_portal_admin, clear_reports, file_format):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type(block_type=Admin.IMAGE)
    data_portal.data_portal_admin.select_image_type_option(block_type=Admin.IMAGE_PARAGRAPH)
    data_portal.data_portal_admin.fill_required_fields_for_image_paragraph(file_format=file_format)
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify that Image paragraph block should contain images larger than 1280x720 pixels')
@pytest.mark.parametrize('file_format_less_1280', AdminData.file_format_less_1280)
@case_id(102086)
def test_that_image_paragraph_block_with_larger_image_size(login_to_data_portal_admin, file_format_less_1280):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type(block_type=Admin.IMAGE)
    data_portal.data_portal_admin.select_image_type_option(block_type=Admin.IMAGE_PARAGRAPH)
    data_portal.data_portal_admin.check_image_limitation_size_for_image_chart(file_format=file_format_less_1280)


@allure.title('Verify ability to add text with Bold, Italic, Underline, and Strikethrough formats, '
              'Verify ability to add text with Superscript and Subscript')
@case_id(102131, 123619)
@pytest.mark.parametrize('format_text', AdminData.format_text,
                         ids=['Bold', 'Italic', 'Underline', 'Strikethrough', 'Subscript', 'Superscript'])
def test_ability_add_formats_for_image_paragraph_block(login_to_data_portal_admin, clear_reports, format_text):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type(block_type=Admin.IMAGE)
    data_portal.data_portal_admin.select_image_type_option(block_type=Admin.IMAGE_PARAGRAPH)
    data_portal.data_portal_admin.fill_required_fields_for_image_paragraph()
    data_portal.data_portal_admin.set_format_text(format_text)
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify ability to add text with Special characters')
@case_id(123620)
def test_ability_add_special_characters_for_image_paragraph_block(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type(block_type=Admin.IMAGE)
    data_portal.data_portal_admin.select_image_type_option(block_type=Admin.IMAGE_PARAGRAPH)
    data_portal.data_portal_admin.fill_required_fields_for_image_paragraph()
    data_portal.data_portal_admin.set_special_character()
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify ability to add text with Hyperlinks')
@case_id(123618)
def test_ability_add_text_with_hyperlinks_for_image_paragraph_block(login_to_data_portal_admin, clear_reports):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type(block_type=Admin.IMAGE)
    data_portal.data_portal_admin.select_image_type_option(block_type=Admin.IMAGE_PARAGRAPH)
    data_portal.data_portal_admin.fill_required_fields_for_image_paragraph()
    data_portal.data_portal_admin.set_hyperlink()
    data_portal.data_portal_admin.save_report_with_content()


@allure.title('Verify ability to add text with different text alignments')
@case_id(123617)
@pytest.mark.parametrize('alignment', AdminData.alignment_text,
                         ids=['Align left', 'Align center', 'Align right', 'Justify'])
def test_ability_add_text_with_different_alignments_for_image_paragraph_block(login_to_data_portal_admin, clear_reports,
                                                                              alignment):
    data_portal.data_portal_admin.click_on_add_report_button()
    data_portal.data_portal_admin.fill_mandatory_fields_for_report()
    data_portal.data_portal_admin.select_content_block_type(block_type=Admin.IMAGE)
    data_portal.data_portal_admin.select_image_type_option(block_type=Admin.IMAGE_PARAGRAPH)
    data_portal.data_portal_admin.fill_required_fields_for_image_paragraph()
    data_portal.data_portal_admin.set_alignment(alignment)
    data_portal.data_portal_admin.save_report_with_content()
