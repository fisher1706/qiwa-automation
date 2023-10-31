from __future__ import annotations

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
    in_person_appointment = s('//div[p="Request new service-in person"]')

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

    @allure.step("Select appointment reason {value}")
    def select_appointment_reason(self, value) -> LaborOfficeAppointmentsCreatePage:
        if self.appointment_reason_section.wait_until(be.visible):
            ss(self.radio_button_appointment_reason)[value.value].click()
            self.next_btn.click()
        return self

    @allure.step("Select service {name}")
    def select_service(self, name: str) -> LaborOfficeAppointmentsCreatePage:
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
        self.input_region.double_click()  # investigate why one click does not work
        self.dropdown_select_region.select_by_text(name)
        return self

    @allure.step("Select office")
    def select_office(self, name) -> LaborOfficeAppointmentsCreatePage:
        self.input_office.wait_until(be.enabled)
        self.input_office.double_click()  # investigate why one click does not work
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

    def select_establishment_by_seq_number(self, labor_office_id: str, sequence_number: str):
        s(f"//div[@for='{labor_office_id}-{sequence_number}']").should(be.visible).click()
        return self

    def select_in_person_appointments(self):
        self.in_person_appointment.should(be.visible).click()
        return self
