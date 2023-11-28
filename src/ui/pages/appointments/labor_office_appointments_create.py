from __future__ import annotations

import time

import allure
from selene import be, have
from selene.support.shared.jquery_style import s, ss

from src.ui.components.raw.dropdown import Dropdown


class LaborOfficeAppointmentsCreatePage:
    search = s("#establishment-list")
    establishment_list = ss("[data-component='RadioButton'] span")
    next_btn = s("[type='submit']")
    dropdown = ss("[class='tippy-content'] li")
    sub_service = s("#subService")
    sub_service_error = s("#subService-error")
    date_picker = s('//*[@id="date"]')
    available_dates = ss('//*[@role="button" and not(@aria-disabled)]')
    appointment_reason_section = s("#reason")
    radio_button_appointment_reason = '//*[@data-component="RadioButton"]'
    in_person_appointment = s('//fieldset//label[4]//p[@id="1-label"]')

    block_new_request_virtual = s('//*[@id="reason"]//label[1]')
    block_follow_up = s('//*[@id="reason"]//label[2]')
    block_inquiry = s('//*[@id="reason"]//label[3]')
    block_request_new_service_in_person = s('//*[@id="reason"]//label[4]')

    edit_creators_info_btn = s('//*[@id="establishment"]//button')
    edit_reason_btn = s('//*[@id="reason"]//button')
    edit_service_btn = s('//*[@id="service"]//button')
    edit_details_btn = s('//*[@id="details"]//button')
    summary_block = s('//*[@id="summary"]/div')
    summary_reason = s('//*[@id="summary"]/div/div[2]/div[1]/div[2]/div[1]')
    summary_office = s('//*[@id="summary"]/div/div[2]/div[1]/div[2]/div[2]')
    summary_date = s('//*[@id="summary"]/div/div[2]/div[1]/div[2]/div[3]')
    summary_time = s('//*[@id="summary"]/div/div[2]/div[1]/div[2]/div[4]')
    summary_type = s('//*[@id="summary"]/div/div[2]/div[1]/div[2]/div[5]')

    # dropdowns
    dropdown_element_locator = '//*[@role="option"]'
    dropdown_select_service = Dropdown(
        s('(//div[@id="service"]//*[@data-component="Select"]//div)[1]'), dropdown_element_locator
    )
    dropdown_select_region = Dropdown(
        s('(//div[@id="details"]//*[@data-component="Select"])[1]'), dropdown_element_locator
    )
    dropdown_select_office = Dropdown(
        s('(//div[@id="details"]//*[@data-component="Select"])[2]'), dropdown_element_locator
    )
    dropdown_select_time = Dropdown(
        s('(//div[@id="details"]//*[@data-component="Select"])[3]'), dropdown_element_locator
    )
    dropdown_select_year = Dropdown(
        s('(//div[@data-component="DatePicker"]//div[contains(@class, "Select")])[2]'),
        dropdown_element_locator,
    )

    error_message = s('//*[@data-component="ErrorMessage"]')

    # inputs
    input_service = s('//input[@id="service"]')
    input_region = s('//input[@id="region"]')
    input_office = s('//input[@id="office"]')
    input_time = s('//input[@name="time"]')

    @allure.step("Select establishment {name}")
    def select_establishment(self, name: str) -> LaborOfficeAppointmentsCreatePage:
        self.search.type(name)
        self.establishment_list.first.click()
        self.next_btn.click()
        return self

    @allure.step("Verify establishment search is visible")
    def verify_select_establishment_visible(self) -> LaborOfficeAppointmentsCreatePage:
        self.search.should(be.visible)
        return self

    @allure.step("Verify next button is visible")
    def verify_next_btn_visible(self) -> LaborOfficeAppointmentsCreatePage:
        self.next_btn.should(be.visible)
        return self

    @allure.step("Verify blocks in Appointment reason page")
    def verify_appointment_reason_blocks_visible(self) -> LaborOfficeAppointmentsCreatePage:
        self.block_new_request_virtual.should(be.visible)
        self.block_follow_up.should(be.visible)
        self.block_inquiry.should(be.visible)
        self.block_request_new_service_in_person.should(be.visible)
        return self

    @allure.step("Verify blocks in service and subservice page")
    def verify_service_and_subservice_blocks_visible(self) -> LaborOfficeAppointmentsCreatePage:
        self.input_service.should(be.visible)
        self.sub_service.should(be.visible)
        return self

    @allure.step("Verify blocks in Appointment details page")
    def verify_appointment_details_blocks_visible(self) -> LaborOfficeAppointmentsCreatePage:
        self.input_region.should(be.visible)
        self.input_office.should(be.visible)
        self.date_picker.should(be.visible)
        return self

    @allure.step("Verify blocks in summary page")
    def verify_summary_blocks_visible(self) -> LaborOfficeAppointmentsCreatePage:
        self.summary_block.should(be.visible)
        self.summary_reason.should(be.visible)
        self.summary_office.should(be.visible)
        self.summary_date.should(be.visible)
        self.summary_time.should(be.visible)
        self.summary_type.should(be.visible)
        return self

    @allure.step("Select appointment reason {value}")
    def select_appointment_reason(self, value) -> LaborOfficeAppointmentsCreatePage:
        if self.appointment_reason_section.wait_until(be.visible):
            ss(self.radio_button_appointment_reason)[value.value].click()
            self.next_btn.click()
        return self

    @allure.step("Select service {name}")
    def select_service(self, name: str) -> LaborOfficeAppointmentsCreatePage:
        self.input_service.wait_until(be.visible)
        self.input_service.click()
        self.input_service.set(name)
        self.dropdown[0].click()
        return self

    @allure.step("Select sub service {name}")
    def select_sub_service(self, name: str) -> LaborOfficeAppointmentsCreatePage:
        self.sub_service.click()
        self.dropdown.element_by(have.exact_text(name)).click()
        return self

    def check_sub_service_error(self, text: str) -> LaborOfficeAppointmentsCreatePage:
        self.sub_service_error.should(have.exact_text(text))
        return self

    @allure.step("Click on next step button")
    def click_next_step_button(self) -> LaborOfficeAppointmentsCreatePage:
        self.next_btn.should(be.visible).click()
        return self

    @allure.step("Select region")
    def select_region(self, name) -> LaborOfficeAppointmentsCreatePage:
        self.input_region.wait_until(be.visible)
        time.sleep(0.5)  # todo: investigate to remove this sleep
        self.input_region.double_click()  # todo: investigate why one click does not work
        self.dropdown_select_region.select_by_text(name)
        return self

    @allure.step("Select office")
    def select_office(self, name) -> LaborOfficeAppointmentsCreatePage:
        self.input_office.wait_until(be.enabled)
        time.sleep(0.5)  # todo: investigate to remove this sleep
        self.input_office.double_click()  # todo: investigate why one click does not work
        self.dropdown_select_office.select_by_text(name)
        return self

    @allure.step("Select date")
    def select_date(
        self, first_available=True, next_year=True
    ) -> LaborOfficeAppointmentsCreatePage:
        self.date_picker.wait_until(be.clickable)
        self.date_picker.click()
        if next_year:
            self.dropdown_select_year.select_by_index(1)
        if first_available:
            self.available_dates[0].click()

        return self

    @allure.step("Select time")
    def select_time(self, first_available=True) -> LaborOfficeAppointmentsCreatePage:
        self.input_time.wait_until(be.enabled)
        self.input_time.double_click()  # investigate why one click does not work
        if first_available:
            self.dropdown_select_time.select_by_index(0)

        return self

    @allure.step("Get list of available services")
    def get_service_list(self):
        pass

    @allure.step("Verify Service list is not empty")
    def should_service_list_be(self):
        assert len(self.dropdown_select_service.options) > 0, "Service list is empty"

    @allure.step("Verify validation message on create additional appointment")
    def should_validation_additional_appointment_be(self):
        self.error_message.should(have.text("You've already booked an appointment"))

    @allure.step("Create appointment flow in create appointment page")
    def book_appointment_flow(
        self, appointment_reason, service, sub_service, region, office, establishment=None
    ):
        if establishment:
            self.select_establishment(establishment)
        self.select_appointment_reason(appointment_reason)
        self.select_service(service)
        self.select_sub_service(sub_service)
        self.click_next_step_button()
        self.select_region(region)
        self.select_office(office)
        self.select_date()
        self.select_time()
        self.click_next_step_button()
        self.click_next_step_button()

    @allure.step
    def select_establishment_by_seq_number(self, labor_office_id: str, sequence_number: str):
        s(f"//div[@for='{labor_office_id}-{sequence_number}']").click()
        return self

    @allure.step
    def select_in_person_appointments(self):
        self.in_person_appointment.click()
        return self
