from __future__ import annotations

import datetime

import pyperclip
from selene import be, browser, have, query
from selene.core.condition import not_
from selene.support.shared.jquery_style import s, ss

from utils.allure import allure_steps
from utils.selene import scroll_into_view_if_needed


@allure_steps
class MyResumePage:
    dropdown = s(".tippy-content")
    add = s("//p[.='Add']")
    submit_btn = s("button[type='submit']")
    edit_btn = s("//p[.='Edit']")
    delete_btn = s("//p[.='Delete']")
    start_date = s("#startDate")
    end_date = s("#endDate")

    add_volunteer_experience = ss('a[href="/my-resume/volunteer-works/add"]').first
    edit_volunteer_experience = ss('#volunteer-works [data-component="Button"]').second
    organization_name = s("#organizationName")
    event_name = s("#volunteerEventName")
    delete_volunteer_exp_btn = s(".Button__Wrapper-ds__sc-6fc6di-0.lcPyRu")
    confirm_delete_experience_btn = s("//p[contains(.,'Delete experience')]")
    about_section_btn = s("//p[contains(text(), 'About')]")
    save_changes_btn = s("//p[normalize-space()='Save changes']")
    volunteering_section = s("#volunteer-works")
    list_of_volunteering_records = ss(
        '#volunteer-works [class="Box__StyledBox-ds__sc-utz9m7-0 icusqv"]'
    )

    summary_section = s("#summary")
    add_summary_btn = s("[href='/my-resume/summary']")
    edit_summary_btn = s('#about [data-component="Button"]')
    delete_summary_btn = s("//p[.='Delete summary']")
    confirm_delete_summary_btn = ss("//p[.='Delete summary']").second

    click_add_training_btn = ss("[href='/my-resume/trainings/add']").second
    training_name = s("#courseName")
    training_provider = s("#courseProvider")
    edit_trainings_btn = s("//section[@id='trainings']//p[.='Edit']")
    resume_sharing_scroll = s("//nav[@aria-label='Breadcrumb']")
    confirm_delete_trainings = s("//p[.='Delete training']")
    trainings_section = s("#trainings")
    training_list_name = ss("//section[@id='trainings'][1]")

    share_resume_btn = s('a[href="/my-resume/resume-sharing"]')
    create_new_link_btn = s("//p[.='Create new link']")
    enter_link_name = s("#linkName")
    expiration_date = s("#expiryDate")
    agreement_checkbox = s('//label[@class="Checkbox__StyledLabel-ds__sc-t2he6b-2 hNRoEh"]')
    next_step_btn = s("//p[normalize-space()='Next step']")
    link_status = s("//p[@class='Text-ds__sc-lk593a-0 gggtgX']")
    back_to_resume_sharing = s("//p[.='Back to Resume sharing']")
    save_changes = s("//button[@form='edit-shared-link-form']")
    confirm_delete_link = s("//button[p[text()='Delete link']]")
    change_link_name = s("//form[@id='edit-shared-link-form']//input[@id='linkName']")
    share_links_tab = s("//p[text()='Shared links']")
    edit_link_tab = s('[id="modalBodyWrapper"]')
    visibility_toggle = s("[data-component='Switch'] input")
    experiences_section = s("#experiences")
    unavailable_resume = s("//p[contains(text(),'Unfortunately, we could not connect')]")
    toggle = s("[data-component='Switch']")
    total_views = s("//p[.='Total views']")
    unique_viewers = s("//p[.='Unique viewers']")
    total_time_spent = s("//p[.='Total time spent']")
    average_time = s("//p[.='Average time']")
    shared_links_list = ss("#shared-links-list")
    copy_link_btn = shared_links_list.all('[data-component="Link"]').first
    link_options = s('[data-component="Actions"]')

    education_section = s("#educations")
    add_education_btn = s('[href="/my-resume/educations/add"]')
    edit_education_btn = ss('#educations [data-component="Button"]').second
    educational_institute_name = s("#instituteName")
    major_or_specialization = s("#majorName")
    country = s("#country")
    qualification_type = s("#qualificationType")
    calendar_days = dropdown.ss('//td[@role="gridcell"]/div[@role="button"]')
    selectable_days = calendar_days.by(not_(have.attribute("aria-disabled")))
    list_of_education_records = ss('#educations [class="Box__StyledBox-ds__sc-utz9m7-0 iPxNsA"]')
    confirm_delete_education_btn = s('[data-testid="loading-button"]')

    skills_section = s("#skills")
    add_new_skill = s('[href="/my-resume/skills"]')
    edit_skills_section = s('#skills [data-component="Button"]')
    your_skill = s("#skill")
    add_skill = s("//p[.='Add skill']")
    delete_skill = s("button[aria-label^='Remove skill']")
    delete_skills = s("//p[.='Delete skills']")
    confirm_delete_skills = ss('[data-testid="loading-button"]').second
    list_of_skills = ss('#skills [data-component="TagGroup"]')

    professional_certificates_section = s("#professional-certificates")
    add_professional_certificates = s('[href="/my-resume/professional-certificates/add"]')
    edit_professional_certificates = ss(
        '#professional-certificates [data-component="Button"]'
    ).second
    certification_name = s("#certificateName")
    credential_id = s("#credentialId")
    issue_date = s("#issueDate")
    does_not_expire = s("#doesNotExpire")
    expiration_certificate_date = s("#expirationDate")
    description = s(".ql-editor.ql-blank")
    upload_file = s("#file-upload-input")
    add_link = s("//p[.='Add a link']")
    list_of_professional_certificates = ss(
        '#professional-certificates [class="Box__StyledBox-ds__sc-utz9m7-0 fVWnPo"]'
    )
    confirm_delete_record = s("//p[.='Delete certificate']")

    def click_add_volunteer_experience(self):
        self.add_volunteer_experience.click()
        return self

    def type_organization_name(self):
        self.organization_name.set("QA TEST " + str(datetime.date.today()))
        return self

    def type_event_name(self):
        self.event_name.set("QA TEST")
        return self

    def click_on_start_date(self):
        self.start_date.click()
        return self

    def select_day(self):
        select_date = datetime.date.today()
        self.selectable_days.element_by(have.exact_text(str(select_date.day))).click()
        return self

    def click_on_end_date(self):
        self.end_date.click()
        return self

    def click_on_submit(self):
        self.submit_btn.click()
        return self

    def verify_volunteering_section_is_visible(self):
        self.volunteering_section.should(be.visible)
        return self

    def verify_volunteering_list(self):
        self.list_of_volunteering_records.should(have.size_greater_than(0))
        return self

    def click_on_edit_volunteer_experience(self):
        self.edit_volunteer_experience.click()
        return self

    def edit_record(self):
        self.edit_btn.click()
        return self

    def click_on_save_changes(self):
        self.save_changes_btn.click()
        return self

    def delete_volunteer_exp(self):
        scroll_into_view_if_needed(self.delete_volunteer_exp_btn)
        self.delete_volunteer_exp_btn.click()
        self.confirm_delete_experience_btn.click()
        return self

    def click_add_summary_record(self):
        self.add_summary_btn.click()
        return self

    def type_summary_section(self):
        self.summary_section.set_value("Test summary")
        return self

    def click_edit_summary_record(self):
        self.edit_summary_btn.click()
        return self

    def edit_summary_section(self):
        self.summary_section.set_value("Test summary edited")
        return self

    def submit_summary_btn(self):
        self.submit_btn.click()
        return self

    def delete_summary_record(self):
        self.delete_summary_btn.click()
        return self

    def click_confirm_delete_summary(self):
        self.confirm_delete_summary_btn.click()
        return self

    def click_add_trainings_record(self):
        self.click_add_training_btn.click()
        return self

    def type_training_name(self):
        self.training_name.set_value("TEST QA NAME")
        return self

    def type_provider_name(self):
        self.training_provider.set_value("TEST QA PROVIDER")
        return self

    def edit_training_record(self):
        self.edit_trainings_btn.click()
        return self

    def edit_training_name(self):
        self.training_name.set_value("QA TEST CHANGED")

    def verify_training_section_is_visible(self):
        self.trainings_section.should(be.visible)
        return self

    def verify_training_list(self):
        self.training_list_name.should(have.size_greater_than(0))
        return self

    def confirm_delete_training_btn(self):
        self.confirm_delete_trainings.click()
        return self

    def click_share_resume(self):
        self.share_resume_btn.click()
        return self

    def click_create_new_link(self):
        self.create_new_link_btn.click()
        return self

    def type_link_name(self, link_name):
        self.enter_link_name.type(link_name)
        return self

    def click_on_expiration_date(self):
        self.expiration_date.click()
        return self

    def click_on_next_step(self):
        self.next_step_btn.click()
        return self

    def click_on_agreement_checkbox(self):
        self.agreement_checkbox.click()
        return self

    def click_on_back_to_resume_sharing(self):
        self.back_to_resume_sharing.click()
        return self

    def click_on_link_options(self):
        self.link_options.click()
        return self

    def click_on_change_link_name(self):
        self.change_link_name.set("TEST QA EDIT 1")
        return self

    def delete_record(self):
        self.delete_btn.click()
        return self

    def click_on_confirm_delete_link(self):
        self.confirm_delete_link.click()
        return self

    def verify_second_added_link_status(self):
        self.visibility_toggle.should(have.attribute("aria-checked", "true"))
        return self

    def share_resume(self):
        self.share_resume_btn.click()
        return self

    def copy_link(self):
        self.copy_link_btn.click()
        return self

    def open_link_in_current_tab(self):
        clipboard_url = str(pyperclip.paste())
        browser.driver.get(clipboard_url)
        return self

    def verify_resume_availability(self):
        self.experiences_section.should(be.visible)
        return self

    def verify_resume_unavailability(self):
        self.unavailable_resume.should(be.visible)
        return self

    def click_on_toggle(self):
        self.toggle.click()
        return self

    def verify_unchecked_toggle(self):
        self.visibility_toggle.should(have.attribute("aria-checked", "false"))
        return self

    def verify_total_views(self):
        self.total_views.should(be.visible)
        return self

    def verify_unique_viewers(self):
        self.unique_viewers.should(be.visible)
        return self

    def verify_total_time_spent(self):
        self.total_time_spent.should(be.visible)
        return self

    def verify_average_time(self):
        self.average_time.should(be.visible)
        return self

    def verify_changed_profile_analytics(self, new_total_views):
        browser.driver.back()
        browser.driver.refresh()
        self.total_views.should(have.no.exact_text(new_total_views))
        return self

    def get_total_views(self) -> str:
        total_views = self.total_views.get(query.text)
        return total_views

    def click_on_add_education_record(self):
        self.add_education_btn.click()
        return self

    def type_educational_institute_name(self):
        self.educational_institute_name.type("Test")
        return self

    def type_major_or_specialization(self):
        self.major_or_specialization.type("Test major")
        return self

    def select_country(self):
        self.country.click()
        self.dropdown.all('[role="option"]').first.click()
        return self

    def select_qualification_type(self):
        self.qualification_type.click()
        self.dropdown.all('[role="option"]').second.click()
        return self

    def verify_education_section(self):
        self.education_section.should(be.visible)
        return self

    def verify_list_of_education_records(self):
        self.list_of_education_records.should(have.size_greater_than(0))
        return self

    def click_edit_the_education_record(self):
        self.edit_education_btn.click()
        return self

    def edit_educational_institute_name(self):
        self.educational_institute_name.set_value("Test edited")
        return self

    def edit_major_or_specialization(self):
        self.major_or_specialization.set_value("Test Major Edited")
        return self

    def confirm_delete_education(self):
        self.confirm_delete_education_btn.click()
        return self

    def click_on_add_skills_record(self) -> MyResumePage:
        self.add_new_skill.click()
        return self

    def type_your_skill(self):
        self.your_skill.type("test skill" + str(datetime.date.today()))
        return self

    def type_edited_skill(self):
        self.your_skill.type("edit skill" + str(datetime.date.today()))
        return self

    def click_add_skill_btn(self):
        self.add_skill.click()
        return self

    def verify_skills_records(self):
        self.skills_section.should(be.visible)
        return self

    def verify_list_of_skills(self):
        self.list_of_skills.should(have.size_greater_than(0))
        return self

    def edit_skills_btn(self):
        self.edit_skills_section.click()
        return self

    def delete_skills_btn(self):
        self.delete_skills.click()
        return self

    def confirm_delete_skills_btn(self):
        self.confirm_delete_skills.click()
        return self

    def click_on_professional_certificates_record(self):
        self.add_professional_certificates.click()
        return self

    def type_certification_name(self):
        self.certification_name.set("test certificate")
        return self

    def type_credential_id(self):
        self.credential_id.type("1234")
        return self

    def click_on_issue_date(self):
        self.issue_date.click()
        return self

    def click_on_expiration_certificate_date(self):
        self.expiration_certificate_date.click()
        return self

    def type_description(self):
        self.description.type("Test description")
        return self

    def verify_professional_certificate_section(self):
        self.professional_certificates_section.should(be.visible)
        return self

    def verify_list_of_professional_certificates(self):
        self.list_of_professional_certificates.should(have.size_greater_than(0))
        return self

    def click_on_edit_professional_certificate_record(self):
        self.edit_professional_certificates.click()
        return self

    def click_on_confirm_delete_record(self):
        self.confirm_delete_record.click()
        return self
