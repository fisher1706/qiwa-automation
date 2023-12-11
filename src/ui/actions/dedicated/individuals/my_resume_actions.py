from __future__ import annotations

from src.ui.qiwa import qiwa
from utils.allure import allure_steps


@allure_steps
class MyResumeActions:
    def add_volunteering_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_add_volunteer_experience()
        qiwa.my_resume_page.type_organization_name()
        qiwa.my_resume_page.type_event_name()
        qiwa.my_resume_page.click_on_start_date()
        qiwa.my_resume_page.select_day()
        qiwa.my_resume_page.click_on_end_date()
        qiwa.my_resume_page.select_day()
        qiwa.my_resume_page.click_on_submit()
        return self

    def verify_volunteering_section(self) -> MyResumeActions:
        qiwa.my_resume_page.verify_volunteering_section_is_visible()
        qiwa.my_resume_page.verify_volunteering_list()
        return self

    def edit_volunteering_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_on_edit_volunteer_experience()
        qiwa.my_resume_page.edit_record()
        qiwa.my_resume_page.type_organization_name()
        qiwa.my_resume_page.type_event_name()
        qiwa.my_resume_page.click_on_save_changes()
        return self

    def delete_volunteering_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_on_edit_volunteer_experience()
        qiwa.my_resume_page.delete_volunteer_exp()
        return self

    def add_summary_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_add_summary_record()
        qiwa.my_resume_page.type_summary_section()
        qiwa.my_resume_page.submit_summary_btn()
        return self

    def edit_summary_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_edit_summary_record()
        qiwa.my_resume_page.edit_summary_section()
        qiwa.my_resume_page.submit_summary_btn()
        return self

    def delete_summary_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_edit_summary_record()
        qiwa.my_resume_page.delete_summary_record()
        qiwa.my_resume_page.click_confirm_delete_summary()
        return self

    def add_trainings_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_add_trainings_record()
        qiwa.my_resume_page.type_training_name()
        qiwa.my_resume_page.type_provider_name()
        qiwa.my_resume_page.click_on_start_date()
        qiwa.my_resume_page.select_day()
        qiwa.my_resume_page.click_on_end_date()
        qiwa.my_resume_page.select_day()
        qiwa.my_resume_page.submit_btn()
        return self

    def verify_training_section(self) -> MyResumeActions:
        qiwa.my_resume_page.verify_training_section_is_visible()
        qiwa.my_resume_page.verify_training_list()
        return self

    def edit_training_record(self) -> MyResumeActions:
        qiwa.my_resume_page.edit_training_record()
        qiwa.my_resume_page.edit_btn()
        qiwa.my_resume_page.edit_training_name()
        qiwa.my_resume_page.submit_btn()
        return self

    def delete_training_record(self) -> MyResumeActions:
        qiwa.my_resume_page.edit_training_record()
        qiwa.my_resume_page.delete_record()
        qiwa.my_resume_page.confirm_delete_training_btn()
        return self

    def add_share_resume_links(self) -> MyResumeActions:
        qiwa.my_resume_page.click_share_resume()
        qiwa.my_resume_page.click_create_new_link()
        qiwa.my_resume_page.type_link_name("Test qa link")
        qiwa.my_resume_page.click_on_expiration_date()
        qiwa.my_resume_page.select_day()
        qiwa.my_resume_page.click_on_next_step()
        qiwa.my_resume_page.click_on_agreement_checkbox()
        qiwa.my_resume_page.click_on_submit()
        qiwa.my_resume_page.click_on_back_to_resume_sharing()
        return self

    def edit_share_resume_links(self) -> MyResumeActions:
        qiwa.my_resume_page.click_on_link_options()
        qiwa.my_resume_page.edit_record()
        qiwa.my_resume_page.click_on_change_link_name()
        qiwa.my_resume_page.click_on_submit()
        return self

    def delete_share_resume_links(self) -> MyResumeActions:
        qiwa.my_resume_page.click_on_link_options()
        qiwa.my_resume_page.delete_record()
        qiwa.my_resume_page.click_on_confirm_delete_link()
        return self

    def create_second_share_resume_links(self) -> MyResumeActions:
        qiwa.my_resume_page.click_create_new_link()
        qiwa.my_resume_page.type_link_name("Test qa link second")
        qiwa.my_resume_page.click_on_expiration_date()
        qiwa.my_resume_page.select_day()
        qiwa.my_resume_page.click_on_next_step()
        qiwa.my_resume_page.click_on_agreement_checkbox()
        qiwa.my_resume_page.click_on_submit()
        qiwa.my_resume_page.click_on_back_to_resume_sharing()
        return self

    def verify_share_resume_link_status(self) -> MyResumeActions:
        qiwa.my_resume_page.click_on_link_options()
        qiwa.my_resume_page.edit_record()
        qiwa.my_resume_page.verify_second_added_link_status()
        return self

    def disable_link_visibility(self) -> MyResumeActions:
        qiwa.my_resume_page.click_on_link_options()
        qiwa.my_resume_page.edit_record()
        qiwa.my_resume_page.click_on_toggle()
        qiwa.my_resume_page.verify_unchecked_toggle()
        qiwa.my_resume_page.click_on_save_changes()
        return self

    def verify_profile_analytics(self) -> MyResumeActions:
        qiwa.my_resume_page.click_share_resume()
        qiwa.my_resume_page.verify_total_views()
        qiwa.my_resume_page.verify_unique_viewers()
        qiwa.my_resume_page.verify_total_time_spent()
        qiwa.my_resume_page.verify_average_time()
        return self

    def add_education_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_on_add_education_record()
        qiwa.my_resume_page.type_educational_institute_name()
        qiwa.my_resume_page.type_major_or_specialization()
        qiwa.my_resume_page.select_country()
        qiwa.my_resume_page.select_qualification_type()
        qiwa.my_resume_page.click_on_start_date()
        qiwa.my_resume_page.select_day()
        qiwa.my_resume_page.click_on_end_date()
        qiwa.my_resume_page.select_day()
        qiwa.my_resume_page.click_on_submit()
        return self

    def verify_education(self) -> MyResumeActions:
        qiwa.my_resume_page.verify_education_section()
        qiwa.my_resume_page.verify_list_of_education_records()
        return self

    def edit_the_education_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_edit_the_education_record()
        qiwa.my_resume_page.edit_record()
        qiwa.my_resume_page.edit_educational_institute_name()
        qiwa.my_resume_page.edit_major_or_specialization()
        qiwa.my_resume_page.click_on_submit()
        return self

    def delete_the_education_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_edit_the_education_record()
        qiwa.my_resume_page.delete_record()
        qiwa.my_resume_page.confirm_delete_education()
        return self

    def add_skills_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_on_add_skills_record()
        qiwa.my_resume_page.type_your_skill()
        qiwa.my_resume_page.click_add_skill_btn()
        qiwa.my_resume_page.click_on_submit()
        return self

    def verify_skills(self) -> MyResumeActions:
        qiwa.my_resume_page.verify_skills_records()
        qiwa.my_resume_page.verify_list_of_skills()
        return self

    def edit_skills(self) -> MyResumeActions:
        qiwa.my_resume_page.edit_skills_btn()
        qiwa.my_resume_page.type_edited_skill()
        qiwa.my_resume_page.click_add_skill_btn()
        qiwa.my_resume_page.click_on_submit()
        return self

    def delete_skills(self) -> MyResumeActions:
        qiwa.my_resume_page.edit_skills_btn()
        qiwa.my_resume_page.delete_skills_btn()
        qiwa.my_resume_page.confirm_delete_skills_btn()
        return self

    def add_professional_certificates_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_on_professional_certificates_record()
        qiwa.my_resume_page.type_organization_name()
        qiwa.my_resume_page.type_certification_name()
        qiwa.my_resume_page.type_credential_id()
        qiwa.my_resume_page.click_on_issue_date()
        qiwa.my_resume_page.select_day()
        qiwa.my_resume_page.click_on_expiration_certificate_date()
        qiwa.my_resume_page.select_day()
        qiwa.my_resume_page.type_description()
        qiwa.my_resume_page.click_on_submit()
        return self

    def verify_professional_certificate(self) -> MyResumeActions:
        qiwa.my_resume_page.verify_professional_certificate_section()
        qiwa.my_resume_page.verify_list_of_professional_certificates()
        return self

    def edit_professional_certificate_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_on_edit_professional_certificate_record()
        qiwa.my_resume_page.edit_record()
        qiwa.my_resume_page.type_organization_name()
        qiwa.my_resume_page.type_certification_name()
        qiwa.my_resume_page.type_credential_id()
        qiwa.my_resume_page.click_on_submit()
        return self

    def delete_professional_certificate_record(self) -> MyResumeActions:
        qiwa.my_resume_page.click_on_edit_professional_certificate_record()
        qiwa.my_resume_page.delete_record()
        qiwa.my_resume_page.click_on_confirm_delete_record()
        return self


my_resume_actions = MyResumeActions()
