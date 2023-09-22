from __future__ import annotations

import allure
from selene import be, browser
from selene.support.shared.jquery_style import s

import config


class LaborOfficeAppointmentsPage:
    book_appointment_btn = s("[data-component='Breadcrumbs'] + div p")
    appointments = s("//p[text()='Labor Office Appointments']")
    upcoming_appointment_row = s('//*[@id="upcoming"]//tr')
    upcoming_appointments_actions = upcoming_appointment_row.element(
        '//*[@data-component="Actions"]'
    )
    success_book_message = s('//*[contains(text(), "You’ve successfully booked an appointment")]')
    confirmation_service_name = '(//tr)[1]//p[contains(text(), "{}")]'
    confirmation_sub_service_name = '(//tr)[2]//p[contains(text(), "{}")]'
    confirmation_office_name = '(//tr)[3]//p[contains(text(), "{}")]'
    button_book_appointment = s('//*[@href="/create"]')
    button_next_step = s('//button[@type="submit"]')
    button_action_cancel_upcoming_appointment = s('//*[@data-component="ActionsMenu"]//button')
    button_cancel_upcoming_appointment_confirmation = s(
        '(//*[@data-component="ButtonGroup"]//button)[1]'
    )
    button_close_modal = s('//button[@aria-label="Close modal"]')
    button_back_to_appointments = s("(//button)[1]")
    button_print = s("(//button)[2]")

    def navigate_to_labor_office_appointments_page(self) -> LaborOfficeAppointmentsPage:
        browser.open(config.qiwa_urls.appointment_booking)
        return self

    @allure.step("Wait Appointments page to load")
    def wait_page_to_load(self) -> LaborOfficeAppointmentsPage:
        self.appointments.wait_until(be.visible)
        return self

    @allure.step("Click on book appointment button")
    def click_book_appointment_btn(self) -> LaborOfficeAppointmentsPage:
        self.book_appointment_btn.click()
        return self

    @allure.step("Cancel active appointment if exists")
    def cancel_active_appointment(self) -> LaborOfficeAppointmentsPage:
        if self.upcoming_appointment_row.matching(be.visible):
            self.upcoming_appointments_actions.click()
            self.button_action_cancel_upcoming_appointment.click()
            self.button_cancel_upcoming_appointment_confirmation.click()
            self.button_close_modal.click()

        return self

    @allure.step("Verify active appointment displayed")
    def should_active_appointment_be_visible(self):
        self.upcoming_appointment_row.should(be.visible)
