import allure
import pytest

from data.constants import AppointmentReason, Language
from data.lo.constants import (
    IndividualService,
    IndividualUser,
    OfficesInfo,
    ServicesInfo,
)
from src.ui.qiwa import qiwa
from utils.allure import TestmoProject, project

case_id = project(TestmoProject.LABOR_OFFICE)


@allure.title("Appointments[Individual]: View appointments list")
@case_id(39179)
def test_view_appointments_page():
    qiwa.login_as_user(login=IndividualUser.ID)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(Language.EN)
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS)
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.should_history_table_headers_have_correct_titles()
    qiwa.labor_office_appointments_page.click_appointments_history_next_page()
    qiwa.labor_office_appointments_page.verify_appointments_history_next_button()
    qiwa.labor_office_appointments_page.verify_appointments_history_previous_button()
    qiwa.labor_office_appointments_page.click_appointments_history_previous_page()
    qiwa.labor_office_appointments_page.verify_appointments_history_next_button()
    qiwa.labor_office_appointments_page.navigate_to_knowledge_center()
    qiwa.labor_office_appointments_page.should_new_tab_knowledge_center_be_opened()


@allure.title("Appointments[Individual]: Book appointment")
@case_id(39180)
@pytest.mark.parametrize("language", [Language.EN])
def test_book_individual_appointment(language):
    qiwa.login_as_user(login=IndividualUser.ID_2)
    qiwa.workspace_page.should_have_workspace_list_appear()
    qiwa.header.change_local(language)
    qiwa.workspace_page.language = language
    qiwa.workspace_page.select_individual_account()
    qiwa.individual_page.wait_page_to_load()
    qiwa.individual_page.click_see_all_services()
    qiwa.individual_page.select_service(IndividualService.APPOINTMENTS)
    qiwa.labor_office_appointments_page.wait_page_to_load()
    qiwa.labor_office_appointments_page.cancel_active_appointment()
    qiwa.labor_office_appointments_page.click_book_appointment_btn()
    qiwa.labor_office_appointments_create_page.book_appointment_flow(
        appointment_reason=AppointmentReason.IN_PERSON,
        service=ServicesInfo.SERVICE_NAME_INDIVIDUALS,
        sub_service=ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS,
        region=OfficesInfo.REGION_MADINAH[language],
        office=OfficesInfo.OFFICE_NAME_VEUM_HANE
    )
    qiwa.labor_office_appointments_create_confirmation_page.check_booked_appointment(
        service=ServicesInfo.SERVICE_NAME_INDIVIDUALS,
        sub_service=ServicesInfo.SUB_SERVICE_NAME_INDIVIDUALS,
        office=OfficesInfo.OFFICE_NAME_VEUM_HANE
    )
    qiwa.labor_office_appointments_create_confirmation_page.go_back_to_appointments_page()
    qiwa.labor_office_appointments_page.should_active_appointment_be_visible()
