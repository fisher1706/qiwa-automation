from __future__ import annotations

import allure
from selene import be
from selene.support.shared.jquery_style import s

from data.constants import Language
from src.ui.pages.appointments.labor_office_appointments_create import (
    LaborOfficeAppointmentsCreatePage,
)


class LaborOfficeAppointmentsEditPage:
    language = Language.EN
    requesters_information_table_title_text = s(
        '//*[@id="establishment"]/div//*[contains(text(), "Requester’s information")]'
    )
    requesters_information_table_est_name_text = s(
        '//*[@id="establishment"]/div//*[contains(text(), "Establishment Name")]'
    )
    requesters_information_table_est_name_value = s(
        '//*[@id="establishment"]/div//*[contains(text(), "شركة التصنيف الدولية للمقاولات")]'
    )
    requesters_information_table_est_id_text = s(
        '//*[@id="establishment"]/div//*[contains(text(), "Establishment ID")]'
    )
    requesters_information_table_est_id_value = s(
        '//*[@id="establishment"]/div/div[2]/div/div[2]/div[2]/p'
    )

    appointment_reason_table_title_text = s(
        '//*[@id="reason"]//*[contains(text(), "Appointment reason")]'
    )
    appointment_reason_table_reason_text = s('//*[@id="reason"]//*[contains(text(), "Reason")]')
    appointment_reason_table_reason_value = s(
        '//*[@id="reason"]//*[contains(text(), "Request new service - in person")]'
    )
    appointment_reason_table_type_text = s('//*[@id="reason"]//*[contains(text(), "Type")]')
    appointment_reason_table_type_value = s('//*[@id="reason"]//*[contains(text(), "In-person")]')

    appointment_service_table_title_text = s(
        '//*[@id="service"]//*[contains(text(), "Service and subservice")]'
    )
    appointment_service_table_service_name_text = s(
        '//*[@id="service"]//*[contains(text(), "Service name")]'
    )
    appointment_service_table_service_name_value = s(
        '//*[@id="service"]//*[contains(text(), "Work Permits")]'
    )
    appointment_service_table_sub_service_name_text = s(
        '//*[@id="service"]//*[contains(text(), "Subservice name")]'
    )
    appointment_service_table_sub_service_name_value = s(
        '//*[@id="service"]//*[contains(text(), "Renew Work Permits")]'
    )

    appointment_details_table_title_text = s(
        '//*[@id="details"]//*[contains(text(), "Appointment details")]'
    )
    appointment_details_table_region_btn_madinah = s('//*[@value="Madinah"]')
    appointment_details_table_office_btn_test = s('//*[@value="Test office 125"]')
    appointment_details_table_date_btn = s('//*[@id="date"]')
    appointment_details_table_time_btn = s('//*[@id="time"]')

    next_step_btn = s('//*[@id="details"]/div/div[2]/button')

    need_more_information_block = s('//*[@id="root"]/span/div[1]/div/div/div[2]/div[2]')
    need_more_information_block_sbs_btn = s(
        '//*[@data-component="Button"]//*[contains(text(), "Step-by-step guide")]'
    )

    knowledge_center_logo_text = s('//*[@id="root"]/div[3]/div[1]/div/div/div/div[1]')

    summary_table_title_text = s('//*[@id="summary"]/div//*[contains(text(), "Summary")]')
    summary_table_reason_text = s(
        '//*[@id="summary"]/div//*[contains(text(), "Appointment reason")]'
    )
    summary_table_reason_value = s(
        '//*[@id="summary"]/div//*[contains(text(), "Request new service - in person")]'
    )
    summary_table_office_text = s('//*[@id="summary"]/div//*[contains(text(), "Office")]')
    summary_table_office_value = '//*[@id="summary"]/div//*[contains(text(), "{office_name}")]'
    summary_table_date_text = s('//*[@id="summary"]/div//*[contains(text(), "Date")]')
    summary_table_date_value = s('//*[@id="summary"]/div/div[2]/div[1]/div[2]/div[3]/div[2]/p')
    summary_table_time_text = s('//*[@id="summary"]/div//*[contains(text(), "Time")]')
    summary_table_time_value = s('//*[@id="summary"]/div/div[2]/div[1]/div[2]/div[4]/div[2]/p')
    summary_table_type_text = s('//*[@id="summary"]/div//*[contains(text(), "Type")]')
    summary_table_type_value = '//*[@id="summary"]/div//*[contains(text(), "{type_value}")]'

    book_app_btn = s('//*[@id="summary"]/div/div[2]/div[2]/button')

    @allure.step("Verify edit page with typical state")
    def verify_edit_page_typical(self):
        self.requesters_information_table_title_text.wait_until(be.visible)
        self.requesters_information_table_est_name_text.wait_until(be.visible)
        self.requesters_information_table_est_name_value.wait_until(be.visible)
        self.requesters_information_table_est_id_text.wait_until(be.visible)
        self.requesters_information_table_est_id_value.wait_until(be.visible)

        self.appointment_reason_table_title_text.wait_until(be.visible)
        self.appointment_reason_table_reason_text.wait_until(be.visible)
        self.appointment_reason_table_reason_value.wait_until(be.visible)
        self.appointment_reason_table_type_text.wait_until(be.visible)
        self.appointment_reason_table_type_value.wait_until(be.visible)

        self.appointment_service_table_title_text.wait_until(be.visible)
        self.appointment_service_table_service_name_text.wait_until(be.visible)
        self.appointment_service_table_service_name_value.wait_until(be.visible)
        self.appointment_service_table_sub_service_name_text.wait_until(be.visible)
        self.appointment_service_table_sub_service_name_value.wait_until(be.visible)

        self.appointment_details_table_title_text.wait_until(be.visible)
        self.appointment_details_table_region_btn_madinah.wait_until(be.visible)
        self.appointment_details_table_office_btn_test.wait_until(be.visible)
        self.appointment_details_table_date_btn.wait_until(be.visible)
        self.appointment_details_table_time_btn.wait_until(be.visible)

        self.next_step_btn.wait_until(be.visible)

    @allure.step("Open knowledge center")
    @allure.step("Verify more info block and open knowledge center")
    def open_knowledge_center(self):
        self.need_more_information_block.should(be.visible)
        self.need_more_information_block_sbs_btn.click()

    @allure.step("Verifying knowledge center is loaded")
    def verify_knowledge_center_page_load(self):
        self.knowledge_center_logo_text.wait_until(be.visible)

    @allure.step("Changing details of app")
    def change_details_fields(self, region, office):
        labor_office_appointments_create_page = LaborOfficeAppointmentsCreatePage()
        labor_office_appointments_create_page.select_region(region)
        labor_office_appointments_create_page.select_office(office)
        labor_office_appointments_create_page.select_date()
        labor_office_appointments_create_page.select_time()

    @allure.step("Next step button click")
    def next_step_btn_click(self):
        self.next_step_btn.click()

    @allure.step("Verifying summary table")
    def verify_summary_table(self, office_name: str, type_value: str):
        self.summary_table_title_text.should(be.visible)
        self.summary_table_reason_text.should(be.visible)
        self.summary_table_reason_value.should(be.visible)
        self.summary_table_office_text.should(be.visible)
        s(self.summary_table_office_value.format(office_name=office_name)).should(be.visible)
        self.summary_table_date_text.should(be.visible)
        self.summary_table_date_value.should(be.visible)
        self.summary_table_time_text.should(be.visible)
        self.summary_table_time_value.should(be.visible)
        self.summary_table_type_text.should(be.visible)
        s(self.summary_table_type_value.format(type_value=type_value)).should(be.visible)

    @allure.step("Clicking on book app button")
    def book_app_btn_click(self):
        self.book_app_btn.click()
