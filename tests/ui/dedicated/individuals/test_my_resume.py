import allure

from data.dedicated.individuals.individuals_constans import IndividualsServices
from data.dedicated.models.individuals import user1
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.INDIVIDUALS)


@allure.title('AS-237, 238, 239, 240 Test add, edit, delete, verify new volunteering record')
@case_id(12044, 12047, 12373, 12374)
def test_verify_add_new_volunteering_record():
    qiwa.login_as_user(user1.personal_number)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.select_service(IndividualsServices.RESUME_MANAGEMENT)
    qiwa.my_resume_page.add_volunteering_record() \
        .edit_volunteering_record() \
        .delete_volunteer_exp()


@allure.title('AS-332, 333 Test add, delete About me summary')
@case_id(13524, 17383)
def test_add_delete_about_me_summary():
    qiwa.login_as_user(user1.personal_number)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.select_service(IndividualsServices.RESUME_MANAGEMENT)
    qiwa.my_resume_page.add_summary_record() \
        .delete_about_summary()


@allure.title('AS-335, 336, 337, 338 Test add training section, add, edit, delete training record')
@case_id(43455, 13526, 43456, 43457)
def test_add_delete_edit_training_record():
    qiwa.login_as_user(user1.personal_number)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.select_service(IndividualsServices.RESUME_MANAGEMENT)
    qiwa.my_resume_page.add_trainings_record() \
        .edit_training_record() \
        .delete_training_record()


@allure.title('AS-242, 250, 251 Test for add, edit, delete Share resume links')
@case_id(16932, 16923, 16921)
def test_add_delete_edit_share_resume_links():
    qiwa.login_as_user(user1.personal_number)
    qiwa.workspace_page.select_individual_account()
    qiwa.my_resume_page.create_new_link() \
        .edit_link() \
        .delete_link()


@allure.title('AS-356 Test for creating more than one link')
@case_id(16924)
def test_multiple_links():
    qiwa.login_as_user(user1.personal_number)
    qiwa.workspace_page.select_individual_account()
    qiwa.my_resume_page.create_new_link() \
        .create_second_link() \
        .verify_second_added_link_status()


@allure.title('AS-358, 362 Test for active links in resume sharing')
@case_id(16925, 16944)
def test_for_active_links():
    qiwa.login_as_user(user1.personal_number)
    qiwa.workspace_page.select_individual_account()
    qiwa.my_resume_page.create_new_link() \
        .copy_link() \
        .open_link_in_current_tab() \
        .verify_resume_availability()


@allure.title('AS-357 Test for inactive links in resume sharing')
@case_id(16926)
def test_for_inactive_links():
    qiwa.login_as_user(user1.personal_number)
    qiwa.workspace_page.select_individual_account()
    qiwa.my_resume_page.create_new_link() \
        .disable_link_visibility() \
        .copy_link() \
        .open_link_in_current_tab() \
        .verify_resume_unavailability()


@allure.title('AS-365 Test for viewing statistics')
@case_id(16918)
def test_for_viewing_statistics():
    qiwa.login_as_user(user1.personal_number)
    qiwa.workspace_page.select_individual_account()
    qiwa.my_resume_page.verify_profile_analytics()


@allure.title('AS-366 Test for generating views')
@case_id(16917)
def test_for_generating_views():
    qiwa.login_as_user(user1.personal_number)
    qiwa.workspace_page.select_individual_account()
    total_views = qiwa.my_resume_page.get_total_views()
    qiwa.my_resume_page.create_new_link() \
        .copy_link() \
        .open_link_in_current_tab() \
        .verify_resume_availability() \
        .verify_changed_profile_analytics(total_views)


@allure.title('AS-398 Test add, edit, delete and verify Education record')
@case_id(162948, 162951, 162952, 162953)
def test_add_edit_delete_verify_education_record():
    qiwa.login_as_user(user1.personal_number)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.select_service(IndividualsServices.RESUME_MANAGEMENT)
    qiwa.my_resume_page.add_education_record() \
        .verify_list_of_education_records() \
        .edit_the_education_record() \
        .delete_the_education_record()


@allure.title('AS-416 Test add, edit, delete and verify Skills record')
@case_id(162959, 164831, 164836, 164838)
def test_add_edit_delete_verify_skills_record():
    qiwa.login_as_user(user1.personal_number)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.select_service(IndividualsServices.RESUME_MANAGEMENT)
    qiwa.my_resume_page.add_skills_record() \
        .verify_skills_records() \
        .edit_skills_record() \
        .delete_skills_record()


@allure.title('AS-421 Test add, edit, delete and verify Certificates record')
@case_id(167371, 167374, 167375, 167379)
def test_add_edit_delete_verify_certificate_record():
    qiwa.login_as_user(user1.personal_number)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.select_service(IndividualsServices.RESUME_MANAGEMENT)
    qiwa.my_resume_page.add_professional_certificates_record() \
        .verify_professional_certificate_records() \
        .edit_professional_certificate_record() \
        .delete_professional_certificate_record()
