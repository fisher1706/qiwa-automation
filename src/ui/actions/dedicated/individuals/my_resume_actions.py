from __future__ import annotations

from src.ui.qiwa import qiwa
from utils.allure import allure_steps


@allure_steps
class MyResumeActions:
    def add_volunteering_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_add_volunteer_experience()
         .type_organization_name()
         .type_event_name()
         .click_on_start_date()
         .select_day()
         .click_on_end_date()
         .select_day()
         .click_on_submit())
        return self

    def verify_volunteering_section(self) -> MyResumeActions:
        (qiwa.my_resume_page.verify_volunteering_section_is_visible()
         .verify_volunteering_list())
        return self

    def edit_volunteering_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_on_edit_volunteer_experience()
         .edit_record()
         .type_organization_name()
         .type_event_name()
         .click_on_save_changes())
        return self

    def delete_volunteering_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_on_edit_volunteer_experience()
         .delete_volunteer_exp())
        return self

    def add_summary_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_add_summary_record()
         .type_summary_section().submit_summary_btn())
        return self

    def edit_summary_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_edit_summary_record()
         .edit_summary_section().submit_summary_btn())
        return self

    def delete_summary_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_edit_summary_record()
         .delete_summary_record().click_confirm_delete_summary())
        return self

    def add_trainings_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_add_trainings_record()
         .type_training_name()
         .type_provider_name()
         .click_on_start_date()
         .select_day()
         .click_on_end_date()
         .select_day()
         .submit_btn())
        return self

    def verify_training_section(self) -> MyResumeActions:
        (qiwa.my_resume_page.verify_training_section_is_visible()
         .verify_training_list())
        return self

    def edit_training_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.edit_training_record()
         .edit_btn()
         .edit_training_name()
         .submit_btn())
        return self

    def delete_training_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.edit_training_record()
         .delete_record()
         .confirm_delete_training_btn())
        return self

    def add_share_resume_links(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_share_resume()
         .click_create_new_link()
         .type_link_name("Test qa link")
         .click_on_expiration_date()
         .select_day()
         .click_on_next_step()
         .click_on_agreement_checkbox()
         .click_on_submit()
         .click_on_back_to_resume_sharing())
        return self

    def edit_share_resume_links(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_on_link_options()
         .edit_record()
         .click_on_change_link_name()
         .click_on_submit())
        return self

    def delete_share_resume_links(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_on_link_options()
         .delete_record()
         .click_on_confirm_delete_link())
        return self

    def create_second_share_resume_links(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_create_new_link()
         .type_link_name("Test qa link second")
         .click_on_expiration_date()
         .select_day()
         .click_on_next_step()
         .click_on_agreement_checkbox()
         .click_on_submit()
         .click_on_back_to_resume_sharing())
        return self

    def verify_share_resume_link_status(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_on_link_options()
         .edit_record()
         .verify_second_added_link_status())
        return self

    def disable_link_visibility(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_on_link_options()
         .edit_record()
         .click_on_toggle()
         .verify_unchecked_toggle()
         .click_on_save_changes())
        return self

    def verify_profile_analytics(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_share_resume()
         .verify_total_views()
         .verify_unique_viewers()
         .verify_total_time_spent()
         .verify_average_time())
        return self

    def add_education_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_on_add_education_record()
         .type_educational_institute_name()
         .type_major_or_specialization()
         .select_country()
         .select_qualification_type()
         .click_on_start_date()
         .select_day()
         .click_on_end_date()
         .select_day()
         .click_on_submit())
        return self

    def verify_education(self) -> MyResumeActions:
        (qiwa.my_resume_page.verify_education_section()
         .verify_list_of_education_records())
        return self

    def edit_the_education_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_edit_the_education_record()
         .edit_record()
         .edit_educational_institute_name()
         .edit_major_or_specialization()
         .click_on_submit())
        return self

    def delete_the_education_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_edit_the_education_record()
         .delete_record()
         .confirm_delete_education())
        return self

    def add_skills_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_on_add_skills_record()
         .type_your_skill()
         .click_add_skill_btn()
         .click_on_submit())
        return self

    def verify_skills(self) -> MyResumeActions:
        (qiwa.my_resume_page.verify_skills_records()
         .verify_list_of_skills())
        return self

    def edit_skills(self) -> MyResumeActions:
        (qiwa.my_resume_page.edit_skills_btn()
         .type_edited_skill()
         .click_add_skill_btn()
         .click_on_submit())
        return self

    def delete_skills(self) -> MyResumeActions:
        (qiwa.my_resume_page.edit_skills_btn()
         .delete_skills_btn()
         .confirm_delete_skills_btn())
        return self

    def add_professional_certificates_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_on_professional_certificates_record()
         .type_organization_name()
         .type_certification_name()
         .type_credential_id()
         .click_on_issue_date()
         .select_day()
         .click_on_expiration_certificate_date()
         .select_day()
         .type_description()
         .click_on_submit())
        return self

    def verify_professional_certificate(self) -> MyResumeActions:
        (qiwa.my_resume_page.verify_professional_certificate_section()
         .verify_list_of_professional_certificates())
        return self

    def edit_professional_certificate_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_on_edit_professional_certificate_record()
         .edit_record()
         .type_organization_name()
         .type_certification_name()
         .type_credential_id()
         .click_on_submit())
        return self

    def delete_professional_certificate_record(self) -> MyResumeActions:
        (qiwa.my_resume_page.click_on_edit_professional_certificate_record()
         .delete_record()
         .click_on_confirm_delete_record())
        return self


my_resume_actions = MyResumeActions()
