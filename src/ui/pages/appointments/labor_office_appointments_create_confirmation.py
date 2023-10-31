from __future__ import annotations

import allure
from selene import be, have
from selene.support.shared.jquery_style import s

from src.ui.pages.appointments.labor_office_appointments import (
    LaborOfficeAppointmentsPage,
)


class LaborOfficeCreateConfirmationPage:
    success_book_message = s('//*[@id="root"]/span/div[1]/div/div/div/span/div/div[2]')
    confirmation_service_name = '(//tr)[2]//p[contains(text(), "{}")]'
    confirmation_sub_service_name = '(//tr)[3]//p[contains(text(), "{}")]'
    confirmation_office_name = '(//tr)[4]//p[contains(text(), "{}")]'
    sub_service_error = s("#subService-error")

    # buttons
    button_back_to_appointments = s("(//button)[1]")
    button_print = s("(//button)[2]")

    @allure.step("Verify success book appointment message")
    def should_success_book_message_be_visible(self) -> LaborOfficeCreateConfirmationPage:
        self.success_book_message.should(be.visible)
        return self

    @allure.step("Verify print button should be visible")
    def should_print_button_be_visible(self) -> LaborOfficeCreateConfirmationPage:
        self.button_print.should(be.visible)
        return self

    @allure.step("Verify service name on confirmation booking page")
    def should_confirmation_service_name_be(
        self, service_name
    ) -> LaborOfficeCreateConfirmationPage:
        s(self.confirmation_service_name.format(service_name)).should(be.visible)
        return self

    @allure.step("Verify sub service name on confirmation booking page")
    def should_confirmation_sub_service_name_be(
        self, sub_service_name
    ) -> LaborOfficeCreateConfirmationPage:
        s(self.confirmation_sub_service_name.format(sub_service_name)).should(be.visible)
        return self

    @allure.step("Verify office name on confirmation booking page")
    def should_confirmation_office_name_be(self, office_name) -> LaborOfficeCreateConfirmationPage:
        s(self.confirmation_office_name.format(office_name)).should(be.visible)
        return self

    @allure.step("Click Back to appointments")
    def go_back_to_appointments_page(self) -> LaborOfficeAppointmentsPage:
        self.button_back_to_appointments.click()
        return LaborOfficeAppointmentsPage().wait_page_to_load()

    @allure.step("Check success page after booking flow")
    def check_booked_appointment(self, service: str, sub_service: str, office: str):
        self.should_success_book_message_be_visible()
        self.should_print_button_be_visible()
        self.should_confirmation_service_name_be(service)
        self.should_confirmation_sub_service_name_be(sub_service)
        self.should_confirmation_office_name_be(office)

    def validate_error_message(self, expected_error_msg: str) -> LaborOfficeCreateConfirmationPage:
        self.sub_service_error.should(be.visible).should(have.exact_text(expected_error_msg))
        return self
