from __future__ import annotations

import datetime
import time

import allure
import pyperclip
from selene import be, browser, have, query
from selene.core.condition import not_
from selene.support.shared.jquery_style import s, ss

from utils.selene import scroll_into_view_if_needed


class MyResumePage:
    dropdown = s(".tippy-content")
    add = s("//p[.='Add']")
    submit_btn = s("button[type='submit']")
    edit_btn = s("//p[.='Edit']")
    delete_btn = s("//p[.='Delete']")
    start_date = s("#startDate")
    end_date = s("#endDate")

    add_volunteer_experience = ss('a[href="/my-resume/volunteer-works/add"]').second
    edit_volunteer_experience = ss('#volunteer-works [data-component="Button"]').second
    organization_name = s("#organizationName")
    event_name = s("#volunteerEventName")
    delete_volunteer_exp_btn = s(".Button__Wrapper-ds__sc-6fc6di-0.lcPyRu")
    confirm_delete_experience_btn = s("//p[contains(.,'Delete experience')]")
    about_section_btn = s("//p[contains(text(), 'About')]")
    save_changes_btn = s("//p[normalize-space()='Save changes']")

    summary_section = s("#summary")
    add_summary = s("[href='/my-resume/summary']")
    edit_summary_btn = s('#about [data-component="Button"]')
    delete_summary_btn = s("//p[.='Delete summary']")
    confirm_delete_summary_btn = ss("//p[.='Delete summary']").second

    add_training_btn = ss("[href='/my-resume/trainings/add']").second
    training_name = s("#courseName")
    training_provider = s("#courseProvider")
    edit_trainings_btn = s("//section[@id='trainings']//p[.='Edit']")
    resume_sharing_scroll = s("//nav[@aria-label='Breadcrumb']")
    confirm_delete_trainings = s("//p[.='Delete training']")
    trainings_section = s("#trainings")
    training_list_name = s("//section[@id='trainings']//h4[text()]")

    share_resume_btn = s('a[href="/my-resume/resume-sharing"]')
    create_new_link_btn = s("//p[.='Create new link']")
    enter_link_name = s("#linkName")
    expiration_date = s("#expiryDate")
    value_expiration_date = s("div.CalendarCell__Cell-ds__sc-1awceb6-0.cPVzib")
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
    organizationName = s("#organizationName")
    certification_name = s("#certificateName")
    credential_id = s("#credentialId")
    issue_date = s("#issueDate")
    does_not_expire = s("#doesNotExpire")
    expiration_certificate_date = s("#expirationDate")
    description = s(".ql-editor.ql-blank")
    upload_file = s("#file-upload-input")
    add_link = s("//p[.='Add a link']")
    list_of_professional_certificates = ss("//p[.='qa sertificare']")
    confirm_delete_record = s("//p[.='Delete certificate']")

    @allure.step
    def add_volunteering_record(self) -> MyResumePage:
        self.add_volunteer_experience.click()
        self.organization_name.type("QA TEST " + str(datetime.date.today()))
        self.event_name.type("QA TEST")
        self.start_date.click()
        select_date = datetime.date.today()
        self.selectable_days.element_by(have.exact_text(str(select_date.day))).click()
        self.end_date.click()
        self.selectable_days.element_by(have.exact_text(str(select_date.day))).click()
        self.submit_btn.click()
        return self

    @allure.step
    def edit_volunteering_record(self) -> MyResumePage:
        self.edit_volunteer_experience.click()
        scroll_into_view_if_needed(self.add)
        self.edit_btn.click()
        self.organization_name.set_value("QA TEST 1")
        self.event_name.set_value("QA TEST 1")
        self.save_changes_btn.click()
        return self

    @allure.step
    def delete_volunteer_exp(self) -> MyResumePage:
        self.edit_volunteer_experience.click()
        time.sleep(2)
        self.delete_volunteer_exp_btn.click()
        self.confirm_delete_experience_btn.click()
        return self

    @allure.step
    def add_summary_record(self) -> MyResumePage:
        self.add_summary.click()
        self.summary_section.set_value("Test summary")
        self.submit_btn.click()
        return self

    @allure.step
    def delete_about_summary(self) -> MyResumePage:
        self.edit_summary_btn.click()
        scroll_into_view_if_needed(self.delete_summary_btn)
        self.delete_summary_btn.click()
        self.confirm_delete_summary_btn.click()
        return self

    @allure.step
    def add_trainings_record(self) -> MyResumePage:
        self.add_training_btn.click()
        self.training_name.set_value("TEST QA NAME")
        self.training_provider.set_value("TEST QA PROVIDER")
        self.start_date.click()
        select_date = datetime.date.today()
        self.selectable_days.element_by(have.exact_text(str(select_date.day))).click()
        self.end_date.click()
        self.selectable_days.element_by(have.exact_text(str(select_date.day))).click()
        self.submit_btn.click()
        return self

    def edit_training_record(self) -> MyResumePage:
        self.edit_trainings_btn.click()
        scroll_into_view_if_needed(self.edit_btn)
        self.edit_btn.click()
        self.training_name.set_value("QA TEST CHANGED")
        self.submit_btn.click()
        self.training_list_name.should(have.exact_text("QA TEST CHANGED"))
        return self

    @allure.step
    def delete_training_record(self) -> MyResumePage:
        self.edit_trainings_btn.click()
        scroll_into_view_if_needed(self.add)
        self.delete_btn.click()
        self.confirm_delete_trainings.click()
        return self

    @allure.step("Create new link")
    def create_new_link(self) -> MyResumePage:
        self.share_resume_btn.click()
        time.sleep(2)
        self.create_new_link_btn.click()
        self.enter_link_name.type("TEST QA LINK 1")
        self.expiration_date.click()
        self.value_expiration_date.click()
        self.next_step_btn.click()
        self.agreement_checkbox.click()
        self.submit_btn.click()
        self.back_to_resume_sharing.click()
        return self

    @allure.step
    def create_second_link(self) -> MyResumePage:
        self.create_new_link_btn.click()
        self.enter_link_name.type("TEST QA LINK 2")
        self.expiration_date.click()
        self.value_expiration_date.click()
        self.next_step_btn.click()
        self.agreement_checkbox.click()
        self.submit_btn.click()
        self.back_to_resume_sharing.click()
        return self

    @allure.step
    def edit_link(self) -> MyResumePage:
        self.link_options.click()
        self.edit_btn.click()
        self.change_link_name.set("TEST QA EDIT 1")
        self.submit_btn.click()
        return self

    @allure.step
    def delete_link(self) -> MyResumePage:
        self.link_options.click()
        self.delete_btn.click()
        self.confirm_delete_link.click()
        return self

    @allure.step
    def verify_second_added_link_status(self) -> MyResumePage:
        self.link_options.click()
        self.edit_btn.click()
        self.visibility_toggle.should(have.attribute("aria-checked", "true"))
        return self

    @allure.step
    def share_resume(self) -> MyResumePage:
        self.share_resume_btn.click()
        return self

    @allure.step
    def copy_link(self) -> MyResumePage:
        self.copy_link_btn.click()
        return self

    @allure.step
    def open_link_in_current_tab(self) -> MyResumePage:
        clipboard_url = str(pyperclip.paste())
        browser.driver.get(clipboard_url)
        return self

    @allure.step
    def verify_resume_availability(self) -> MyResumePage:
        self.experiences_section.should(be.visible)
        return self

    @allure.step
    def verify_resume_unavailability(self) -> MyResumePage:
        self.unavailable_resume.should(be.visible)
        return self

    @allure.step
    def disable_link_visibility(self) -> MyResumePage:
        self.link_options.click()
        self.edit_btn.click()
        self.toggle.click()
        self.visibility_toggle.should(have.attribute("aria-checked", "false"))
        self.save_changes_btn.click()
        return self

    @allure.step
    def verify_profile_analytics(self) -> MyResumePage:
        self.share_resume_btn.click()
        self.total_views.should(be.visible)
        self.unique_viewers.should(be.visible)
        self.total_time_spent.should(be.visible)
        self.average_time.should(be.visible)
        return self

    @allure.step
    def verify_changed_profile_analytics(self, new_total_views) -> MyResumePage:
        browser.driver.back()
        browser.driver.refresh()
        self.total_views.should(have.no.exact_text(new_total_views))
        return self

    @allure.step
    def get_total_views(self) -> str:
        total_views = self.total_views.get(query.text)
        return total_views

    @allure.step
    def add_education_record(self) -> MyResumePage:
        self.add_education_btn.click()
        self.educational_institute_name.type("test")
        self.major_or_specialization.type("test major")
        self.country.click()
        self.dropdown.all('[role="option"]').first.click()
        self.qualification_type.click()
        self.dropdown.all('[role="option"]').second.click()
        self.start_date.click()
        select_date = datetime.date.today()
        self.selectable_days.element_by(have.exact_text(str(select_date.day))).click()
        self.end_date.click()
        self.selectable_days.element_by(have.exact_text(str(select_date.day))).click()
        self.submit_btn.click()
        return self

    @allure.step
    def verify_list_of_education_records(self) -> MyResumePage:
        self.education_section.should(be.visible)
        self.list_of_education_records.should(have.size_greater_than(0))
        return self

    @allure.step
    def edit_the_education_record(self) -> MyResumePage:
        scroll_into_view_if_needed(self.edit_education_btn)
        self.edit_education_btn.click()
        self.edit_btn.click()
        self.educational_institute_name.set_value("test edited")
        self.major_or_specialization.set_value("test major edited")
        self.submit_btn.click()
        return self

    @allure.step
    def delete_the_education_record(self) -> MyResumePage:
        scroll_into_view_if_needed(self.edit_education_btn)
        self.edit_education_btn.click()
        self.delete_btn.click()
        self.confirm_delete_education_btn.click()
        return self

    @allure.step
    def add_skills_record(self) -> MyResumePage:
        self.add_new_skill.click()
        self.your_skill.type("test skill" + str(datetime.date.today()))
        self.add_skill.click()
        self.submit_btn.click()
        return self

    @allure.step
    def verify_skills_records(self) -> MyResumePage:
        self.skills_section.should(be.visible)
        self.list_of_skills.should(have.size_greater_than(0))
        return self

    @allure.step
    def edit_skills_record(self) -> MyResumePage:
        self.edit_skills_section.click()
        scroll_into_view_if_needed(self.delete_skill)
        self.delete_skill.click()
        self.submit_btn.click()
        return self

    @allure.step
    def delete_skills_record(self) -> MyResumePage:
        self.edit_skills_section.click()
        scroll_into_view_if_needed(self.delete_skills)
        self.delete_skills.click()
        self.confirm_delete_skills.click()
        return self

    @allure.step
    def add_professional_certificates_record(self) -> MyResumePage:
        self.add_professional_certificates.click()
        self.organization_name.type("test organization")
        self.certification_name.type("test certificate")
        self.credential_id.type("123")
        self.issue_date.click()
        select_date = datetime.date.today()
        self.selectable_days.element_by(have.exact_text(str(select_date.day))).click()
        self.expiration_certificate_date.click()
        self.selectable_days.element_by(have.exact_text(str(select_date.day))).click()
        self.description.type("Test description")
        self.submit_btn.click()
        return self

    @allure.step
    def verify_professional_certificate_records(self) -> MyResumePage:
        scroll_into_view_if_needed(self.professional_certificates_section)
        self.professional_certificates_section.should(be.visible)
        self.list_of_professional_certificates.should(have.size_greater_than(0))
        return self

    @allure.step
    def edit_professional_certificate_record(self) -> MyResumePage:
        self.edit_professional_certificates.click()
        scroll_into_view_if_needed(self.edit_btn)
        self.edit_btn.click()
        self.organization_name.set("test organization 2")
        self.certification_name.set("test certificate 2")
        self.credential_id.set("123456")
        self.submit_btn.click()
        return self

    @allure.step
    def delete_professional_certificate_record(self) -> MyResumePage:
        self.edit_professional_certificates.click()
        scroll_into_view_if_needed(self.delete_btn)
        self.delete_btn.click()
        self.confirm_delete_record.click()
        return self
