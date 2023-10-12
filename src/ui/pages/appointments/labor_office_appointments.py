from __future__ import annotations

import time

import allure
from selene import be, browser, have
from selene.support.shared.jquery_style import s

from src.ui.components.raw.dropdown import Dropdown
from src.ui.components.raw.table import Table
from src.ui.pages.appointments.labor_office_appointments_create import (
    LaborOfficeAppointmentsCreatePage,
)
from utils.assertion import assert_that


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
    button_action_view_upcoming_appointment = s('//*[@data-component="ActionsMenu"]//a[1]')
    button_action_cancel_upcoming_appointment = s('//*[@data-component="ActionsMenu"]//button')
    button_cancel_upcoming_appointment_confirmation = s(
        '(//*[@data-component="ButtonGroup"]//button)[1]'
    )
    button_close_modal = s('//button[@aria-label="Close modal"]')
    button_back_to_appointments = s("(//button)[1]")
    button_print = s("(//button)[2]")
    button_upcoming_appointments = s('(//button[contains(@class, "Navigation")])[1]')
    button_appointments_history = s('(//button[contains(@class, "Navigation")])[2]')
    button_clear_search_history = s('//button[@aria-label="Delete"]')
    button_knowledge_center = s('//*[contains(text(), "Go to Knowledge Center")]//ancestor::a')
    section_upcoming_appointments = s("#upcoming")
    section_appointments_history = s("#archieved")

    input_search = s('//*[@id="test"]')
    dropdown_status = Dropdown(
        s('//div[contains(@class, "Select")]'),
        LaborOfficeAppointmentsCreatePage.dropdown_element_locator,
    )

    table_loader = s('//tr[@data-testid="req-loader"]')
    table_history = Table(section_appointments_history)
    locator_search_no_results = '//*[contains(text(), "No data was found")]'

    by_appointments_history_search_no_results = '//*[contains(text(), "No data was found")]'

    view_appointment_details_from_history_last = s(
        "//*[@id='archieved']/div/div[2]/div/table/tbody/tr[1]/td[8]/a"
    )

    @allure.step("Wait Appointments page to load")
    def wait_page_to_load(self) -> LaborOfficeAppointmentsPage:
        self.appointments.wait_until(be.visible)
        return self

    @allure.step("Click on book appointment button")
    def click_book_appointment_btn(self) -> LaborOfficeAppointmentsPage:
        self.book_appointment_btn.click()
        return self

    @allure.step("Clear appointments history search field")
    def click_clear_search(self):
        self.button_clear_search_history.click()
        return self

    @allure.step("Cancel active appointment if exists")
    def cancel_active_appointment(self) -> LaborOfficeAppointmentsPage:
        # todo: investigate possibility to remove this sleep
        time.sleep(1)
        if self.upcoming_appointment_row.matching(be.visible):
            self.upcoming_appointments_actions.click()
            self.button_action_cancel_upcoming_appointment.click()
            self.button_cancel_upcoming_appointment_confirmation.click()
            self.button_close_modal.click()

        return self

    @allure.step("View active appointment")
    def view_active_appointment(self) -> LaborOfficeAppointmentsPage:
        # todo: investigate possibility to remove this sleep
        time.sleep(1)
        if self.upcoming_appointment_row.matching(be.visible):
            self.upcoming_appointments_actions.click()
            self.button_action_view_upcoming_appointment.click()

        return self

    @allure.step("View appointment from history")
    def view_appointment_from_history_last(self) -> LaborOfficeAppointmentsPage:
        # todo: investigate possibility to remove this sleep
        time.sleep(1)
        self.view_appointment_details_from_history_last.click()

        return self

    @allure.step("Navigate to appointments history section")
    def navigate_to_appointments_history(self):
        self.button_appointments_history.click()
        return self

    @allure.step("Navigate to Knowledge Center")
    def navigate_to_knowledge_center(self):
        self.button_knowledge_center.click()
        return self

    @allure.step("Search appointment by: {value}")
    def search_appointments(self, value):
        self.input_search.type(value)
        self.table_history.body.wait_until(be.visible)
        return self

    @allure.step("Filter appointments history by status: {status}")
    def filter_appointments_history_by_status(self, status):
        self.dropdown_status.select_by_index(status.value)
        self.table_loader.wait_until(be.not_.visible)
        return self

    @allure.step("Verify appointments history table have correct titles")
    def should_history_table_headers_have_correct_titles(self):
        for row, header in zip(
            self.table_history.headers,
            ["Date", "Reference number", "Time", "Office", "Type", "Status", "Actions"],
        ):
            row.should(have.text(header))
        return self

    @allure.step("Verify search")
    def should_history_search_results_have(self, by_index, value):
        time.sleep(1.5)  # todo: investigate possibility to remove this sleep
        for i, _ in enumerate(self.table_history.rows, start=1):
            self.table_history.cell(row=i, column=by_index).should(have.text(value))
        return self

    @allure.step("Verify search results are empty")
    def should_history_search_results_be_empty(self):
        s(self.locator_search_no_results).should(be.visible)
        return self

    @allure.step("Verify active appointment is visible")
    def should_active_appointment_be_visible(self):
        self.upcoming_appointment_row.should(be.visible)
        return self

    @allure.step("Verify appointments history search field is visible")
    def should_search_history_be_visible(self):
        self.input_search.should(be.visible)
        return self

    @allure.step("Verify upcoming appointments section is visible")
    def should_upcoming_appointments_section_be_visible(self):
        self.section_upcoming_appointments.should(be.visible)
        return self

    @allure.step("Verify appointments history section is visible")
    def should_appointments_history_section_be_visible(self):
        self.section_appointments_history.should(be.visible)
        return self

    @allure.step("Verify status filter for appointments history is visible")
    def should_status_filter_be_visible(self):
        self.dropdown_status.element.should(be.visible)
        return self

    @allure.step("Verify new page with knowledge center page opened in the new tab")
    def should_new_tab_knowledge_center_be_opened(self):
        browser.switch_to_next_tab()
        assert_that(browser.driver.current_url.startswith("https://knowledge-center.qiwa.info/"))
        return self
