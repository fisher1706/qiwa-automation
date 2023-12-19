from __future__ import annotations

import allure
from selene import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from data.constants import Language
from src.ui.pages.appointments.labor_office_appointments_create import (
    LaborOfficeAppointmentsCreatePage,
)


class LaborOfficeAppointmentsEditPage:
    language = Language.EN

    requesters_information_table_title_text = {
        Language.EN: s(
            '//*[@id="establishment"]/div//*[contains(text(), "Requester’s information")]'
        ),
        Language.AR: s('//*[@id="establishment"]/div//*[contains(text(), "معلومات مقدم الطلب")]'),
    }

    requesters_information_table_est_name_text = {
        Language.EN: s('//*[@id="establishment"]/div//*[contains(text(), "Establishment Name")]'),
        Language.AR: s('//*[@id="establishment"]/div//*[contains(text(), "اسم المنشأة")]'),
    }
    requesters_information_table_est_name_value = s(
        '//*[@id="establishment"]/div//*[contains(text(), "شركة التصنيف الدولية للمقاولات")]'
    )
    requesters_information_table_est_id_text = {
        Language.EN: s('//*[@id="establishment"]/div//*[contains(text(), "Establishment ID")]'),
        Language.AR: s('//*[@id="establishment"]/div//*[contains(text(), "رقم المنشأة")]'),
    }
    requesters_information_table_est_id_value = s(
        '//*[@id="establishment"]/div/div[2]/div/div[2]/div[2]/p'
    )

    appointment_reason_table_title_text = {
        Language.EN: s('//*[@id="reason"]//*[contains(text(), "Appointment reason")]'),
        Language.AR: s('//*[@id="reason"]//*[contains(text(), "سبب الزيارة")]'),
    }
    appointment_reason_table_reason_text = {
        Language.EN: s('//*[@id="reason"]//*[contains(text(), "Reason")]'),
        Language.AR: s('//*[@id="reason"]//*[contains(text(), "سبب الزيارة")]'),
    }
    appointment_reason_table_reason_value = '//*[@id="reason"]//*[contains(text(), "{reason}")]'
    appointment_reason_table_type_text = {
        Language.EN: s('//*[@id="reason"]//*[contains(text(), "Type")]'),
        Language.AR: s('//*[@id="reason"]//*[contains(text(), "النوع")]'),
    }
    appointment_reason_table_type_value = '//*[@id="reason"]//*[contains(text(), "{type}")]'

    appointment_service_table_title_text = {
        Language.EN: s('//*[@id="service"]//*[contains(text(), "Service and subservice")]'),
        Language.AR: s(
            '//*[@id="service"]//*[contains(text(), "الخدمة الأساسية والخدمة الفرعية")]'
        ),
    }
    appointment_service_table_service_name_text = {
        Language.EN: s('//*[@id="service"]//*[contains(text(), "Service name")]'),
        Language.AR: s('//*[@id="service"]//*[contains(text(), "اسم الخدمة")]'),
    }
    appointment_service_table_service_name_value = (
        '//*[@id="service"]//*[contains(text(), "{service}")]'
    )
    appointment_service_table_sub_service_name_text = {
        Language.EN: s('//*[@id="service"]//*[contains(text(), "Subservice name")]'),
        Language.AR: s('//*[@id="service"]//*[contains(text(), "الخدمة الفرعية")]'),
    }
    appointment_service_table_sub_service_name_value = (
        '//*[@id="service"]//*[contains(text(), "{sub_service}")]'
    )

    appointment_details_table_title_text = {
        Language.EN: s('//*[@id="details"]//*[contains(text(), "Appointment details")]'),
        Language.AR: s('//*[@id="details"]//*[contains(text(), "تفاصيل الموعد")]'),
    }
    appointment_details_table_region = '//*[@value="{region}"]'
    appointment_details_table_office = '//*[@value="{office}"]'
    appointment_details_table_date_btn = s('//*[@id="date"]')
    appointment_details_table_time_btn = s('//*[@name="time"]')

    next_step_btn = s('//*[@id="details"]//button[@type="submit"]')

    need_more_information_block = s('//*[@id="root"]/span/div[1]/div/div/div[2]/div[2]')

    need_more_information_block_sbs_btn = {
        Language.EN: s('//*[@data-component="Button"]//*[contains(text(), "Step-by-step guide")]'),
        Language.AR: s('//*[@data-component="Button"]//*[contains(text(), "الخطوات الإرشادية")]'),
    }

    knowledge_center_section = s('//div[@class="service-overview-hero-section"]')

    summary_table_title_text = {
        Language.EN: s('//*[@id="summary"]/div//*[contains(text(), "Summary")]'),
        Language.AR: s('//*[@id="summary"]/div//*[contains(text(), "الملخص")]'),
    }

    summary_table_reason_text = {
        Language.EN: s('//*[@id="summary"]/div//*[contains(text(), "Appointment reason")]'),
        Language.AR: s('//*[@id="summary"]/div//*[contains(text(), "سبب الموعد")]'),
    }

    summary_table_reason_value = {
        Language.EN: s(
            '//*[@id="summary"]/div//*[contains(text(), "Request new service - in person")]'
        ),
        Language.AR: s(
            '//*[@id="summary"]/div//*[contains(text(), "طلب خدمة جديدة - موعد حضوري")]'
        ),
    }

    summary_table_office_text = {
        Language.EN: s('//*[@id="summary"]/div//*[contains(text(), "Office")]'),
        Language.AR: s('//*[@id="summary"]/div//*[contains(text(), "المكتب")]'),
    }
    summary_table_office_value = '//*[@id="summary"]/div//*[contains(text(), "{office_name}")]'
    summary_table_date_text = {
        Language.EN: s('//*[@id="summary"]/div//*[contains(text(), "Date")]'),
        Language.AR: s('//*[@id="summary"]/div//*[contains(text(), "التاريخ")]'),
    }
    summary_table_date_value = s('//*[@id="summary"]/div/div[2]/div[1]/div[2]/div[3]/div[2]/p')
    summary_table_time_text = {
        Language.EN: s('//*[@id="summary"]/div//*[contains(text(), "Time")]'),
        Language.AR: s('//*[@id="summary"]/div//*[contains(text(), "الوقت")]'),
    }
    summary_table_time_value = s('//*[@id="summary"]/div/div[2]/div[1]/div[2]/div[4]/div[2]/p')
    summary_table_type_text = {
        Language.EN: s('//*[@id="summary"]/div//*[contains(text(), "Type")]'),
        Language.AR: s('//*[@id="summary"]/div//*[contains(text(), "النوع")]'),
    }
    summary_table_type_value = '//*[@id="summary"]/div//*[contains(text(), "{type_value}")]'

    book_app_btn = s('//*[@id="summary"]//button[@type="submit"]')

    @allure.step("Verify edit page with typical state")
    def verify_edit_page_typical(
        self,
        appointment_reason: str,
        appointment_type: str,
        service: str,
        sub_service: str,
        region: str,
        office: str,
    ):
        self.requesters_information_table_title_text[self.language].should(be.visible)
        self.requesters_information_table_est_name_text[self.language].should(be.visible)
        self.requesters_information_table_est_name_value.should(be.visible)
        self.requesters_information_table_est_id_text[self.language].should(be.visible)
        self.requesters_information_table_est_id_value.should(be.visible)

        self.appointment_reason_table_title_text[self.language].should(be.visible)
        self.appointment_reason_table_reason_text[self.language].should(be.visible)
        s(self.appointment_reason_table_reason_value.format(reason=appointment_reason)).should(
            be.visible
        )
        self.appointment_reason_table_type_text[self.language].should(be.visible)
        s(self.appointment_reason_table_type_value.format(type=appointment_type)).should(
            be.visible
        )

        self.appointment_service_table_title_text[self.language].should(be.visible)
        self.appointment_service_table_service_name_text[self.language].should(be.visible)
        s(self.appointment_service_table_service_name_value.format(service=service)).should(
            be.visible
        )
        self.appointment_service_table_sub_service_name_text[self.language].should(be.visible)
        s(
            self.appointment_service_table_sub_service_name_value.format(sub_service=sub_service)
        ).should(be.visible)

        self.appointment_details_table_title_text[self.language].should(be.visible)
        s(self.appointment_details_table_region.format(region=region)).should(be.visible)
        s(self.appointment_details_table_office.format(office=office)).should(be.visible)
        self.appointment_details_table_date_btn.should(be.visible)
        self.appointment_details_table_time_btn.should(be.visible)

        self.next_step_btn.should(be.visible)

    @allure.step("Open knowledge center")
    @allure.step("Verify more info block and open knowledge center")
    def open_knowledge_center(self):
        self.need_more_information_block.should(be.visible)
        self.need_more_information_block_sbs_btn[self.language].click()

    @allure.step("Verifying knowledge center is loaded")
    def verify_knowledge_center_page_load(self):
        browser.switch_to_next_tab()
        self.knowledge_center_section.should(be.visible)
        browser.switch_to_previous_tab()

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
        self.summary_table_title_text[self.language].should(be.visible)
        self.summary_table_reason_text[self.language].should(be.visible)
        self.summary_table_reason_value[self.language].should(be.visible)
        self.summary_table_office_text[self.language].should(be.visible)
        s(self.summary_table_office_value.format(office_name=office_name)).should(be.visible)
        self.summary_table_date_text[self.language].should(be.visible)
        self.summary_table_date_value.should(be.visible)
        self.summary_table_time_text[self.language].should(be.visible)
        self.summary_table_time_value.should(be.visible)
        self.summary_table_type_text[self.language].should(be.visible)
        s(self.summary_table_type_value.format(type_value=type_value)).should(be.visible)

    @allure.step("Clicking on book app button")
    def book_app_btn_click(self):
        self.book_app_btn.click()
