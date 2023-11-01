import allure

from data.dedicated.models.individuals import user1
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.INDIVIDUALS)


@allure.title('AS-237, 238, 239, 240 Test add, edit, delete, verify new volunteering record')
@case_id(12044, 12047, 12373, 12374)
def test_verify_add_new_volunteering_record():
    qiwa.login_as_user(user1.login_id)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.navigate_to_resume_management() \
        .add_resume_section() \
        .navigate_to_volunteer_section() \
        .fill_volunteer_details() \
        .navigate_to_edit_volunteer_exp() \
        .edit_field_volunteer_details() \
        .delete_volunteer_exp()


@allure.title('AS-332, 333 Test add, delete About me summary')
@case_id(13524, 17383)
def test_add_delete_about_me_summary():
    qiwa.login_as_user(user1.login_id)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.navigate_to_resume_management() \
        .add_resume_section() \
        .click_on_about_section() \
        .add_summary() \
        .delete_about_summary()


@allure.title('AS-335, 336, 337, 338 Test add training section, add, edit, delete training record')
@case_id(43455, 13526, 43456, 43457)
def test_add_delete_edit_training_record():
    qiwa.login_as_user(user1.login_id)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.navigate_to_resume_management() \
        .add_resume_section() \
        .click_on_trainings_section() \
        .add_trainings_record() \
        .edit_training_record() \
        .delete_training_record()


@allure.title('AS-242, 250, 251 Test for add, edit, delete Share resume links')
@case_id(16932, 16923, 16921)
def test_add_delete_edit_share_resume_links():
    qiwa.login_as_user(user1.login_id)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.navigate_to_resume_management() \
        .click_on_share_resume_btn() \
        .create_new_link() \
        .edit_link() \
        .delete_link()


@allure.title('AS-356 Test for creating more than one link')
@case_id(16924)
def test_multiple_links():
    qiwa.login_as_user(user1.login_id)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.navigate_to_resume_management() \
        .click_on_share_resume_btn() \
        .create_new_link() \
        .create_second_link() \
        .navigate_to_shared_links_tab() \
        .verify_second_added_link_status()


@allure.title('AS-358, 362 Test for active links in resume sharing')
@case_id(16925, 16944)
def test_for_active_links():
    qiwa.login_as_user(user1.login_id)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.navigate_to_resume_management() \
        .click_on_share_resume_btn() \
        .create_new_link() \
        .copy_link() \
        .open_link_in_new_tab() \
        .verify_resume_availability()


@allure.title('AS-357 Test for inactive links in resume sharing')
@case_id(16926)
def test_for_inactive_links():
    qiwa.login_as_user(user1.login_id)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.navigate_to_resume_management() \
        .click_on_share_resume_btn() \
        .disable_link_visibility() \
        .copy_link() \
        .open_link_in_new_tab() \
        .verify_resume_unavailability()


@allure.title('AS-365 Test for viewing statistics')
@case_id()
def test_for_viewing_statistics():
    qiwa.login_as_user(user1.login_id)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.navigate_to_resume_management() \
        .click_on_share_resume_btn() \
        .verify_profile_analytics()


@allure.title('AS-366 Test for generating views')
@case_id()
def test_for_generating_views():
    qiwa.login_as_user(user1.login_id)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.navigate_to_resume_management()
    qiwa.individual_page.click_on_share_resume_btn()
    total_views = qiwa.individual_page.get_total_views()
    qiwa.individual_page.create_new_link()
    qiwa.individual_page.copy_link()
    qiwa.individual_page.open_link_in_new_tab()
    qiwa.individual_page.verify_resume_availability()
    qiwa.individual_page.verify_changed_profile_analytics(total_views)
