from __future__ import annotations

import datetime
import time

import allure
import pyperclip
from selene import be, browser, have, query
from selene.support.shared.jquery_style import s, ss
from selenium.webdriver.common.keys import Keys

from data.constants import Language
from src.ui.components.raw.table import Table


class IndividualPage:
    service_card = ss('[data-component="ActionTile"] div')
    field_confirmation_code = ss('[inputmode="numeric"]')
    checkbox_agree = s("#termsOfService")
    btn_accept_the_request = s('//button[.="Accept"]')
    btn_reject_the_request = s('//button[.="Reject"]')
    btn_modal_accept_the_request = s('//button[.="Accept transfer"]')
    btn_modal_reject_the_request = s('//button[.="Reject transfer"]')
    # TODO(dp): Redesign elements using raw dropdown
    dropdown_modal_reject_reason = s("#reasonType")
    dropdown = s(".tippy-content")
    locale = s("#language-select")
    modal = s(".basic-modal__header")
    modal_meet_qiwa = s('//*[@data-component="Modal"]')
    button_close_modal = s('//*[@aria-label="Close modal"]')
    individual_table = Table(s(".table"))
    status = s('[role="status"]')
    see_all_services = s('//a[@href="/services"]')
    go_to_resume_management = s("//p[normalize-space()='Go to Resume Management']")
    services = s("//p[normalize-space()='Services']")
    links = ss("[data-component='Menu'] a")
    lang_links = {
        Language.EN: links.first,
        Language.AR: links.second,
    }

    add_resume_section_btn = s("//button[p[text()='Add resume section']]")
    volunteer_experience_btn = s("//p[contains(text(), 'Volunteer experience')]")
    organization_name = s("#organizationName")
    event_name = s("#volunteerEventName")
    volunteering_start_date = s("#startDate")
    value_start_date = s("//p[@class='Text-ds__sc-lk593a-0 jKDmWU'][normalize-space()='1']")
    volunteering_end_date = s("#endDate")
    value_end_date = s("//p[@class='Text-ds__sc-lk593a-0 jKDmWU'][normalize-space()='8']")
    add_volunteer_experience_btn = s("//button[@type='submit']")
    edit_volunteer_exp_btn = s("//*[@id='volunteer-works']//p[contains(., 'Edit')]")
    edit_volunteer_exp_btn2 = s("a[class='Button__Wrapper-ds__sc-6fc6di-0 gTsTky']")
    delete_volunteer_exp_btn = s(".Button__Wrapper-ds__sc-6fc6di-0.lcPyRu")
    confirm_delete_experience_btn = s("//p[contains(.,'Delete experience')]")
    about_section_btn = s("//p[contains(text(), 'About')]")

    summary = s("#summary")
    submit_btn = s("button[type='submit']")
    edit_summary_btn = s("//section[@id='about']//p[text()='Edit']")
    delete_summary_btn = s("//button[p[text()='Delete summary']]")
    confirm_delete_summary_btn = s("//p[text()='Yes, delete summary']")

    training_section_btn = s("//p[contains(text(), 'Trainings')]")
    training_name = s("#courseName")
    training_provider = s("#courseProvider")
    edit_trainings_btn = s("//section[@id='trainings']//p[text()='Edit']")
    edit_record_btn = s("//p[text()='Edit']")
    delete_record_btn = s("//button[p[text()='Delete']]")
    confirm_delete_trainings = s("//p[text()='Delete training']")
    trainings_section = s("#trainings")
    training_list_name = s("//section[@id='trainings']//h4[text()]")
    ms_end_date = s('(//section[@id="experiences"]//p[@class="Text-ds__sc-lk593a-0 gggtgX"])[5]')
    ms_end_date2 = s('(//section[@id="experiences"]//p[@class="Text-ds__sc-lk593a-0 gggtgX"])[1]')

    share_resume_btn = s("//p[text()='Share resume']")
    enter_link_name = s("#linkName")
    expiration_date = s("#expiryDate")
    value_expiration_date = s("div.CalendarCell__Cell-ds__sc-1awceb6-0.cPVzib")
    agreement_checkbox = s('//label[@class="Checkbox__StyledLabel-ds__sc-t2he6b-2 hNRoEh"]')
    link_status = s("p[class='Text-ds__sc-lk593a-0 gXgHhG']")
    stay_in_resume_sharing_btn = s("//button[p[text()='Stay in resume sharing']]")
    save_changes = s("//button[@form='edit-shared-link-form']")
    confirm_delete_link = s("//button[p[text()='Delete link']]")
    change_link_name = s("//form[@id='edit-shared-link-form']//input[@id='linkName']")
    share_links_tab = s("//p[text()='Shared links']")
    visibility_toggle = ss("[data-component='Switch'] input")
    copy_link_btn = ss("[data-component='Button'] ").second
    experiences_section = s("#experiences")
    unavailable_resume = s("//p[contains(text(),'Unfortunately, we could not connect')]")
    toggle = ss("[data-component='Switch']")
    total_views = s("//p[normalize-space()='Total views']")
    unique_viewers = s("//p[normalize-space()='Unique viewers']")
    total_time_spent = s("//p[normalize-space()='Total time spent']")
    average_time = s("//p[normalize-space()='Average time']")
    close_modal_window = s("button[aria-label='Close modal']")

    def navigate_to_services(self) -> IndividualPage:
        self.services.click()
        return self

    @allure.step("Close Meet Qiwa 2.0 modal")
    def close_meet_qiwa_modal(self):
        if self.modal_meet_qiwa.wait_until(be.visible):
            self.button_close_modal.click()

    @allure.step("Wait Individual page to load")
    def wait_page_to_load(self) -> IndividualPage:
        self.close_meet_qiwa_modal()
        self.service_card.first.should(be.visible)
        return self

    @allure.step("Click on See all services")
    def click_see_all_services(self) -> IndividualPage:
        self.see_all_services.click()
        self.service_card.first.should(be.visible)
        return self

    def select_service(self, text: str) -> IndividualPage:
        self.service_card.element_by(have.text(text)).click()
        return self

    def click_agree_checkbox(self) -> IndividualPage:
        self.checkbox_agree.press(Keys.SPACE)
        return self

    def click_btn_accept_the_request(self) -> IndividualPage:
        self.btn_accept_the_request.click()
        return self

    def click_btn_reject_the_request(self) -> IndividualPage:
        self.btn_reject_the_request.click()
        return self

    def click_btn_modal_accept_the_request(self) -> IndividualPage:
        self.btn_modal_accept_the_request.click()
        return self

    def click_btn_modal_reject_the_request(self) -> IndividualPage:
        self.btn_modal_reject_the_request.click()
        return self

    def verify_expected_status(self, text: str) -> IndividualPage:
        # TODO(dp): Remove this sleep after fixing an issue with the shown section
        time.sleep(10)
        browser.driver.refresh()
        self.status.should(have.exact_text(text))
        return self

    def select_rejection_reason(self, reason: str) -> IndividualPage:
        self.dropdown_modal_reject_reason.click()
        self.dropdown.all('[role="option"]').element_by(have.text(reason)).click()
        return self

    def wait_until_popup_disappears(self) -> IndividualPage:
        self.modal.wait_until(be.not_.visible)
        return self

    def navigate_to_resume_management(self) -> IndividualPage:
        self.go_to_resume_management.click()
        return self

    def add_resume_section(self):
        self.add_resume_section_btn.click()
        return self

    def navigate_to_volunteer_section(self):
        self.volunteer_experience_btn.click()
        return self

    def fill_volunteer_details(self) -> IndividualPage:
        self.organization_name.type("QA TEST2" + str(datetime.date.today()))
        self.event_name.type("QA TEST")
        self.volunteering_start_date.click()
        self.value_start_date.click()
        self.volunteering_end_date.click()
        self.value_end_date.click()
        self.add_volunteer_experience()
        return self

    def add_volunteer_experience(self) -> IndividualPage:
        self.add_volunteer_experience_btn.click()
        return self

    def navigate_to_edit_volunteer_exp(self) -> IndividualPage:
        browser.driver.refresh()
        self.edit_volunteer_exp_btn.click()
        self.edit_volunteer_exp_btn2.click()
        return self

    def edit_field_volunteer_details(self) -> IndividualPage:
        self.organization_name.set_value("QA TEST 1")
        self.event_name.set_value("QA TEST 1")
        self.add_volunteer_experience()
        return self

    def delete_volunteer_exp(self) -> IndividualPage:
        browser.driver.refresh()
        self.edit_volunteer_exp_btn.hover().click()
        self.delete_volunteer_exp_btn.click()
        self.confirm_delete_experience_btn.click()
        return self

    def click_on_about_section(self) -> IndividualPage:
        self.about_section_btn.click()
        return self

    def add_summary(self) -> IndividualPage:
        self.summary.type("TEST QA")
        self.submit_btn.click()
        return self

    def delete_about_summary(self) -> IndividualPage:
        self.edit_summary_btn.click()
        self.delete_summary_btn.click()
        self.confirm_delete_summary_btn.click()
        return self

    def click_on_trainings_section(self) -> IndividualPage:
        self.training_section_btn.click()
        return self

    def add_trainings_record(self) -> IndividualPage:
        self.training_name.type("TEST QA NAME")
        self.training_provider.type("TEST QA PROVIDER")
        self.volunteering_start_date.click()
        self.value_start_date.click()
        self.volunteering_end_date.click()
        self.value_end_date.click()
        self.submit_btn.click()
        self.trainings_section.should(be.visible)
        browser.driver.refresh()
        return self

    def edit_training_record(self) -> IndividualPage:
        self.edit_trainings_btn.click()
        browser.driver.refresh()
        self.edit_record_btn.click()
        self.training_name.set_value("QA TEST CHANGED")
        self.submit_btn.click()
        self.training_list_name.should(have.exact_text("QA TEST CHANGED"))
        return self

    def delete_training_record(self) -> IndividualPage:
        browser.driver.refresh()
        self.edit_trainings_btn.click()
        browser.driver.refresh()
        self.delete_record_btn.click()
        self.confirm_delete_trainings.click()
        return self

    def verify_expired_date(self, end_date) -> str:
        expired_date = self.ms_end_date2.get(query.text).split(" - ")[1]
        assert expired_date == end_date
        return expired_date

    def click_on_share_resume_btn(self) -> IndividualPage:
        self.share_resume_btn.click()
        return self

    def create_new_link(self) -> IndividualPage:
        self.enter_link_name.type("TEST QA LINK")
        self.expiration_date.click()
        self.value_expiration_date.click()
        self.agreement_checkbox.click()
        self.submit_btn.click()
        self.link_status.should(have.exact_text("New link created"))
        self.stay_in_resume_sharing_btn.click()
        return self

    def create_second_link(self) -> IndividualPage:
        self.enter_link_name.type("TEST QA LINK")
        self.expiration_date.click()
        self.value_expiration_date.click()
        self.agreement_checkbox.click()
        self.submit_btn.click()
        return self

    def edit_link(self) -> IndividualPage:
        self.edit_record_btn.click()
        self.change_link_name.set("QA12")
        self.save_changes.click()
        return self

    def delete_link(self) -> IndividualPage:
        self.delete_record_btn.click()
        self.confirm_delete_link.click()
        return self

    def verify_second_added_link_status(self) -> IndividualPage:
        self.visibility_toggle.first.should(have.attribute("aria-checked", "true"))
        return self

    def navigate_to_shared_links_tab(self) -> IndividualPage:
        self.share_links_tab.click()
        return self

    def copy_link(self) -> IndividualPage:
        self.copy_link_btn.click()
        return self

    def open_link_in_new_tab(self) -> IndividualPage:
        clipboard_url = str(pyperclip.paste())
        browser.driver.get(clipboard_url)
        return self

    def verify_resume_availability(self) -> IndividualPage:
        self.experiences_section.should(be.visible)
        return self

    def verify_resume_unavailability(self) -> IndividualPage:
        self.unavailable_resume.should(be.visible)
        return self

    def disable_link_visibility(self) -> IndividualPage:
        self.navigate_to_shared_links_tab()
        self.toggle.first.click()
        self.visibility_toggle.first.should(have.attribute("aria-checked", "false"))
        return self

    def close_modal(self) -> IndividualPage:
        self.close_modal_window.click()
        return self

    def verify_profile_analytics(self) -> IndividualPage:
        self.total_views.should(be.visible)
        self.unique_viewers.should(be.visible)
        self.total_time_spent.should(be.visible)
        self.average_time.should(be.visible)
        return self

    def verify_changed_profile_analytics(self, new_total_views) -> IndividualPage:
        browser.driver.back()
        browser.driver.refresh()
        self.total_views.should(have.no.exact_text(new_total_views))
        return self

    def get_total_views(self) -> str:
        total_views = self.total_views.get(query.text)
        return total_views
